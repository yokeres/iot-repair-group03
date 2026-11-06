# 实验二个人小结与体会（A）

- 姓名/角色：组长 A
- GitHub 用户名：yokeres
- 个人分支：`docs/requirements-a`、`docs/submission-a`

## 本人完成的内容

1. 在实验一需求与用例图基础上，建立 A 的任务 Issue #1 和个人分支 `docs/requirements-a`，提交 PR #2。
2. 完成 A 的需求复核记录、用例图检查记录和实验一个人小结，并将实验一成果放入 PR #2。
3. 按“A 审 B”核对 B 的 PR #5：检查状态图是否只允许两条转换、`COMPLETED` 是否为终态、类属性和 `1 : 0..*` 多重性是否完整、PNG/PlantUML/SVG 文件是否齐全。
4. 发现 B 的 PR 最初把目标分支选成 `feat/status-c`。要求改回 `main` 后重新检查，目标分支正确后提交最终 Approve。
5. 在最新 `main` 的 ZIP 快照中运行 `python3 test_status_rule.py`，确认 T01 至 T04 全部 PASS，汇总 `4/4 passed`，退出码 `0`。
6. 建立 `docs/submission-a` 分支和 PR #4，整理三人任务 Issue、主要 PR、评审记录、真实测试结果和最终验收清单。

## 一次真实评审与修订

B 的 PR #5 第一次提交时，模型内容符合要求，但 Pull Request 的 base 错误地设为 `feat/status-c`，会把 B 的成果先合入 C 的分支。A 在 Files changed 中确认文件差异后提交 `Request changes`，明确要求将 base 改为 `main`。B 修改目标分支后，A 重新检查并正式 Approve。

## 关键检查结论

- 状态转换只有 `PENDING → PROCESSING` 与 `PROCESSING → COMPLETED`。
- 跳级、回退、同状态和其他组合均拒绝，`COMPLETED` 为终态。
- `Device` 包含 `deviceId`、`name`、`location`。
- `WorkOrder` 包含 `orderId`、`deviceId`、`description`、`status`。
- 一台设备对应 `0..*` 张工单，每张工单对应 `1` 台设备。

## 协作中发现的问题

A 已为 C 建立任务 Issue #9。C 目前尚未形成有效的主要 PR：PR #6 的 base 与 compare 方向相反，文件差异为 0；PR #7 只产生了空合并，也不能作为 C 的代码成果。C 需要在 `feat/status-c` 分支提交本人实际修改和测试记录，创建 `base=main` 的正式 PR，并请 B 评审；同时 C 还需正式评审 A 的 PR #2。

## 体会

本次实验中，分支内容正确不代表 Pull Request 一定正确，base 和 compare 的方向必须在合并前核对。评审意见应写出具体文件和检查依据，不能只写“很好”。最终验收应以最新 `main` 下载的 ZIP 复测结果为准，而不是用个人分支或文档中的文字代替实际运行。
