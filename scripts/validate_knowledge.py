#!/usr/bin/env python3
"""Validate canonical Pensieve knowledge without third-party packages."""
from __future__ import annotations
import json, re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
K = ROOT / "knowledge"

def load(name):
    return json.loads((K / name).read_text(encoding="utf-8"))

tools = load("tools.json")["records"]
playbooks = load("playbooks.json")["playbooks"]
projects = load("projects.json")["projects"]

errors = []
ids = set()
for n,t in enumerate(tools,1):
    missing = [k for k in ("id","name","category","url","inputs","outputs","stages","region","status","last_reviewed") if k not in t]
    if missing: errors.append(f"tool {n}: missing {missing}")
    tid = t.get("id","")
    if not re.fullmatch(r"[a-z0-9-]+", tid): errors.append(f"tool {n}: invalid id {tid!r}")
    if tid in ids: errors.append(f"duplicate tool id: {tid}")
    ids.add(tid)
    u = urlparse(t.get("url",""))
    if u.scheme not in ("http","https") or not u.netloc: errors.append(f"{tid}: invalid url")
    if not isinstance(t.get("caveats",[]), list): errors.append(f"{tid}: caveats must be a list")

pb_ids=set()
for p in playbooks:
    if p["id"] in pb_ids: errors.append(f"duplicate playbook id: {p['id']}")
    pb_ids.add(p["id"])
    if not p.get("steps"): errors.append(f"playbook {p['id']}: no steps")
    if not p.get("failure_modes"): errors.append(f"playbook {p['id']}: no failure modes")

proj_ids=[p["id"] for p in projects]
if len(proj_ids)!=len(set(proj_ids)): errors.append("duplicate project id")

if errors:
    print("\n".join("ERROR: "+e for e in errors))
    raise SystemExit(1)
print(f"OK: {len(tools)} tools, {len(playbooks)} playbooks, {len(projects)} projects")
