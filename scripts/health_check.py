#!/usr/bin/env python3
"""Best-effort public URL health snapshot.

A network error or anti-bot response is not classified as 'dead'. The output is
temporal metadata for human review, not an availability oracle.
"""
from __future__ import annotations
import json, ssl, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]
records=json.loads((ROOT/"knowledge/tools.json").read_text(encoding="utf-8"))["records"]
out=[]
ctx=ssl.create_default_context()
for t in records:
    url=t["url"]
    status="unknown"; code=None; final=url; note=""
    try:
        req=Request(url, method="HEAD", headers={"User-Agent":"PensieveHealth/1.0 (+https://github.com/Ridd1kulusC0d3r/The-Pensieve-OSINT)"})
        with urlopen(req, timeout=12, context=ctx) as r:
            code=r.status; final=r.geturl()
        if 200 <= code < 400: status="reachable"
        elif code in (401,403,405,429): status="automation-blocked"
        else: status="unexpected"
    except HTTPError as e:
        code=e.code
        status="automation-blocked" if code in (401,403,405,429) else ("not-found" if code==404 else "http-error")
        note=str(e.reason)
    except (URLError, TimeoutError, OSError) as e:
        status="network-error"; note=str(e)[:160]
    out.append({"id":t["id"],"url":url,"status":status,"http_code":code,"final_url":final,"note":note})
    time.sleep(0.05)
payload={"generated_at":datetime.now(timezone.utc).isoformat(),"meaning":"Best-effort automated reachability; not an analytical reliability score.","records":out}
(ROOT/"data").mkdir(exist_ok=True)
(ROOT/"data/health.json").write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
counts={}
for r in out: counts[r["status"]]=counts.get(r["status"],0)+1
lines=["# Tool/source health snapshot","",f"Generated: {payload['generated_at']}","","> Automated reachability is not analytical reliability. Anti-bot blocking is reported separately.","","## Summary",""]
for k,v in sorted(counts.items()): lines.append(f"- **{k}**: {v}")
(ROOT/"data/HEALTH-DIFF.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
print(counts)
