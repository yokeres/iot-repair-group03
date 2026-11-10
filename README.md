# 校园物联网设备报修实验

组号：03

| 成员 | 角色 | GitHub 用户名 | 主要成果 |
| --- | --- | --- | --- |
| A | 组长 | yokeres | 需求说明、用例图、仓库初始化与提交索引 |
| B | 组员 | Esponjs | 状态图、简单类图及源材料 |
| C | 组员 | Sunsh-212 | Python 状态函数与实际测试记录 |

本组选定语言：**Python 3**

## 范围

只分析查看设备、提交报修、更新工单状态三项功能，只编程实现状态判断函数。

不接入真实硬件，不实现数据库、网页、登录或 MQTT。

## 固定规则

新工单为 `PENDING`。仅允许 `PENDING → PROCESSING`、`PROCESSING → COMPLETED`，其他转换一律拒绝，包括状态不变。

## 实验成果

- [x] 3 条功能需求：`docs/requirements.md`
- [x] 用例图与可编辑源文件：`docs/usecase.md`、`docs/assets/usecase.png`、`docs/assets/usecase.puml`
- [x] 状态图与简单类图内容：`docs/models.md`（B 的 PR #5 已由 A 批准，待合并）
- [x] Python 状态函数：`src/python/status_rule.py`
- [x] 4 项测试及真实输出：`docs/test-results.md`
- [x] 当前 `main` ZIP 复测：2026-11-10，`4/4 passed`，退出码 `0`
- [x] A 的实验二个人小结：`docs/experiment-two-summary-a.md`
- [ ] 三人任务 Issue、主要 PR 与交叉评审全部完成

## 运行

在 `src/python` 目录运行：

```bash
python3 test_status_rule.py
```

预期 `Summary: 4/4 passed`，退出码为 `0`。

## 协作进度

- **A**：Issue [#1](https://github.com/yokeres/iot-repair-group03/issues/1)，分支 `docs/requirements-a`，主要 PR [#2](https://github.com/yokeres/iot-repair-group03/pull/2)。已请求 C 评审；C 目前只留下评论，仍需正式提交 `Approve` 或 `Request changes`。
- **B**：Issue [#3](https://github.com/yokeres/iot-repair-group03/issues/3)，分支 `docs/models-b`，主要 PR [#5](https://github.com/yokeres/iot-repair-group03/pull/5)。A 已完成内容核验并正式批准（[评审记录](https://github.com/yokeres/iot-repair-group03/pull/5#pullrequestreview-5796960897)），PR 可进入最终合并阶段。
- **C**：任务 Issue [#10](https://github.com/yokeres/iot-repair-group03/issues/10)，分支 `feat/status-c`，主要 PR [#11](https://github.com/yokeres/iot-repair-group03/pull/11)。PR #11 的 base 为 `main`、compare 为 `feat/status-c`，方向已正确；仍需补齐 Issue 关联、修正测试命令中的本机绝对路径和测试脚本比较表达式，并请 B 正式评审。PR #6、#7、#8 为方向错误或零差异的无效记录，不作为 C 的主要 PR。C 还需正式评审 A 的 PR #2。
- **最终索引**：A 已在分支 `docs/submission-a` 创建 PR [#4](https://github.com/yokeres/iot-repair-group03/pull/4)，待 C 的有效 PR 和三人评审补齐后完成最终核验并合并。

## 交叉评审顺序

按 A 审 B、B 审 C、C 审 A 执行。评审必须说明具体检查依据，并使用 `Review changes` 提交 `Approve` 或 `Request changes`。

最终以最新 `main` 下载 ZIP 后的复测结果为准。
