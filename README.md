# Cloud & Systems Roadmap

A learning repo for exploring the cloud / systems side of computer science. The goal is not to learn everything, but to **build the pipeline once by hand, then take it apart layer by layer** and find out which specific sub-area actually holds my interest.

Progress is tracked with Issues: each Issue is one task with a checklist and a self-test; Milestones correspond to phases.

## Phases at a glance

| Phase | What | Time | Output |
|---|---|---|---|
| Phase 1 | Fundamentals: Linux / networking / OS / Docker | 3–4 weeks | A cloud VM I configured myself + all self-tests passed |
| Phase 2 | Deploy a web app with a database from scratch | 2–3 weeks | Public HTTPS site, CI/CD auto-deploy, basic monitoring |
| Phase 3 | Scale to a small cluster, break things on purpose | 3–4 weeks | 3 replicas on k8s, primary/replica DB, a load-test report |
| Phase 4 | Pick a direction and go deep | ongoing | Core labs of one systems course + paper notes |

Roughly 8–10 hours a week, 2–3 months total.

## Why it's structured this way

"Cloud computing" is not a single research direction. It is a pipeline where every stage belongs to a different field (scheduling, virtualization, storage, networking, security, observability, …). Walk the pipeline yourself first; whichever layer makes you stop and want to dig in is your direction.

Phase 2 gives a first signal. Phase 3 confirms it. Phase 4 is where the actual "studying a direction" begins.

## Repo layout

```
.
├── README.md              # this file
├── docs/
│   ├── phase-1.md         # fundamentals checklist
│   ├── phase-2.md         # single-machine deployment project
│   ├── phase-3.md         # cluster & failure experiments
│   ├── phase-4.md         # choosing a direction
│   └── reading-list.md    # papers and blogs
├── notes/                 # study notes and the "why?" log
│   ├── questions.md       # every "why?" I run into — this is the interest map
│   └── papers/            # one page per paper
└── projects/              # code for Phase 2/3
```

## Habits that run through every phase

- **Read primary sources**: AWS Architecture Blog, Google SRE Book, Cloudflare Blog
- **One classic paper a week**: start with MapReduce and GFS, see `docs/reading-list.md`
- **Log every "why?"**: anything you don't understand goes into `notes/questions.md`; in a few months it will be obvious what you care about
- **Bring something to show**: once Phase 2 is done, take the project and the questions list to a systems professor or engineer and talk

## Progress

See [Issues](../../issues) and [Milestones](../../milestones).
