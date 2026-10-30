# Phase 4: Pick a direction and go deep

Based on which layer you kept stopping at in Phases 2–3, pick the matching course and papers.

| Where you kept stopping | Direction | Next step | Home venues |
|---|---|---|---|
| Replica consistency, choosing a new primary | Distributed systems | MIT 6.824 / 6.5840, do the Raft lab; read Raft, Dynamo | OSDI / SOSP / NSDI |
| How the database stores and finds things fast | Database systems | CMU 15-445, write a storage engine | SIGMOD / VLDB |
| How containers isolate, how the scheduler places things | OS / virtualization | Berkeley CS162 or MIT 6.828; read Borg, Firecracker | OSDI / SOSP / EuroSys |
| How requests get routed, why latency is high | Networking | Stanford CS144, implement TCP | NSDI / SIGCOMM |
| Protecting secrets, isolating tenants | Systems security | gVisor and Firecracker design docs; confidential computing | S&P / CCS / USENIX Security |
| Analyzing logs from thousands of machines, auto-detecting failures | Observability / AIOps | Google SRE Book; mostly industry | — |
| Training and serving large models across hundreds of GPUs | ML systems | Megatron-LM, vLLM; make sure ML basics are solid first | MLSys / OSDI |

## A note on academic competition

- Classic distributed systems (consensus, consistency) is relatively saturated. The open space is in ML systems, new-hardware-driven redesigns (CXL / RDMA / SmartNICs), confidential computing, serverless, and LLMs for systems operations
- Top North American systems groups are few, with few slots per year, and admissions weigh **prior systems research** heavily. If a PhD is the goal, get into a lab early
- If a job is the goal, none of that competition applies — distributed-systems engineering skill is hard currency

## Output of this phase

- [ ] Pick one direction and write `notes/why-this-direction.md`: why this one, and which moments in Phases 2–3 pointed at it
- [ ] Finish the core labs of the matching course
- [ ] Read 5 papers in that direction, one page of notes each
- [ ] If in school: take the Phase 2/3 work and your questions list to a professor in that area and talk
