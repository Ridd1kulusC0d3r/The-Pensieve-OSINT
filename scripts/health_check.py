#!/usr/bin/env python3
"""Best-effort temporal source health and diff.

Reachability is intentionally separate from analytical reliability.
"""
from __future__ import annotations
import json, ssl, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]
health_path=ROOT/"data/health.json"
previous={}
if health_path.exists():
    try:
        old=json.loads(health_path.read_text(encoding="utf-8"))
        previous={r["id"]:r for r in old.get("records",[])}
    except Exception:
        previous={}

records=json.loads((ROOT/"knowledge/tools.json").read_text(encoding="utf-8"))["records"]
out=[]; ctx=ssl.create_default_context()
for t in records:
    url=t["url"]; status="unknown"; code=None; final=url; note=""
    try:
        req=Request(url,method="HEAD",headers={"User-Agent":"PensieveHealth/1.0 (+https://github.com/Ridd1kulusC0d3r/The-Pensieve-OSINT)"})
        with urlopen(req,timeout=12,context=ctx) as r:
            code=r.status; final=r.geturl()
        status="reachable" if 200<=code<400 else ("automation-blocked" if code in (401,403,405,429) else "unexpected")
    except HTTPError as e:
        code=e.code; note=str(e.reason)
        status="automation-blocked" if code in (401,403,405,429) else ("not-found" if code==404 else "http-error")
    except (URLError,TimeoutError,OSError) as e:
        status="network-error"; note=str(e)[:160]
    out.append({"id":t["id"],"url":url,"status":status,"http_code":code,"final_url":final,"note":note})
    time.sleep(0.05)

now=datetime.now(timezone.utc).isoformat()
payload={"generated_at":now,"meaning":"Best-effort automated reachability; not an analytical reliability score.","records":out}
health_path.parent.mkdir(exist_ok=True)
health_path.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

counts={}
for r in out: counts[r["status"]]=counts.get(r["status"],0)+1
changes=[]
current={r["id"]:r for r in out}
for rid,r in current.items():
    old=previous.get(rid)
    if not old:
        changes.append(f"- ADDED {rid}: {r['status']}")
    elif old.get("status")!=r.get("status") or old.get("final_url")!=r.get("final_url"):
        changes.append(f"- CHANGED {rid}: {old.get('status')} → {r.get('status')}")
for rid,old in previous.items():
    if rid not in current: changes.append(f"- REMOVED {rid}: previously {old.get('status')}")

lines=["# Tool/source health diff","",f"Generated: {now}","","> Automated reachability is not analytical reliability. Anti-bot blocking and network errors require human interpretation.","","## Current summary",""]
for k,v in sorted(counts.items()): lines.append(f"- **{k}**: {v}")
lines += ["","## Changes since previous snapshot",""]
lines += changes or ["- No status/redirect changes detected."]
(ROOT/"data/HEALTH-DIFF.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
print(counts); print(f"changes={len(changes)}")
