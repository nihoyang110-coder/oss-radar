# AGENTS.md：oss-radar 协作规则

这个仓库是蔡向阳的「需求 × 开源 × 自有项目」总档案。三方共同维护：

- **Claude**：每天的雷达任务负责外部调研，即每个需求的 Top3、自研判断，并把仓库同步到雷达页面。
- **Codex**：负责把自己做过、正在做的项目成果写进 `projects/`，提出新需求，记录探索进展。
- **向阳本人**：最终拍板，可以直接改任何文件。

所有内容用中文书写，日文专有名词保留原文。

## 目录

| 路径 | 内容 | 谁来改 |
|---|---|---|
| `needs/<id>.json` | 一个需求一份：说明、Top3 开源项目、自研判断 | 字段分工见下 |
| `projects/<id>.json` | 一个自有项目一份：做到哪、和哪些需求相关、下一步 | Codex / 本人 |
| `log/YYYY-MM-DD.md` | 当天谁改了什么，一行一条 | 所有人追加 |
| `RULES.md` | 开源项目的评选规则 | 只有本人改 |
| `scripts/validate.py` | 格式检查，提交前必须通过 | 不要改 |

## needs/：字段分工

- **Codex 可以改**：`name`、`group`、`order`、`note`；可以新建需求文件，此时 `status` 写 `"待调研"`、`top` 写 `[]`，其余字段留空字符串。
- **只有 Claude 改**：`top`、`build`、`change`、`status`、`updatedAt`、`loop`。Codex 不要动这几个字段。对排名有意见时，写进 `log/` 或项目的 `next`，下次雷达复核时处理。
- `id` 用小写英文加连字符，和文件名一致，建成后不要改。

## projects/：怎样记录自己的成果

每个项目一个文件。现有字段：`cat`（分类）、`name`、`desc`（一句话）、`source`（Claude / Codex / 工作区）、`stage`、`position`（和开源对比后的定位）、`similar`（同类开源）、`improve`（可借鉴的改进）、`order`。

Codex 更新项目时，额外维护这几个字段：

```json
"needs": ["job-agent", "resume"],
"repo": "https://github.com/…（没有就留空）",
"progress": [
  {"date": "2026-10-20", "by": "Codex", "done": "doda 列表抓取跑通，200 条职位入库"}
],
"next": "接入履歴書 PDF 模板"
```

- `needs`：这个项目回应的需求 id，至少一个。如果没有合适的需求，先在 `needs/` 新建一个。
- `progress`：只追加，不删旧条目，最新的放在最后。一条写一件已经完成、可以验证的事，不写计划。
- `stage` 用这几档之一：`构想`、`立项`、`原型`、`MVP`、`试运行`、`日常在用`、`暂停`。
- `next`：下一步只写一件最重要的事。

## 每次工作的流程

1. 先 `git pull`。
2. 修改或新增文件。
3. 运行 `python3 scripts/validate.py`，必须显示 OK。
4. 在 `log/今天日期.md` 追加一行，例如 `- Codex：projects/p-job 新增进展「doda 抓取跑通」`。
5. 提交，commit message 用中文一句话，然后 `git push`。

## 不要写进仓库的内容

本仓库可能公开，因此不要写入：密码、API Key、Token、个人住址、电话、证件号、客户与合作方的真实姓名或未公开的商业信息、他人的个人信息。需要时写成「某酒店」「某客户」。
