# 实验一个人小结与体会（A）

- 姓名/角色：组长 A
- GitHub 用户名：yokeres
- 个人分支：`docs/requirements-a`

## 本人完成的内容

1. 分析校园物联网设备报修场景，完成 `docs/requirements.md` 中的 FR-01、FR-02、FR-03，写明角色、前提、输入、正常结果、异常结果和验收方法。
2. 完成 `docs/usecase.md`，说明报修人和维修人员两个参与者及查看设备、提交报修、更新工单状态三个用例。
3. 完成标准用例图及可编辑源文件：`docs/assets/usecase.png`、`docs/assets/usecase.puml`。
4. 完成仓库初始化、README 成员登记和提交索引模板。

## 一次检查与修订

检查用例图显示时发现 SVG 在 GitHub 页面中无法直接渲染，因此保留 PlantUML 源文件并导出 PNG，改为在 `usecase.md` 中引用 `usecase.png`，确保教师可以直接查看图形且组员仍可编辑源材料。

## 对协作流程的理解

个人分支从 `main` 创建后，分支上的提交不会立即出现在 `main`。只有经过 Pull Request 评审并合并后，修改才进入 `main`，因此个人修改与共享版本相互隔离。

## 待后续实验完成

- A 的任务 Issue 与主要 PR
- 三人交叉评审记录
- 最新 `main` 的最终 ZIP 复测
