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
- [x] 状态图与简单类图：`docs/models.md`、`docs/assets/state.*`、`docs/assets/class.*`
- [x] Python 状态函数：`src/python/status_rule.py`
- [x] 4 项测试及真实输出：`docs/test-results.md`
- [x] 当前 `main` ZIP 复测：2026-11-10，`4/4 passed`，退出码 `0`
- [x] A 的实验二个人小结：`docs/experiment-two-summary-a.md`
- [x] 三人任务 Issue、主要 PR 与交叉评审记录已提交

## 运行

在 `src/python` 目录运行：

```bash
python3 test_status_rule.py
```

预期 `Summary: 4/4 passed`，退出码为 `0`。

## 协作进度

- **A**：Issue [#1](https://github.com/yokeres/iot-repair-group03/issues/1)，分支 `docs/requirements-a`，主要 PR [#2](https://github.com/yokeres/iot-repair-group03/pull/2) 已合并。C 已按需求、用例图和状态一致性提交评审记录。
- **B**：Issue [#3](https://github.com/yokeres/iot-repair-group03/issues/3)，分支 `docs/models-b`，主要 PR [#5](https://github.com/yokeres/iot-repair-group03/pull/5) 已合并。A 已完成内容核验并正式批准（[评审记录](https://github.com/yokeres/iot-repair-group03/pull/5#pullrequestreview-5796960897)）。
- **C**：任务 Issue [#10](https://github.com/yokeres/iot-repair-group03/issues/10)，分支 `feat/status-c`，主要 PR [#11](https://github.com/yokeres/iot-repair-group03/pull/11) 已合并。测试记录使用 C 的 GitHub 用户名并保留真实 `4/4 passed` 输出。
- **最终索引**：A 的收尾 PR [#4](https://github.com/yokeres/iot-repair-group03/pull/4) 已合并，`docs/submission.md` 登记最终仓库、Issue、PR、评审和复测信息。

## 交叉评审顺序

按 A 审 B、B 审 C、C 审 A 执行。评审必须说明具体检查依据，并使用 `Review changes` 提交 `Approve` 或 `Request changes`。

最终以最新 `main` 下载 ZIP 后的复测结果为准。
