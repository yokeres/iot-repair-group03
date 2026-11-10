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

C 已建立任务 Issue #10，并提交方向正确的 PR #11（base=main，compare=feat/status-c）。PR #11 仍有测试命令绝对路径、测试脚本比较表达式和 Issue 关联需要修正；修订后请 B 正式评审。PR #6、#7、#8 的方向或差异不符合要求，不能作为主要 PR。C 还需把对 A 的 PR #2 的评审从 COMMENTS 提交为正式 Approve。

## 体会

本次实验中，分支内容正确不代表 Pull Request 一定正确，base 和 compare 的方向必须在合并前核对。评审意见应写出具体文件和检查依据，不能只写“很好”。最终验收应以最新 `main` 下载的 ZIP 复测结果为准，而不是用个人分支或文档中的文字代替实际运行。
