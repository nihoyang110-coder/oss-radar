# 外部资源 Top3：逐项目对比

核验日期：2026-10-13。只展示每项最多三个合格推荐，自建状况独立放在[自建项目评价](SELF-BUILT.md)。分数与不确定性见[方法](METHOD.md)，全量候选取舍见[审计记录](AUDIT.md)。

星数为本轮读取快照。所有候选均未在本轮安装或运行；能力来自README，适配和排序是建议。总分区间包含增长、语言两项待核，不代表效果评分。

<a id="p-design-runtime"></a>
## 设计 Agent Runtime（Univer + Blender）

项目要解决：结构化建筑 API → 校验器 → 审图 → 草稿 → 人工审批，Agent 永不覆盖已审批文件。 本轮重点：Gate 2至4尚未完成，不能把局部成功说成完整设计运行时。

搜索：`blender MCP`；卡ID `github-20261013-15`（同组复用）。 [自建不足](SELF-BUILT.md#p-design-runtime) · [候选取舍](AUDIT.md#p-design-runtime)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [dream-num/univer](https://github.com/dream-num/univer) | 80–92 | 30/29/6/5/10 | 22,583 | 2026-10-13 | Apache-2.0 |
| 2. [blender/blender](https://github.com/blender/blender) | 79–91 | 30/29/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 3. [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | 77–89 | 30/25/8/7/7 | 34,238 | 2026-10-13 | LGPL-2.1 |

### 1. dream-num/univer
- 能做什么：可嵌入的表格、文档等办公应用SDK。
- 为什么保留：可复用表格编辑、插件接口和参数录入界面。 适配判断29/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：部分功能属于商业扩展；它不负责几何内核或设计正确性。
- 与自建比较：当前缺口是“Gate 2至4尚未完成，不能把局部成功说成完整设计运行时。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/dream-num/univer/tree/301e357e5df2cee47f3071f47eee366622d14641#readme) · [仓库元数据](https://api.github.com/repos/dream-num/univer) · [成熟发行 v0.1.1](https://github.com/dream-num/univer/releases/tag/v0.1.1)（2024-03-01）。

### 2. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断29/30；按统一权重已知分79，在本项目候选中列第2。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“Gate 2至4尚未完成，不能把局部成功说成完整设计运行时。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 3. FreeCAD/FreeCAD
- 能做什么：参数化实体、尺寸约束与工程建模。
- 为什么保留：可补尺寸驱动、保存重开和工程导出基础。 适配判断25/30；按统一权重已知分77，在本项目候选中列第3。
- 代价和不能替代的部分：不是日本规范验算或施工批准工具；跨软件交换需单独测试。
- 与自建比较：当前缺口是“Gate 2至4尚未完成，不能把局部成功说成完整设计运行时。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/FreeCAD/FreeCAD/tree/c8c9ea855080c9e0f2f22b583cddbed1c0cf2a07#readme) · [仓库元数据](https://api.github.com/repos/FreeCAD/FreeCAD) · [成熟发行 0.15](https://github.com/FreeCAD/FreeCAD/releases/tag/0.15)（2015-07-03）。

采用前同样本检查：先完成Gate 2同一参数变更在表格与模型两端的回读一致性。

<a id="p-furniture"></a>
## 家具模型库（代码生成）

项目要解决：看真实房屋照片，用代码复刻家具，沉淀成非商用模型库。 本轮重点：本轮未重新运行26套生成器，现存预览不能证明仍可生成。

搜索：`parametric CAD`；卡ID `github-20261013-13`（同组复用）。 [自建不足](SELF-BUILT.md#p-furniture) · [候选取舍](AUDIT.md#p-furniture)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [CadQuery/cadquery](https://github.com/CadQuery/cadquery) | 79–91 | 30/30/4/5/10 | 5,925 | 2026-10-10 | Apache-2.0 |
| 2. [princeton-vl/infinigen](https://github.com/princeton-vl/infinigen) | 78–90 | 30/30/4/4/10 | 7,321 | 2026-10-08 | BSD-3-Clause |
| 3. [blender/blender](https://github.com/blender/blender) | 78–90 | 30/28/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |

### 1. CadQuery/cadquery
- 能做什么：用Python脚本生成可复用的参数化CAD实体。
- 为什么保留：适合家具及构件批量参数化、尺寸回归。 适配判断30/30；按统一权重已知分79，在本项目候选中列第1。
- 代价和不能替代的部分：不是完整设计协作界面；依赖CAD内核和Python环境。
- 与自建比较：当前缺口是“本轮未重新运行26套生成器，现存预览不能证明仍可生成。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/CadQuery/cadquery/tree/5f5bc62b255f62e3512105740025361b6c31eddd#readme) · [仓库元数据](https://api.github.com/repos/CadQuery/cadquery) · [成熟发行 2.0](https://github.com/CadQuery/cadquery/releases/tag/2.0)（2020-04-24）。

### 2. princeton-vl/infinigen
- 能做什么：基于程序规则生成场景与资产，包含家具和室内生成方向。
- 为什么保留：可借鉴部件生成、随机参数及大批量场景验证。 适配判断30/30；按统一权重已知分78，在本项目候选中列第2。
- 代价和不能替代的部分：科研和程序生成工作流；计算开销高，生成资产不等于可制造尺寸。
- 与自建比较：当前缺口是“本轮未重新运行26套生成器，现存预览不能证明仍可生成。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/princeton-vl/infinigen/tree/a0d1a0dd5644904d3cb921ff24260160ac06ae08#readme) · [仓库元数据](https://api.github.com/repos/princeton-vl/infinigen) · [成熟发行 v1.0.1](https://github.com/princeton-vl/infinigen/releases/tag/v1.0.1)（2023-07-01）。

### 3. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断28/30；按统一权重已知分78，在本项目候选中列第3。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“本轮未重新运行26套生成器，现存预览不能证明仍可生成。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

采用前同样本检查：抽一套家具在三个尺寸档生成，核对尺寸、碰撞和可编辑结构。

<a id="p-housing-views"></a>
## 住宅观点 md（可加载的“我”）

项目要解决：把自己对住宅的观点写成 md，别人加载进 AI 就能和“我”讨论，结果回流给我。 本轮重点：没有可核验正文，不能声称已建立个人住宅观点库。

搜索：`knowledge management`；卡ID `github-20261013-16`（同组复用）。 [自建不足](SELF-BUILT.md#p-housing-views) · [候选取舍](AUDIT.md#p-housing-views)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) | 80–92 | 30/29/8/8/5 | 46,741 | 2026-10-04 | AGPL-3.0 |
| 2. [foambubble/foam](https://github.com/foambubble/foam) | 79–91 | 30/27/6/6/10 | 17,446 | 2026-10-12 | MIT |
| 3. [logseq/logseq](https://github.com/logseq/logseq) | 74–86 | 30/26/8/5/5 | 45,220 | 2026-10-13 | AGPL-3.0 |

### 1. siyuan-note/siyuan
- 能做什么：重视隐私与块级引用的个人知识管理系统。
- 为什么保留：可补引用、检索、结构化笔记和中文编辑。 适配判断29/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：部分同步等功能付费；不能自动保证来源正确或学习效果。
- 与自建比较：当前缺口是“没有可核验正文，不能声称已建立个人住宅观点库。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/siyuan-note/siyuan/tree/fb3355f07d22bff36f1d785999fd5ded6a90d468#readme) · [仓库元数据](https://api.github.com/repos/siyuan-note/siyuan) · [成熟发行 v0.1.0](https://github.com/siyuan-note/siyuan/releases/tag/v0.1.0)（2020-08-31）。

### 2. foambubble/foam
- 能做什么：建立在VSCode和Markdown文件上的知识管理。
- 为什么保留：适合保留可版本控制的文本与链接关系。 适配判断27/30；按统一权重已知分79，在本项目候选中列第2。
- 代价和不能替代的部分：偏开发者环境，移动操作和非技术使用者体验需另验证。
- 与自建比较：当前缺口是“没有可核验正文，不能声称已建立个人住宅观点库。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/foambubble/foam/tree/6acaa0b10d8198f096a6c2462a227674de322a48#readme) · [仓库元数据](https://api.github.com/repos/foambubble/foam) · [成熟发行 v0.2.0](https://github.com/foambubble/foam/releases/tag/v0.2.0)（2020-07-12）。

### 3. logseq/logseq
- 能做什么：大纲式个人知识管理，当前主线含数据库图谱方向。
- 为什么保留：可借鉴块级记录、链接和每日笔记组织。 适配判断26/30；按统一权重已知分74，在本项目候选中列第3。
- 代价和不能替代的部分：当前README明确数据库版beta、移动与实时协作alpha及数据丢失风险，不能直接迁移唯一权威库。
- 与自建比较：当前缺口是“没有可核验正文，不能声称已建立个人住宅观点库。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/logseq/logseq/tree/7dfa9b45aee9d6a9387ddb3375018356f1e7c6a8#readme) · [仓库元数据](https://api.github.com/repos/logseq/logseq) · [成熟发行 v0.0.1](https://github.com/logseq/logseq/releases/tag/v0.0.1)（2020-10-01）。

采用前同样本检查：先定位唯一权威稿；找不到则只保留构想，不生成替代性事实。

<a id="p-cad"></a>
## CAD 转换与结构软件 MCP

项目要解决：施工图 PDF → 1:1 可编辑 DXF；SAP2000 接 MCP。 本轮重点：AutoCAD内的独立DIST测距尚未完成。

搜索：`DXF PDF`；卡ID `github-20261013-14`（同组复用）。 [自建不足](SELF-BUILT.md#p-cad) · [候选取舍](AUDIT.md#p-cad)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [pymupdf/PyMuPDF](https://github.com/pymupdf/PyMuPDF) | 76–88 | 30/29/6/6/5 | 10,896 | 2026-10-12 | AGPL-3.0 |
| 2. [LibreCAD/LibreCAD](https://github.com/LibreCAD/LibreCAD) | 73–85 | 30/25/4/8/6 | 6,475 | 2026-10-13 | GPL-2.0 |
| 3. [BentleySystems/openstaad-mcp](https://github.com/BentleySystems/openstaad-mcp) | 65–77 | 30/21/1/3/10 | 51 | 2026-10-01 | MIT |

### 1. pymupdf/PyMuPDF
- 能做什么：PDF文本、图像、几何路径提取与渲染库。
- 为什么保留：可做PDF到CAD前的几何抽取及独立图纸回看。 适配判断29/30；按统一权重已知分76，在本项目候选中列第1。
- 代价和不能替代的部分：AGPL或商业授权边界需按实际分发方式核对；不会自动恢复完整CAD语义。
- 与自建比较：当前缺口是“AutoCAD内的独立DIST测距尚未完成。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/pymupdf/PyMuPDF/tree/de0c505f96ed3889ff119ba8e68722c5a48dd740#readme) · [仓库元数据](https://api.github.com/repos/pymupdf/PyMuPDF) · [成熟发行 v1.7](https://github.com/pymupdf/PyMuPDF/releases/tag/v1.7)（2015-11-13）。

### 2. LibreCAD/LibreCAD
- 能做什么：跨平台二维CAD，界面支持多语言。
- 为什么保留：适合DXF检查、修改与独立二维复核。 适配判断25/30；按统一权重已知分73，在本项目候选中列第2。
- 代价和不能替代的部分：不负责PDF语义重建，也不能代替SAP2000或三维BIM。
- 与自建比较：当前缺口是“AutoCAD内的独立DIST测距尚未完成。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/LibreCAD/LibreCAD/tree/08f50dee10b9291d6e19723d3c1c8d68aaaa50ef#readme) · [仓库元数据](https://api.github.com/repos/LibreCAD/LibreCAD) · [成熟发行 2.0.11](https://github.com/LibreCAD/LibreCAD/releases/tag/2.0.11)（2016-05-23）。

### 3. BentleySystems/openstaad-mcp
- 能做什么：通过MCP控制STAAD.Pro的官方接口适配器。
- 为什么保留：可借鉴结构软件工具定义、反馈和本地模型操作的接口设计。 适配判断21/30；按统一权重已知分65，在本项目候选中列第3。
- 代价和不能替代的部分：依赖STAAD.Pro与其运行环境；不是SAP2000适配器，也不自带日本规范校核。
- 与自建比较：当前缺口是“AutoCAD内的独立DIST测距尚未完成。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/BentleySystems/openstaad-mcp/tree/1b12202f2344e9d7a4981d6342840807666aee6d#readme) · [仓库元数据](https://api.github.com/repos/BentleySystems/openstaad-mcp) · [成熟发行 v1.0.0](https://github.com/BentleySystems/openstaad-mcp/releases/tag/v1.0.0)（2026-04-15）。

采用前同样本检查：在独立CAD软件复测至少十条已知尺寸，并核对单位、图层和可编辑性。

<a id="p-landscape"></a>
## 景观 AI 出图工具

项目要解决：景观设计效果图 AI 生成（C003）。 本轮重点：首次局部重绘与非蒙版区域保持尚未验收。

搜索：`ComfyUI`；卡ID `github-20261013-34`（同组复用）。 [自建不足](SELF-BUILT.md#p-landscape) · [候选取舍](AUDIT.md#p-landscape)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 80–92 | 30/30/10/4/6 | 137,283 | 2026-10-13 | GPL-3.0 |
| 2. [blender/blender](https://github.com/blender/blender) | 74–86 | 30/24/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 3. [princeton-vl/infinigen](https://github.com/princeton-vl/infinigen) | 71–83 | 30/23/4/4/10 | 7,321 | 2026-10-08 | BSD-3-Clause |

### 1. Comfy-Org/ComfyUI
- 能做什么：节点式图像、视频及其他生成模型工作流。
- 为什么保留：可保留可复用节点、输入参数与可重复的生成过程。 适配判断30/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：不同模型权重及插件许可分别核对；显存和速度随模型变化，macOS运行不等于大模型可流畅使用。
- 与自建比较：当前缺口是“首次局部重绘与非蒙版区域保持尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/Comfy-Org/ComfyUI/tree/8010b48d2c1be986613f8e8c761527d205bd756f#readme) · [仓库元数据](https://api.github.com/repos/Comfy-Org/ComfyUI) · [成熟发行 v0.0.1](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.0.1)（2024-07-12）。

### 2. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断24/30；按统一权重已知分74，在本项目候选中列第2。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“首次局部重绘与非蒙版区域保持尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 3. princeton-vl/infinigen
- 能做什么：基于程序规则生成场景与资产，包含家具和室内生成方向。
- 为什么保留：可借鉴部件生成、随机参数及大批量场景验证。 适配判断23/30；按统一权重已知分71，在本项目候选中列第3。
- 代价和不能替代的部分：科研和程序生成工作流；计算开销高，生成资产不等于可制造尺寸。
- 与自建比较：当前缺口是“首次局部重绘与非蒙版区域保持尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/princeton-vl/infinigen/tree/a0d1a0dd5644904d3cb921ff24260160ac06ae08#readme) · [仓库元数据](https://api.github.com/repos/princeton-vl/infinigen) · [成熟发行 v1.0.1](https://github.com/princeton-vl/infinigen/releases/tag/v1.0.1)（2023-07-01）。

采用前同样本检查：先做同一张图的局部重绘，量化非蒙版区域差异并人工检查。

<a id="p-land-risk"></a>
## 日本土地开发避坑软件

项目要解决：输入地块，提示用途地域、法规、手续、灾害等开发风险（C002）。 本轮重点：项目处于暂停，尚非经过专业审查的尽调产品。

搜索：`geospatial`；卡ID `github-20261013-27`（同组复用）。 [自建不足](SELF-BUILT.md#p-land-risk) · [候选取舍](AUDIT.md#p-land-risk)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [qgis/QGIS](https://github.com/qgis/QGIS) | 78–90 | 30/29/6/7/6 | 14,551 | 2026-10-13 | GPL-2.0 |
| 2. [geopandas/geopandas](https://github.com/geopandas/geopandas) | 78–90 | 30/28/4/6/10 | 5,277 | 2026-10-12 | BSD-3-Clause |
| 3. [ozekik/plateaukit](https://github.com/ozekik/plateaukit) | 64–76 | 24/24/1/5/10 | 29 | 2026-09-07 | MIT |

### 1. qgis/QGIS
- 能做什么：支持矢量、栅格等数据的跨平台GIS。
- 为什么保留：可补图层核对、坐标转换和独立空间检查。 适配判断29/30；按统一权重已知分78，在本项目候选中列第1。
- 代价和不能替代的部分：工具能叠图不代表图层时效或开发许可成立；需保留来源和专业核实。
- 与自建比较：当前缺口是“项目处于暂停，尚非经过专业审查的尽调产品。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/qgis/QGIS/tree/d835ed0a563f5c286127c6f5efbdb5b1473e9adb#readme) · [仓库元数据](https://api.github.com/repos/qgis/QGIS) · [成熟发行 final-3_16_3](https://github.com/qgis/QGIS/releases/tag/final-3_16_3)（2021-01-15）。

### 2. geopandas/geopandas
- 能做什么：Python地理数据分析与空间操作库。
- 为什么保留：可补可重复的坐标、范围和空间连接检查。 适配判断28/30；按统一权重已知分78，在本项目候选中列第2。
- 代价和不能替代的部分：坐标参考不一致仍可能产生错误；没有尽调判断和行政许可结论。
- 与自建比较：当前缺口是“项目处于暂停，尚非经过专业审查的尽调产品。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/geopandas/geopandas/tree/ee889bb6365319dee15b43ad001539ef10b090f0#readme) · [仓库元数据](https://api.github.com/repos/geopandas/geopandas) · [成熟发行 v0.2.1](https://github.com/geopandas/geopandas/releases/tag/v0.2.1)（2016-07-30）。

### 3. ozekik/plateaukit
- 能做什么：围绕日本PLATEAU三维城市数据的Python工具。
- 为什么保留：可补公开城市模型读取与研究流程。 适配判断24/30；按统一权重已知分64，在本项目候选中列第3。
- 代价和不能替代的部分：社区较小；具体地区覆盖、数据年份及数据许可需逐项确认。
- 与自建比较：当前缺口是“项目处于暂停，尚非经过专业审查的尽调产品。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/ozekik/plateaukit/tree/f55a53285d2e00a0844d0a0c9667366bdb432a89#readme) · [仓库元数据](https://api.github.com/repos/ozekik/plateaukit) · [成熟发行 v0.11.2](https://github.com/ozekik/plateaukit/releases/tag/v0.11.2)（2024-03-05）。

采用前同样本检查：保持暂停；恢复时用一个公开样本逐条核对模板的来源和待核项。

<a id="p-re-cockpit"></a>
## 房地产管理者 AI 巡检驾驶舱

项目要解决：盯开发项目、合同、手续、物业事件，带证据链（R001）。 本轮重点：后端导入与提交测试尚未完成。

搜索：`property management`；卡ID `github-20261013-40`（同组复用）。 [自建不足](SELF-BUILT.md#p-re-cockpit) · [候选取舍](AUDIT.md#p-re-cockpit)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | 79–91 | 30/29/8/6/6 | 46,611 | 2026-10-12 | GPL-3.0 |
| 2. [open-condo-software/condo](https://github.com/open-condo-software/condo) | 74–86 | 30/28/2/4/10 | 421 | 2026-10-13 | MIT |
| 3. [frappe/erpnext](https://github.com/frappe/erpnext) | 71–83 | 30/23/8/4/6 | 40,096 | 2026-10-13 | GPL-3.0 |

### 1. paperless-ngx/paperless-ngx
- 能做什么：纸质与电子文档的可搜索归档系统。
- 为什么保留：适合报表、票据和资料的文档底座。 适配判断29/30；按统一权重已知分79，在本项目候选中列第1。
- 代价和不能替代的部分：不等于房地产经营驾驶舱；权限、导入来源和业务对账需自行实现。
- 与自建比较：当前缺口是“后端导入与提交测试尚未完成。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/paperless-ngx/paperless-ngx/tree/6e717817c6cf09b4f3570db5cd4272e15ed0d7c4#readme) · [仓库元数据](https://api.github.com/repos/paperless-ngx/paperless-ngx) · [成熟发行 ngx-1.6.0](https://github.com/paperless-ngx/paperless-ngx/releases/tag/ngx-1.6.0)（2022-03-10）。

### 2. open-condo-software/condo
- 能做什么：面向物业管理的开源服务应用。
- 为什么保留：可比较物业业务对象与管理流程。 适配判断28/30；按统一权重已知分74，在本项目候选中列第2。
- 代价和不能替代的部分：部署组件较多，日本管理流程及业务数据迁移未验证。
- 与自建比较：当前缺口是“后端导入与提交测试尚未完成。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/open-condo-software/condo/tree/fd32c3e826aaaca47ebab7d4b6ba01ed666a763d#readme) · [仓库元数据](https://api.github.com/repos/open-condo-software/condo) · [成熟发行 release-v1.24.8](https://github.com/open-condo-software/condo/releases/tag/release-v1.24.8)（2021-11-03）。

### 3. frappe/erpnext
- 能做什么：集成财务、库存、人事等模块的ERP。
- 为什么保留：可对照成熟业务单据与基础管理流程。 适配判断23/30；按统一权重已知分71，在本项目候选中列第3。
- 代价和不能替代的部分：不是专门为日本物业设计，配置、迁移和专业规则验证成本高。
- 与自建比较：当前缺口是“后端导入与提交测试尚未完成。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/frappe/erpnext/tree/0b2c356ccedd7a20c67e6ad54aa298b36828e055#readme) · [仓库元数据](https://api.github.com/repos/frappe/erpnext) · [成熟发行 v3.2.0](https://github.com/frappe/erpnext/releases/tag/v3.2.0)（2013-12-12）。

采用前同样本检查：使用脱敏样本完成提交、入库、回读及重复提交检查。

<a id="p-future-home"></a>
## 未来住宅与家庭机器人研究

项目要解决：“站在未来看现在”的住宅研究、模块化智能第二居所事业构想。 本轮重点：设备能力、家庭部署与商业合作尚未验证。

搜索：`home automation`；卡ID `github-20261013-25`（同组复用）。 [自建不足](SELF-BUILT.md#p-future-home) · [候选取舍](AUDIT.md#p-future-home)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [home-assistant/core](https://github.com/home-assistant/core) | 85–97 | 30/30/8/7/10 | 91,465 | 2026-10-13 | Apache-2.0 |
| 2. [esphome/esphome](https://github.com/esphome/esphome) | 71–83 | 30/24/6/5/6 | 11,860 | 2026-10-13 | MIT / GPL-3.0（按组件） |

**只保留2个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. home-assistant/core
- 能做什么：强调本地控制的家庭自动化平台。
- 为什么保留：优先复用设备集成和自动化规则，不必重写家庭网关。 适配判断30/30；按统一权重已知分85，在本项目候选中列第1。
- 代价和不能替代的部分：具体设备型号、云依赖和断网行为仍要逐台验证；不能视作通用家务机器人。
- 与自建比较：当前缺口是“设备能力、家庭部署与商业合作尚未验证。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/home-assistant/core/tree/aeb1a1c65922739ccb8e7b9abf3d6f554299b912#readme) · [仓库元数据](https://api.github.com/repos/home-assistant/core) · [成熟发行 Last-Python2-release](https://github.com/home-assistant/core/releases/tag/Last-Python2-release)（2014-04-13）。

### 2. esphome/esphome
- 能做什么：为嵌入式设备提供配置化固件与家庭自动化集成。
- 为什么保留：可补传感器与自定义小设备接口。 适配判断24/30；按统一权重已知分71，在本项目候选中列第2。
- 代价和不能替代的部分：Python部分MIT、运行时GPL-3.0；需要适配实际硬件，不等于成品家电兼容。
- 与自建比较：当前缺口是“设备能力、家庭部署与商业合作尚未验证。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/esphome/esphome/tree/29a668af0443ab80e29fa29753a56160bbd57db3#readme) · [仓库元数据](https://api.github.com/repos/esphome/esphome) · [成熟发行 v1.1](https://github.com/esphome/esphome/releases/tag/v1.1)（2018-04-06）。

采用前同样本检查：优先验证一条小范围本地自动化，并记录断网时仍能否工作。

<a id="p-hotel-phone"></a>
## 酒店自动接电话

项目要解决：语音 AI 接电话、短信转人工、对接 PMS；北极星：客人不用重复说。 本轮重点：尚无真实电话和真实PMS端到端验收。

搜索：`voice agents`；卡ID `github-20261013-29`（同组复用）。 [自建不足](SELF-BUILT.md#p-hotel-phone) · [候选取舍](AUDIT.md#p-hotel-phone)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) | 81–93 | 30/30/6/5/10 | 16,424 | 2026-10-13 | BSD-2-Clause |
| 2. [livekit/agents](https://github.com/livekit/agents) | 80–92 | 30/29/6/5/10 | 14,726 | 2026-10-13 | Apache-2.0 |
| 3. [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | 76–88 | 30/27/4/5/10 | 5,860 | 2026-10-13 | BSD-2-Clause |

### 1. pipecat-ai/pipecat
- 能做什么：Python实时语音和多模态对话管线框架。
- 为什么保留：适合语音传输、识别、合成及对话流程的模块替换。 适配判断30/30；按统一权重已知分81，在本项目候选中列第1。
- 代价和不能替代的部分：需要自己接电话与业务工具；不是PMS成品，延迟和中日切换需实呼测量。
- 与自建比较：当前缺口是“尚无真实电话和真实PMS端到端验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/pipecat-ai/pipecat/tree/24007373eea11403047a681e9ea0470ddef1fc89#readme) · [仓库元数据](https://api.github.com/repos/pipecat-ai/pipecat) · [成熟发行 v0.0.2](https://github.com/pipecat-ai/pipecat/releases/tag/v0.0.2)（2024-05-14）。

### 2. livekit/agents
- 能做什么：基于WebRTC生态的实时语音代理框架。
- 为什么保留：可借鉴端侧SDK、会话和语义轮次检测。 适配判断29/30；按统一权重已知分80，在本项目候选中列第2。
- 代价和不能替代的部分：自托管与云服务成本不同；电话和PMS集成仍需开发。
- 与自建比较：当前缺口是“尚无真实电话和真实PMS端到端验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/livekit/agents/tree/fe5a00b9447541436e3b4f04ee15c79766d240c7#readme) · [仓库元数据](https://api.github.com/repos/livekit/agents) · [成熟发行 livekit-agents@0.8.0](https://github.com/livekit/agents/releases/tag/livekit-agents%400.8.0)（2024-07-24）。

### 3. dograh-hq/dograh
- 能做什么：带自部署入口和电话工作流的语音代理应用。
- 为什么保留：可作为更完整的电话运营界面与配置流程对照。 适配判断27/30；按统一权重已知分76，在本项目候选中列第3。
- 代价和不能替代的部分：默认快速启动可能开放外网隧道与注册；须逐项配置，实呼表现未测。
- 与自建比较：当前缺口是“尚无真实电话和真实PMS端到端验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/dograh-hq/dograh/tree/0a5564fd50911cdc70829506f3c04a64d8633255#readme) · [仓库元数据](https://api.github.com/repos/dograh-hq/dograh) · [成熟发行 dograh-copy-v1.1.0](https://github.com/dograh-hq/dograh/releases/tag/dograh-copy-v1.1.0)（2025-10-10）。

采用前同样本检查：具备账号与号码后，完成一次受控实呼并记录延迟、转人工及最终记录。

<a id="p-tender-sim"></a>
## 酒店招标桌面推演

项目要解决：基于某酒店真实招标的多角色推演，事实与模拟判断分开记录。 本轮重点：模拟还未证明能提高现实招标决策，也不是造价证据。

搜索：`agent simulation`；卡ID `github-20261013-42`（同组复用）。 [自建不足](SELF-BUILT.md#p-tender-sim) · [候选取舍](AUDIT.md#p-tender-sim)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [google-deepmind/concordia](https://github.com/google-deepmind/concordia) | 77–89 | 30/30/3/4/10 | 1,773 | 2026-10-12 | Apache-2.0 |
| 2. [mesa/mesa](https://github.com/mesa/mesa) | 75–87 | 30/26/4/5/10 | 3,881 | 2026-10-09 | Apache-2.0 |
| 3. [camel-ai/oasis](https://github.com/camel-ai/oasis) | 69–81 | 30/22/4/3/10 | 5,268 | 2026-10-12 | Apache-2.0 |

### 1. google-deepmind/concordia
- 能做什么：生成式主体社会模拟框架。
- 为什么保留：贴近角色、事件与情景推演，可固定实验输入。 适配判断30/30；按统一权重已知分77，在本项目候选中列第1。
- 代价和不能替代的部分：模拟人的反应不等于真实市场或工程决策，需记录假设和现实验证。
- 与自建比较：当前缺口是“模拟还未证明能提高现实招标决策，也不是造价证据。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/google-deepmind/concordia/tree/70aa01cca819bbfad43face568010891a0cd90aa#readme) · [仓库元数据](https://api.github.com/repos/google-deepmind/concordia) · [成熟发行 v1.0.0](https://github.com/google-deepmind/concordia/releases/tag/v1.0.0)（2023-12-08）。

### 2. mesa/mesa
- 能做什么：Python的基于主体的模拟框架。
- 为什么保留：适合显式规则、重复实验和随机种子控制。 适配判断26/30；按统一权重已知分75，在本项目候选中列第2。
- 代价和不能替代的部分：不是LLM自动替代现实；模型假设和现实校准需自己负责。
- 与自建比较：当前缺口是“模拟还未证明能提高现实招标决策，也不是造价证据。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/mesa/mesa/tree/5451086fe47ab78e9ba894aa1b4c3063f4c247f1#readme) · [仓库元数据](https://api.github.com/repos/mesa/mesa) · [成熟发行 v1.1.1](https://github.com/mesa/mesa/releases/tag/v1.1.1)（2022-10-21）。

### 3. camel-ai/oasis
- 能做什么：围绕多主体社会互动的模拟框架。
- 为什么保留：可借鉴大量角色的互动与观测机制。 适配判断22/30；按统一权重已知分69，在本项目候选中列第3。
- 代价和不能替代的部分：偏社会平台而非工程招标，模型调用和运行成本较高。
- 与自建比较：当前缺口是“模拟还未证明能提高现实招标决策，也不是造价证据。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/camel-ai/oasis/tree/bc805a19978a620bb400f4c644ce9d772ccbfc70#readme) · [仓库元数据](https://api.github.com/repos/camel-ai/oasis) · [成熟发行 v0.1.1](https://github.com/camel-ai/oasis/releases/tag/v0.1.1)（2025-04-25）。

采用前同样本检查：固定同一标段情景，仅改变一个压力条件，比较责任与决策变化。

<a id="p-yangzai"></a>
## 阳仔（多模型编排）

项目要解决：协调 Claude / Codex / Gemini / Kimi，跨模型盲审，记录回放会话，逐步自动化。 本轮重点：项目仍暂停，整体工作台没有验收。

搜索：`coding agents`；卡ID `github-20261013-45`（同组复用）。 [自建不足](SELF-BUILT.md#p-yangzai) · [候选取舍](AUDIT.md#p-yangzai)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | 83–95 | 30/30/8/5/10 | 39,862 | 2026-10-13 | MIT |
| 2. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 80–92 | 30/28/8/4/10 | 90,792 | 2026-10-13 | MIT |
| 3. [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | 76–88 | 30/24/6/6/10 | 28,461 | 2026-10-13 | Apache-2.0 |

### 1. Yeachan-Heo/oh-my-claudecode
- 能做什么：围绕Claude Code的代理协作与编排扩展。
- 为什么保留：可比较任务编排、协作状态和工具组织。 适配判断30/30；按统一权重已知分83，在本项目候选中列第1。
- 代价和不能替代的部分：依赖特定代理环境并快速变化；同任务成本和失败恢复未在本地验证。
- 与自建比较：当前缺口是“项目仍暂停，整体工作台没有验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/Yeachan-Heo/oh-my-claudecode/tree/7eb8f08fc13ad253c41bd58763b3c185c7047932#readme) · [仓库元数据](https://api.github.com/repos/Yeachan-Heo/oh-my-claudecode) · [成熟发行 v1.2.1](https://github.com/Yeachan-Heo/oh-my-claudecode/releases/tag/v1.2.1)（2026-01-09）。

### 2. OpenHands/OpenHands
- 能做什么：支持多运行后端的代码代理平台。
- 为什么保留：可借鉴执行环境、工作空间和任务操作。 适配判断28/30；按统一权重已知分80，在本项目候选中列第2。
- 代价和不能替代的部分：平台较重且有企业部分；受控执行与权限隔离须另验收。
- 与自建比较：当前缺口是“项目仍暂停，整体工作台没有验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/OpenHands/OpenHands/tree/62491b193d5924d9f1a1fbcec0ebed93c7962128#readme) · [仓库元数据](https://api.github.com/repos/OpenHands/OpenHands) · [成熟发行 0.6.1](https://github.com/OpenHands/OpenHands/releases/tag/0.6.1)（2024-06-04）。

### 3. QwenLM/qwen-code
- 能做什么：支持多模型协议的终端代码代理。
- 为什么保留：可比较多提供商接口和代码工作流。 适配判断24/30；按统一权重已知分76，在本项目候选中列第3。
- 代价和不能替代的部分：需要模型端点与开发环境；不能直接证明多人多终端恢复可靠。
- 与自建比较：当前缺口是“项目仍暂停，整体工作台没有验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/QwenLM/qwen-code/tree/53579861dabaf32ed4433f13996c3adb2ea7e79a#readme) · [仓库元数据](https://api.github.com/repos/QwenLM/qwen-code) · [成熟发行 v0.0.2](https://github.com/QwenLM/qwen-code/releases/tag/v0.0.2)（2025-08-01）。

采用前同样本检查：维持暂停；恢复时用单任务比较一个成熟编排器与现有方案的总成本。

<a id="p-koyo"></a>
## KOYO（指挥官式多终端外壳）

项目要解决：真终端跑官方 Claude Code，指挥官派活、收文件化汇报、验收，可请 GPT 复审。 本轮重点：验收仅限该修复范围，不能推成全部多终端场景稳定。

搜索：`coding agent terminal`；卡ID `github-20261013-33`（同组复用）。 [自建不足](SELF-BUILT.md#p-koyo) · [候选取舍](AUDIT.md#p-koyo)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | 81–93 | 30/29/6/6/10 | 28,346 | 2026-09-19 | Apache-2.0 |
| 2. [smtg-ai/claude-squad](https://github.com/smtg-ai/claude-squad) | 69–81 | 24/30/4/6/5 | 8,593 | 2026-08-20 | AGPL-3.0 |

**只保留2个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. BloopAI/vibe-kanban
- 能做什么：以任务看板与工作空间组织代码代理执行。
- 为什么保留：可借鉴计划、工作空间、审查与任务连接。 适配判断29/30；按统一权重已知分81，在本项目候选中列第1。
- 代价和不能替代的部分：旧记录曾标停更，本轮已核见近期更新；迁移不能丢弃已有状态与审计。
- 与自建比较：当前缺口是“验收仅限该修复范围，不能推成全部多终端场景稳定。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/BloopAI/vibe-kanban/tree/d5cbb5380fa0b32e98ef9b8d987f63decce4be3a#readme) · [仓库元数据](https://api.github.com/repos/BloopAI/vibe-kanban) · [成熟发行 v0.0.29](https://github.com/BloopAI/vibe-kanban/releases/tag/v0.0.29)（2025-07-01）。

### 2. smtg-ai/claude-squad
- 能做什么：管理多个代码代理与独立工作空间的终端应用。
- 为什么保留：与多终端外壳的工作区隔离和任务切换较贴近。 适配判断30/30；按统一权重已知分69，在本项目候选中列第2。
- 代价和不能替代的部分：依赖外部代码代理；状态验收及长时运行需自行测试。
- 与自建比较：当前缺口是“验收仅限该修复范围，不能推成全部多终端场景稳定。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/smtg-ai/claude-squad/tree/ce1ffb4392b01f38e2c4599c7c84d2a93973b138#readme) · [仓库元数据](https://api.github.com/repos/smtg-ai/claude-squad) · [成熟发行 v1.0.0](https://github.com/smtg-ai/claude-squad/releases/tag/v1.0.0)（2025-04-03）。

采用前同样本检查：让一项任务经历终端重启和会话恢复，检查状态与输出是否一致。

<a id="p-hakuu"></a>
## Hakuu（个人 AI 系统）

项目要解决：Claude Code + Codex 双终端、受控本地操作、连接器、状态与恢复证据。 本轮重点：真实反向执行和整体接续尚未验收。

搜索：`personal AI assistant`；卡ID `github-20261013-28`（同组复用）。 [自建不足](SELF-BUILT.md#p-hakuu) · [候选取舍](AUDIT.md#p-hakuu)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [openclaw/openclaw](https://github.com/openclaw/openclaw) | 82–94 | 30/27/10/5/10 | 391,852 | 2026-10-13 | MIT |
| 2. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 81–93 | 30/26/10/5/10 | 253,353 | 2026-10-13 | MIT |
| 3. [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) | 76–88 | 24/27/8/7/10 | 33,488 | 2026-09-09 | Apache-2.0 |

### 1. openclaw/openclaw
- 能做什么：支持多通信渠道的个人AI助手运行平台。
- 为什么保留：可对照渠道接入、本地状态和个人助手工作流。 适配判断27/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：广泛工具权限增加配置与维护复杂度；不会自动遵守自有确认协议。
- 与自建比较：当前缺口是“真实反向执行和整体接续尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/openclaw/openclaw/tree/f3e011a6bdd3d76a61c4cb91296d17285f8c9229#readme) · [仓库元数据](https://api.github.com/repos/openclaw/openclaw) · [成熟发行 v0.1.1](https://github.com/openclaw/openclaw/releases/tag/v0.1.1)（2025-11-25）。

### 2. NousResearch/hermes-agent
- 能做什么：包含工具、记忆和多平台部署入口的AI代理。
- 为什么保留：可对照已有个人协作系统的运行壳和工具接口。 适配判断26/30；按统一权重已知分81，在本项目候选中列第2。
- 代价和不能替代的部分：需配置模型与运行环境；跨模型交接是否可靠仍需同任务实测。
- 与自建比较：当前缺口是“真实反向执行和整体接续尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/NousResearch/hermes-agent/tree/6e7b83a2f1c093e992a8d838ed77ea320fbd8e51#readme) · [仓库元数据](https://api.github.com/repos/NousResearch/hermes-agent) · [成熟发行 v2026.3.12](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.3.12)（2026-03-12）。

### 3. iOfficeAI/AionUi
- 能做什么：将多种代理接入桌面协作界面的应用。
- 为什么保留：可借鉴可见操作、统一会话和桌面交互。 适配判断27/30；按统一权重已知分76，在本项目候选中列第3。
- 代价和不能替代的部分：不同代理的权限、状态和会话接续不是天然一致；不要平行维护第二账本。
- 与自建比较：当前缺口是“真实反向执行和整体接续尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/iOfficeAI/AionUi/tree/6744099b279b991c17e31c243f0920477bd31cb6#readme) · [仓库元数据](https://api.github.com/repos/iOfficeAI/AionUi) · [成熟发行 v1.0.0](https://github.com/iOfficeAI/AionUi/releases/tag/v1.0.0)（2025-08-07）。

采用前同样本检查：做一次可回读的双向交接，分别记录四种状态并注入一次超时。

<a id="p-memory-sync"></a>
## AI 记忆接口（多模型同步）

项目要解决：跨模型共享经授权的项目事实与交接；各模型私有记忆不互相导入。 本轮重点：自动同步和多端接续尚未验证。

搜索：`AI memory`；卡ID `github-20261013-37`（同组复用）。 [自建不足](SELF-BUILT.md#p-memory-sync) · [候选取舍](AUDIT.md#p-memory-sync)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [mem0ai/mem0](https://github.com/mem0ai/mem0) | 80–92 | 30/27/8/5/10 | 67,108 | 2026-10-12 | Apache-2.0 |
| 2. [basicmachines-co/basic-memory](https://github.com/basicmachines-co/basic-memory) | 75–87 | 30/30/4/6/5 | 4,162 | 2026-10-12 | AGPL-3.0 |
| 3. [foambubble/foam](https://github.com/foambubble/foam) | 72–84 | 30/20/6/6/10 | 17,446 | 2026-10-12 | MIT |

### 1. mem0ai/mem0
- 能做什么：面向AI代理的记忆层与接口。
- 为什么保留：可比较记忆写入、提取和检索基础。 适配判断27/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：当前README描述ADD-only及迁移变化；冲突、删除、权限和来源不能默认交给库解决。
- 与自建比较：当前缺口是“自动同步和多端接续尚未验证。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/mem0ai/mem0/tree/d26ba5e4518cef7fff3c66d4f715b21adf9feabe#readme) · [仓库元数据](https://api.github.com/repos/mem0ai/mem0) · [成熟发行 release](https://github.com/mem0ai/mem0/releases/tag/release)（2023-07-14）。

### 2. basicmachines-co/basic-memory
- 能做什么：本地优先的Markdown知识与AI访问工具。
- 为什么保留：与现有文本权威源较贴近，可减少迁移阻力。 适配判断30/30；按统一权重已知分75，在本项目候选中列第2。
- 代价和不能替代的部分：同步或团队云能力与本地功能需区分；README有依赖预发布提示，须锁版本试验。
- 与自建比较：当前缺口是“自动同步和多端接续尚未验证。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/basicmachines-co/basic-memory/tree/d1275262b202b97f339b7dfcd1bfecfb4d97410a#readme) · [仓库元数据](https://api.github.com/repos/basicmachines-co/basic-memory) · [成熟发行 v0.1.0](https://github.com/basicmachines-co/basic-memory/releases/tag/v0.1.0)（2025-02-07）。

### 3. foambubble/foam
- 能做什么：建立在VSCode和Markdown文件上的知识管理。
- 为什么保留：适合保留可版本控制的文本与链接关系。 适配判断20/30；按统一权重已知分72，在本项目候选中列第3。
- 代价和不能替代的部分：偏开发者环境，移动操作和非技术使用者体验需另验证。
- 与自建比较：当前缺口是“自动同步和多端接续尚未验证。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/foambubble/foam/tree/6acaa0b10d8198f096a6c2462a227674de322a48#readme) · [仓库元数据](https://api.github.com/repos/foambubble/foam) · [成熟发行 v0.2.0](https://github.com/foambubble/foam/releases/tag/v0.2.0)（2020-07-12）。

采用前同样本检查：用两端对同一条非敏感事实做更新，核对冲突和来源保留行为。

<a id="p-radar"></a>
## 开源 Top3 雷达

项目要解决：需求、开源调研快照与自有项目成果的公开摘要；外部调研和项目进展分工维护。 本轮重点：此前榜单存在停更、归档与许可证变更未回填的情况。

搜索：`github analytics`；卡ID `github-20261013-39`（同组复用）。 [自建不足](SELF-BUILT.md#p-radar) · [候选取舍](AUDIT.md#p-radar)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [release-argus/Argus](https://github.com/release-argus/Argus) | 72–84 | 30/24/2/6/10 | 755 | 2026-10-08 | Apache-2.0 |

**只保留1个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. release-argus/Argus
- 能做什么：跟踪软件版本发布的自托管工具。
- 为什么保留：可补发行变化提醒和候选版本刷新。 适配判断24/30；按统一权重已知分72，在本项目候选中列第1。
- 代价和不能替代的部分：不是功能评测或完整Top3评分器；README默认认证关闭，部署前须配置。
- 与自建比较：当前缺口是“此前榜单存在停更、归档与许可证变更未回填的情况。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/release-argus/Argus/tree/d93b73a381810654ee2bce3c771db64dc4a6e939#readme) · [仓库元数据](https://api.github.com/repos/release-argus/Argus) · [成熟发行 0.0.0](https://github.com/release-argus/Argus/releases/tag/0.0.0)（2022-04-21）。

采用前同样本检查：按固定日期保存证据快照，下一轮只刷新发生变化的候选和项目。

<a id="p-takken"></a>
## 宅建冲刺页 + Obsidian 题库

项目要解决：過去問题库、逐选项解析、Root→Sub-rule→Variable 归档、错题复测。 本轮重点：浏览教材与网页答对不能作为掌握结论。

搜索：`spaced repetition`；卡ID `github-20261013-21`（同组复用）。 [自建不足](SELF-BUILT.md#p-takken) · [候选取舍](AUDIT.md#p-takken)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [ankitects/anki](https://github.com/ankitects/anki) | 80–92 | 30/29/8/8/5 | 31,984 | 2026-10-13 | AGPL-3.0-or-later（部分文件另许可） |
| 2. [learningequality/kolibri](https://github.com/learningequality/kolibri) | 73–85 | 30/23/3/7/10 | 1,143 | 2026-10-12 | MIT |
| 3. [st3v3nmw/obsidian-spaced-repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) | 71–83 | 24/28/3/6/10 | 2,585 | 2026-08-03 | MIT |

### 1. ankitects/anki
- 能做什么：成熟的间隔复习与闪卡程序。
- 为什么保留：可补遗忘调度、复习日志与题目重复学习。 适配判断29/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：不能核验专业答案或推断掌握；平台客户端和同步成本需另看，手机导入需实测。
- 与自建比较：当前缺口是“浏览教材与网页答对不能作为掌握结论。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/ankitects/anki/tree/b15d4c71eadd3c4a74afaba74f93f4b3f70ac97c#readme) · [仓库元数据](https://api.github.com/repos/ankitects/anki) · [成熟发行 2.1.20](https://github.com/ankitects/anki/releases/tag/2.1.20)（2020-03-07）。

### 2. learningequality/kolibri
- 能做什么：离线优先的教学学习平台。
- 为什么保留：适合教材分发、离线访问和教育场景组织。 适配判断23/30；按统一权重已知分73，在本项目候选中列第2。
- 代价和不能替代的部分：需部署并准备有授权的内容；日文题型和家庭点读流程仍要适配。
- 与自建比较：当前缺口是“浏览教材与网页答对不能作为掌握结论。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/learningequality/kolibri/tree/5d47c94a8eccc63667afa097ccebe6ac9de640b0#readme) · [仓库元数据](https://api.github.com/repos/learningequality/kolibri) · [成熟发行 v0.2.1](https://github.com/learningequality/kolibri/releases/tag/v0.2.1)（2017-03-10）。

### 3. st3v3nmw/obsidian-spaced-repetition
- 能做什么：为Obsidian笔记增加闪卡和整篇复习。
- 为什么保留：贴合已有Markdown题库与笔记习惯。 适配判断28/30；按统一权重已知分71，在本项目候选中列第3。
- 代价和不能替代的部分：依赖Obsidian；移动保存、插件兼容及完整考试流程需另验证。
- 与自建比较：当前缺口是“浏览教材与网页答对不能作为掌握结论。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/st3v3nmw/obsidian-spaced-repetition/tree/3d5079f3bcd54531b084040d1c0178f15f681510#readme) · [仓库元数据](https://api.github.com/repos/st3v3nmw/obsidian-spaced-repetition) · [成熟发行 1.0.0](https://github.com/st3v3nmw/obsidian-spaced-repetition/releases/tag/1.0.0)（2021-04-09）。

采用前同样本检查：对一处真实卡点完成原题解释与同Root变式复测，保留首答。

<a id="p-ikkyu"></a>
## 一级建筑士备考

项目要解决：学科 + 製図；過去問 + YouTube 讲解 + 製図突破计划。 本轮重点：19项出处和手机使用仍待核验。

搜索：`spaced repetition`；卡ID `github-20261013-21`（同组复用）。 [自建不足](SELF-BUILT.md#p-ikkyu) · [候选取舍](AUDIT.md#p-ikkyu)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [ankitects/anki](https://github.com/ankitects/anki) | 80–92 | 30/29/8/8/5 | 31,984 | 2026-10-13 | AGPL-3.0-or-later（部分文件另许可） |
| 2. [learningequality/kolibri](https://github.com/learningequality/kolibri) | 73–85 | 30/23/3/7/10 | 1,143 | 2026-10-12 | MIT |
| 3. [st3v3nmw/obsidian-spaced-repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) | 71–83 | 24/28/3/6/10 | 2,585 | 2026-08-03 | MIT |

### 1. ankitects/anki
- 能做什么：成熟的间隔复习与闪卡程序。
- 为什么保留：可补遗忘调度、复习日志与题目重复学习。 适配判断29/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：不能核验专业答案或推断掌握；平台客户端和同步成本需另看，手机导入需实测。
- 与自建比较：当前缺口是“19项出处和手机使用仍待核验。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/ankitects/anki/tree/b15d4c71eadd3c4a74afaba74f93f4b3f70ac97c#readme) · [仓库元数据](https://api.github.com/repos/ankitects/anki) · [成熟发行 2.1.20](https://github.com/ankitects/anki/releases/tag/2.1.20)（2020-03-07）。

### 2. learningequality/kolibri
- 能做什么：离线优先的教学学习平台。
- 为什么保留：适合教材分发、离线访问和教育场景组织。 适配判断23/30；按统一权重已知分73，在本项目候选中列第2。
- 代价和不能替代的部分：需部署并准备有授权的内容；日文题型和家庭点读流程仍要适配。
- 与自建比较：当前缺口是“19项出处和手机使用仍待核验。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/learningequality/kolibri/tree/5d47c94a8eccc63667afa097ccebe6ac9de640b0#readme) · [仓库元数据](https://api.github.com/repos/learningequality/kolibri) · [成熟发行 v0.2.1](https://github.com/learningequality/kolibri/releases/tag/v0.2.1)（2017-03-10）。

### 3. st3v3nmw/obsidian-spaced-repetition
- 能做什么：为Obsidian笔记增加闪卡和整篇复习。
- 为什么保留：贴合已有Markdown题库与笔记习惯。 适配判断28/30；按统一权重已知分71，在本项目候选中列第3。
- 代价和不能替代的部分：依赖Obsidian；移动保存、插件兼容及完整考试流程需另验证。
- 与自建比较：当前缺口是“19项出处和手机使用仍待核验。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/st3v3nmw/obsidian-spaced-repetition/tree/3d5079f3bcd54531b084040d1c0178f15f681510#readme) · [仓库元数据](https://api.github.com/repos/st3v3nmw/obsidian-spaced-repetition) · [成熟发行 1.0.0](https://github.com/st3v3nmw/obsidian-spaced-repetition/releases/tag/1.0.0)（2021-04-09）。

采用前同样本检查：先核对一项待定出处，再完成对应题的原题与变式复测。

<a id="p-lang"></a>
## 日语 / 英语输出练习

项目要解决：中文意图→自己说日语→AI 真实追问→只纠一个点；托福口语；儿童式日语习得。 本轮重点：练习材料与个人掌握分开，尚缺可比较的迁移表现证据。

搜索：`language learning`；卡ID `github-20261013-35`（同组复用）。 [自建不足](SELF-BUILT.md#p-lang) · [候选取舍](AUDIT.md#p-lang)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [ankitects/anki](https://github.com/ankitects/anki) | 75–87 | 30/24/8/8/5 | 31,984 | 2026-10-13 | AGPL-3.0-or-later（部分文件另许可） |
| 2. [LuteOrg/lute-v3](https://github.com/LuteOrg/lute-v3) | 69–81 | 24/26/3/6/10 | 1,587 | 2026-09-05 | MIT |
| 3. [ZuodaoTech/everyone-can-use-english](https://github.com/ZuodaoTech/everyone-can-use-english) | 68–80 | 18/29/8/7/6 | 38,915 | 2026-06-29 | GPL-3.0 |

### 1. ankitects/anki
- 能做什么：成熟的间隔复习与闪卡程序。
- 为什么保留：可补遗忘调度、复习日志与题目重复学习。 适配判断24/30；按统一权重已知分75，在本项目候选中列第1。
- 代价和不能替代的部分：不能核验专业答案或推断掌握；平台客户端和同步成本需另看，手机导入需实测。
- 与自建比较：当前缺口是“练习材料与个人掌握分开，尚缺可比较的迁移表现证据。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/ankitects/anki/tree/b15d4c71eadd3c4a74afaba74f93f4b3f70ac97c#readme) · [仓库元数据](https://api.github.com/repos/ankitects/anki) · [成熟发行 2.1.20](https://github.com/ankitects/anki/releases/tag/2.1.20)（2020-03-07）。

### 2. LuteOrg/lute-v3
- 能做什么：围绕阅读材料和词汇状态的语言学习工具。
- 为什么保留：可补原文阅读、词汇复习和长期阅读记录。 适配判断26/30；按统一权重已知分69，在本项目候选中列第2。
- 代价和不能替代的部分：不是完整口语教练；日语分词、词典和移动体验需用真实材料核验。
- 与自建比较：当前缺口是“练习材料与个人掌握分开，尚缺可比较的迁移表现证据。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/LuteOrg/lute-v3/tree/933d0840aede93b3999e6017ba7f5eba5e41206d#readme) · [仓库元数据](https://api.github.com/repos/LuteOrg/lute-v3) · [成熟发行 3.0.0](https://github.com/LuteOrg/lute-v3/releases/tag/3.0.0)（2023-11-22）。

### 3. ZuodaoTech/everyone-can-use-english
- 能做什么：英语输入、听读与相关学习工具。
- 为什么保留：可借鉴原语材料、听读循环和练习入口。 适配判断29/30；按统一权重已知分68，在本项目候选中列第3。
- 代价和不能替代的部分：不能直接替代日语业务表达训练；外部语音和网页内容有各自依赖。
- 与自建比较：当前缺口是“练习材料与个人掌握分开，尚缺可比较的迁移表现证据。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/ZuodaoTech/everyone-can-use-english/tree/3d799132046993eade5a364ddd1e557906854eda#readme) · [仓库元数据](https://api.github.com/repos/ZuodaoTech/everyone-can-use-english) · [成熟发行 v0.2.0](https://github.com/ZuodaoTech/everyone-can-use-english/releases/tag/v0.2.0)（2024-03-25）。

采用前同样本检查：用同一意图在新场景再表达一次，只记录一个关键错误和复测结果。

<a id="p-voice"></a>
## 中日双轨语音翻译机

项目要解决：SwiftUI 前端 + Python VAD/流程，Whisper、Apple Translation、半双工。 本轮重点：Whisper切段仍使用保守固定阈值，连续口语和打断边界存在待测项。

搜索：`speech recognition translation`；卡ID `github-20261013-47`（同组复用）。 [自建不足](SELF-BUILT.md#p-voice) · [候选取舍](AUDIT.md#p-voice)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [argmaxinc/argmax-oss-swift](https://github.com/argmaxinc/argmax-oss-swift) | 79–91 | 30/29/4/6/10 | 6,403 | 2026-10-11 | MIT |
| 2. [KoljaB/RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) | 79–91 | 30/28/6/5/10 | 10,184 | 2026-09-17 | MIT |
| 3. [QuentinFuxa/WhisperLiveKit](https://github.com/QuentinFuxa/WhisperLiveKit) | 75–87 | 24/30/6/5/10 | 11,137 | 2026-08-30 | Apache-2.0 |

### 1. argmaxinc/argmax-oss-swift
- 能做什么：Apple平台本地语音推理的Swift SDK。
- 为什么保留：适合当前Mac环境的端侧识别对照。 适配判断29/30；按统一权重已知分79，在本项目候选中列第1。
- 代价和不能替代的部分：仓库已更名argmax-oss-swift，Pro与开源能力要区分；不自带完整翻译流程。
- 与自建比较：当前缺口是“Whisper切段仍使用保守固定阈值，连续口语和打断边界存在待测项。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/argmaxinc/argmax-oss-swift/tree/9f99b5cb6a907730543823ad271b82532782a899#readme) · [仓库元数据](https://api.github.com/repos/argmaxinc/argmax-oss-swift) · [成熟发行 v0.1.0](https://github.com/argmaxinc/argmax-oss-swift/releases/tag/v0.1.0)（2024-01-30）。

### 2. KoljaB/RealtimeSTT
- 能做什么：支持音频流、唤醒词与实时识别的Python库。
- 为什么保留：可补流式采集、分段和识别组件。 适配判断28/30；按统一权重已知分79，在本项目候选中列第2。
- 代价和不能替代的部分：只覆盖识别部分；嘈杂环境与中日混说需要固定样本对照。
- 与自建比较：当前缺口是“Whisper切段仍使用保守固定阈值，连续口语和打断边界存在待测项。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/KoljaB/RealtimeSTT/tree/777727553eedfa19aead15337ce66bab549add3f#readme) · [仓库元数据](https://api.github.com/repos/KoljaB/RealtimeSTT) · [成熟发行 v0.1.3](https://github.com/KoljaB/RealtimeSTT/releases/tag/v0.1.3)（2023-09-06）。

### 3. QuentinFuxa/WhisperLiveKit
- 能做什么：面向实时语音转写的流式工具链。
- 为什么保留：可对照分段策略、延迟和实时输出稳定性。 适配判断30/30；按统一权重已知分75，在本项目候选中列第3。
- 代价和不能替代的部分：不等于中日同传完整系统；翻译、系统音频和硬件表现需另测。
- 与自建比较：当前缺口是“Whisper切段仍使用保守固定阈值，连续口语和打断边界存在待测项。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/QuentinFuxa/WhisperLiveKit/tree/363e4f6d029694d9c81ae548beddd9d3c88a3637#readme) · [仓库元数据](https://api.github.com/repos/QuentinFuxa/WhisperLiveKit) · [成熟发行 0.1.1](https://github.com/QuentinFuxa/WhisperLiveKit/releases/tag/0.1.1)（2025-03-19）。

采用前同样本检查：用固定中日双语短样本比较切段准确率、延迟和误打断次数。

<a id="p-job"></a>
## JobMesh 招聘聚合 + 履歴書

项目要解决：中日双语全行业职位聚合、雇主发帖、AI 匹配；日式履歴書/職務経歴書生成。 本轮重点：doda与Indeed仍未取得数据；多站抓取和评分尚未证明真实面试或录用效果。

搜索：`job scraper`；卡ID `github-20261013-30`（同组复用）。 [自建不足](SELF-BUILT.md#p-job) · [候选取舍](AUDIT.md#p-job)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [speedyapply/JobSpy](https://github.com/speedyapply/JobSpy) | 80–92 | 30/30/4/6/10 | 4,472 | 2026-10-12 | MIT |
| 2. [srbhr/Resume-Matcher](https://github.com/srbhr/Resume-Matcher) | 80–92 | 30/28/6/6/10 | 28,655 | 2026-10-13 | Apache-2.0 |
| 3. [reactive-resume/reactive-resume](https://github.com/reactive-resume/reactive-resume) | 80–92 | 30/25/8/7/10 | 44,230 | 2026-10-13 | MIT |

### 1. speedyapply/JobSpy
- 能做什么：聚合多个招聘平台的职位抓取库。
- 为什么保留：可复用通用站点字段和抓取接口，减少重复维护。 适配判断30/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：日本本地站点覆盖不等于JobMesh现有七站；403、限流和使用权限仍须遵守。
- 与自建比较：当前缺口是“doda与Indeed仍未取得数据；多站抓取和评分尚未证明真实面试或录用效果。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/speedyapply/JobSpy/tree/4e61c000919750d110d73a3680af76be157bef8d#readme) · [仓库元数据](https://api.github.com/repos/speedyapply/JobSpy) · [成熟发行 v1.0.1](https://github.com/speedyapply/JobSpy/releases/tag/v1.0.1)（2023-09-03）。

### 2. srbhr/Resume-Matcher
- 能做什么：简历与职位描述的匹配分析工具。
- 为什么保留：可补可解释匹配和简历修改对照。 适配判断28/30；按统一权重已知分80，在本项目候选中列第2。
- 代价和不能替代的部分：不能将模型评分等同真实录用概率；日文履歴書结构与个人信息处理需另验收。
- 与自建比较：当前缺口是“doda与Indeed仍未取得数据；多站抓取和评分尚未证明真实面试或录用效果。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/srbhr/Resume-Matcher/tree/db0e6ac9bce8774d6abd692ddccbc02421b0ded2#readme) · [仓库元数据](https://api.github.com/repos/srbhr/Resume-Matcher) · [成熟发行 0.1.2-old-resume-matcher](https://github.com/srbhr/Resume-Matcher/releases/tag/0.1.2-old-resume-matcher)（2025-05-26）。

### 3. reactive-resume/reactive-resume
- 能做什么：可自行部署的简历编辑和导出工具。
- 为什么保留：可补简历编辑、模板与导出交互。 适配判断25/30；按统一权重已知分80，在本项目候选中列第3。
- 代价和不能替代的部分：日文履歴書、職務経歴書格式需专门适配；不是招聘抓取器。
- 与自建比较：当前缺口是“doda与Indeed仍未取得数据；多站抓取和评分尚未证明真实面试或录用效果。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/reactive-resume/reactive-resume/tree/5d3bc56d3e5b2acc21711c3773a3b77a1110a5e2#readme) · [仓库元数据](https://api.github.com/repos/reactive-resume/reactive-resume) · [成熟发行 v1](https://github.com/reactive-resume/reactive-resume/releases/tag/v1)（2020-07-17）。

采用前同样本检查：分别抽取高、中、低分各十条，核对职位有效性和评分解释，并记录应入选却被低估的样本。

<a id="p-news"></a>
## GitHub 动态 / 新闻追踪

项目要解决：追踪外部信息流，按项目筛选信号，转成可执行建议（N001）。 本轮重点：尚无定时采集持续运行的证据。

搜索：`RSS aggregator`；卡ID `github-20261013-38`（同组复用）。 [自建不足](SELF-BUILT.md#p-news) · [候选取舍](AUDIT.md#p-news)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [FreshRSS/FreshRSS](https://github.com/FreshRSS/FreshRSS) | 79–91 | 30/30/6/8/5 | 16,280 | 2026-10-12 | AGPL-3.0 |
| 2. [newsnext/newsnow](https://github.com/newsnext/newsnow) | 78–90 | 30/26/6/6/10 | 22,024 | 2026-10-13 | MIT |

**只保留2个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. FreshRSS/FreshRSS
- 能做什么：自托管RSS聚合器，含标签、API与移动客户端支持。
- 为什么保留：可直接承担订阅、阅读和基础去重。 适配判断30/30；按统一权重已知分79，在本项目候选中列第1。
- 代价和不能替代的部分：不自动做新闻事实核查、立场对照或研究结论。
- 与自建比较：当前缺口是“尚无定时采集持续运行的证据。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/FreshRSS/FreshRSS/tree/15d57cea88cc7a8ac2af98ad4b2815a82e0f873c#readme) · [仓库元数据](https://api.github.com/repos/FreshRSS/FreshRSS) · [成熟发行 1.0.0](https://github.com/FreshRSS/FreshRSS/releases/tag/1.0.0)（2015-05-30）。

### 2. newsnext/newsnow
- 能做什么：聚合不同新闻源的阅读界面和源适配结构。
- 为什么保留：可借鉴来源接入和热点展示。 适配判断26/30；按统一权重已知分78，在本项目候选中列第2。
- 代价和不能替代的部分：仓库已迁至newsnext/newsnow；热榜不是可信度排序，内容版权与接口稳定性需另核。
- 与自建比较：当前缺口是“尚无定时采集持续运行的证据。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/newsnext/newsnow/tree/0560c993b226cd2fd07d8a79875d50551f52c584#readme) · [仓库元数据](https://api.github.com/repos/newsnext/newsnow) · [成熟发行 v0.0.1](https://github.com/newsnext/newsnow/releases/tag/v0.0.1)（2024-10-19）。

采用前同样本检查：用一个新闻事件检查原始来源、发布时间和两种不同解释的证据。

<a id="p-market"></a>
## 市场与产品研究

项目要解决：太阳能储能入日、Makuake 产品分析等，移动端 HTML + PDF，保留来源与局限。 本轮重点：研究产物尚未转换为成交或商业验证。

搜索：`deep research`；卡ID `github-20261013-23`（同组复用）。 [自建不足](SELF-BUILT.md#p-market) · [候选取舍](AUDIT.md#p-market)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 82–94 | 30/29/8/5/10 | 30,072 | 2026-10-10 | Apache-2.0 |

**只保留1个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. assafelovic/gpt-researcher
- 能做什么：带搜索、来源引用和报告输出的研究代理框架。
- 为什么保留：可借鉴查询分解、引用组织和研究流程编排。 适配判断29/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：需要模型/搜索服务配置且会产生调用成本；引用存在不等于可靠，不得把报告当市场验证。
- 与自建比较：当前缺口是“研究产物尚未转换为成交或商业验证。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/assafelovic/gpt-researcher/tree/3582a6841fe7dc801e2a34e34ee408641aea9bce#readme) · [仓库元数据](https://api.github.com/repos/assafelovic/gpt-researcher) · [成熟发行 v1.0.1](https://github.com/assafelovic/gpt-researcher/releases/tag/v1.0.1)（2023-07-10）。

采用前同样本检查：将一个研究结论写成可被推翻的假设，并规定最小现实观察。

<a id="p-web"></a>
## 个人主页与合作方网页

项目要解决：GitHub Pages 个人主页（日中英）、合作方内容审核稿。 本轮重点：公开发布记录不能替代所有表单、权限和真实设备验收。

搜索：`documentation website`；卡ID `github-20261013-18`（同组复用）。 [自建不足](SELF-BUILT.md#p-web) · [候选取舍](AUDIT.md#p-web)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [withastro/astro](https://github.com/withastro/astro) | 84–96 | 30/29/8/7/10 | 63,202 | 2026-10-13 | MIT |
| 2. [facebook/docusaurus](https://github.com/facebook/docusaurus) | 83–95 | 30/28/8/7/10 | 66,478 | 2026-10-09 | MIT |
| 3. [getzola/zola](https://github.com/getzola/zola) | 75–87 | 30/25/6/7/7 | 17,509 | 2026-10-08 | EUPL-1.2 |

### 1. withastro/astro
- 能做什么：面向内容网站的Web框架。
- 为什么保留：适合轻量主页、资料展示和按需交互。 适配判断29/30；按统一权重已知分84，在本项目候选中列第1。
- 代价和不能替代的部分：需要前端开发；权限、支付和学习反馈不会自动具备。
- 与自建比较：当前缺口是“公开发布记录不能替代所有表单、权限和真实设备验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/withastro/astro/tree/59b9cc00726495bb45f5c4b000dbbb7b5a19d662#readme) · [仓库元数据](https://api.github.com/repos/withastro/astro) · [成熟发行 astro@0.18.9](https://github.com/withastro/astro/releases/tag/astro%400.18.9)（2021-08-05）。

### 2. facebook/docusaurus
- 能做什么：基于文档、博客和本地化的网站构建工具。
- 为什么保留：适合把教材、证据页面和项目说明做成结构一致的网站。 适配判断28/30；按统一权重已知分83，在本项目候选中列第2。
- 代价和不能替代的部分：不是学习记录后端；构建与内容审核仍需维护，真机体验需验收。
- 与自建比较：当前缺口是“公开发布记录不能替代所有表单、权限和真实设备验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/facebook/docusaurus/tree/c245217563f6491fdb79bf5ac91bfa16536e5de9#readme) · [仓库元数据](https://api.github.com/repos/facebook/docusaurus) · [成熟发行 v1.0.3](https://github.com/facebook/docusaurus/releases/tag/v1.0.3)（2017-12-19）。

### 3. getzola/zola
- 能做什么：独立程序形式的静态网站生成器。
- 为什么保留：适合简单、可版本化的内容页面。 适配判断25/30；按统一权重已知分75，在本项目候选中列第3。
- 代价和不能替代的部分：动态学习记录和复杂交互需另接；模板迁移有成本。
- 与自建比较：当前缺口是“公开发布记录不能替代所有表单、权限和真实设备验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/getzola/zola/tree/9740ae258f382d742b7732f7b89b3cd529973f4b#readme) · [仓库元数据](https://api.github.com/repos/getzola/zola) · [成熟发行 v0.0.2](https://github.com/getzola/zola/releases/tag/v0.0.2)（2017-03-24）。

采用前同样本检查：检查一条公开阅读链与一条受限入口，确认返回、跳转和访问边界。

<a id="p-ares"></a>
## 不動産ファイナンス学习资料

项目要解决：ARES 两年真题、术语与手机学习资料。 本轮重点：手机或iPad试读与讲解质量尚未验收。

搜索：`spaced repetition`；卡ID `github-20261013-21`（同组复用）。 [自建不足](SELF-BUILT.md#p-ares) · [候选取舍](AUDIT.md#p-ares)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [ankitects/anki](https://github.com/ankitects/anki) | 81–93 | 30/30/8/8/5 | 31,984 | 2026-10-13 | AGPL-3.0-or-later（部分文件另许可） |
| 2. [learningequality/kolibri](https://github.com/learningequality/kolibri) | 77–89 | 30/27/3/7/10 | 1,143 | 2026-10-12 | MIT |
| 3. [st3v3nmw/obsidian-spaced-repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) | 66–78 | 24/23/3/6/10 | 2,585 | 2026-08-03 | MIT |

### 1. ankitects/anki
- 能做什么：成熟的间隔复习与闪卡程序。
- 为什么保留：可补遗忘调度、复习日志与题目重复学习。 适配判断30/30；按统一权重已知分81，在本项目候选中列第1。
- 代价和不能替代的部分：不能核验专业答案或推断掌握；平台客户端和同步成本需另看，手机导入需实测。
- 与自建比较：当前缺口是“手机或iPad试读与讲解质量尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/ankitects/anki/tree/b15d4c71eadd3c4a74afaba74f93f4b3f70ac97c#readme) · [仓库元数据](https://api.github.com/repos/ankitects/anki) · [成熟发行 2.1.20](https://github.com/ankitects/anki/releases/tag/2.1.20)（2020-03-07）。

### 2. learningequality/kolibri
- 能做什么：离线优先的教学学习平台。
- 为什么保留：适合教材分发、离线访问和教育场景组织。 适配判断27/30；按统一权重已知分77，在本项目候选中列第2。
- 代价和不能替代的部分：需部署并准备有授权的内容；日文题型和家庭点读流程仍要适配。
- 与自建比较：当前缺口是“手机或iPad试读与讲解质量尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/learningequality/kolibri/tree/5d47c94a8eccc63667afa097ccebe6ac9de640b0#readme) · [仓库元数据](https://api.github.com/repos/learningequality/kolibri) · [成熟发行 v0.2.1](https://github.com/learningequality/kolibri/releases/tag/v0.2.1)（2017-03-10）。

### 3. st3v3nmw/obsidian-spaced-repetition
- 能做什么：为Obsidian笔记增加闪卡和整篇复习。
- 为什么保留：贴合已有Markdown题库与笔记习惯。 适配判断23/30；按统一权重已知分66，在本项目候选中列第3。
- 代价和不能替代的部分：依赖Obsidian；移动保存、插件兼容及完整考试流程需另验证。
- 与自建比较：当前缺口是“手机或iPad试读与讲解质量尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/st3v3nmw/obsidian-spaced-repetition/tree/3d5079f3bcd54531b084040d1c0178f15f681510#readme) · [仓库元数据](https://api.github.com/repos/st3v3nmw/obsidian-spaced-repetition) · [成熟发行 1.0.0](https://github.com/st3v3nmw/obsidian-spaced-repetition/releases/tag/1.0.0)（2021-04-09）。

采用前同样本检查：在目标设备完成一节学习和五道首答，保留卡点及次日复测记录。

<a id="p-n2"></a>
## JLPT N2 学习页

项目要解决：日语题目、听力入口与表达练习。 本轮重点：发布不等于学习记录正确，更不等于已掌握N2。

搜索：`spaced repetition`；卡ID `github-20261013-21`（同组复用）。 [自建不足](SELF-BUILT.md#p-n2) · [候选取舍](AUDIT.md#p-n2)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [ankitects/anki](https://github.com/ankitects/anki) | 80–92 | 30/29/8/8/5 | 31,984 | 2026-10-13 | AGPL-3.0-or-later（部分文件另许可） |
| 2. [learningequality/kolibri](https://github.com/learningequality/kolibri) | 73–85 | 30/23/3/7/10 | 1,143 | 2026-10-12 | MIT |
| 3. [st3v3nmw/obsidian-spaced-repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) | 71–83 | 24/28/3/6/10 | 2,585 | 2026-08-03 | MIT |

### 1. ankitects/anki
- 能做什么：成熟的间隔复习与闪卡程序。
- 为什么保留：可补遗忘调度、复习日志与题目重复学习。 适配判断29/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：不能核验专业答案或推断掌握；平台客户端和同步成本需另看，手机导入需实测。
- 与自建比较：当前缺口是“发布不等于学习记录正确，更不等于已掌握N2。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/ankitects/anki/tree/b15d4c71eadd3c4a74afaba74f93f4b3f70ac97c#readme) · [仓库元数据](https://api.github.com/repos/ankitects/anki) · [成熟发行 2.1.20](https://github.com/ankitects/anki/releases/tag/2.1.20)（2020-03-07）。

### 2. learningequality/kolibri
- 能做什么：离线优先的教学学习平台。
- 为什么保留：适合教材分发、离线访问和教育场景组织。 适配判断23/30；按统一权重已知分73，在本项目候选中列第2。
- 代价和不能替代的部分：需部署并准备有授权的内容；日文题型和家庭点读流程仍要适配。
- 与自建比较：当前缺口是“发布不等于学习记录正确，更不等于已掌握N2。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/learningequality/kolibri/tree/5d47c94a8eccc63667afa097ccebe6ac9de640b0#readme) · [仓库元数据](https://api.github.com/repos/learningequality/kolibri) · [成熟发行 v0.2.1](https://github.com/learningequality/kolibri/releases/tag/v0.2.1)（2017-03-10）。

### 3. st3v3nmw/obsidian-spaced-repetition
- 能做什么：为Obsidian笔记增加闪卡和整篇复习。
- 为什么保留：贴合已有Markdown题库与笔记习惯。 适配判断28/30；按统一权重已知分71，在本项目候选中列第3。
- 代价和不能替代的部分：依赖Obsidian；移动保存、插件兼容及完整考试流程需另验证。
- 与自建比较：当前缺口是“发布不等于学习记录正确，更不等于已掌握N2。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/st3v3nmw/obsidian-spaced-repetition/tree/3d5079f3bcd54531b084040d1c0178f15f681510#readme) · [仓库元数据](https://api.github.com/repos/st3v3nmw/obsidian-spaced-repetition) · [成熟发行 1.0.0](https://github.com/st3v3nmw/obsidian-spaced-repetition/releases/tag/1.0.0)（2021-04-09）。

采用前同样本检查：完成五道首答并保存卡点，次日用同语法变式核对掌握。

<a id="p-github-course"></a>
## GitHub 中文实操与点读教材

项目要解决：把公开仓库资料做成保留来源的中文实操课和双语点读。 本轮重点：真实手机或iPad阅读和实际操作效果未验收。

搜索：`knowledge management`；卡ID `github-20261013-16`（同组复用）。 [自建不足](SELF-BUILT.md#p-github-course) · [候选取舍](AUDIT.md#p-github-course)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [facebook/docusaurus](https://github.com/facebook/docusaurus) | 85–97 | 30/30/8/7/10 | 66,478 | 2026-10-09 | MIT |
| 2. [withastro/astro](https://github.com/withastro/astro) | 83–95 | 30/28/8/7/10 | 63,202 | 2026-10-13 | MIT |
| 3. [getzola/zola](https://github.com/getzola/zola) | 75–87 | 30/25/6/7/7 | 17,509 | 2026-10-08 | EUPL-1.2 |

### 1. facebook/docusaurus
- 能做什么：基于文档、博客和本地化的网站构建工具。
- 为什么保留：适合把教材、证据页面和项目说明做成结构一致的网站。 适配判断30/30；按统一权重已知分85，在本项目候选中列第1。
- 代价和不能替代的部分：不是学习记录后端；构建与内容审核仍需维护，真机体验需验收。
- 与自建比较：当前缺口是“真实手机或iPad阅读和实际操作效果未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/facebook/docusaurus/tree/c245217563f6491fdb79bf5ac91bfa16536e5de9#readme) · [仓库元数据](https://api.github.com/repos/facebook/docusaurus) · [成熟发行 v1.0.3](https://github.com/facebook/docusaurus/releases/tag/v1.0.3)（2017-12-19）。

### 2. withastro/astro
- 能做什么：面向内容网站的Web框架。
- 为什么保留：适合轻量主页、资料展示和按需交互。 适配判断28/30；按统一权重已知分83，在本项目候选中列第2。
- 代价和不能替代的部分：需要前端开发；权限、支付和学习反馈不会自动具备。
- 与自建比较：当前缺口是“真实手机或iPad阅读和实际操作效果未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/withastro/astro/tree/59b9cc00726495bb45f5c4b000dbbb7b5a19d662#readme) · [仓库元数据](https://api.github.com/repos/withastro/astro) · [成熟发行 astro@0.18.9](https://github.com/withastro/astro/releases/tag/astro%400.18.9)（2021-08-05）。

### 3. getzola/zola
- 能做什么：独立程序形式的静态网站生成器。
- 为什么保留：适合简单、可版本化的内容页面。 适配判断25/30；按统一权重已知分75，在本项目候选中列第3。
- 代价和不能替代的部分：动态学习记录和复杂交互需另接；模板迁移有成本。
- 与自建比较：当前缺口是“真实手机或iPad阅读和实际操作效果未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/getzola/zola/tree/9740ae258f382d742b7732f7b89b3cd529973f4b#readme) · [仓库元数据](https://api.github.com/repos/getzola/zola) · [成熟发行 v0.0.2](https://github.com/getzola/zola/releases/tag/v0.0.2)（2017-03-24）。

采用前同样本检查：在目标设备完成一课，再不看步骤独立完成一个同类小任务。

<a id="p-kids-reading"></a>
## 家庭儿童阅读工具

项目要解决：面向家庭使用的点读、翻译和阅读入口。 本轮重点：文件存在不代表儿童真机阅读、点击播放和访问边界均已验收。

搜索：`educational games`；卡ID `github-20261013-31`（同组复用）。 [自建不足](SELF-BUILT.md#p-kids-reading) · [候选取舍](AUDIT.md#p-kids-reading)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [learningequality/kolibri](https://github.com/learningequality/kolibri) | 80–92 | 30/30/3/7/10 | 1,143 | 2026-10-12 | MIT |
| 2. [ankitects/anki](https://github.com/ankitects/anki) | 71–83 | 30/20/8/8/5 | 31,984 | 2026-10-13 | AGPL-3.0-or-later（部分文件另许可） |
| 3. [SpringRoll/SpringRoll](https://github.com/SpringRoll/SpringRoll) | 55–67 | 18/22/1/4/10 | 89 | 2026-04-16 | MIT |

### 1. learningequality/kolibri
- 能做什么：离线优先的教学学习平台。
- 为什么保留：适合教材分发、离线访问和教育场景组织。 适配判断30/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：需部署并准备有授权的内容；日文题型和家庭点读流程仍要适配。
- 与自建比较：当前缺口是“文件存在不代表儿童真机阅读、点击播放和访问边界均已验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/learningequality/kolibri/tree/5d47c94a8eccc63667afa097ccebe6ac9de640b0#readme) · [仓库元数据](https://api.github.com/repos/learningequality/kolibri) · [成熟发行 v0.2.1](https://github.com/learningequality/kolibri/releases/tag/v0.2.1)（2017-03-10）。

### 2. ankitects/anki
- 能做什么：成熟的间隔复习与闪卡程序。
- 为什么保留：可补遗忘调度、复习日志与题目重复学习。 适配判断20/30；按统一权重已知分71，在本项目候选中列第2。
- 代价和不能替代的部分：不能核验专业答案或推断掌握；平台客户端和同步成本需另看，手机导入需实测。
- 与自建比较：当前缺口是“文件存在不代表儿童真机阅读、点击播放和访问边界均已验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/ankitects/anki/tree/b15d4c71eadd3c4a74afaba74f93f4b3f70ac97c#readme) · [仓库元数据](https://api.github.com/repos/ankitects/anki) · [成熟发行 2.1.20](https://github.com/ankitects/anki/releases/tag/2.1.20)（2020-03-07）。

### 3. SpringRoll/SpringRoll
- 能做什么：用于教育类HTML5游戏的开发生态。
- 为什么保留：可借鉴可访问性与交互式教育内容组织。 适配判断22/30；按统一权重已知分55，在本项目候选中列第3。
- 代价和不能替代的部分：是开发框架，不含家庭读物库、现成点读内容或学习成效保证。
- 与自建比较：当前缺口是“文件存在不代表儿童真机阅读、点击播放和访问边界均已验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/SpringRoll/SpringRoll/tree/67a360e87c1e82aa2d25d79d5be9f0c97c7a1791#readme) · [仓库元数据](https://api.github.com/repos/SpringRoll/SpringRoll) · [成熟发行 0.3.0](https://github.com/SpringRoll/SpringRoll/releases/tag/0.3.0)（2015-05-14）。

采用前同样本检查：在真实设备完成一本授权读物的打开、点读、返回和受限访问检查。

<a id="p-book-research"></a>
## 书籍解构与证据索引

项目要解决：按原文位置积累书籍认知地图与行动问题。 本轮重点：尚未验证书中一个命题对实际场景是否有用。

搜索：`knowledge management`；卡ID `github-20261013-16`（同组复用）。 [自建不足](SELF-BUILT.md#p-book-research) · [候选取舍](AUDIT.md#p-book-research)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) | 80–92 | 30/29/8/8/5 | 46,741 | 2026-10-04 | AGPL-3.0 |
| 2. [foambubble/foam](https://github.com/foambubble/foam) | 80–92 | 30/28/6/6/10 | 17,446 | 2026-10-12 | MIT |
| 3. [logseq/logseq](https://github.com/logseq/logseq) | 73–85 | 30/25/8/5/5 | 45,220 | 2026-10-13 | AGPL-3.0 |

### 1. siyuan-note/siyuan
- 能做什么：重视隐私与块级引用的个人知识管理系统。
- 为什么保留：可补引用、检索、结构化笔记和中文编辑。 适配判断29/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：部分同步等功能付费；不能自动保证来源正确或学习效果。
- 与自建比较：当前缺口是“尚未验证书中一个命题对实际场景是否有用。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/siyuan-note/siyuan/tree/fb3355f07d22bff36f1d785999fd5ded6a90d468#readme) · [仓库元数据](https://api.github.com/repos/siyuan-note/siyuan) · [成熟发行 v0.1.0](https://github.com/siyuan-note/siyuan/releases/tag/v0.1.0)（2020-08-31）。

### 2. foambubble/foam
- 能做什么：建立在VSCode和Markdown文件上的知识管理。
- 为什么保留：适合保留可版本控制的文本与链接关系。 适配判断28/30；按统一权重已知分80，在本项目候选中列第2。
- 代价和不能替代的部分：偏开发者环境，移动操作和非技术使用者体验需另验证。
- 与自建比较：当前缺口是“尚未验证书中一个命题对实际场景是否有用。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/foambubble/foam/tree/6acaa0b10d8198f096a6c2462a227674de322a48#readme) · [仓库元数据](https://api.github.com/repos/foambubble/foam) · [成熟发行 v0.2.0](https://github.com/foambubble/foam/releases/tag/v0.2.0)（2020-07-12）。

### 3. logseq/logseq
- 能做什么：大纲式个人知识管理，当前主线含数据库图谱方向。
- 为什么保留：可借鉴块级记录、链接和每日笔记组织。 适配判断25/30；按统一权重已知分73，在本项目候选中列第3。
- 代价和不能替代的部分：当前README明确数据库版beta、移动与实时协作alpha及数据丢失风险，不能直接迁移唯一权威库。
- 与自建比较：当前缺口是“尚未验证书中一个命题对实际场景是否有用。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/logseq/logseq/tree/7dfa9b45aee9d6a9387ddb3375018356f1e7c6a8#readme) · [仓库元数据](https://api.github.com/repos/logseq/logseq) · [成熟发行 v0.0.1](https://github.com/logseq/logseq/releases/tag/v0.0.1)（2020-10-01）。

采用前同样本检查：用一个原文命题解释真实案例，并记录不能解释的反例。

<a id="p-file-md"></a>
## 文件转 Markdown

项目要解决：把 EPUB、PDF 等材料转换为可追溯 Markdown。 本轮重点：现有验证限于原样本，未做全书校对或本轮重跑。

搜索：`document markdown`；卡ID `github-20261013-22`（同组复用）。 [自建不足](SELF-BUILT.md#p-file-md) · [候选取舍](AUDIT.md#p-file-md)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [docling-project/docling](https://github.com/docling-project/docling) | 84–96 | 30/30/8/6/10 | 68,814 | 2026-10-13 | MIT |
| 2. [microsoft/markitdown](https://github.com/microsoft/markitdown) | 84–96 | 30/26/10/8/10 | 189,927 | 2026-10-04 | MIT |
| 3. [opendatalab/MinerU](https://github.com/opendatalab/MinerU) | 74–86 | 30/28/8/4/4 | 81,641 | 2026-10-11 | Apache-2.0附商业门槛和署名条款（非标准） |

### 1. docling-project/docling
- 能做什么：解析多种文档、版面、表格与阅读顺序并导出结构化结果。
- 为什么保留：可补复杂PDF和多格式解析，保留现有来源锚点与质量检查。 适配判断30/30；按统一权重已知分84，在本项目候选中列第1。
- 代价和不能替代的部分：模型依赖、速度与本地资源成本需实测；复杂竖排、图表仍不能免抽查。
- 与自建比较：当前缺口是“现有验证限于原样本，未做全书校对或本轮重跑。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/docling-project/docling/tree/cb1df981e0b49906d638c652a27bfeeeb13ec5d1#readme) · [仓库元数据](https://api.github.com/repos/docling-project/docling) · [成熟发行 v0.1.1](https://github.com/docling-project/docling/releases/tag/v0.1.1)（2024-07-15）。

### 2. microsoft/markitdown
- 能做什么：轻量多格式文件到Markdown转换库。
- 为什么保留：适合保留普通文档结构并嵌入现有转换管线。 适配判断26/30；按统一权重已知分84，在本项目候选中列第2。
- 代价和不能替代的部分：README定位是文本分析输入，不能默认高保真版式、图片和复杂表格均正确。
- 与自建比较：当前缺口是“现有验证限于原样本，未做全书校对或本轮重跑。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/microsoft/markitdown/tree/4cc9fa17653d695d64fb9eee5b33d4de55ff84e8#readme) · [仓库元数据](https://api.github.com/repos/microsoft/markitdown) · [成熟发行 v0.0.1](https://github.com/microsoft/markitdown/releases/tag/v0.0.1)（2025-03-06）。

### 3. opendatalab/MinerU
- 能做什么：文档解析、OCR与结构化输出工具。
- 为什么保留：可作为扫描件、表格和公式的对照转换器。 适配判断28/30；按统一权重已知分74，在本项目候选中列第3。
- 代价和不能替代的部分：Apache-2.0附加商业门槛及署名条款，非纯标准许可；模型依赖及算力成本较高。
- 与自建比较：当前缺口是“现有验证限于原样本，未做全书校对或本轮重跑。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/opendatalab/MinerU/tree/b7f3dd0c5f6e6d66a298239ffd02b328b873918e#readme) · [仓库元数据](https://api.github.com/repos/opendatalab/MinerU) · [成熟发行 magic_pdf-0.1.0-released](https://github.com/opendatalab/MinerU/releases/tag/magic_pdf-0.1.0-released)（2024-03-04）。

采用前同样本检查：用下一份真实文档抽查正文、图片、表格及来源锚点，和Docling同样本比较。

<a id="p-future-simulator"></a>
## 时光机情景模拟器

项目要解决：比较条件变化下的未来情景并保留现实反馈入口。 本轮重点：情景效果、真机使用和反馈重算尚未验收。

搜索：`simulation dashboard`；卡ID `github-20261013-26`（同组复用）。 [自建不足](SELF-BUILT.md#p-future-simulator) · [候选取舍](AUDIT.md#p-future-simulator)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [streamlit/streamlit](https://github.com/streamlit/streamlit) | 84–96 | 30/28/8/8/10 | 45,971 | 2026-10-13 | Apache-2.0 |
| 2. [plotly/dash](https://github.com/plotly/dash) | 82–94 | 30/29/6/7/10 | 24,448 | 2026-10-09 | MIT |
| 3. [mesa/mesa](https://github.com/mesa/mesa) | 75–87 | 30/26/4/5/10 | 3,881 | 2026-10-09 | Apache-2.0 |

### 1. streamlit/streamlit
- 能做什么：快速构建数据与模型交互页面的Python框架。
- 为什么保留：可补情景参数输入、图表和计算过程展示。 适配判断28/30；按统一权重已知分84，在本项目候选中列第1。
- 代价和不能替代的部分：交互界面不保证预测有效；持久化、多用户和复杂前端需额外开发。
- 与自建比较：当前缺口是“情景效果、真机使用和反馈重算尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/streamlit/streamlit/tree/59479cb8b73dc881a209ebcf902171842d2b9bb8#readme) · [仓库元数据](https://api.github.com/repos/streamlit/streamlit) · [成熟发行 0.73.1](https://github.com/streamlit/streamlit/releases/tag/0.73.1)（2020-12-22）。

### 2. plotly/dash
- 能做什么：用Python构建交互图表和数据应用。
- 为什么保留：适合敏感性分析、多个参数联动和可解释结果。 适配判断29/30；按统一权重已知分82，在本项目候选中列第2。
- 代价和不能替代的部分：需要自己建立模型与回调；企业能力与开源能力要分开。
- 与自建比较：当前缺口是“情景效果、真机使用和反馈重算尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/plotly/dash/tree/8f3f73557b91a0bc8a269c1193bd0b93490f309d#readme) · [仓库元数据](https://api.github.com/repos/plotly/dash) · [成熟发行 v1.1.0](https://github.com/plotly/dash/releases/tag/v1.1.0)（2019-08-05）。

### 3. mesa/mesa
- 能做什么：Python的基于主体的模拟框架。
- 为什么保留：适合显式规则、重复实验和随机种子控制。 适配判断26/30；按统一权重已知分75，在本项目候选中列第3。
- 代价和不能替代的部分：不是LLM自动替代现实；模型假设和现实校准需自己负责。
- 与自建比较：当前缺口是“情景效果、真机使用和反馈重算尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/mesa/mesa/tree/5451086fe47ab78e9ba894aa1b4c3063f4c247f1#readme) · [仓库元数据](https://api.github.com/repos/mesa/mesa) · [成熟发行 v1.1.1](https://github.com/mesa/mesa/releases/tag/v1.1.1)（2022-10-21）。

采用前同样本检查：固定三项假设，改变其中一项，检查结果变化是否可解释且可重算。

<a id="p-ai-os"></a>
## AI 一人公司操作系统

项目要解决：用单一任务账本组织工作与验证。 本轮重点：启动包和规则存在，完整任务到成果回填尚需实测。

搜索：`project management`；卡ID `github-20261013-19`（同组复用）。 [自建不足](SELF-BUILT.md#p-ai-os) · [候选取舍](AUDIT.md#p-ai-os)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [MrLesk/Backlog.md](https://github.com/MrLesk/Backlog.md) | 81–93 | 30/30/4/7/10 | 7,018 | 2026-10-12 | MIT |
| 2. [kanboard/kanboard](https://github.com/kanboard/kanboard) | 80–92 | 30/28/4/8/10 | 9,906 | 2026-10-12 | MIT |
| 3. [makeplane/plane](https://github.com/makeplane/plane) | 74–86 | 30/26/8/5/5 | 60,770 | 2026-10-08 | AGPL-3.0 |

### 1. MrLesk/Backlog.md
- 能做什么：在Git仓库中用Markdown维护人和AI的任务。
- 为什么保留：与现有文件账本、审查记录和版本回滚较接近。 适配判断30/30；按统一权重已知分81，在本项目候选中列第1。
- 代价和不能替代的部分：不能另起一套权威状态；真实交接和发布授权仍需原有规则。
- 与自建比较：当前缺口是“启动包和规则存在，完整任务到成果回填尚需实测。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/MrLesk/Backlog.md/tree/92c79f84de5e8f1f6844ec5316f7b663da9fd4b9#readme) · [仓库元数据](https://api.github.com/repos/MrLesk/Backlog.md) · [成熟发行 v0.1.0](https://github.com/MrLesk/Backlog.md/releases/tag/v0.1.0)（2025-06-13）。

### 2. kanboard/kanboard
- 能做什么：轻量自托管看板与任务管理。
- 为什么保留：可补明确任务状态、看板和基本协作。 适配判断28/30；按统一权重已知分80，在本项目候选中列第2。
- 代价和不能替代的部分：不会自动把验收证据绑定到完成状态，也不理解自有代理协议。
- 与自建比较：当前缺口是“启动包和规则存在，完整任务到成果回填尚需实测。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/kanboard/kanboard/tree/ec3398d0d2b31d5051e2a077f475e286b5dd1228#readme) · [仓库元数据](https://api.github.com/repos/kanboard/kanboard) · [成熟发行 v1.0.9](https://github.com/kanboard/kanboard/releases/tag/v1.0.9)（2017-10-06）。

### 3. makeplane/plane
- 能做什么：提供任务、项目和协作视图的自托管平台。
- 为什么保留：可对照成熟任务状态、筛选和协作界面。 适配判断26/30；按统一权重已知分74，在本项目候选中列第3。
- 代价和不能替代的部分：AGPL与付费功能边界需区分；部署和迁移比轻量文件账本重。
- 与自建比较：当前缺口是“启动包和规则存在，完整任务到成果回填尚需实测。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/makeplane/plane/tree/bab49bb978ccb56af1d78dec6c6d54dfe8d03c1c#readme) · [仓库元数据](https://api.github.com/repos/makeplane/plane) · [成熟发行 v0.23.0](https://github.com/makeplane/plane/releases/tag/v0.23.0)（2024-10-07）。

采用前同样本检查：用一项真实任务走到账本登记、执行、验收、失败恢复与结果回填。

<a id="p-search-hub"></a>
## 统一搜索入口与来源库

项目要解决：跨信源查询、缓存与增量来源记录。 本轮重点：本轮实际出现短时限流且失败计入本地配额，可用次数被消耗。

搜索：`metasearch`；卡ID `github-20261013-41`（同组复用）。 [自建不足](SELF-BUILT.md#p-search-hub) · [候选取舍](AUDIT.md#p-search-hub)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [deedy5/ddgs](https://github.com/deedy5/ddgs) | 69–81 | 24/25/4/6/10 | 3,017 | 2026-08-26 | MIT |
| 2. [khoj-ai/khoj](https://github.com/khoj-ai/khoj) | 64–76 | 24/22/8/5/5 | 37,669 | 2026-08-02 | AGPL-3.0 |

**只保留2个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. deedy5/ddgs
- 能做什么：通过统一接口聚合多种网页搜索服务的库。
- 为什么保留：可借鉴搜索结果标准化与适配接口。 适配判断25/30；按统一权重已知分69，在本项目候选中列第1。
- 代价和不能替代的部分：不提供本地配额账本或可信度审查；后端限流仍存在，本轮不替换既有入口。
- 与自建比较：当前缺口是“本轮实际出现短时限流且失败计入本地配额，可用次数被消耗。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/deedy5/ddgs/tree/70a5635510fb8d5b15d5ba6ceced6a67e212149b#readme) · [仓库元数据](https://api.github.com/repos/deedy5/ddgs) · [成熟发行 v0.3](https://github.com/deedy5/ddgs/releases/tag/v0.3)（2021-05-05）。

### 2. khoj-ai/khoj
- 能做什么：结合个人文档与网络检索的AI应用。
- 为什么保留：可参考搜索到问答的交互及来源展示。 适配判断22/30；按统一权重已知分64，在本项目候选中列第2。
- 代价和不能替代的部分：比现有搜索中枢更重；模型、向量和部署成本需评估，不能同时建立第二知识真相。
- 与自建比较：当前缺口是“本轮实际出现短时限流且失败计入本地配额，可用次数被消耗。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/khoj-ai/khoj/tree/ae229ca894c0b80ad84664afcfdde523b5e87057#readme) · [仓库元数据](https://api.github.com/repos/khoj-ai/khoj) · [成熟发行 v0.1.6](https://github.com/khoj-ai/khoj/releases/tag/v0.1.6)（2022-08-19）。

采用前同样本检查：为一次限流保留状态，并以固定样本核对恢复后不重复计卡或漏项。

<a id="p-aduo-pipeline"></a>
## 阿舵知识生产管线

项目要解决：收集输入、保存状态与输出知识材料。 本轮重点：当前持续运行与维护归属未复核；资产保存不代表链路仍通。

搜索：`knowledge management`；卡ID `github-20261013-16`（同组复用）。 [自建不足](SELF-BUILT.md#p-aduo-pipeline) · [候选取舍](AUDIT.md#p-aduo-pipeline)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [siyuan-note/siyuan](https://github.com/siyuan-note/siyuan) | 80–92 | 30/29/8/8/5 | 46,741 | 2026-10-04 | AGPL-3.0 |
| 2. [foambubble/foam](https://github.com/foambubble/foam) | 79–91 | 30/27/6/6/10 | 17,446 | 2026-10-12 | MIT |
| 3. [logseq/logseq](https://github.com/logseq/logseq) | 74–86 | 30/26/8/5/5 | 45,220 | 2026-10-13 | AGPL-3.0 |

### 1. siyuan-note/siyuan
- 能做什么：重视隐私与块级引用的个人知识管理系统。
- 为什么保留：可补引用、检索、结构化笔记和中文编辑。 适配判断29/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：部分同步等功能付费；不能自动保证来源正确或学习效果。
- 与自建比较：当前缺口是“当前持续运行与维护归属未复核；资产保存不代表链路仍通。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/siyuan-note/siyuan/tree/fb3355f07d22bff36f1d785999fd5ded6a90d468#readme) · [仓库元数据](https://api.github.com/repos/siyuan-note/siyuan) · [成熟发行 v0.1.0](https://github.com/siyuan-note/siyuan/releases/tag/v0.1.0)（2020-08-31）。

### 2. foambubble/foam
- 能做什么：建立在VSCode和Markdown文件上的知识管理。
- 为什么保留：适合保留可版本控制的文本与链接关系。 适配判断27/30；按统一权重已知分79，在本项目候选中列第2。
- 代价和不能替代的部分：偏开发者环境，移动操作和非技术使用者体验需另验证。
- 与自建比较：当前缺口是“当前持续运行与维护归属未复核；资产保存不代表链路仍通。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/foambubble/foam/tree/6acaa0b10d8198f096a6c2462a227674de322a48#readme) · [仓库元数据](https://api.github.com/repos/foambubble/foam) · [成熟发行 v0.2.0](https://github.com/foambubble/foam/releases/tag/v0.2.0)（2020-07-12）。

### 3. logseq/logseq
- 能做什么：大纲式个人知识管理，当前主线含数据库图谱方向。
- 为什么保留：可借鉴块级记录、链接和每日笔记组织。 适配判断26/30；按统一权重已知分74，在本项目候选中列第3。
- 代价和不能替代的部分：当前README明确数据库版beta、移动与实时协作alpha及数据丢失风险，不能直接迁移唯一权威库。
- 与自建比较：当前缺口是“当前持续运行与维护归属未复核；资产保存不代表链路仍通。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/logseq/logseq/tree/7dfa9b45aee9d6a9387ddb3375018356f1e7c6a8#readme) · [仓库元数据](https://api.github.com/repos/logseq/logseq) · [成熟发行 v0.0.1](https://github.com/logseq/logseq/releases/tag/v0.0.1)（2020-10-01）。

采用前同样本检查：保持暂停；恢复时用同一条输入验证接收、去重、落盘、失败恢复四步。

<a id="p-ai-management"></a>
## AI 协作管理研究

项目要解决：以来源与离线评估检查协作方法。 本轮重点：离线评估尚未证明真实业务效率改善。

搜索：`project management`；卡ID `github-20261013-19`（同组复用）。 [自建不足](SELF-BUILT.md#p-ai-management) · [候选取舍](AUDIT.md#p-ai-management)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [MrLesk/Backlog.md](https://github.com/MrLesk/Backlog.md) | 77–89 | 30/26/4/7/10 | 7,018 | 2026-10-12 | MIT |
| 2. [kanboard/kanboard](https://github.com/kanboard/kanboard) | 77–89 | 30/25/4/8/10 | 9,906 | 2026-10-12 | MIT |
| 3. [opf/openproject](https://github.com/opf/openproject) | 75–87 | 30/28/6/5/6 | 16,404 | 2026-10-13 | GPL-3.0 |

### 1. MrLesk/Backlog.md
- 能做什么：在Git仓库中用Markdown维护人和AI的任务。
- 为什么保留：与现有文件账本、审查记录和版本回滚较接近。 适配判断26/30；按统一权重已知分77，在本项目候选中列第1。
- 代价和不能替代的部分：不能另起一套权威状态；真实交接和发布授权仍需原有规则。
- 与自建比较：当前缺口是“离线评估尚未证明真实业务效率改善。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/MrLesk/Backlog.md/tree/92c79f84de5e8f1f6844ec5316f7b663da9fd4b9#readme) · [仓库元数据](https://api.github.com/repos/MrLesk/Backlog.md) · [成熟发行 v0.1.0](https://github.com/MrLesk/Backlog.md/releases/tag/v0.1.0)（2025-06-13）。

### 2. kanboard/kanboard
- 能做什么：轻量自托管看板与任务管理。
- 为什么保留：可补明确任务状态、看板和基本协作。 适配判断25/30；按统一权重已知分77，在本项目候选中列第2。
- 代价和不能替代的部分：不会自动把验收证据绑定到完成状态，也不理解自有代理协议。
- 与自建比较：当前缺口是“离线评估尚未证明真实业务效率改善。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/kanboard/kanboard/tree/ec3398d0d2b31d5051e2a077f475e286b5dd1228#readme) · [仓库元数据](https://api.github.com/repos/kanboard/kanboard) · [成熟发行 v1.0.9](https://github.com/kanboard/kanboard/releases/tag/v1.0.9)（2017-10-06）。

### 3. opf/openproject
- 能做什么：包含工作包、甘特和项目协作的管理系统。
- 为什么保留：适合进度依赖、工程任务和责任跟踪。 适配判断28/30；按统一权重已知分75，在本项目候选中列第3。
- 代价和不能替代的部分：企业功能及运维成本需核对；个人轻量任务可能过重。
- 与自建比较：当前缺口是“离线评估尚未证明真实业务效率改善。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/opf/openproject/tree/496f9c5b7c4929379429970a2786a7f2402f940b#readme) · [仓库元数据](https://api.github.com/repos/opf/openproject) · [成熟发行 v9.0.0](https://github.com/opf/openproject/releases/tag/v9.0.0)（2019-06-05）。

采用前同样本检查：选一项现有业务，用相同输入分别按原流程与候选流程完成并计时。

<a id="p-project-board"></a>
## 项目进度公告板

项目要解决：从原账本生成可读项目状态视图。 本轮重点：冻结版本有隐私和状态语义问题，当前不能作为可交付公告板。

搜索：`project management`；卡ID `github-20261013-19`（同组复用）。 [自建不足](SELF-BUILT.md#p-project-board) · [候选取舍](AUDIT.md#p-project-board)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [MrLesk/Backlog.md](https://github.com/MrLesk/Backlog.md) | 81–93 | 30/30/4/7/10 | 7,018 | 2026-10-12 | MIT |
| 2. [kanboard/kanboard](https://github.com/kanboard/kanboard) | 80–92 | 30/28/4/8/10 | 9,906 | 2026-10-12 | MIT |
| 3. [makeplane/plane](https://github.com/makeplane/plane) | 74–86 | 30/26/8/5/5 | 60,770 | 2026-10-08 | AGPL-3.0 |

### 1. MrLesk/Backlog.md
- 能做什么：在Git仓库中用Markdown维护人和AI的任务。
- 为什么保留：与现有文件账本、审查记录和版本回滚较接近。 适配判断30/30；按统一权重已知分81，在本项目候选中列第1。
- 代价和不能替代的部分：不能另起一套权威状态；真实交接和发布授权仍需原有规则。
- 与自建比较：当前缺口是“冻结版本有隐私和状态语义问题，当前不能作为可交付公告板。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/MrLesk/Backlog.md/tree/92c79f84de5e8f1f6844ec5316f7b663da9fd4b9#readme) · [仓库元数据](https://api.github.com/repos/MrLesk/Backlog.md) · [成熟发行 v0.1.0](https://github.com/MrLesk/Backlog.md/releases/tag/v0.1.0)（2025-06-13）。

### 2. kanboard/kanboard
- 能做什么：轻量自托管看板与任务管理。
- 为什么保留：可补明确任务状态、看板和基本协作。 适配判断28/30；按统一权重已知分80，在本项目候选中列第2。
- 代价和不能替代的部分：不会自动把验收证据绑定到完成状态，也不理解自有代理协议。
- 与自建比较：当前缺口是“冻结版本有隐私和状态语义问题，当前不能作为可交付公告板。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/kanboard/kanboard/tree/ec3398d0d2b31d5051e2a077f475e286b5dd1228#readme) · [仓库元数据](https://api.github.com/repos/kanboard/kanboard) · [成熟发行 v1.0.9](https://github.com/kanboard/kanboard/releases/tag/v1.0.9)（2017-10-06）。

### 3. makeplane/plane
- 能做什么：提供任务、项目和协作视图的自托管平台。
- 为什么保留：可对照成熟任务状态、筛选和协作界面。 适配判断26/30；按统一权重已知分74，在本项目候选中列第3。
- 代价和不能替代的部分：AGPL与付费功能边界需区分；部署和迁移比轻量文件账本重。
- 与自建比较：当前缺口是“冻结版本有隐私和状态语义问题，当前不能作为可交付公告板。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/makeplane/plane/tree/bab49bb978ccb56af1d78dec6c6d54dfe8d03c1c#readme) · [仓库元数据](https://api.github.com/repos/makeplane/plane) · [成熟发行 v0.23.0](https://github.com/makeplane/plane/releases/tag/v0.23.0)（2024-10-07）。

采用前同样本检查：先修复QA中的公开边界与状态映射，再复跑同一失败用例。

<a id="p-founder-validation"></a>
## 创业服务验证研究

项目要解决：用历史证据和真实客户验证服务假设。 本轮重点：尚无真实客户购买验证，研究报告不能证明需求成立。

搜索：`deep research`；卡ID `github-20261013-23`（同组复用）。 [自建不足](SELF-BUILT.md#p-founder-validation) · [候选取舍](AUDIT.md#p-founder-validation)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 82–94 | 30/29/8/5/10 | 30,072 | 2026-10-10 | Apache-2.0 |

**只保留1个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. assafelovic/gpt-researcher
- 能做什么：带搜索、来源引用和报告输出的研究代理框架。
- 为什么保留：可借鉴查询分解、引用组织和研究流程编排。 适配判断29/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：需要模型/搜索服务配置且会产生调用成本；引用存在不等于可靠，不得把报告当市场验证。
- 与自建比较：当前缺口是“尚无真实客户购买验证，研究报告不能证明需求成立。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/assafelovic/gpt-researcher/tree/3582a6841fe7dc801e2a34e34ee408641aea9bce#readme) · [仓库元数据](https://api.github.com/repos/assafelovic/gpt-researcher) · [成熟发行 v1.0.1](https://github.com/assafelovic/gpt-researcher/releases/tag/v1.0.1)（2023-07-10）。

采用前同样本检查：保留研究成果，待恢复时只验证一个明确服务是否有人愿意支付。

<a id="p-hakuba-gis"></a>
## 公开地块 GIS 初筛工具

项目要解决：用公开空间资料做保留来源与不确定性的离线初筛。 本轮重点：现有成果不能替代专业尽调或直接给出投资批准。

搜索：`geospatial`；卡ID `github-20261013-27`（同组复用）。 [自建不足](SELF-BUILT.md#p-hakuba-gis) · [候选取舍](AUDIT.md#p-hakuba-gis)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [qgis/QGIS](https://github.com/qgis/QGIS) | 78–90 | 30/29/6/7/6 | 14,551 | 2026-10-13 | GPL-2.0 |
| 2. [geopandas/geopandas](https://github.com/geopandas/geopandas) | 78–90 | 30/28/4/6/10 | 5,277 | 2026-10-12 | BSD-3-Clause |
| 3. [ozekik/plateaukit](https://github.com/ozekik/plateaukit) | 64–76 | 24/24/1/5/10 | 29 | 2026-09-07 | MIT |

### 1. qgis/QGIS
- 能做什么：支持矢量、栅格等数据的跨平台GIS。
- 为什么保留：可补图层核对、坐标转换和独立空间检查。 适配判断29/30；按统一权重已知分78，在本项目候选中列第1。
- 代价和不能替代的部分：工具能叠图不代表图层时效或开发许可成立；需保留来源和专业核实。
- 与自建比较：当前缺口是“现有成果不能替代专业尽调或直接给出投资批准。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/qgis/QGIS/tree/d835ed0a563f5c286127c6f5efbdb5b1473e9adb#readme) · [仓库元数据](https://api.github.com/repos/qgis/QGIS) · [成熟发行 final-3_16_3](https://github.com/qgis/QGIS/releases/tag/final-3_16_3)（2021-01-15）。

### 2. geopandas/geopandas
- 能做什么：Python地理数据分析与空间操作库。
- 为什么保留：可补可重复的坐标、范围和空间连接检查。 适配判断28/30；按统一权重已知分78，在本项目候选中列第2。
- 代价和不能替代的部分：坐标参考不一致仍可能产生错误；没有尽调判断和行政许可结论。
- 与自建比较：当前缺口是“现有成果不能替代专业尽调或直接给出投资批准。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/geopandas/geopandas/tree/ee889bb6365319dee15b43ad001539ef10b090f0#readme) · [仓库元数据](https://api.github.com/repos/geopandas/geopandas) · [成熟发行 v0.2.1](https://github.com/geopandas/geopandas/releases/tag/v0.2.1)（2016-07-30）。

### 3. ozekik/plateaukit
- 能做什么：围绕日本PLATEAU三维城市数据的Python工具。
- 为什么保留：可补公开城市模型读取与研究流程。 适配判断24/30；按统一权重已知分64，在本项目候选中列第3。
- 代价和不能替代的部分：社区较小；具体地区覆盖、数据年份及数据许可需逐项确认。
- 与自建比较：当前缺口是“现有成果不能替代专业尽调或直接给出投资批准。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/ozekik/plateaukit/tree/f55a53285d2e00a0844d0a0c9667366bdb432a89#readme) · [仓库元数据](https://api.github.com/repos/ozekik/plateaukit) · [成熟发行 v0.11.2](https://github.com/ozekik/plateaukit/releases/tag/v0.11.2)（2024-03-05）。

采用前同样本检查：用一个已知公开地块核对坐标、数据年份及缺失图层的Hold行为。

<a id="p-design-workflow"></a>
## 统一设计工作流

项目要解决：连接来源、参数模型、图纸、视觉检查与恢复。 本轮重点：入口齐全不代表所有案例的生成、导出、验收均已闭环。

搜索：`parametric CAD`；卡ID `github-20261013-13`（同组复用）。 [自建不足](SELF-BUILT.md#p-design-workflow) · [候选取舍](AUDIT.md#p-design-workflow)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | 82–94 | 30/30/8/7/7 | 34,238 | 2026-10-13 | LGPL-2.1 |
| 2. [blender/blender](https://github.com/blender/blender) | 78–90 | 30/28/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 3. [CadQuery/cadquery](https://github.com/CadQuery/cadquery) | 74–86 | 30/25/4/5/10 | 5,925 | 2026-10-10 | Apache-2.0 |

### 1. FreeCAD/FreeCAD
- 能做什么：参数化实体、尺寸约束与工程建模。
- 为什么保留：可补尺寸驱动、保存重开和工程导出基础。 适配判断30/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：不是日本规范验算或施工批准工具；跨软件交换需单独测试。
- 与自建比较：当前缺口是“入口齐全不代表所有案例的生成、导出、验收均已闭环。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/FreeCAD/FreeCAD/tree/c8c9ea855080c9e0f2f22b583cddbed1c0cf2a07#readme) · [仓库元数据](https://api.github.com/repos/FreeCAD/FreeCAD) · [成熟发行 0.15](https://github.com/FreeCAD/FreeCAD/releases/tag/0.15)（2015-07-03）。

### 2. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断28/30；按统一权重已知分78，在本项目候选中列第2。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“入口齐全不代表所有案例的生成、导出、验收均已闭环。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 3. CadQuery/cadquery
- 能做什么：用Python脚本生成可复用的参数化CAD实体。
- 为什么保留：适合家具及构件批量参数化、尺寸回归。 适配判断25/30；按统一权重已知分74，在本项目候选中列第3。
- 代价和不能替代的部分：不是完整设计协作界面；依赖CAD内核和Python环境。
- 与自建比较：当前缺口是“入口齐全不代表所有案例的生成、导出、验收均已闭环。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/CadQuery/cadquery/tree/5f5bc62b255f62e3512105740025361b6c31eddd#readme) · [仓库元数据](https://api.github.com/repos/CadQuery/cadquery) · [成熟发行 2.0](https://github.com/CadQuery/cadquery/releases/tag/2.0)（2020-04-24）。

采用前同样本检查：选择一个已有案例，从修改到导出再到独立验收完整重放一次。

<a id="p-material-library"></a>
## 设计素材库

项目要解决：按来源与使用许可登记可复用模型和材质。 本轮重点：本轮未重新审查许可，登记不代表每个用途都可商用。

搜索：`digital asset management`；卡ID `github-20261013-17`（同组复用）。 [自建不足](SELF-BUILT.md#p-material-library) · [候选取舍](AUDIT.md#p-material-library)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [blender/blender](https://github.com/blender/blender) | 80–92 | 30/30/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 2. [immich-app/immich](https://github.com/immich-app/immich) | 76–88 | 30/24/10/7/5 | 116,145 | 2026-10-13 | AGPL-3.0 |
| 3. [hydrusnetwork/hydrus](https://github.com/hydrusnetwork/hydrus) | 65–77 | 30/23/4/4/4 | 3,238 | 2026-09-30 | WTFPL v3（非标准许可） |

### 1. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断30/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“本轮未重新审查许可，登记不代表每个用途都可商用。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 2. immich-app/immich
- 能做什么：自托管照片与视频管理，支持相册、去重与多设备访问。
- 为什么保留：适合参考图、视觉对比和素材浏览。 适配判断24/30；按统一权重已知分76，在本项目候选中列第2。
- 代价和不能替代的部分：不负责材质节点、授权审查或审美偏好学习；需服务端和备份，不能只保留图库一份。
- 与自建比较：当前缺口是“本轮未重新审查许可，登记不代表每个用途都可商用。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/immich-app/immich/tree/d519140a6c4d9bc8c392e08a29679ddf3326d917#readme) · [仓库元数据](https://api.github.com/repos/immich-app/immich) · [成熟发行 v1.43.0](https://github.com/immich-app/immich/releases/tag/v1.43.0)（2023-01-27）。

### 3. hydrusnetwork/hydrus
- 能做什么：以标签为核心的桌面图片、视频等媒体管理。
- 为什么保留：适合大量参考图的分类、检索和相似素材整理。 适配判断23/30；按统一权重已知分65，在本项目候选中列第3。
- 代价和不能替代的部分：许可证为自定义WTFPL v3，按非标准许可处理；README提供的可执行包主要为Windows/Linux，macOS需额外核实。
- 与自建比较：当前缺口是“本轮未重新审查许可，登记不代表每个用途都可商用。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/hydrusnetwork/hydrus/tree/2656f9a1fad88bf261feb29c1b24ddd93bbc3205#readme) · [仓库元数据](https://api.github.com/repos/hydrusnetwork/hydrus) · [成熟发行 v132](https://github.com/hydrusnetwork/hydrus/releases/tag/v132)（2014-10-01）。

采用前同样本检查：抽一个真实项目，核对三件素材的来源、许可、色彩空间和尺寸。

<a id="p-aesthetic-dictionary"></a>
## 共同审美字典

项目要解决：通过实际图像比较积累可解释的设计偏好。 本轮重点：尚无人工偏好确认，不能将图片排版当作已学到审美。

搜索：`digital asset management`；卡ID `github-20261013-17`（同组复用）。 [自建不足](SELF-BUILT.md#p-aesthetic-dictionary) · [候选取舍](AUDIT.md#p-aesthetic-dictionary)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [immich-app/immich](https://github.com/immich-app/immich) | 82–94 | 30/30/10/7/5 | 116,145 | 2026-10-13 | AGPL-3.0 |
| 2. [blender/blender](https://github.com/blender/blender) | 72–84 | 30/22/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 3. [hydrusnetwork/hydrus](https://github.com/hydrusnetwork/hydrus) | 70–82 | 30/28/4/4/4 | 3,238 | 2026-09-30 | WTFPL v3（非标准许可） |

### 1. immich-app/immich
- 能做什么：自托管照片与视频管理，支持相册、去重与多设备访问。
- 为什么保留：适合参考图、视觉对比和素材浏览。 适配判断30/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：不负责材质节点、授权审查或审美偏好学习；需服务端和备份，不能只保留图库一份。
- 与自建比较：当前缺口是“尚无人工偏好确认，不能将图片排版当作已学到审美。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/immich-app/immich/tree/d519140a6c4d9bc8c392e08a29679ddf3326d917#readme) · [仓库元数据](https://api.github.com/repos/immich-app/immich) · [成熟发行 v1.43.0](https://github.com/immich-app/immich/releases/tag/v1.43.0)（2023-01-27）。

### 2. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断22/30；按统一权重已知分72，在本项目候选中列第2。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“尚无人工偏好确认，不能将图片排版当作已学到审美。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 3. hydrusnetwork/hydrus
- 能做什么：以标签为核心的桌面图片、视频等媒体管理。
- 为什么保留：适合大量参考图的分类、检索和相似素材整理。 适配判断28/30；按统一权重已知分70，在本项目候选中列第3。
- 代价和不能替代的部分：许可证为自定义WTFPL v3，按非标准许可处理；README提供的可执行包主要为Windows/Linux，macOS需额外核实。
- 与自建比较：当前缺口是“尚无人工偏好确认，不能将图片排版当作已学到审美。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/hydrusnetwork/hydrus/tree/2656f9a1fad88bf261feb29c1b24ddd93bbc3205#readme) · [仓库元数据](https://api.github.com/repos/hydrusnetwork/hydrus) · [成熟发行 v132](https://github.com/hydrusnetwork/hydrus/releases/tag/v132)（2014-10-01）。

采用前同样本检查：完成一次同条件两图比较，记录喜欢与不喜欢的具体元素，并复测一次。

<a id="p-muji-model"></a>
## 公开小屋虚拟设计委托

项目要解决：依据公开小屋资料做有限虚拟设计验证。 本轮重点：整体细节和原生修改仍待验收。

搜索：`parametric CAD`；卡ID `github-20261013-13`（同组复用）。 [自建不足](SELF-BUILT.md#p-muji-model) · [候选取舍](AUDIT.md#p-muji-model)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | 82–94 | 30/30/8/7/7 | 34,238 | 2026-10-13 | LGPL-2.1 |
| 2. [blender/blender](https://github.com/blender/blender) | 78–90 | 30/28/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 3. [CadQuery/cadquery](https://github.com/CadQuery/cadquery) | 74–86 | 30/25/4/5/10 | 5,925 | 2026-10-10 | Apache-2.0 |

### 1. FreeCAD/FreeCAD
- 能做什么：参数化实体、尺寸约束与工程建模。
- 为什么保留：可补尺寸驱动、保存重开和工程导出基础。 适配判断30/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：不是日本规范验算或施工批准工具；跨软件交换需单独测试。
- 与自建比较：当前缺口是“整体细节和原生修改仍待验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/FreeCAD/FreeCAD/tree/c8c9ea855080c9e0f2f22b583cddbed1c0cf2a07#readme) · [仓库元数据](https://api.github.com/repos/FreeCAD/FreeCAD) · [成熟发行 0.15](https://github.com/FreeCAD/FreeCAD/releases/tag/0.15)（2015-07-03）。

### 2. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断28/30；按统一权重已知分78，在本项目候选中列第2。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“整体细节和原生修改仍待验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 3. CadQuery/cadquery
- 能做什么：用Python脚本生成可复用的参数化CAD实体。
- 为什么保留：适合家具及构件批量参数化、尺寸回归。 适配判断25/30；按统一权重已知分74，在本项目候选中列第3。
- 代价和不能替代的部分：不是完整设计协作界面；依赖CAD内核和Python环境。
- 与自建比较：当前缺口是“整体细节和原生修改仍待验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/CadQuery/cadquery/tree/5f5bc62b255f62e3512105740025361b6c31eddd#readme) · [仓库元数据](https://api.github.com/repos/CadQuery/cadquery) · [成熟发行 2.0](https://github.com/CadQuery/cadquery/releases/tag/2.0)（2020-04-24）。

采用前同样本检查：用原生工具改一个关键尺寸，核对相关平面、立面和效果图。

<a id="p-container-model"></a>
## 模块房屋模型验证

项目要解决：用独立版本验证模块房屋布局、开洞与材质修改。 本轮重点：新版技术检查与用户验收仍是分开的未闭合环节。

搜索：`parametric CAD`；卡ID `github-20261013-13`（同组复用）。 [自建不足](SELF-BUILT.md#p-container-model) · [候选取舍](AUDIT.md#p-container-model)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | 82–94 | 30/30/8/7/7 | 34,238 | 2026-10-13 | LGPL-2.1 |
| 2. [blender/blender](https://github.com/blender/blender) | 78–90 | 30/28/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 3. [CadQuery/cadquery](https://github.com/CadQuery/cadquery) | 74–86 | 30/25/4/5/10 | 5,925 | 2026-10-10 | Apache-2.0 |

### 1. FreeCAD/FreeCAD
- 能做什么：参数化实体、尺寸约束与工程建模。
- 为什么保留：可补尺寸驱动、保存重开和工程导出基础。 适配判断30/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：不是日本规范验算或施工批准工具；跨软件交换需单独测试。
- 与自建比较：当前缺口是“新版技术检查与用户验收仍是分开的未闭合环节。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/FreeCAD/FreeCAD/tree/c8c9ea855080c9e0f2f22b583cddbed1c0cf2a07#readme) · [仓库元数据](https://api.github.com/repos/FreeCAD/FreeCAD) · [成熟发行 0.15](https://github.com/FreeCAD/FreeCAD/releases/tag/0.15)（2015-07-03）。

### 2. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断28/30；按统一权重已知分78，在本项目候选中列第2。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“新版技术检查与用户验收仍是分开的未闭合环节。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 3. CadQuery/cadquery
- 能做什么：用Python脚本生成可复用的参数化CAD实体。
- 为什么保留：适合家具及构件批量参数化、尺寸回归。 适配判断25/30；按统一权重已知分74，在本项目候选中列第3。
- 代价和不能替代的部分：不是完整设计协作界面；依赖CAD内核和Python环境。
- 与自建比较：当前缺口是“新版技术检查与用户验收仍是分开的未闭合环节。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/CadQuery/cadquery/tree/5f5bc62b255f62e3512105740025361b6c31eddd#readme) · [仓库元数据](https://api.github.com/repos/CadQuery/cadquery) · [成熟发行 2.0](https://github.com/CadQuery/cadquery/releases/tag/2.0)（2020-04-24）。

采用前同样本检查：改一个开洞尺寸，核对模型、立面、材料量和碰撞检查是否同步。

<a id="p-hotel-room-model"></a>
## 酒店客房设计技术小样

项目要解决：有限客房模型、节点图和材料表的联动验证。 本轮重点：技术小样不构成施工设计批准。

搜索：`parametric CAD`；卡ID `github-20261013-13`（同组复用）。 [自建不足](SELF-BUILT.md#p-hotel-room-model) · [候选取舍](AUDIT.md#p-hotel-room-model)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | 82–94 | 30/30/8/7/7 | 34,238 | 2026-10-13 | LGPL-2.1 |
| 2. [blender/blender](https://github.com/blender/blender) | 78–90 | 30/28/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 3. [CadQuery/cadquery](https://github.com/CadQuery/cadquery) | 74–86 | 30/25/4/5/10 | 5,925 | 2026-10-10 | Apache-2.0 |

### 1. FreeCAD/FreeCAD
- 能做什么：参数化实体、尺寸约束与工程建模。
- 为什么保留：可补尺寸驱动、保存重开和工程导出基础。 适配判断30/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：不是日本规范验算或施工批准工具；跨软件交换需单独测试。
- 与自建比较：当前缺口是“技术小样不构成施工设计批准。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/FreeCAD/FreeCAD/tree/c8c9ea855080c9e0f2f22b583cddbed1c0cf2a07#readme) · [仓库元数据](https://api.github.com/repos/FreeCAD/FreeCAD) · [成熟发行 0.15](https://github.com/FreeCAD/FreeCAD/releases/tag/0.15)（2015-07-03）。

### 2. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断28/30；按统一权重已知分78，在本项目候选中列第2。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“技术小样不构成施工设计批准。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 3. CadQuery/cadquery
- 能做什么：用Python脚本生成可复用的参数化CAD实体。
- 为什么保留：适合家具及构件批量参数化、尺寸回归。 适配判断25/30；按统一权重已知分74，在本项目候选中列第3。
- 代价和不能替代的部分：不是完整设计协作界面；依赖CAD内核和Python环境。
- 与自建比较：当前缺口是“技术小样不构成施工设计批准。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/CadQuery/cadquery/tree/5f5bc62b255f62e3512105740025361b6c31eddd#readme) · [仓库元数据](https://api.github.com/repos/CadQuery/cadquery) · [成熟发行 2.0](https://github.com/CadQuery/cadquery/releases/tag/2.0)（2020-04-24）。

采用前同样本检查：选择一处节点，核对模型、图纸、材料表和现场尺寸的一致性。

<a id="p-house-vol114"></a>
## 公开住宅整栋建模

项目要解决：依据公开住宅资料建立可检查的整栋模型。 本轮重点：现有报告明确有急转、面壁及门洞净距不足，不能认定成片通过。

搜索：`parametric CAD`；卡ID `github-20261013-13`（同组复用）。 [自建不足](SELF-BUILT.md#p-house-vol114) · [候选取舍](AUDIT.md#p-house-vol114)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [blender/blender](https://github.com/blender/blender) | 80–92 | 30/30/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 2. [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | 77–89 | 30/25/8/7/7 | 34,238 | 2026-10-13 | LGPL-2.1 |
| 3. [mltframework/shotcut](https://github.com/mltframework/shotcut) | 76–88 | 30/26/6/8/6 | 15,411 | 2026-10-12 | GPL-3.0 |

### 1. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断30/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“现有报告明确有急转、面壁及门洞净距不足，不能认定成片通过。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 2. FreeCAD/FreeCAD
- 能做什么：参数化实体、尺寸约束与工程建模。
- 为什么保留：可补尺寸驱动、保存重开和工程导出基础。 适配判断25/30；按统一权重已知分77，在本项目候选中列第2。
- 代价和不能替代的部分：不是日本规范验算或施工批准工具；跨软件交换需单独测试。
- 与自建比较：当前缺口是“现有报告明确有急转、面壁及门洞净距不足，不能认定成片通过。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/FreeCAD/FreeCAD/tree/c8c9ea855080c9e0f2f22b583cddbed1c0cf2a07#readme) · [仓库元数据](https://api.github.com/repos/FreeCAD/FreeCAD) · [成熟发行 0.15](https://github.com/FreeCAD/FreeCAD/releases/tag/0.15)（2015-07-03）。

### 3. mltframework/shotcut
- 能做什么：跨平台视频编辑器。
- 为什么保留：可补时间线剪辑、音画同步和导出检查。 适配判断26/30；按统一权重已知分76，在本项目候选中列第3。
- 代价和不能替代的部分：不是文生视频模型，也不会自动审核脚本、适龄性或来源权利。
- 与自建比较：当前缺口是“现有报告明确有急转、面壁及门洞净距不足，不能认定成片通过。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/mltframework/shotcut/tree/f360166260fa5dbe93003c5756567cb4b132dbdb#readme) · [仓库元数据](https://api.github.com/repos/mltframework/shotcut) · [成熟发行 v14.05](https://github.com/mltframework/shotcut/releases/tag/v14.05)（2014-05-03）。

采用前同样本检查：修复一段急转和门洞净距，再用同一路径前后对比检查。

<a id="p-house-corner"></a>
## 公开转角住宅建模

项目要解决：依据公开案例建立模型并保留再生成步骤。 本轮重点：本轮未做视觉或施工验收，旧手顺还曾落后于文件现状。

搜索：`parametric CAD`；卡ID `github-20261013-13`（同组复用）。 [自建不足](SELF-BUILT.md#p-house-corner) · [候选取舍](AUDIT.md#p-house-corner)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | 82–94 | 30/30/8/7/7 | 34,238 | 2026-10-13 | LGPL-2.1 |
| 2. [blender/blender](https://github.com/blender/blender) | 78–90 | 30/28/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 3. [CadQuery/cadquery](https://github.com/CadQuery/cadquery) | 74–86 | 30/25/4/5/10 | 5,925 | 2026-10-10 | Apache-2.0 |

### 1. FreeCAD/FreeCAD
- 能做什么：参数化实体、尺寸约束与工程建模。
- 为什么保留：可补尺寸驱动、保存重开和工程导出基础。 适配判断30/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：不是日本规范验算或施工批准工具；跨软件交换需单独测试。
- 与自建比较：当前缺口是“本轮未做视觉或施工验收，旧手顺还曾落后于文件现状。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/FreeCAD/FreeCAD/tree/c8c9ea855080c9e0f2f22b583cddbed1c0cf2a07#readme) · [仓库元数据](https://api.github.com/repos/FreeCAD/FreeCAD) · [成熟发行 0.15](https://github.com/FreeCAD/FreeCAD/releases/tag/0.15)（2015-07-03）。

### 2. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断28/30；按统一权重已知分78，在本项目候选中列第2。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“本轮未做视觉或施工验收，旧手顺还曾落后于文件现状。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 3. CadQuery/cadquery
- 能做什么：用Python脚本生成可复用的参数化CAD实体。
- 为什么保留：适合家具及构件批量参数化、尺寸回归。 适配判断25/30；按统一权重已知分74，在本项目候选中列第3。
- 代价和不能替代的部分：不是完整设计协作界面；依赖CAD内核和Python环境。
- 与自建比较：当前缺口是“本轮未做视觉或施工验收，旧手顺还曾落后于文件现状。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/CadQuery/cadquery/tree/5f5bc62b255f62e3512105740025361b6c31eddd#readme) · [仓库元数据](https://api.github.com/repos/CadQuery/cadquery) · [成熟发行 2.0](https://github.com/CadQuery/cadquery/releases/tag/2.0)（2020-04-24）。

采用前同样本检查：确认正式册子包含四张现行效果图，并抽查图纸与模型版本一致。

<a id="p-plan-material-cases"></a>
## 公开图纸与材质案例库

项目要解决：保留公开图纸链接、文件与材料深度边界。 本轮重点：案例类型不同，不能直接横比成可施工模板。

搜索：`digital asset management`；卡ID `github-20261013-17`（同组复用）。 [自建不足](SELF-BUILT.md#p-plan-material-cases) · [候选取舍](AUDIT.md#p-plan-material-cases)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [eikek/docspell](https://github.com/eikek/docspell) | 72–84 | 30/29/3/5/5 | 2,336 | 2026-10-13 | AGPL-3.0 |
| 2. [immich-app/immich](https://github.com/immich-app/immich) | 70–82 | 30/18/10/7/5 | 116,145 | 2026-10-13 | AGPL-3.0 |
| 3. [DSpace/DSpace](https://github.com/DSpace/DSpace) | 65–77 | 30/20/3/2/10 | 1,102 | 2026-10-12 | BSD-3-Clause |

### 1. eikek/docspell
- 能做什么：面向个人和家庭的文档整理、标签与检索服务。
- 为什么保留：可借鉴文件归档与文档元数据管理。 适配判断29/30；按统一权重已知分72，在本项目候选中列第1。
- 代价和不能替代的部分：需部署服务；不是PBR材质管理器，审美和许可判断仍需自己记录。
- 与自建比较：当前缺口是“案例类型不同，不能直接横比成可施工模板。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/eikek/docspell/tree/b0006733c13e6e7a848a424af56dc3d92576674d#readme) · [仓库元数据](https://api.github.com/repos/eikek/docspell) · [成熟发行 v0.1.0](https://github.com/eikek/docspell/releases/tag/v0.1.0)（2019-09-21）。

### 2. immich-app/immich
- 能做什么：自托管照片与视频管理，支持相册、去重与多设备访问。
- 为什么保留：适合参考图、视觉对比和素材浏览。 适配判断18/30；按统一权重已知分70，在本项目候选中列第2。
- 代价和不能替代的部分：不负责材质节点、授权审查或审美偏好学习；需服务端和备份，不能只保留图库一份。
- 与自建比较：当前缺口是“案例类型不同，不能直接横比成可施工模板。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/immich-app/immich/tree/d519140a6c4d9bc8c392e08a29679ddf3326d917#readme) · [仓库元数据](https://api.github.com/repos/immich-app/immich) · [成熟发行 v1.43.0](https://github.com/immich-app/immich/releases/tag/v1.43.0)（2023-01-27）。

### 3. DSpace/DSpace
- 能做什么：面向机构的数字资源与资料库管理。
- 为什么保留：可借鉴档案元数据和资源出处管理。 适配判断20/30；按统一权重已知分65，在本项目候选中列第3。
- 代价和不能替代的部分：机构级系统较重，个人26套家具与少量材质不宜为此整体迁移。
- 与自建比较：当前缺口是“案例类型不同，不能直接横比成可施工模板。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/DSpace/DSpace/tree/de3b0536d3ef9b11edc739f8160b5016fd740cda#readme) · [仓库元数据](https://api.github.com/repos/DSpace/DSpace) · [成熟发行 dspace-1.7.2](https://github.com/DSpace/DSpace/releases/tag/dspace-1.7.2)（2015-07-21）。

采用前同样本检查：选择一个案例，核对一张图的比例、材料标注和原始出处。

<a id="p-smart-home"></a>
## 智能家居参考研究

项目要解决：整理 HomeKit 与未来居住的公开参考。 本轮重点：视频备案不等于型号、接口、购买或部署已核实。

搜索：`home automation`；卡ID `github-20261013-25`（同组复用）。 [自建不足](SELF-BUILT.md#p-smart-home) · [候选取舍](AUDIT.md#p-smart-home)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [home-assistant/core](https://github.com/home-assistant/core) | 85–97 | 30/30/8/7/10 | 91,465 | 2026-10-13 | Apache-2.0 |
| 2. [esphome/esphome](https://github.com/esphome/esphome) | 71–83 | 30/24/6/5/6 | 11,860 | 2026-10-13 | MIT / GPL-3.0（按组件） |

**只保留2个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. home-assistant/core
- 能做什么：强调本地控制的家庭自动化平台。
- 为什么保留：优先复用设备集成和自动化规则，不必重写家庭网关。 适配判断30/30；按统一权重已知分85，在本项目候选中列第1。
- 代价和不能替代的部分：具体设备型号、云依赖和断网行为仍要逐台验证；不能视作通用家务机器人。
- 与自建比较：当前缺口是“视频备案不等于型号、接口、购买或部署已核实。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/home-assistant/core/tree/aeb1a1c65922739ccb8e7b9abf3d6f554299b912#readme) · [仓库元数据](https://api.github.com/repos/home-assistant/core) · [成熟发行 Last-Python2-release](https://github.com/home-assistant/core/releases/tag/Last-Python2-release)（2014-04-13）。

### 2. esphome/esphome
- 能做什么：为嵌入式设备提供配置化固件与家庭自动化集成。
- 为什么保留：可补传感器与自定义小设备接口。 适配判断24/30；按统一权重已知分71，在本项目候选中列第2。
- 代价和不能替代的部分：Python部分MIT、运行时GPL-3.0；需要适配实际硬件，不等于成品家电兼容。
- 与自建比较：当前缺口是“视频备案不等于型号、接口、购买或部署已核实。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/esphome/esphome/tree/29a668af0443ab80e29fa29753a56160bbd57db3#readme) · [仓库元数据](https://api.github.com/repos/esphome/esphome) · [成熟发行 v1.1](https://github.com/esphome/esphome/releases/tag/v1.1)（2018-04-06）。

采用前同样本检查：选一台已有设备，核对协议并测试一次断网后的本地控制。

<a id="p-video-workflow"></a>
## 视频生产与研究工作流

项目要解决：保留视频来源、镜头拆解与有限制作成果。 本轮重点：文件归集不代表生成器路径迁移和案例生产仍可运行。

搜索：`video generation`；卡ID `github-20261013-32`（同组复用）。 [自建不足](SELF-BUILT.md#p-video-workflow) · [候选取舍](AUDIT.md#p-video-workflow)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 82–94 | 30/26/10/6/10 | 130,463 | 2026-10-13 | MIT |
| 2. [mltframework/shotcut](https://github.com/mltframework/shotcut) | 79–91 | 30/29/6/8/6 | 15,411 | 2026-10-12 | GPL-3.0 |
| 3. [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 77–89 | 30/27/10/4/6 | 137,283 | 2026-10-13 | GPL-3.0 |

### 1. harry0703/MoneyPrinterTurbo
- 能做什么：将文案、素材、配音和字幕组合成视频的应用。
- 为什么保留：可参考流水线编排、批量生成及字幕输出。 适配判断26/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：外部素材和TTS有独立许可与依赖；默认合成声不能替代已认可音色，自动成片仍需审片。
- 与自建比较：当前缺口是“文件归集不代表生成器路径迁移和案例生产仍可运行。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/harry0703/MoneyPrinterTurbo/tree/bbe7eb9ae3e7a44f4553070b82d4a126aad62a33#readme) · [仓库元数据](https://api.github.com/repos/harry0703/MoneyPrinterTurbo) · [成熟发行 v1.1.0](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.1.0)（2024-04-11）。

### 2. mltframework/shotcut
- 能做什么：跨平台视频编辑器。
- 为什么保留：可补时间线剪辑、音画同步和导出检查。 适配判断29/30；按统一权重已知分79，在本项目候选中列第2。
- 代价和不能替代的部分：不是文生视频模型，也不会自动审核脚本、适龄性或来源权利。
- 与自建比较：当前缺口是“文件归集不代表生成器路径迁移和案例生产仍可运行。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/mltframework/shotcut/tree/f360166260fa5dbe93003c5756567cb4b132dbdb#readme) · [仓库元数据](https://api.github.com/repos/mltframework/shotcut) · [成熟发行 v14.05](https://github.com/mltframework/shotcut/releases/tag/v14.05)（2014-05-03）。

### 3. Comfy-Org/ComfyUI
- 能做什么：节点式图像、视频及其他生成模型工作流。
- 为什么保留：可保留可复用节点、输入参数与可重复的生成过程。 适配判断27/30；按统一权重已知分77，在本项目候选中列第3。
- 代价和不能替代的部分：不同模型权重及插件许可分别核对；显存和速度随模型变化，macOS运行不等于大模型可流畅使用。
- 与自建比较：当前缺口是“文件归集不代表生成器路径迁移和案例生产仍可运行。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/Comfy-Org/ComfyUI/tree/8010b48d2c1be986613f8e8c761527d205bd756f#readme) · [仓库元数据](https://api.github.com/repos/Comfy-Org/ComfyUI) · [成熟发行 v0.0.1](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.0.1)（2024-07-12）。

采用前同样本检查：选一个旧案例，以新权威路径完整重放一个短片段并核对依赖。

<a id="p-kids-video"></a>
## 儿童影片生产线

项目要解决：儿童内容的脚本、分镜与制作阶段管理。 本轮重点：没有本轮成片验收，不能把生产计划当交付。

搜索：`video generation`；卡ID `github-20261013-32`（同组复用）。 [自建不足](SELF-BUILT.md#p-kids-video) · [候选取舍](AUDIT.md#p-kids-video)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [mltframework/shotcut](https://github.com/mltframework/shotcut) | 80–92 | 30/30/6/8/6 | 15,411 | 2026-10-12 | GPL-3.0 |
| 2. [blender/blender](https://github.com/blender/blender) | 79–91 | 30/29/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 3. [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 76–88 | 30/20/10/6/10 | 130,463 | 2026-10-13 | MIT |

### 1. mltframework/shotcut
- 能做什么：跨平台视频编辑器。
- 为什么保留：可补时间线剪辑、音画同步和导出检查。 适配判断30/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：不是文生视频模型，也不会自动审核脚本、适龄性或来源权利。
- 与自建比较：当前缺口是“没有本轮成片验收，不能把生产计划当交付。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/mltframework/shotcut/tree/f360166260fa5dbe93003c5756567cb4b132dbdb#readme) · [仓库元数据](https://api.github.com/repos/mltframework/shotcut) · [成熟发行 v14.05](https://github.com/mltframework/shotcut/releases/tag/v14.05)（2014-05-03）。

### 2. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断29/30；按统一权重已知分79，在本项目候选中列第2。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“没有本轮成片验收，不能把生产计划当交付。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 3. harry0703/MoneyPrinterTurbo
- 能做什么：将文案、素材、配音和字幕组合成视频的应用。
- 为什么保留：可参考流水线编排、批量生成及字幕输出。 适配判断20/30；按统一权重已知分76，在本项目候选中列第3。
- 代价和不能替代的部分：外部素材和TTS有独立许可与依赖；默认合成声不能替代已认可音色，自动成片仍需审片。
- 与自建比较：当前缺口是“没有本轮成片验收，不能把生产计划当交付。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/harry0703/MoneyPrinterTurbo/tree/bbe7eb9ae3e7a44f4553070b82d4a126aad62a33#readme) · [仓库元数据](https://api.github.com/repos/harry0703/MoneyPrinterTurbo) · [成熟发行 v1.1.0](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.1.0)（2024-04-11）。

采用前同样本检查：维持暂停；恢复时只制作一个短片段并完成适龄与音画核对。

<a id="p-cinedrop"></a>
## 视频案例与原创剧本研究

项目要解决：分析参考视频并保留独立原创剧本。 本轮重点：剧本尚未转成可审看的原创成片。

搜索：`video generation`；卡ID `github-20261013-32`（同组复用）。 [自建不足](SELF-BUILT.md#p-cinedrop) · [候选取舍](AUDIT.md#p-cinedrop)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 82–94 | 30/26/10/6/10 | 130,463 | 2026-10-13 | MIT |
| 2. [mltframework/shotcut](https://github.com/mltframework/shotcut) | 79–91 | 30/29/6/8/6 | 15,411 | 2026-10-12 | GPL-3.0 |
| 3. [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 77–89 | 30/27/10/4/6 | 137,283 | 2026-10-13 | GPL-3.0 |

### 1. harry0703/MoneyPrinterTurbo
- 能做什么：将文案、素材、配音和字幕组合成视频的应用。
- 为什么保留：可参考流水线编排、批量生成及字幕输出。 适配判断26/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：外部素材和TTS有独立许可与依赖；默认合成声不能替代已认可音色，自动成片仍需审片。
- 与自建比较：当前缺口是“剧本尚未转成可审看的原创成片。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/harry0703/MoneyPrinterTurbo/tree/bbe7eb9ae3e7a44f4553070b82d4a126aad62a33#readme) · [仓库元数据](https://api.github.com/repos/harry0703/MoneyPrinterTurbo) · [成熟发行 v1.1.0](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.1.0)（2024-04-11）。

### 2. mltframework/shotcut
- 能做什么：跨平台视频编辑器。
- 为什么保留：可补时间线剪辑、音画同步和导出检查。 适配判断29/30；按统一权重已知分79，在本项目候选中列第2。
- 代价和不能替代的部分：不是文生视频模型，也不会自动审核脚本、适龄性或来源权利。
- 与自建比较：当前缺口是“剧本尚未转成可审看的原创成片。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/mltframework/shotcut/tree/f360166260fa5dbe93003c5756567cb4b132dbdb#readme) · [仓库元数据](https://api.github.com/repos/mltframework/shotcut) · [成熟发行 v14.05](https://github.com/mltframework/shotcut/releases/tag/v14.05)（2014-05-03）。

### 3. Comfy-Org/ComfyUI
- 能做什么：节点式图像、视频及其他生成模型工作流。
- 为什么保留：可保留可复用节点、输入参数与可重复的生成过程。 适配判断27/30；按统一权重已知分77，在本项目候选中列第3。
- 代价和不能替代的部分：不同模型权重及插件许可分别核对；显存和速度随模型变化，macOS运行不等于大模型可流畅使用。
- 与自建比较：当前缺口是“剧本尚未转成可审看的原创成片。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/Comfy-Org/ComfyUI/tree/8010b48d2c1be986613f8e8c761527d205bd756f#readme) · [仓库元数据](https://api.github.com/repos/Comfy-Org/ComfyUI) · [成熟发行 v0.0.1](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.0.1)（2024-07-12）。

采用前同样本检查：用现有剧本做三个连续镜头，检查角色一致、因果表达和素材许可。

<a id="p-wechat-video"></a>
## 视频号样片与拆解

项目要解决：围绕参考样片研究排版、声音与制作过程。 本轮重点：尚未证明原创成片完成或视频号实际运营有效。

搜索：`video generation`；卡ID `github-20261013-32`（同组复用）。 [自建不足](SELF-BUILT.md#p-wechat-video) · [候选取舍](AUDIT.md#p-wechat-video)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 82–94 | 30/26/10/6/10 | 130,463 | 2026-10-13 | MIT |
| 2. [mltframework/shotcut](https://github.com/mltframework/shotcut) | 79–91 | 30/29/6/8/6 | 15,411 | 2026-10-12 | GPL-3.0 |
| 3. [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 77–89 | 30/27/10/4/6 | 137,283 | 2026-10-13 | GPL-3.0 |

### 1. harry0703/MoneyPrinterTurbo
- 能做什么：将文案、素材、配音和字幕组合成视频的应用。
- 为什么保留：可参考流水线编排、批量生成及字幕输出。 适配判断26/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：外部素材和TTS有独立许可与依赖；默认合成声不能替代已认可音色，自动成片仍需审片。
- 与自建比较：当前缺口是“尚未证明原创成片完成或视频号实际运营有效。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/harry0703/MoneyPrinterTurbo/tree/bbe7eb9ae3e7a44f4553070b82d4a126aad62a33#readme) · [仓库元数据](https://api.github.com/repos/harry0703/MoneyPrinterTurbo) · [成熟发行 v1.1.0](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.1.0)（2024-04-11）。

### 2. mltframework/shotcut
- 能做什么：跨平台视频编辑器。
- 为什么保留：可补时间线剪辑、音画同步和导出检查。 适配判断29/30；按统一权重已知分79，在本项目候选中列第2。
- 代价和不能替代的部分：不是文生视频模型，也不会自动审核脚本、适龄性或来源权利。
- 与自建比较：当前缺口是“尚未证明原创成片完成或视频号实际运营有效。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/mltframework/shotcut/tree/f360166260fa5dbe93003c5756567cb4b132dbdb#readme) · [仓库元数据](https://api.github.com/repos/mltframework/shotcut) · [成熟发行 v14.05](https://github.com/mltframework/shotcut/releases/tag/v14.05)（2014-05-03）。

### 3. Comfy-Org/ComfyUI
- 能做什么：节点式图像、视频及其他生成模型工作流。
- 为什么保留：可保留可复用节点、输入参数与可重复的生成过程。 适配判断27/30；按统一权重已知分77，在本项目候选中列第3。
- 代价和不能替代的部分：不同模型权重及插件许可分别核对；显存和速度随模型变化，macOS运行不等于大模型可流畅使用。
- 与自建比较：当前缺口是“尚未证明原创成片完成或视频号实际运营有效。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/Comfy-Org/ComfyUI/tree/8010b48d2c1be986613f8e8c761527d205bd756f#readme) · [仓库元数据](https://api.github.com/repos/Comfy-Org/ComfyUI) · [成熟发行 v0.0.1](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.0.1)（2024-07-12）。

采用前同样本检查：先完成一个有明确原创改动的短片段，核对音画和来源，不自动发布。

<a id="p-xiaohongshu"></a>
## 小红书内容与获客探索

项目要解决：围绕学习材料讨论内容表达与验证。 本轮重点：当前仍是构想，没有获客或收入验证。

搜索：`deep research`；卡ID `github-20261013-23`（同组复用）。 [自建不足](SELF-BUILT.md#p-xiaohongshu) · [候选取舍](AUDIT.md#p-xiaohongshu)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 82–94 | 30/29/8/5/10 | 30,072 | 2026-10-10 | Apache-2.0 |

**只保留1个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. assafelovic/gpt-researcher
- 能做什么：带搜索、来源引用和报告输出的研究代理框架。
- 为什么保留：可借鉴查询分解、引用组织和研究流程编排。 适配判断29/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：需要模型/搜索服务配置且会产生调用成本；引用存在不等于可靠，不得把报告当市场验证。
- 与自建比较：当前缺口是“当前仍是构想，没有获客或收入验证。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/assafelovic/gpt-researcher/tree/3582a6841fe7dc801e2a34e34ee408641aea9bce#readme) · [仓库元数据](https://api.github.com/repos/assafelovic/gpt-researcher) · [成熟发行 v1.0.1](https://github.com/assafelovic/gpt-researcher/releases/tag/v1.0.1)（2023-07-10）。

采用前同样本检查：只把一个主题写成可供目标读者评价的小样，记录是否解决具体问题。

<a id="p-furniture-shop"></a>
## 家具电商网站

项目要解决：家具展示与电商流程原型。 本轮重点：本轮未复跑支付或部署，不能标为可成交商店。

搜索：`commerce`；卡ID `github-20261013-24`（同组复用）。 [自建不足](SELF-BUILT.md#p-furniture-shop) · [候选取舍](AUDIT.md#p-furniture-shop)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [medusajs/medusa](https://github.com/medusajs/medusa) | 79–91 | 30/30/8/5/6 | 36,727 | 2026-10-13 | MIT核心 / Enterprise另许可 |
| 2. [saleor/saleor](https://github.com/saleor/saleor) | 78–90 | 30/28/6/4/10 | 23,438 | 2026-10-12 | BSD-3-Clause |
| 3. [nopSolutions/nopCommerce](https://github.com/nopSolutions/nopCommerce) | 67–79 | 30/23/6/5/3 | 10,157 | 2026-10-13 | NPL（AGPL-3.0加品牌要求，非标准） |

### 1. medusajs/medusa
- 能做什么：模块化电商后端与可扩展商业框架。
- 为什么保留：可补商品、订单和交易基础，保留家具业务的差异逻辑。 适配判断30/30；按统一权重已知分79，在本项目候选中列第1。
- 代价和不能替代的部分：核心MIT，Enterprise材料另授权；支付、配送、税务和区域规则仍须真实集成验收。
- 与自建比较：当前缺口是“本轮未复跑支付或部署，不能标为可成交商店。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/medusajs/medusa/tree/d37c79548bad6e9ef2ad00cfa63bdcf4be123ba4#readme) · [仓库元数据](https://api.github.com/repos/medusajs/medusa) · [成熟发行 v1.3.6](https://github.com/medusajs/medusa/releases/tag/v1.3.6)（2022-08-29）。

### 2. saleor/saleor
- 能做什么：以API为中心的电商后端与扩展机制。
- 为什么保留：适合商品、交易服务和独立前端。 适配判断28/30；按统一权重已知分78，在本项目候选中列第2。
- 代价和不能替代的部分：服务化组件和部署较重；小规模家具网站不宜无验证整体迁移。
- 与自建比较：当前缺口是“本轮未复跑支付或部署，不能标为可成交商店。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/saleor/saleor/tree/a31848549f5dc5843fe9e66422bf34a915559ee5#readme) · [仓库元数据](https://api.github.com/repos/saleor/saleor) · [成熟发行 v2016.07.0](https://github.com/saleor/saleor/releases/tag/v2016.07.0)（2016-08-08）。

### 3. nopSolutions/nopCommerce
- 能做什么：基于.NET的电商系统。
- 为什么保留：可比较成熟商品和订单功能。 适配判断23/30；按统一权重已知分67，在本项目候选中列第3。
- 代价和不能替代的部分：NPL在AGPL上增加品牌显示要求，按非标准许可处理；生态与现有技术栈迁移成本较高。
- 与自建比较：当前缺口是“本轮未复跑支付或部署，不能标为可成交商店。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/nopSolutions/nopCommerce/tree/4039867e44d54cf8e7accaa669e0faced8fe306b#readme) · [仓库元数据](https://api.github.com/repos/nopSolutions/nopCommerce) · [成熟发行 release-1.80](https://github.com/nopSolutions/nopCommerce/releases/tag/release-1.80)（2016-01-12）。

采用前同样本检查：在测试环境完成下单、支付回调、取消退款与库存回补闭环。

<a id="p-archer"></a>
## 弓手试炼玩法小样

项目要解决：有限五房战斗切片与玩法交互验证。 本轮重点：完整五房实战与真实触屏设备尚未验收。

搜索：`2D game engine`；卡ID `github-20261013-20`（同组复用）。 [自建不足](SELF-BUILT.md#p-archer) · [候选取舍](AUDIT.md#p-archer)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [godotengine/godot](https://github.com/godotengine/godot) | 85–97 | 30/28/10/7/10 | 118,386 | 2026-10-13 | MIT |
| 2. [phaserjs/phaser](https://github.com/phaserjs/phaser) | 79–91 | 24/30/8/7/10 | 40,467 | 2026-08-21 | MIT |
| 3. [hajimehoshi/ebiten](https://github.com/hajimehoshi/ebiten) | 73–85 | 30/22/6/5/10 | 13,551 | 2026-10-13 | Apache-2.0 |

### 1. godotengine/godot
- 能做什么：支持二维与三维的跨平台游戏引擎。
- 为什么保留：可借鉴输入、场景、资源和导出系统。 适配判断28/30；按统一权重已知分85，在本项目候选中列第1。
- 代价和不能替代的部分：迁移现有小游戏并非零成本；引擎功能不能替代玩法与触屏验收。
- 与自建比较：当前缺口是“完整五房实战与真实触屏设备尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/godotengine/godot/tree/40237c278d218591222d1d7c24597b83bf7038e6#readme) · [仓库元数据](https://api.github.com/repos/godotengine/godot) · [成熟发行 1.0-stable](https://github.com/godotengine/godot/releases/tag/1.0-stable)（2014-12-17）。

### 2. phaserjs/phaser
- 能做什么：面向浏览器的二维游戏框架。
- 为什么保留：贴合HTML游戏、触屏输入和小型战斗切片。 适配判断30/30；按统一权重已知分79，在本项目候选中列第2。
- 代价和不能替代的部分：仍需自己实现规则、存档和设备测试，不是直接可玩的成品。
- 与自建比较：当前缺口是“完整五房实战与真实触屏设备尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/phaserjs/phaser/tree/02d8931b626d9764c133cbb3fbf99966c03c757c#readme) · [仓库元数据](https://api.github.com/repos/phaserjs/phaser) · [成熟发行 1.1.3](https://github.com/phaserjs/phaser/releases/tag/1.1.3)（2014-02-07）。

### 3. hajimehoshi/ebiten
- 能做什么：使用Go制作二维游戏的框架。
- 为什么保留：可作为轻量跨平台渲染与输入实现对照。 适配判断22/30；按统一权重已知分73，在本项目候选中列第3。
- 代价和不能替代的部分：改用Go有迁移成本，和现有网页资产的复用程度较低。
- 与自建比较：当前缺口是“完整五房实战与真实触屏设备尚未验收。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/hajimehoshi/ebiten/tree/bdd9476fcfd89cb649daeed1a74c3f37ec577dcf#readme) · [仓库元数据](https://api.github.com/repos/hajimehoshi/ebiten) · [成熟发行 v1.0.0](https://github.com/hajimehoshi/ebiten/releases/tag/v1.0.0)（2016-06-26）。

采用前同样本检查：在真实触屏设备完整通关一次，记录死亡点、误触和帧率下降位置。

<a id="p-ai-history"></a>
## AI 三家公司发展历程展示

项目要解决：以页面整理AI公司公开发展资料。 本轮重点：关键历史节点的原始来源未完成逐项核验。

搜索：`documentation website`；卡ID `github-20261013-18`（同组复用）。 [自建不足](SELF-BUILT.md#p-ai-history) · [候选取舍](AUDIT.md#p-ai-history)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [withastro/astro](https://github.com/withastro/astro) | 84–96 | 30/29/8/7/10 | 63,202 | 2026-10-13 | MIT |
| 2. [facebook/docusaurus](https://github.com/facebook/docusaurus) | 83–95 | 30/28/8/7/10 | 66,478 | 2026-10-09 | MIT |
| 3. [getzola/zola](https://github.com/getzola/zola) | 75–87 | 30/25/6/7/7 | 17,509 | 2026-10-08 | EUPL-1.2 |

### 1. withastro/astro
- 能做什么：面向内容网站的Web框架。
- 为什么保留：适合轻量主页、资料展示和按需交互。 适配判断29/30；按统一权重已知分84，在本项目候选中列第1。
- 代价和不能替代的部分：需要前端开发；权限、支付和学习反馈不会自动具备。
- 与自建比较：当前缺口是“关键历史节点的原始来源未完成逐项核验。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/withastro/astro/tree/59b9cc00726495bb45f5c4b000dbbb7b5a19d662#readme) · [仓库元数据](https://api.github.com/repos/withastro/astro) · [成熟发行 astro@0.18.9](https://github.com/withastro/astro/releases/tag/astro%400.18.9)（2021-08-05）。

### 2. facebook/docusaurus
- 能做什么：基于文档、博客和本地化的网站构建工具。
- 为什么保留：适合把教材、证据页面和项目说明做成结构一致的网站。 适配判断28/30；按统一权重已知分83，在本项目候选中列第2。
- 代价和不能替代的部分：不是学习记录后端；构建与内容审核仍需维护，真机体验需验收。
- 与自建比较：当前缺口是“关键历史节点的原始来源未完成逐项核验。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/facebook/docusaurus/tree/c245217563f6491fdb79bf5ac91bfa16536e5de9#readme) · [仓库元数据](https://api.github.com/repos/facebook/docusaurus) · [成熟发行 v1.0.3](https://github.com/facebook/docusaurus/releases/tag/v1.0.3)（2017-12-19）。

### 3. getzola/zola
- 能做什么：独立程序形式的静态网站生成器。
- 为什么保留：适合简单、可版本化的内容页面。 适配判断25/30；按统一权重已知分75，在本项目候选中列第3。
- 代价和不能替代的部分：动态学习记录和复杂交互需另接；模板迁移有成本。
- 与自建比较：当前缺口是“关键历史节点的原始来源未完成逐项核验。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/getzola/zola/tree/9740ae258f382d742b7732f7b89b3cd529973f4b#readme) · [仓库元数据](https://api.github.com/repos/getzola/zola) · [成熟发行 v0.0.2](https://github.com/getzola/zola/releases/tag/v0.0.2)（2017-03-24）。

采用前同样本检查：抽取三个关键节点，逐条补官方原文、事件日期和链接。

<a id="p-trial-rea"></a>
## REA 代码分析实测

项目要解决：对自制已知行为程序做有限分析与重建。 本轮重点：语义查询仍存在partial或ambiguous，不能宣称完整理解代码。

搜索：`coding agents`；卡ID `github-20261013-45`（同组复用）。 [自建不足](SELF-BUILT.md#p-trial-rea) · [候选取舍](AUDIT.md#p-trial-rea)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 78–90 | 30/26/8/4/10 | 90,792 | 2026-10-13 | MIT |
| 2. [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | 77–89 | 30/25/6/6/10 | 28,461 | 2026-10-13 | Apache-2.0 |
| 3. [Aider-AI/aider](https://github.com/Aider-AI/aider) | 69–81 | 18/27/8/6/10 | 49,525 | 2026-05-22 | Apache-2.0 |

### 1. OpenHands/OpenHands
- 能做什么：支持多运行后端的代码代理平台。
- 为什么保留：可借鉴执行环境、工作空间和任务操作。 适配判断26/30；按统一权重已知分78，在本项目候选中列第1。
- 代价和不能替代的部分：平台较重且有企业部分；受控执行与权限隔离须另验收。
- 与自建比较：当前缺口是“语义查询仍存在partial或ambiguous，不能宣称完整理解代码。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/OpenHands/OpenHands/tree/62491b193d5924d9f1a1fbcec0ebed93c7962128#readme) · [仓库元数据](https://api.github.com/repos/OpenHands/OpenHands) · [成熟发行 0.6.1](https://github.com/OpenHands/OpenHands/releases/tag/0.6.1)（2024-06-04）。

### 2. QwenLM/qwen-code
- 能做什么：支持多模型协议的终端代码代理。
- 为什么保留：可比较多提供商接口和代码工作流。 适配判断25/30；按统一权重已知分77，在本项目候选中列第2。
- 代价和不能替代的部分：需要模型端点与开发环境；不能直接证明多人多终端恢复可靠。
- 与自建比较：当前缺口是“语义查询仍存在partial或ambiguous，不能宣称完整理解代码。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/QwenLM/qwen-code/tree/53579861dabaf32ed4433f13996c3adb2ea7e79a#readme) · [仓库元数据](https://api.github.com/repos/QwenLM/qwen-code) · [成熟发行 v0.0.2](https://github.com/QwenLM/qwen-code/releases/tag/v0.0.2)（2025-08-01）。

### 3. Aider-AI/aider
- 能做什么：通过终端与模型协作修改现有代码。
- 为什么保留：可对照代码理解、修改和测试回路。 适配判断27/30；按统一权重已知分69，在本项目候选中列第3。
- 代价和不能替代的部分：不是语义索引真值；默认分支更新较慢，模型表现需同仓库比较。
- 与自建比较：当前缺口是“语义查询仍存在partial或ambiguous，不能宣称完整理解代码。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/Aider-AI/aider/tree/5dc9490bb35f9729ef2c95d00a19ccd30c26339c#readme) · [仓库元数据](https://api.github.com/repos/Aider-AI/aider) · [成熟发行 v0.5.0](https://github.com/Aider-AI/aider/releases/tag/v0.5.0)（2023-06-07）。

采用前同样本检查：选择一个歧义查询，人工建立真值，再比较REA与候选工具的引用定位。

<a id="p-trial-earthquake"></a>
## 地震地球视图实测

项目要解决：在原项目运行日本地震观察视图。 本轮重点：真实手机和用户阅读验收未完成。

搜索：`3D globe`；卡ID `github-20261013-44`（同组复用）。 [自建不足](SELF-BUILT.md#p-trial-earthquake) · [候选取舍](AUDIT.md#p-trial-earthquake)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [CesiumGS/cesium](https://github.com/CesiumGS/cesium) | 83–95 | 30/30/6/7/10 | 15,828 | 2026-10-12 | Apache-2.0 |
| 2. [maplibre/maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js) | 77–89 | 30/25/6/6/10 | 11,858 | 2026-10-13 | BSD-3-Clause |

**只保留2个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. CesiumGS/cesium
- 能做什么：浏览器三维地球、二维地图与动态空间数据展示。
- 为什么保留：与现有地震可视化链贴合，可复用空间和时间可视化能力。 适配判断30/30；按统一权重已知分83，在本项目候选中列第1。
- 代价和不能替代的部分：底图、地形及托管服务有独立条款；不是地震预测或告警保证。
- 与自建比较：当前缺口是“真实手机和用户阅读验收未完成。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/CesiumGS/cesium/tree/201f20f232f7fb046a43568fc51324acb4a846cc#readme) · [仓库元数据](https://api.github.com/repos/CesiumGS/cesium) · [成熟发行 1.36](https://github.com/CesiumGS/cesium/releases/tag/1.36)（2017-08-01）。

### 2. maplibre/maplibre-gl-js
- 能做什么：在网页展示矢量地图的WebGL库。
- 为什么保留：适合移动地图交互与图层展示的轻量对照。 适配判断25/30；按统一权重已知分77，在本项目候选中列第2。
- 代价和不能替代的部分：不是Cesium完整三维地球的等价替代；数据源与离线能力另配置。
- 与自建比较：当前缺口是“真实手机和用户阅读验收未完成。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/maplibre/maplibre-gl-js/tree/a6976b2d21ad4f88439a6fde4e5255101b5b6507#readme) · [仓库元数据](https://api.github.com/repos/maplibre/maplibre-gl-js) · [成熟发行 v1.14.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v1.14.0)（2021-03-24）。

采用前同样本检查：在真实手机查看一个已知事件，核对时间、位置、震级和缺测提示。

<a id="p-trial-context"></a>
## Context Mode 长日志实测

项目要解决：比较长日志定位准确性和回传体积。 本轮重点：结论只限一个合成样本，不能泛化为任何长上下文都无损。

搜索：`context compression`；卡ID `github-20261013-43`（同组复用）。 [自建不足](SELF-BUILT.md#p-trial-context) · [候选取舍](AUDIT.md#p-trial-context)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [microsoft/LLMLingua](https://github.com/microsoft/LLMLingua) | 73–85 | 24/30/4/5/10 | 6,747 | 2026-09-10 | MIT |

**只保留1个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. microsoft/LLMLingua
- 能做什么：提示词压缩及相关评估工具。
- 为什么保留：可对照压缩前后的任务表现和证据保留。 适配判断30/30；按统一权重已知分73，在本项目候选中列第1。
- 代价和不能替代的部分：压缩率不等于语义无损，需模型资源和独立任务真值。
- 与自建比较：当前缺口是“结论只限一个合成样本，不能泛化为任何长上下文都无损。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/microsoft/LLMLingua/tree/5a4c78ae18ab17a98cf997e8259354e546081d64#readme) · [仓库元数据](https://api.github.com/repos/microsoft/LLMLingua) · [成熟发行 v0.1.2](https://github.com/microsoft/LLMLingua/releases/tag/v0.1.2)（2023-10-09）。

采用前同样本检查：用一份脱敏真实日志做盲测，比较漏报、误报和证据定位，而非只比压缩率。

<a id="p-trial-artcraft"></a>
## ArtCraft 分镜实测

项目要解决：验证同一场景的相机、分镜和保存重开。 本轮重点：账号条件阻塞核心测试，三幅分镜未产出。

搜索：`video generation`；卡ID `github-20261013-32`（同组复用）。 [自建不足](SELF-BUILT.md#p-trial-artcraft) · [候选取舍](AUDIT.md#p-trial-artcraft)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [blender/blender](https://github.com/blender/blender) | 80–92 | 30/30/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 2. [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 78–90 | 30/28/10/4/6 | 137,283 | 2026-10-13 | GPL-3.0 |
| 3. [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 76–88 | 30/20/10/6/10 | 130,463 | 2026-10-13 | MIT |

### 1. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断30/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“账号条件阻塞核心测试，三幅分镜未产出。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 2. Comfy-Org/ComfyUI
- 能做什么：节点式图像、视频及其他生成模型工作流。
- 为什么保留：可保留可复用节点、输入参数与可重复的生成过程。 适配判断28/30；按统一权重已知分78，在本项目候选中列第2。
- 代价和不能替代的部分：不同模型权重及插件许可分别核对；显存和速度随模型变化，macOS运行不等于大模型可流畅使用。
- 与自建比较：当前缺口是“账号条件阻塞核心测试，三幅分镜未产出。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/Comfy-Org/ComfyUI/tree/8010b48d2c1be986613f8e8c761527d205bd756f#readme) · [仓库元数据](https://api.github.com/repos/Comfy-Org/ComfyUI) · [成熟发行 v0.0.1](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.0.1)（2024-07-12）。

### 3. harry0703/MoneyPrinterTurbo
- 能做什么：将文案、素材、配音和字幕组合成视频的应用。
- 为什么保留：可参考流水线编排、批量生成及字幕输出。 适配判断20/30；按统一权重已知分76，在本项目候选中列第3。
- 代价和不能替代的部分：外部素材和TTS有独立许可与依赖；默认合成声不能替代已认可音色，自动成片仍需审片。
- 与自建比较：当前缺口是“账号条件阻塞核心测试，三幅分镜未产出。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/harry0703/MoneyPrinterTurbo/tree/bbe7eb9ae3e7a44f4553070b82d4a126aad62a33#readme) · [仓库元数据](https://api.github.com/repos/harry0703/MoneyPrinterTurbo) · [成熟发行 v1.1.0](https://github.com/harry0703/MoneyPrinterTurbo/releases/tag/v1.1.0)（2024-04-11）。

采用前同样本检查：先用已可用的Blender生成三幅同场景分镜，核对连续性与可编辑性。

<a id="p-trial-webui"></a>
## Open WebUI 问答实测

项目要解决：用虚构FAQ验证有据回答与未知拒答。 本轮重点：模型端到端问答仍阻塞，上传成功不等于文档问答可用。

搜索：`local LLM webui`；卡ID `github-20261013-46`（同组复用）。 [自建不足](SELF-BUILT.md#p-trial-webui) · [候选取舍](AUDIT.md#p-trial-webui)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 84–96 | 30/29/8/7/10 | 67,021 | 2026-10-12 | MIT |
| 2. [open-webui/open-webui](https://github.com/open-webui/open-webui) | 80–92 | 30/30/10/6/4 | 155,532 | 2026-10-10 | Open WebUI License（附品牌条款，非标准） |

**只保留2个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. Mintplex-Labs/anything-llm
- 能做什么：本地文档问答与AI工作空间应用。
- 为什么保留：可比较较完整的文档导入到问答路径。 适配判断29/30；按统一权重已知分84，在本项目候选中列第1。
- 代价和不能替代的部分：回答准确度、引用和权限仍须真实文档检验，不能默认离线模型已可用。
- 与自建比较：当前缺口是“模型端到端问答仍阻塞，上传成功不等于文档问答可用。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/Mintplex-Labs/anything-llm/tree/3e4f9411b67f2dd7fa9fc6f2b95dfacbda0633ba#readme) · [仓库元数据](https://api.github.com/repos/Mintplex-Labs/anything-llm) · [成熟发行 v1.0.0](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.0.0)（2024-07-26）。

### 2. open-webui/open-webui
- 能做什么：可自托管的模型聊天与知识问答界面。
- 为什么保留：可复用模型接入、上传与问答交互，贴合现有试验。 适配判断30/30；按统一权重已知分80，在本项目候选中列第2。
- 代价和不能替代的部分：许可证有品牌保留条款及例外，非简单MIT；上传成功不代表检索回答正确。
- 与自建比较：当前缺口是“模型端到端问答仍阻塞，上传成功不等于文档问答可用。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/open-webui/open-webui/tree/f8ae8a6c328946dc62cd0712961a0632574581bf#readme) · [仓库元数据](https://api.github.com/repos/open-webui/open-webui) · [成熟发行 v0.1.102](https://github.com/open-webui/open-webui/releases/tag/v0.1.102)（2024-02-23）。

采用前同样本检查：先解除模型连接阻塞，用三条有标准答案的问题检查回答及引用。

<a id="p-external-tools"></a>
## 他山之石与外部工作流库

项目要解决：保留开源工具能力和外部工作流的来源与适用边界。 本轮重点：旧能力结论不能自动视为当前版本可用。

搜索：`deep research`；卡ID `github-20261013-23`（同组复用）。 [自建不足](SELF-BUILT.md#p-external-tools) · [候选取舍](AUDIT.md#p-external-tools)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) | 82–94 | 30/29/8/5/10 | 30,072 | 2026-10-10 | Apache-2.0 |

**只保留1个**：其他候选门槛或适配证据不足，第三名不凑数。

### 1. assafelovic/gpt-researcher
- 能做什么：带搜索、来源引用和报告输出的研究代理框架。
- 为什么保留：可借鉴查询分解、引用组织和研究流程编排。 适配判断29/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：需要模型/搜索服务配置且会产生调用成本；引用存在不等于可靠，不得把报告当市场验证。
- 与自建比较：当前缺口是“旧能力结论不能自动视为当前版本可用。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/assafelovic/gpt-researcher/tree/3582a6841fe7dc801e2a34e34ee408641aea9bce#readme) · [仓库元数据](https://api.github.com/repos/assafelovic/gpt-researcher) · [成熟发行 v1.0.1](https://github.com/assafelovic/gpt-researcher/releases/tag/v1.0.1)（2023-07-10）。

采用前同样本检查：选一个准备再次使用的工具，按原样本复跑并回填版本与差异。

<a id="p-learning-products"></a>
## 数字学习材料产品探索

项目要解决：围绕手机学习材料测试可交付形式与产品假设。 本轮重点：尚无上架、成交或学习成效证据。

搜索：`spaced repetition`；卡ID `github-20261013-21`（同组复用）。 [自建不足](SELF-BUILT.md#p-learning-products) · [候选取舍](AUDIT.md#p-learning-products)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [learningequality/kolibri](https://github.com/learningequality/kolibri) | 80–92 | 30/30/3/7/10 | 1,143 | 2026-10-12 | MIT |
| 2. [ankitects/anki](https://github.com/ankitects/anki) | 75–87 | 30/24/8/8/5 | 31,984 | 2026-10-13 | AGPL-3.0-or-later（部分文件另许可） |
| 3. [st3v3nmw/obsidian-spaced-repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) | 63–75 | 24/20/3/6/10 | 2,585 | 2026-08-03 | MIT |

### 1. learningequality/kolibri
- 能做什么：离线优先的教学学习平台。
- 为什么保留：适合教材分发、离线访问和教育场景组织。 适配判断30/30；按统一权重已知分80，在本项目候选中列第1。
- 代价和不能替代的部分：需部署并准备有授权的内容；日文题型和家庭点读流程仍要适配。
- 与自建比较：当前缺口是“尚无上架、成交或学习成效证据。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/learningequality/kolibri/tree/5d47c94a8eccc63667afa097ccebe6ac9de640b0#readme) · [仓库元数据](https://api.github.com/repos/learningequality/kolibri) · [成熟发行 v0.2.1](https://github.com/learningequality/kolibri/releases/tag/v0.2.1)（2017-03-10）。

### 2. ankitects/anki
- 能做什么：成熟的间隔复习与闪卡程序。
- 为什么保留：可补遗忘调度、复习日志与题目重复学习。 适配判断24/30；按统一权重已知分75，在本项目候选中列第2。
- 代价和不能替代的部分：不能核验专业答案或推断掌握；平台客户端和同步成本需另看，手机导入需实测。
- 与自建比较：当前缺口是“尚无上架、成交或学习成效证据。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/ankitects/anki/tree/b15d4c71eadd3c4a74afaba74f93f4b3f70ac97c#readme) · [仓库元数据](https://api.github.com/repos/ankitects/anki) · [成熟发行 2.1.20](https://github.com/ankitects/anki/releases/tag/2.1.20)（2020-03-07）。

### 3. st3v3nmw/obsidian-spaced-repetition
- 能做什么：为Obsidian笔记增加闪卡和整篇复习。
- 为什么保留：贴合已有Markdown题库与笔记习惯。 适配判断20/30；按统一权重已知分63，在本项目候选中列第3。
- 代价和不能替代的部分：依赖Obsidian；移动保存、插件兼容及完整考试流程需另验证。
- 与自建比较：当前缺口是“尚无上架、成交或学习成效证据。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/st3v3nmw/obsidian-spaced-repetition/tree/3d5079f3bcd54531b084040d1c0178f15f681510#readme) · [仓库元数据](https://api.github.com/repos/st3v3nmw/obsidian-spaced-repetition) · [成熟发行 1.0.0](https://github.com/st3v3nmw/obsidian-spaced-repetition/releases/tag/1.0.0)（2021-04-09）。

采用前同样本检查：先让一名目标使用者完成一个小样任务，记录理解与操作障碍。

<a id="p-realestate-loop"></a>
## 房地产开发经验学习系统

项目要解决：以脱敏案例回放组织判断练习和现实回填。 本轮重点：学习材料不能替代真实地块和行政条件核实。

搜索：`geospatial`；卡ID `github-20261013-27`（同组复用）。 [自建不足](SELF-BUILT.md#p-realestate-loop) · [候选取舍](AUDIT.md#p-realestate-loop)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [qgis/QGIS](https://github.com/qgis/QGIS) | 78–90 | 30/29/6/7/6 | 14,551 | 2026-10-13 | GPL-2.0 |
| 2. [geopandas/geopandas](https://github.com/geopandas/geopandas) | 78–90 | 30/28/4/6/10 | 5,277 | 2026-10-12 | BSD-3-Clause |
| 3. [ozekik/plateaukit](https://github.com/ozekik/plateaukit) | 64–76 | 24/24/1/5/10 | 29 | 2026-09-07 | MIT |

### 1. qgis/QGIS
- 能做什么：支持矢量、栅格等数据的跨平台GIS。
- 为什么保留：可补图层核对、坐标转换和独立空间检查。 适配判断29/30；按统一权重已知分78，在本项目候选中列第1。
- 代价和不能替代的部分：工具能叠图不代表图层时效或开发许可成立；需保留来源和专业核实。
- 与自建比较：当前缺口是“学习材料不能替代真实地块和行政条件核实。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/qgis/QGIS/tree/d835ed0a563f5c286127c6f5efbdb5b1473e9adb#readme) · [仓库元数据](https://api.github.com/repos/qgis/QGIS) · [成熟发行 final-3_16_3](https://github.com/qgis/QGIS/releases/tag/final-3_16_3)（2021-01-15）。

### 2. geopandas/geopandas
- 能做什么：Python地理数据分析与空间操作库。
- 为什么保留：可补可重复的坐标、范围和空间连接检查。 适配判断28/30；按统一权重已知分78，在本项目候选中列第2。
- 代价和不能替代的部分：坐标参考不一致仍可能产生错误；没有尽调判断和行政许可结论。
- 与自建比较：当前缺口是“学习材料不能替代真实地块和行政条件核实。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/geopandas/geopandas/tree/ee889bb6365319dee15b43ad001539ef10b090f0#readme) · [仓库元数据](https://api.github.com/repos/geopandas/geopandas) · [成熟发行 v0.2.1](https://github.com/geopandas/geopandas/releases/tag/v0.2.1)（2016-07-30）。

### 3. ozekik/plateaukit
- 能做什么：围绕日本PLATEAU三维城市数据的Python工具。
- 为什么保留：可补公开城市模型读取与研究流程。 适配判断24/30；按统一权重已知分64，在本项目候选中列第3。
- 代价和不能替代的部分：社区较小；具体地区覆盖、数据年份及数据许可需逐项确认。
- 与自建比较：当前缺口是“学习材料不能替代真实地块和行政条件核实。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/ozekik/plateaukit/tree/f55a53285d2e00a0844d0a0c9667366bdb432a89#readme) · [仓库元数据](https://api.github.com/repos/ozekik/plateaukit) · [成熟发行 v0.11.2](https://github.com/ozekik/plateaukit/releases/tag/v0.11.2)（2024-03-05）。

采用前同样本检查：用一个公开新案例复做判断，记录与旧案例不同的关键条件。

<a id="p-meeting-plan"></a>
## 会议记录到行动计划

项目要解决：从会议原文形成可追溯计划并保留未决问题。 本轮重点：会议建议不是已派单、已接受或已执行的任务。

搜索：`meeting transcription`；卡ID `github-20261013-36`（同组复用）。 [自建不足](SELF-BUILT.md#p-meeting-plan) · [候选取舍](AUDIT.md#p-meeting-plan)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | 79–91 | 24/30/8/7/10 | 31,688 | 2026-09-10 | MIT |
| 2. [chidiwilliams/buzz](https://github.com/chidiwilliams/buzz) | 79–91 | 30/25/6/8/10 | 21,971 | 2026-10-11 | MIT |
| 3. [kanboard/kanboard](https://github.com/kanboard/kanboard) | 72–84 | 30/20/4/8/10 | 9,906 | 2026-10-12 | MIT |

### 1. Zackriya-Solutions/meetily
- 能做什么：本地会议录音转写与摘要应用。
- 为什么保留：可补会议输入和本地处理体验。 适配判断30/30；按统一权重已知分79，在本项目候选中列第1。
- 代价和不能替代的部分：社区版与PRO功能不同；不能把摘要当派单或负责人承诺，音频识别需现场样本测试。
- 与自建比较：当前缺口是“会议建议不是已派单、已接受或已执行的任务。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/Zackriya-Solutions/meetily/tree/a2cb62e827da7ef59f65064c97233efb2313878e#readme) · [仓库元数据](https://api.github.com/repos/Zackriya-Solutions/meetily) · [成熟发行 v0.0.4](https://github.com/Zackriya-Solutions/meetily/releases/tag/v0.0.4)（2025-05-01）。

### 2. chidiwilliams/buzz
- 能做什么：离线音频转写桌面工具，支持多种Whisper类后端。
- 为什么保留：适合为会议、语言和声音评估提供可回读文本。 适配判断25/30；按统一权重已知分79，在本项目候选中列第2。
- 代价和不能替代的部分：是识别工具而非任务执行或TTS；当前Mac支持范围需核对，系统音频与翻译需另配。
- 与自建比较：当前缺口是“会议建议不是已派单、已接受或已执行的任务。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/chidiwilliams/buzz/tree/851c8b359343db8c9460aa15ee59a40f2ab66aa8#readme) · [仓库元数据](https://api.github.com/repos/chidiwilliams/buzz) · [成熟发行 v0.1.0](https://github.com/chidiwilliams/buzz/releases/tag/v0.1.0)（2022-09-27）。

### 3. kanboard/kanboard
- 能做什么：轻量自托管看板与任务管理。
- 为什么保留：可补明确任务状态、看板和基本协作。 适配判断20/30；按统一权重已知分72，在本项目候选中列第3。
- 代价和不能替代的部分：不会自动把验收证据绑定到完成状态，也不理解自有代理协议。
- 与自建比较：当前缺口是“会议建议不是已派单、已接受或已执行的任务。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/kanboard/kanboard/tree/ec3398d0d2b31d5051e2a077f475e286b5dd1228#readme) · [仓库元数据](https://api.github.com/repos/kanboard/kanboard) · [成熟发行 v1.0.9](https://github.com/kanboard/kanboard/releases/tag/v1.0.9)（2017-10-06）。

采用前同样本检查：从一次会议只选一条行动，记录确认、执行、结果和会议原文位置。

<a id="p-tts-eval"></a>
## 自然语音试听与评估

项目要解决：以短试听和明确验收记录选择可用声音。 本轮重点：目前只能证明评估资产存在，没有本轮认可音色或正式音频交付。

搜索：`speech recognition translation`；卡ID `github-20261013-47`（同组复用）。 [自建不足](SELF-BUILT.md#p-tts-eval) · [候选取舍](AUDIT.md#p-tts-eval)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 82–94 | 30/30/8/4/10 | 62,760 | 2026-10-08 | MIT |
| 2. [VOICEVOX/voicevox](https://github.com/VOICEVOX/voicevox) | 75–87 | 30/27/4/7/7 | 3,266 | 2026-10-11 | LGPL-3.0 / 可另取其他许可；音色条款独立 |
| 3. [chidiwilliams/buzz](https://github.com/chidiwilliams/buzz) | 74–86 | 30/20/6/8/10 | 21,971 | 2026-10-11 | MIT |

### 1. RVC-Boss/GPT-SoVITS
- 能做什么：支持中日英等语言的少样本语音合成工具。
- 为什么保留：可作为自然配音和中日短稿试听候选。 适配判断30/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：GPU/CPU性能、模型权重和音色权利独立核验；不使用未经授权的声音，不默认通过自然度验收。
- 与自建比较：当前缺口是“目前只能证明评估资产存在，没有本轮认可音色或正式音频交付。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/RVC-Boss/GPT-SoVITS/tree/1b47ca07ef43a284e0b8bd7f29d3e1e3ff76082a#readme) · [仓库元数据](https://api.github.com/repos/RVC-Boss/GPT-SoVITS) · [成熟发行 20240821v2](https://github.com/RVC-Boss/GPT-SoVITS/releases/tag/20240821v2)（2024-08-21）。

### 2. VOICEVOX/voicevox
- 能做什么：日语语音合成编辑器，配套独立引擎。
- 为什么保留：适合可调节的日文试听与编辑对照。 适配判断27/30；按统一权重已知分75，在本项目候选中列第2。
- 代价和不能替代的部分：代码LGPL-3.0与角色声音条款分开；声音可能不符合自然度偏好，必须短样试听。
- 与自建比较：当前缺口是“目前只能证明评估资产存在，没有本轮认可音色或正式音频交付。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/VOICEVOX/voicevox/tree/f191db96b82f998adadbe3d0b13e37ac64116e62#readme) · [仓库元数据](https://api.github.com/repos/VOICEVOX/voicevox) · [成熟发行 0.1.1](https://github.com/VOICEVOX/voicevox/releases/tag/0.1.1)（2021-08-04）。

### 3. chidiwilliams/buzz
- 能做什么：离线音频转写桌面工具，支持多种Whisper类后端。
- 为什么保留：适合为会议、语言和声音评估提供可回读文本。 适配判断20/30；按统一权重已知分74，在本项目候选中列第3。
- 代价和不能替代的部分：是识别工具而非任务执行或TTS；当前Mac支持范围需核对，系统音频与翻译需另配。
- 与自建比较：当前缺口是“目前只能证明评估资产存在，没有本轮认可音色或正式音频交付。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/chidiwilliams/buzz/tree/851c8b359343db8c9460aa15ee59a40f2ab66aa8#readme) · [仓库元数据](https://api.github.com/repos/chidiwilliams/buzz) · [成熟发行 v0.1.0](https://github.com/chidiwilliams/buzz/releases/tag/v0.1.0)（2022-09-27）。

采用前同样本检查：用同一段中日文短稿生成候选试听，保留参数，待醒后进行自然度判断。

<a id="p-freecad-research"></a>
## FreeCAD 与 Blender 互通研究

项目要解决：保留互通来源、软件实测与技术限制。 本轮重点：FreeCAD和Blender的实际文件交换、专业交接仍未实测。

搜索：`parametric CAD`；卡ID `github-20261013-13`（同组复用）。 [自建不足](SELF-BUILT.md#p-freecad-research) · [候选取舍](AUDIT.md#p-freecad-research)

| 排名 / 资源 | 分数区间 | 维护/适配/规模/部署/许可 | Stars | 最近默认分支提交 | 许可证 |
|---|---|---|---:|---|---|
| 1. [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | 82–94 | 30/30/8/7/7 | 34,238 | 2026-10-13 | LGPL-2.1 |
| 2. [blender/blender](https://github.com/blender/blender) | 80–92 | 30/30/6/8/6 | 20,867 | 2026-10-13 | GPL-3.0 |
| 3. [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell) | 72–84 | 30/27/3/5/7 | 2,851 | 2026-10-13 | LGPL-3.0 |

### 1. FreeCAD/FreeCAD
- 能做什么：参数化实体、尺寸约束与工程建模。
- 为什么保留：可补尺寸驱动、保存重开和工程导出基础。 适配判断30/30；按统一权重已知分82，在本项目候选中列第1。
- 代价和不能替代的部分：不是日本规范验算或施工批准工具；跨软件交换需单独测试。
- 与自建比较：当前缺口是“FreeCAD和Blender的实际文件交换、专业交接仍未实测。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/FreeCAD/FreeCAD/tree/c8c9ea855080c9e0f2f22b583cddbed1c0cf2a07#readme) · [仓库元数据](https://api.github.com/repos/FreeCAD/FreeCAD) · [成熟发行 0.15](https://github.com/FreeCAD/FreeCAD/releases/tag/0.15)（2015-07-03）。

### 2. blender/blender
- 能做什么：完整三维建模、动画、渲染和合成工具。
- 为什么保留：可复用当前模型与脚本，补资产管理、镜头和渲染。 适配判断30/30；按统一权重已知分80，在本项目候选中列第2。
- 代价和不能替代的部分：几何可见不等于尺寸、施工或规范正确；需要控制版本和插件。
- 与自建比较：当前缺口是“FreeCAD和Blender的实际文件交换、专业交接仍未实测。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/blender/blender/tree/3e451b5580bb54df6029ecfa5d0f3958e32d1000#readme) · [仓库元数据](https://api.github.com/repos/blender/blender) · [成熟发行 4.2](https://www.blender.org/download/releases/4-2/)（2024-07-16）。

### 3. IfcOpenShell/IfcOpenShell
- 能做什么：解析IFC及相关建筑信息标准的库和工具生态。
- 为什么保留：可补构件语义、IFC交换与模型数据检查。 适配判断27/30；按统一权重已知分72，在本项目候选中列第3。
- 代价和不能替代的部分：包含IFC库及Bonsai等组件；正式发行证据来自同仓库BlenderBIM组件，具体库版本与交换保真仍须另验收。
- 与自建比较：当前缺口是“FreeCAD和Blender的实际文件交换、专业交接仍未实测。”。这是引入或借鉴它要解决的事，不因星数多就整体迁移。
- 证据：[固定提交README](https://github.com/IfcOpenShell/IfcOpenShell/tree/201c467140594bf48e167a79446321ec87ada9a2#readme) · [仓库元数据](https://api.github.com/repos/IfcOpenShell/IfcOpenShell) · [成熟发行 blenderbim-210308](https://github.com/IfcOpenShell/IfcOpenShell/releases/tag/blenderbim-210308)（2021-03-08）。

采用前同样本检查：让同一带尺寸构件完成一次往返交换，逐项比较单位、拓扑与标识。
