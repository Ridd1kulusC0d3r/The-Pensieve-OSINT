#!/usr/bin/env python3
"""Build derived Pensieve artifacts from canonical JSON knowledge.

Standard-library only by design.
"""
from __future__ import annotations
import csv, json, shutil
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
K = ROOT / "knowledge"
SITE = ROOT / "site"
SITE_DATA = SITE / "data"
DATA = ROOT / "data"

def load(name):
    return json.loads((K / name).read_text(encoding="utf-8"))

def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

tools = load("tools.json")["records"]
inputs = load("inputs.json")["inputs"]
projects = load("projects.json")["projects"]
playbooks = load("playbooks.json")["playbooks"]
taxonomy = load("int-taxonomy.json")["disciplines"]
relations = load("relations.json")["relations"]

# CSV export for people and simple scripts.
DATA.mkdir(exist_ok=True)
fields = ["category","name","url","access","input","stage","region","status"]
with (DATA / "tools.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for t in tools:
        w.writerow({
            "category": t["category"],
            "name": t["name"],
            "url": t["url"],
            "access": t.get("access",""),
            "input": "|".join(t.get("inputs",[])),
            "stage": "|".join(t.get("stages",[])),
            "region": t.get("region","global"),
            "status": t.get("status","unknown"),
        })

SITE_DATA.mkdir(parents=True, exist_ok=True)
dump(SITE_DATA / "index.json", {
    "schema_version":"1.0.0",
    "tools":tools,
    "inputs":inputs,
    "projects":projects,
    "taxonomy":taxonomy,
})
dump(SITE_DATA / "playbooks.json", {"playbooks":playbooks})

# Build a graph that is useful without pretending every edge is evidence.
nodes = []
edges = []
seen = set()
def node(nid, label, kind):
    if nid not in seen:
        seen.add(nid)
        nodes.append({"id":nid,"label":label,"type":kind})
for i in inputs:
    node("input:"+i["id"], i["label"], "input")
for p in projects:
    node("project:"+p["id"], p["name"], "project")
for t in tools:
    tid = "tool:"+t["id"]
    node(tid, t["name"], "tool")
    for inp in t.get("inputs",[]):
        node("input:"+inp, inp, "input")
        edges.append({"from":tid,"type":"accepts","to":"input:"+inp})
for rel in relations:
    node("concept:"+rel["from"], rel["from"], "concept")
    node("concept:"+rel["to"], rel["to"], "concept")
    edges.append({"from":"concept:"+rel["from"],"type":rel["type"],"to":"concept:"+rel["to"]})
dump(SITE_DATA / "graph.json", {"nodes":nodes,"edges":edges})

# Public AI manifests on Pages.
shutil.copy2(ROOT / "llms.txt", SITE / "llms.txt")
shutil.copy2(ROOT / "llms-full.txt", SITE / "llms-full.txt")
shutil.copy2(ROOT / "ai-index.json", SITE / "ai-index.json")

base = "https://ridd1kulusc0d3r.github.io/The-Pensieve-OSINT"
urls = ["","/graph.html","/llms.txt","/llms-full.txt","/ai-index.json"]
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for suffix in urls:
    sitemap.append(f"  <url><loc>{escape(base+suffix)}</loc></url>")
sitemap.append("</urlset>")
(SITE / "sitemap.xml").write_text("\n".join(sitemap)+"\n", encoding="utf-8")

schema_org = {
    "@context":"https://schema.org",
    "@graph":[
        {
            "@type":"WebSite",
            "@id":base+"/#website",
            "name":"The Pensieve OSINT",
            "url":base+"/",
            "description":"Analyst second brain for Open-Source Intelligence.",
            "inLanguage":["en","pt-BR"],
            "keywords":["OSINT","SOCMINT","GEOINT","IMINT","CTI","open-source intelligence","knowledge graph","digital investigation","Brazil OSINT","LATAM OSINT"]
        },
        {
            "@type":"Dataset",
            "@id":base+"/#dataset",
            "name":"The Pensieve OSINT Knowledge Catalog",
            "description":"Machine-readable catalog of OSINT tools, public sources, inputs, outputs, playbooks, projects and analytical relations.",
            "url":base+"/ai-index.json",
            "isAccessibleForFree":True,
            "license":"https://github.com/Ridd1kulusC0d3r/The-Pensieve-OSINT",
            "distribution":[
                {"@type":"DataDownload","encodingFormat":"application/json","contentUrl":base+"/data/index.json"},
                {"@type":"DataDownload","encodingFormat":"application/json","contentUrl":base+"/data/playbooks.json"}
            ]
        }
    ]
}
dump(SITE_DATA / "schema-org.json", schema_org)

print(f"Built {len(tools)} tools, {len(playbooks)} playbooks, {len(nodes)} graph nodes and {len(edges)} edges.")
