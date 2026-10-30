# Phase 1：补基础（3–4 周）

顺序：**Linux → 网络 → OS → Docker**。Linux 必须第一个，Docker 放最后。每天 1 小时左右，关键是每天都碰命令行。

第一天先去 AWS / GCP 开一台免费额度的 Ubuntu 虚拟机，之后所有练习都在那台机器上做，顺便熟悉云控制台、安全组、ssh 密钥。

---

## 1. Linux 命令行（约 1 周）

### 要掌握
- 文件操作：`ls cd cp mv rm mkdir find cat less head tail`
- 权限：`chmod chown sudo`，理解 rwx 和 755
- 进程：`ps top htop kill`，PID、后台进程、信号
- 文本处理：`grep sed awk`、管道 `|`、重定向 `> >> 2>&1`
- 网络工具：`ssh scp curl wget ping ss dig`
- 服务与日志：`systemctl`、`journalctl`、`/var/log`
- 环境：环境变量、`PATH`、`.bashrc`、软链接
- 包管理：`apt`
- 能写 20 行以内带循环和判断的 shell 脚本

### 资源
- MIT "The Missing Semester of Your CS Education" 前几讲（有中文字幕）
- linuxjourney.com
- OverTheWire Bandit（闯关式练习）

### 过关自测
- [ ] 不查资料，ssh 到远程机器，找到占 CPU 最高的进程并杀掉
- [ ] 从几万行日志里筛出含 "error" 的行，统计每小时出现次数
- [ ] 写脚本：遍历目录下所有 .log 文件，把超过 7 天的压缩归档

---

## 2. 计算机网络基础（约 1 周）

### 要掌握
- 分层概念：应用层 / 传输层 / 网络层各管什么
- DNS：A 记录、CNAME、为什么改 DNS 要等生效
- IP 与端口：公网 / 内网 IP，80 和 443 为什么特殊
- TCP vs UDP：三次握手的概念
- HTTP/HTTPS：方法、状态码（200/301/404/500/502/504）、header、cookie、证书与信任链
- NAT 与防火墙：为什么家里电脑没有公网 IP，云的安全组是什么
- 负载均衡和反向代理：Nginx 放在应用前面干什么
- 排查工具：`ping traceroute dig curl -v telnet`

### 资源
- 《网络是怎样连接的》（户根勤）—— 最推荐，一两天读完
- 《图解 HTTP》《图解 TCP/IP》挑着看
- 动手：`curl -v` 访问一个网站，把每一行输出搞懂；`dig` 查域名看每个字段

### 过关自测
- [ ] 用自己的话讲清楚从输入 `github.com` 到页面出现的全过程（DNS → TCP → TLS → HTTP）
- [ ] 云服务器上起了服务但浏览器访问不了，能列出至少 4 个可能原因并逐个排查
- [ ] 看到 502 和 504，知道大概哪一层出了问题

---

## 3. 操作系统基础（约 1 周，上过 OS 课可跳过）

### 要掌握
- 进程与线程：区别、为什么进程间默认看不到彼此的内存
- 虚拟内存：为什么每个进程都觉得自己有完整内存；什么是 OOM
- CPU 调度：时间片
- 文件系统：文件描述符、inode、"一切皆文件"
- 系统调用：用户态 / 内核态
- 并发：锁、死锁、竞态条件
- Linux 对应物：`/proc`、`ulimit`、**cgroups 和 namespaces**（容器的基础，必须懂）

### 资源
- 《Operating Systems: Three Easy Pieces》（OSTEP，免费，有中译）——只读"虚拟化"部分和"并发"前几章，约 150 页
- 动手：`strace` 跟踪一个程序看系统调用；`cat /proc/<pid>/status`

### 过关自测
- [ ] 能解释为什么程序用了 8GB 内存但机器只有 4GB 还能跑
- [ ] 一句话说清楚容器和虚拟机的本质区别
- [ ] 看到服务被 OOM killed，知道发生了什么、去哪看日志

---

## 4. Docker（3–5 天）

### 要掌握
- 镜像 vs 容器
- Dockerfile：`FROM RUN COPY WORKDIR EXPOSE CMD`，分层与缓存
- 命令：`build run ps logs exec stop rm`，`-p -v -e`
- Docker Compose：一个 yaml 起应用 + 数据库
- 为什么容器一删数据就没了，volume 是什么
- Docker Hub push/pull

### 资源
- Docker 官方 Get Started，两三个小时
- 然后直接把自己写过的任何小项目容器化

### 过关自测
- [ ] 给一个 Python 或 Node 项目写 Dockerfile，镜像体积合理
- [ ] 用 Compose 起 Web 应用 + PostgreSQL，应用能连上库，重启后数据还在
- [ ] 容器起不来，能用 `docker logs` 和 `docker exec -it ... sh` 排查
