# Interview prep (runs alongside every phase)

LeetCode is an interview tool, not a way to learn cloud. For infra roles it is a filter you must pass, not where you stand out. What stands out is the project work in Phases 2–3 and system design. So: **get stable on mediums, then stop and spend the time on system design and projects.**

## What an infra interview looks like

1. **Algorithms (1–2 rounds)** — same as any SWE loop, mostly medium. Goal: don't fail.
2. **System design (1–2 rounds)** — design a URL shortener, a message queue, a distributed cache. **This is the main event for infra roles.** Phases 2–3 of this roadmap are direct preparation.
3. **Practical coding (some companies)** — implement an LRU cache, a rate limiter, a concurrent KV store, top-K from a log stream. Overlaps with LeetCode but closer to real code.

## Algorithm problems: scope

Pick **NeetCode 150** or **Grind 75** and work through it by pattern, not by problem number. After those ~150, returns diminish sharply.

Patterns with the highest payoff for infra:

- Hash maps and heaps (top-K, merging K sorted streams — log processing and schedulers)
- Intervals (merge intervals, meeting rooms — resource allocation)
- Graph BFS/DFS, topological sort (dependency resolution, task scheduling)
- Sliding window (rate limiting, streaming stats)
- LRU / LFU cache (near-certain to appear, and a real systems component)
- Trie (route matching, prefix lookup)
- Binary search on sorted data (everywhere in storage systems)

Lower priority: hard DP, exotic string problems, math puzzles. Medium-level competence is enough.

Also do, because LeetCode's main lists skip them:

- **Concurrency** category on LeetCode (FooBar, Dining Philosophers, H2O) — locks and semaphores
- **Design-flavored problems**: Design Hit Counter, Design Rate Limiter, Design Log Storage System, Time-Based Key-Value Store, Design In-Memory File System

## Pace

- **Phases 1–2**: 3–4 problems a week. If stuck past 40 minutes, read the solution, then redo it from scratch the next day. Cover every pattern once.
- **Phase 3**: drop to 2 a week to keep sharp; start system design. Read *Designing Data-Intensive Applications* (DDIA) — it lines up with Phase 3 exactly.
- **1–2 months before applying**: redo everything you got wrong, do mock interviews.

Never let problems crowd out hands-on time. Someone who finished the Raft lab beats someone with 500 solved problems in an infra loop.

## Language

Python is fastest for practice. Infra interviews often prefer Go or Java; consider switching for the final stretch once the patterns are solid.

## System design resources (from Phase 3 on)

- *Designing Data-Intensive Applications* — the book for this
- Google SRE Book, first 10 chapters
- Practice designing: URL shortener, rate limiter, message queue, distributed cache, log aggregation, object storage. For each: requirements → API → data model → scaling → failure modes.
