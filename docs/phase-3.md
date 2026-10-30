# Phase 3: Scale to a small cluster and break things (3–4 weeks)

Upgrading from one machine to a cluster is where the real distributed-systems problems show up. By the end you should be able to answer: **am I hooked on "keeping the system up", or does this feel like tedious configuration?** Either answer is useful.

Code lives in `projects/phase-3/`.

## Steps

1. **Cluster**: local Kubernetes with kind or k3s (or a cloud provider's managed k8s free tier)
2. **Deploy**: run the Phase 2 app with 3 replicas, with a Service and an Ingress
3. **Kill a replica**: `kubectl delete pod` one of them; watch traffic shift and how long recovery takes
4. **Database replication**: PostgreSQL primary + replica; then kill the primary and see what happens (usually a mess — that's expected)
5. **Load test**: k6 or locust; find the bottleneck; try to tune it (replica count, resource limits, connection pool, cache)
6. **Observability**: Prometheus scraping cluster metrics — pod restarts, CPU/memory, latency distribution

## This phase's "why?"s

- How do replicas stay consistent → distributed consistency
- Who becomes the new primary when the old one dies → leader election, consensus
- Why did the scheduler put this pod on that node → the scheduler
- Why did a memory limit make things slower → resource management
- Which layer is the bottleneck under load → performance analysis

## Done when

- [ ] 3 replicas running; killing any one doesn't interrupt service
- [ ] Performed a primary → replica failover at least once (manual is fine)
- [ ] A load-test report: QPS, p50/p99 latency, where the bottleneck was, what you changed
- [ ] Can answer "if traffic goes up 10×, what breaks first?"
