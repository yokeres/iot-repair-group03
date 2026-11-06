
# 校园物联网设备报修实验

组号：03

| 成员 | 角色 | GitHub 用户名 | 主要成果 |
| --- | --- | --- | --- |
| A | 组长 | yokeres | 需求说明、用例图、仓库初始化与提交索引 |
| B | 组员 | Esponjs | 状态图、简单类图及源材料 |
| C | 组员 | Sunsh-212 | Python 状态函数、测试记录与真实测试输出 |

本组选定语言：**Python 3**

## 范围

只分析查看设备、提交报修、更新工单状态三项功能，只编程实现状态判断函数。

不接入真实硬件，不实现数据库、网页、登录或 MQTT。

## 固定规则

新工单为 `PENDING`。仅允许 `PENDING → PROCESSING`、`PROCESSING → COMPLETED`，其他转换一律拒绝，包括状态不变。

## 实验成果

- [x] 3 条功能需求：`docs/requirements.md`
- [x] 用例图与可编辑源文件：`docs/usecase.md`、`docs/assets/usecase.png`、`docs/assets/usecase.puml`
- [x] 状态图与简单类图内容：`docs/models.md`（B 的个人分支待创建 PR）
- [x] Python 状态函数：`src/python/status_rule.py`
- [x] 4 项测试及真实输出：`docs/test-results.md`
- [x] 最新 `main` ZIP 复测：2026-11-06，`4/4 passed`，退出码 `0`
- [ ] 个人分支、PR、交叉评审与最终提交索引全部完成

## 运行

在 `src/python` 目录运行：

```bash
python3 test_status_rule.py
```

预期 `Summary: 4/4 passed`，退出码为 `0`。

## 协作进度

- **A**：Issue [#1](https://github.com/yokeres/iot-repair-group03/issues/1)，分支 `docs/requirements-a`，主要 PR [#2](https://github.com/yokeres/iot-repair-group03/pull/2)。已请求 C 评审；目前 C 仅留下评论，仍需正式提交 `Approve` 或 `Request changes`。
- **B**：Issue [#3](https://github.com/yokeres/iot-repair-group03/issues/3)，分支 `docs/models-b` 已完成状态图、类图和可编辑源文件，尚需创建 PR 并请求 A 评审。
- **C**：分支 `feat/status-c` 当前与 `main` 相同，尚需创建任务 Issue、提交自己的测试记录并创建 PR；同时需正式评审 A 的 PR #2。
- **最终索引**：A 已在分支 `docs/submission-a` 创建 PR [#4](https://github.com/yokeres/iot-repair-group03/pull/4)，待 B、C 的 PR 完成后补全真实链接再合并。

## 交叉评审顺序

按 A 审 B、B 审 C、C 审 A 执行。评审必须说明具体检查依据，并使用 `Review changes` 提交 `Approve` 或 `Request changes`。

最终以最新 `main` 下载 ZIP 后的复测结果为准。
