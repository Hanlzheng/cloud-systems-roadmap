#!/usr/bin/env python3
"""Create labels, milestones and issues from issues.json using the gh CLI.

Usage:  python3 .github/bootstrap_issues.py OWNER/REPO
Idempotent: skips labels/milestones/issues whose names already exist.
"""
import json
import subprocess
import sys
from pathlib import Path


def gh(*args, input_data=None):
    r = subprocess.run(["gh", *args], capture_output=True, text=True, input=input_data)
    if r.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)}\n{r.stderr}")
    return r.stdout


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    repo = sys.argv[1]
    data = json.loads((Path(__file__).parent / "issues.json").read_text())

    # labels
    existing = {l["name"] for l in json.loads(gh("label", "list", "-R", repo, "--json", "name", "-L", "200"))}
    for l in data["labels"]:
        if l["name"] in existing:
            continue
        gh("label", "create", l["name"], "-R", repo, "-c", l["color"], "-d", l["description"])
        print("label  +", l["name"])

    # milestones (gh has no milestone subcommand; use the API)
    ms = json.loads(gh("api", f"repos/{repo}/milestones?state=all&per_page=100"))
    ms_by_title = {m["title"]: m["number"] for m in ms}
    for m in data["milestones"]:
        if m["title"] in ms_by_title:
            continue
        out = json.loads(gh("api", f"repos/{repo}/milestones", "-f", f"title={m['title']}",
                            "-f", f"description={m['description']}"))
        ms_by_title[m["title"]] = out["number"]
        print("mstone +", m["title"])

    # issues
    existing_titles = {i["title"] for i in json.loads(
        gh("issue", "list", "-R", repo, "--state", "all", "--json", "title", "-L", "500"))}
    for i in data["issues"]:
        if i["title"] in existing_titles:
            continue
        args = ["issue", "create", "-R", repo, "-t", i["title"], "-F", "-"]
        for lab in i["labels"]:
            args += ["-l", lab]
        if i.get("milestone"):
            args += ["-m", i["milestone"]]
        url = gh(*args, input_data=i["body"]).strip()
        print("issue  +", i["title"], "->", url)


if __name__ == "__main__":
    main()
