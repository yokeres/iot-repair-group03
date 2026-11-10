# 最终提交索引

小组仓库地址：https://github.com/yokeres/iot-repair-group03

选定语言：Python 3

| 成员 | GitHub 用户名 | 任务 Issue 链接 | 主要 PR 链接 | 评审记录链接 |
| --- | --- | --- | --- | --- |
| A | yokeres | [#1](https://github.com/yokeres/iot-repair-group03/issues/1) | [#2](https://github.com/yokeres/iot-repair-group03/pull/2) | C 已有评论但未提交正式评审；待补齐 |
| B | Esponjs | [#3](https://github.com/yokeres/iot-repair-group03/issues/3) | [#5](https://github.com/yokeres/iot-repair-group03/pull/5) | [A 的最终 Approve](https://github.com/yokeres/iot-repair-group03/pull/5#pullrequestreview-5796960897) |
| C | Sunsh-212 | [#10](https://github.com/yokeres/iot-repair-group03/issues/10) | [#11](https://github.com/yokeres/iot-repair-group03/pull/11) | 待 B 正式评审；C 的 PR 尚需修订 |

## 最终复核

当前 `main` 下载 ZIP 后运行的实际结果：2026-11-10，`4/4 passed`，退出码 `0`。三人主要 PR 全部合并后需再次从最新 `main` 复测。

## C 的协作记录说明

- PR #6 的 base 为 `feat/status-c`、compare 为 `main`，方向相反且文件差异为 0。
- PR #7 仅将空合并记录带回 `main`，文件差异为 0；PR #8 也是零差异的重复候选，三者均不能作为 C 的主要 PR。
- C 已创建任务 Issue #10 和方向正确的 PR #11，PR #11 当前修改 `docs/test-results.md`。合并前仍需关联 Issue #10、把测试命令改为从仓库目录可复现的相对路径、将测试脚本中的 `actual is expected` 改为 `actual == expected`，并由 B 正式评审。
- C 还需正式评审 A 的 PR #2。C 已给出具体检查内容，但当前记录仍是 `COMMENTED`，需要重新使用 Review changes 提交 Approve。

## 个人简短总结

A：完成仓库初始化、需求说明、用例图和实验一小结；已建立 Issue #1 和 PR #2，并请求 C 评审。评审完成后负责组织 A、B、C 的有效 PR 按顺序合并和最终核验。详细记录见 [实验二个人小结](experiment-two-summary-a.md)。

B：状态图、简单类图及可编辑源材料已在 `docs/models-b` 完成，并创建 PR #5；A 已核对内容，PR 目标分支已修正为 `main`。

C：指定成果为 Python 状态函数与测试验收。任务 Issue #10 和主要 PR #11 已建立，PR 方向正确；尚待内容修订、B 正式评审和正式评审 A 的 PR。

## 验收清单

- [x] 3 条功能需求完整
- [x] 3 种图齐全且源材料可编辑
- [x] 一种语言的 Python 状态函数与 4 项测试
- [ ] 三人均有实际提交和同伴评审
- [ ] 三个主要 PR 均已有效合并且未污染 `main`
- [x] 公开仓库可被教师访问
