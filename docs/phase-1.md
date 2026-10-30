# Phase 1: Fundamentals (3–4 weeks)

Order: **Linux → Networking → OS → Docker**. Linux has to come first; Docker goes last. About an hour a day — the key is touching the command line every day.

On day one, spin up a free-tier Ubuntu VM on AWS or GCP and do every exercise on that machine. You'll get used to the cloud console, security groups and ssh keys as a side effect.

---

## 1. Linux command line (~1 week)

### What to know
- File ops: `ls cd cp mv rm mkdir find cat less head tail`
- Permissions: `chmod chown sudo`, understand rwx and 755
- Processes: `ps top htop kill`, PIDs, background jobs, signals
- Text: `grep sed awk`, pipes `|`, redirection `> >> 2>&1`
- Network tools: `ssh scp curl wget ping ss dig`
- Services & logs: `systemctl`, `journalctl`, `/var/log`
- Environment: env vars, `PATH`, `.bashrc`, symlinks
- Packages: `apt`
- Write a shell script under 20 lines with a loop and a conditional

### Resources
- MIT "The Missing Semester of Your CS Education", first few lectures
- linuxjourney.com
- OverTheWire Bandit (game-style, one command per level)

### Self-test
- [ ] Without looking anything up, ssh into a remote box, find the process using the most CPU and kill it
- [ ] From a log file with tens of thousands of lines, pull out lines containing "error" and count them per hour
- [ ] Write a script that walks a directory, finds every `.log` older than 7 days and compresses it

---

## 2. Networking basics (~1 week)

### What to know
- Layering: what the application / transport / network layers each do
- DNS: A records, CNAME, why changes take time to propagate
- IPs and ports: public vs private IP, why 80 and 443 are special
- TCP vs UDP, the three-way handshake
- HTTP/HTTPS: methods, status codes (200/301/404/500/502/504), headers, cookies, certificates and the chain of trust
- NAT and firewalls: why your laptop has no public IP, what a cloud security group is
- Load balancers and reverse proxies: what Nginx in front of an app does
- Tools: `ping traceroute dig curl -v telnet`

### Resources
- *How the Internet Really Works* / *Computer Networking: A Top-Down Approach* (skim ch. 1–2 only for now; come back later)
- Julia Evans' networking zines
- Hands-on: `curl -v` a site and understand every line of output; `dig` a domain and read every field

### Self-test
- [ ] Explain in your own words everything that happens from typing `github.com` to the page rendering (DNS → TCP → TLS → HTTP)
- [ ] A service on your cloud VM isn't reachable from the browser — list at least 4 possible causes and how to rule each out
- [ ] Seeing a 502 vs a 504, know roughly which layer broke

---

## 3. Operating systems basics (~1 week, skip if you've taken an OS course)

### What to know
- Processes vs threads; why processes can't see each other's memory by default
- Virtual memory; what OOM is
- CPU scheduling, time slices
- File descriptors, inodes, "everything is a file"
- System calls, user mode vs kernel mode
- Concurrency: locks, deadlock, race conditions
- Linux equivalents: `/proc`, `ulimit`, **cgroups and namespaces** (the basis of containers — must understand)

### Resources
- *Operating Systems: Three Easy Pieces* (OSTEP, free online) — only the "Virtualization" part and the first few "Concurrency" chapters, ~150 pages
- Hands-on: `strace` a simple program; `cat /proc/<pid>/status`

### Self-test
- [ ] Explain why a program can use 8 GB of memory on a machine with 4 GB
- [ ] One sentence on the real difference between a container and a VM
- [ ] Seeing "OOM killed", know what happened and where the logs are

---

## 4. Docker (3–5 days)

### What to know
- Image vs container
- Dockerfile: `FROM RUN COPY WORKDIR EXPOSE CMD`, layers and caching
- Commands: `build run ps logs exec stop rm`, flags `-p -v -e`
- Docker Compose: one yaml that brings up app + database
- Why data disappears when a container is removed; what a volume is
- Docker Hub push / pull

### Resources
- Docker's official Get Started guide, 2–3 hours
- Then containerize any small project you've written

### Self-test
- [ ] Write a Dockerfile for a Python or Node project with a reasonable image size
- [ ] Bring up a web app + PostgreSQL with Compose; the app connects, and data survives a restart
- [ ] A container won't start — debug it with `docker logs` and `docker exec -it ... sh`
