# Phase 4：选一个方向往深走

根据 Phase 2/3 哪一层最让你停留，选对应的课和论文。

| 你停留的地方 | 对应方向 | 下一步 | 主场会议 |
|---|---|---|---|
| 副本一致性、主库挂了怎么选新的 | 分布式系统 | MIT 6.824 / 6.5840，做 Raft lab；读 Raft、Dynamo | OSDI / SOSP / NSDI |
| 数据库内部怎么存、怎么查快 | 数据库系统 | CMU 15-445，自己写存储引擎 | SIGMOD / VLDB |
| 容器怎么隔离、调度器怎么分配 | 操作系统 / 虚拟化 | Berkeley CS162 或 MIT 6.828；读 Borg、Firecracker | OSDI / SOSP / EuroSys |
| 请求怎么路由、为什么延迟高 | 网络 | Stanford CS144，自己实现 TCP | NSDI / SIGCOMM |
| secrets 怎么保护、租户怎么隔离 | 系统安全 | 读 gVisor、Firecracker 设计文档；机密计算 | S&P / CCS / USENIX Security |
| 几千台机器的日志怎么分析、怎么自动发现故障 | 可观测性 / AIOps | Google SRE Book；偏工业界 | — |
| 大模型怎么在几百张卡上训练和推理 | ML 系统 | 读 Megatron-LM、vLLM；先确保 ML 基础够 | MLSys / OSDI |

## 关于学术竞争的现实

- 经典分布式系统（共识、一致性）相对饱和，新空间在：ML 系统、新硬件驱动的重设计（CXL / RDMA / SmartNIC）、机密计算、serverless、LLM 做系统运维
- 北美顶尖系统组少、坑位少、申请时看重**已经做过系统研究**。想读博要尽早进实验室
- 想工作则以上竞争基本不存在，分布式系统工程能力是硬通货

## 这一阶段的产出

- [ ] 选定 1 个方向，写一篇 `notes/why-this-direction.md` 说清楚为什么
- [ ] 完成对应课程的核心 lab
- [ ] 读完 5 篇该方向的论文，每篇一页笔记
- [ ] 如果在学校：带着 Phase 2/3 的东西和问题列表去找该方向的教授聊一次
