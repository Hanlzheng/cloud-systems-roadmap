#!/usr/bin/env python3
"""Create labels, milestones and issues from issues.json via the GitHub REST API (gh api).

Usage:  python3 .github/bootstrap_issues.py OWNER/REPO
Idempotent: skips labels/milestones/issues whose names already exist.
"""
import json
import subprocess
import sys
from pathlib import Path


def api(method, path, body=None):
    args = ["gh", "api", "-X", method, path]
    if body is not None:
        args += ["--input", "-"]
    r = subprocess.run(args, capture_output=True, text=True,
                       input=json.dumps(body) if body is not None else None)
    if r.returncode != 0:
        raise RuntimeError(f"{method} {path}\n{r.stderr}")
    return json.loads(r.stdout) if r.stdout.strip() else None


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    repo = sys.argv[1]
    data = json.loads((Path(__file__).parent / "issues.json").read_text())

    # labels
    existing = {l["name"] for l in api("GET", f"repos/{repo}/labels?per_page=100")}
    for l in data["labels"]:
        if l["name"] in existing:
            continue
        api("POST", f"repos/{repo}/labels", l)
        print("label  +", l["name"])

    # milestones
    ms = api("GET", f"repos/{repo}/milestones?state=all&per_page=100")
    ms_by_title = {m["title"]: m["number"] for m in ms}
    for m in data["milestones"]:
        if m["title"] in ms_by_title:
            continue
        out = api("POST", f"repos/{repo}/milestones", m)
        ms_by_title[m["title"]] = out["number"]
        print("mstone +", m["title"])

    # issues
    existing_titles = {i["title"] for i in api("GET", f"repos/{repo}/issues?state=all&per_page=100")}
    for i in data["issues"]:
        if i["title"] in existing_titles:
            continue
        body = {"title": i["title"], "body": i["body"], "labels": i["labels"]}
        if i.get("milestone"):
            body["milestone"] = ms_by_title[i["milestone"]]
        out = api("POST", f"repos/{repo}/issues", body)
        print("issue  +", i["title"], "->", out["html_url"])


if __name__ == "__main__":
    main()
