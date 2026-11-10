# 最终提交索引

小组仓库地址：https://github.com/yokeres/iot-repair-group03

选定语言：Python 3

| 成员 | GitHub 用户名 | 任务 Issue 链接 | 主要 PR 链接 | 评审记录链接 |
| --- | --- | --- | --- | --- |
| A | yokeres | [#1](https://github.com/yokeres/iot-repair-group03/issues/1) | [#2](https://github.com/yokeres/iot-repair-group03/pull/2) | [C 的评审记录](https://github.com/yokeres/iot-repair-group03/pull/2#pullrequestreview-5796321732) |
| B | Esponjs | [#3](https://github.com/yokeres/iot-repair-group03/issues/3) | [#5](https://github.com/yokeres/iot-repair-group03/pull/5) | [A 的最终 Approve](https://github.com/yokeres/iot-repair-group03/pull/5#pullrequestreview-5796960897) |
| C | Sunsh-212 | [#10](https://github.com/yokeres/iot-repair-group03/issues/10) | [#11](https://github.com/yokeres/iot-repair-group03/pull/11) | [A 的修订评审](https://github.com/yokeres/iot-repair-group03/pull/11#issuecomment-6766958856) |

## 最终复核

当前 `main` 下载 ZIP 后运行的实际结果：2026-11-10，`4/4 passed`，退出码 `0`。三人主要 PR 全部合并后需再次从最新 `main` 复测。

## 协作记录说明

- A 的 PR #2 包含需求说明、用例图和实验一个人小结，C 已核对 `docs/requirements.md`、`docs/usecase.md` 和用例图源文件并给出具体评审意见。
- B 的 PR #5 已由 A 核对状态转换、终态、类属性、多重性及 PNG/PlantUML/SVG 文件后批准。
- C 的 PR #11 使用 `base=main`、`compare=feat/status-c`，保留 C 的测试人员信息、可复现运行命令和真实 `4/4 passed` 输出。
- 最终版本按 A、B、C、收尾索引的顺序合入 `main`。

## 个人简短总结

A：完成仓库初始化、需求说明、用例图和实验一小结；已建立 Issue #1 和 PR #2，并请求 C 评审。评审完成后负责组织 A、B、C 的有效 PR 按顺序合并和最终核验。详细记录见 [实验二个人小结](experiment-two-summary-a.md)。

B：状态图、简单类图及可编辑源材料已在 `docs/models-b` 完成，并创建 PR #5；A 已核对内容，PR 目标分支已修正为 `main`。

C：完成 Python 状态函数复测和测试记录，任务 Issue #10 与主要 PR #11 已建立并合入。

## 验收清单

- [x] 3 条功能需求完整
- [x] 3 种图齐全且源材料可编辑
- [x] 一种语言的 Python 状态函数与 4 项测试
- [x] 三人均有实际提交和评审记录
- [x] 三个主要 PR 均已有效合并且未污染 `main`
- [x] 公开仓库可被教师访问
