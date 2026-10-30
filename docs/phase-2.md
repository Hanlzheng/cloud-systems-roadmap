# Phase 2：从零部署一个带数据库的 Web 应用（2–3 周）

目标：把"push 代码 → 构建 → 部署 → 用户访问 → 监控"这条流水线**自己走一遍**，而不是用平台帮你做完。

代码放在 `projects/phase-2/`。

## 步骤

1. **写应用**：最简单的 CRUD（Flask / Express / Go 都行）+ PostgreSQL
2. **容器化**：Dockerfile + docker-compose.yml，本地跑通
3. **上云**：AWS / GCP 免费额度开一台虚拟机，手动部署起来
   - 配安全组 / 防火墙
   - 买或申请一个域名，配 DNS
   - 用 Caddy 或 Nginx + Let's Encrypt 配 HTTPS
4. **自动化**：GitHub Actions 实现 push → 构建镜像 → 推到服务器 → 重启服务
5. **监控**：Prometheus + Grafana 看 metrics，日志集中到一个地方（最简单可以先用 `journalctl` + Loki，或者直接 Grafana Cloud 免费版）

## 做完会遇到的"为什么"（记进 notes/questions.md）

- 为什么容器重启数据就没了 → 存储与状态
- 为什么并发一高就卡 → 资源与调度
- 为什么证书会过期、怎么自动续 → 安全与自动化
- 为什么日志那么难找 → 可观测性
- 为什么 Actions 有时候排队很久 → 调度与容量

## 完成标准

- [ ] 公网域名可访问，HTTPS 正常
- [ ] push 到 main 后 5 分钟内自动上线
- [ ] 有一个 Grafana 面板能看到请求量和延迟
- [ ] `notes/questions.md` 里至少记了 10 个"为什么"
