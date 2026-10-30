# Phase 2: Deploy a web app with a database from scratch (2–3 weeks)

Goal: walk the whole pipeline — push code → build → deploy → users hit it → monitor — **by hand**, instead of letting a platform do it for you.

Code lives in `projects/phase-2/`.

## Steps

1. **Write the app**: the simplest CRUD you can (Flask / Express / Go) + PostgreSQL
2. **Containerize**: Dockerfile + docker-compose.yml, runs locally
3. **Put it on a VM**: AWS / GCP free tier
   - Configure security group / firewall
   - Get a domain, point DNS at the box
   - HTTPS with Caddy or Nginx + Let's Encrypt
4. **Automate**: GitHub Actions does push → build image → push to server → restart
5. **Monitor**: Prometheus + Grafana for metrics; ship logs somewhere central (Grafana Cloud free tier or local Loki is enough)

## The "why?"s you'll hit (log them in notes/questions.md)

- Why does the data vanish when the container restarts → storage and state
- Why does it fall over under concurrency → resources and scheduling
- Why do certificates expire, how do they auto-renew → security and automation
- Why are the logs so hard to find → observability
- Why does Actions sometimes queue for ages → scheduling and capacity

## Done when

- [ ] Public domain reachable over HTTPS
- [ ] A push to main is live within 5 minutes
- [ ] A Grafana dashboard shows request rate and latency
- [ ] At least 10 entries in `notes/questions.md`
