#!/usr/bin/env python3
"""检查 needs/ 和 projects/ 的格式。用法：python3 scripts/validate.py"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
STAGES = {"构想", "立项", "原型", "MVP", "试运行", "日常在用", "暂停"}
errors = []


def load(kind):
    out = {}
    d = os.path.join(ROOT, kind)
    for f in sorted(os.listdir(d)):
        if not f.endswith(".json"):
            continue
        p = os.path.join(d, f)
        try:
            data = json.load(open(p, encoding="utf-8"))
        except Exception as e:
            errors.append(f"{kind}/{f}: JSON 无法解析：{e}")
            continue
        i = f[:-5]
        if data.get("id") != i:
            errors.append(f"{kind}/{f}: id 必须等于文件名「{i}」")
        if not ID_RE.match(i):
            errors.append(f"{kind}/{f}: 文件名只能用小写字母、数字和连字符")
        out[i] = data
    return out


needs = load("needs")
projects = load("projects")

for i, n in needs.items():
    for k in ("name", "group", "status"):
        if not n.get(k):
            errors.append(f"needs/{i}: 缺少 {k}")
    if n.get("status") not in ("待调研", "已调研"):
        errors.append(f"needs/{i}: status 只能是 待调研 / 已调研")
    if not isinstance(n.get("order"), (int, float)):
        errors.append(f"needs/{i}: order 必须是数字")
    if not isinstance(n.get("top", []), list) or len(n.get("top", [])) > 3:
        errors.append(f"needs/{i}: top 必须是最多 3 项的数组")
    b = n.get("build")
    if b and b.get("verdict") not in ("直接用", "二次开发", "自研"):
        errors.append(f"needs/{i}: build.verdict 不合法")

for i, p in projects.items():
    for k in ("name", "cat", "desc", "stage"):
        if not p.get(k):
            errors.append(f"projects/{i}: 缺少 {k}")
    for nid in p.get("needs", []) or []:
        if nid not in needs:
            errors.append(f"projects/{i}: needs 里的「{nid}」在 needs/ 中不存在")
    prog = p.get("progress", [])
    if not isinstance(prog, list):
        errors.append(f"projects/{i}: progress 必须是数组")
    else:
        for e in prog:
            if not (isinstance(e, dict) and re.match(r"^\d{4}-\d{2}-\d{2}$", str(e.get("date", ""))) and e.get("done")):
                errors.append(f"projects/{i}: progress 每条需要 date(YYYY-MM-DD) 和 done")
    if "needs" in p and p.get("stage") not in STAGES:
        errors.append(f"projects/{i}: 新格式项目的 stage 应为 {sorted(STAGES)} 之一")

if errors:
    print("发现问题：")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print(f"OK：needs {len(needs)} 个，projects {len(projects)} 个")
