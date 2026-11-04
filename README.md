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
- [x] 状态图与简单类图：`docs/models.md`
- [x] Python 状态函数：`src/python/status_rule.py`
- [x] 4 项测试记录：`docs/test-results.md`
- [x] 个人分支、PR、交叉评审与最终提交索引按 GitHub 协作流程补充

## 运行

在 `src/python` 目录运行：

```bash
python3 test_status_rule.py
```

预期 `Summary: 4/4 passed`，退出码为 `0`。

## 协作

每人一个个人任务 Issue、个人分支和主要 PR；按 A 审 B、B 审 C、C 审 A 的顺序交叉评审，修订后合入 `main`。最终以最新 `main` 下载 ZIP 后复测的结果为准。

- A：仓库初始化、需求说明与用例图，负责 `docs/requirements.md`、`docs/usecase.md` 及提交索引整理。
- B：状态图、简单类图与源材料，负责 `docs/models.md` 及图表原稿。
- C（Sunsh-212）：负责状态判断函数与测试验收，主要提交内容包括：
  - 个人任务 Issue：`状态规则与测试验收`
  - 个人分支：`Sunsh-212/status-rule`
  - 主要 PR：`feat: implement work-order status transition rule and validation tests`
  - 代码文件：`src/python/status_rule.py`
  - 测试记录：`docs/test-results.md`
  - 交叉评审：B 审 C，C 审 A
  - 最终验证：在更新后的 `main` 分支下载 ZIP 后复测，结果仍为 `Summary: 4/4 passed`，退出码为 `0`

本次实验中，C 的工作已在个人分支上完成实现，并���过最终 ZIP 复测确认状态规则与测试结果一致，符合实验要求。