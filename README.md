# oss-radar

向阳的长期探索底本：我需要什么（needs）、外面已有什么（每个需求的开源 Top3）、我自己做到哪（projects）。

- 雷达页面：https://claude.ai/artifact/NjUZfiSnYw3iTi5FTtTzEJ （Claude 每天调研并更新）
- 协作规则：见 `AGENTS.md`
- 评选规则：见 `RULES.md`

## 三方怎么配合

```
向阳 / Codex ──写入──▶ 本仓库（needs 新增、projects 进展）
                          │
                 Claude 每日任务读取
                          ▼
              雷达页面（调研 Top3、自研判断）
                          │
              按需导出快照回写到本仓库
```

## 每个需求怎样越挖越深

一个需求文件回答「外面做到哪」，关联它的项目文件回答「我做到哪」，项目的 `next` 回答「下一步缺什么」。新的发现写回这三处，名单就会越挖越深。
