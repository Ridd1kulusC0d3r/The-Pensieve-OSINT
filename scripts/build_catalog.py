#!/usr/bin/env python3
"""Build derived Pensieve artifacts from canonical JSON knowledge."""
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
synonyms = load("synonyms.json")["groups"]
inference_rules = load("inference-rules.json")["rules"]
source_quality = load("source-quality.json")
questions = load("questions.json")["templates"]

DATA.mkdir(exist_ok=True)
fields = ["category","name","url","access","input","stage","region","status"]
with (DATA / "tools.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for t in tools:
        w.writerow({
            "category": t["category"], "name": t["name"], "url": t["url"],
            "access": t.get("access",""), "input": "|".join(t.get("inputs",[])),
            "stage": "|".join(t.get("stages",[])), "region": t.get("region","global"),
            "status": t.get("status","unknown"),
        })

SITE_DATA.mkdir(parents=True, exist_ok=True)
dump(SITE_DATA / "index.json", {
    "schema_version":"1.1.0",
    "tools":tools, "inputs":inputs, "projects":projects, "taxonomy":taxonomy,
    "synonyms":synonyms, "inference_rules":inference_rules,
    "source_quality":source_quality, "questions":questions
})
dump(SITE_DATA / "playbooks.json", {"playbooks":playbooks})

nodes=[]; edges=[]; seen=set()
def node(nid,label,kind):
    if nid not in seen:
        seen.add(nid); nodes.append({"id":nid,"label":label,"type":kind})

for i in inputs: node("input:"+i["id"],i["label"],"input")
for p in projects: node("project:"+p["id"],p["name"],"project")
for t in tools:
    tid="tool:"+t["id"]; node(tid,t["name"],"tool")
    for inp in t.get("inputs",[]):
        node("input:"+inp,inp,"input")
        edges.append({"from":tid,"type":"accepts","to":"input:"+inp})
    for output in t.get("outputs",[]):
        node("output:"+output,output,"output")
        edges.append({"from":tid,"type":"produces","to":"output:"+output})
for rel in relations:
    node("concept:"+rel["from"],rel["from"],"concept")
    node("concept:"+rel["to"],rel["to"],"concept")
    edges.append({"from":"concept:"+rel["from"],"type":rel["type"],"to":"concept:"+rel["to"]})
dump(SITE_DATA / "graph.json", {"nodes":nodes,"edges":edges})

for src,dst in [
    (ROOT/"llms.txt",SITE/"llms.txt"),
    (ROOT/"llms-full.txt",SITE/"llms-full.txt"),
    (ROOT/"ai-index.json",SITE/"ai-index.json")
]:
    shutil.copy2(src,dst)

base="https://ridd1kulusc0d3r.github.io/The-Pensieve-OSINT"
urls=["","/graph.html","/llms.txt","/llms-full.txt","/ai-index.json","/data/index.json","/data/playbooks.json","/data/graph.json"]
sitemap=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for suffix in urls:
    sitemap.append(f"  <url><loc>{escape(base+suffix)}</loc></url>")
sitemap.append("</urlset>")
(SITE/"sitemap.xml").write_text("\n".join(sitemap)+"\n",encoding="utf-8")

schema_org={
 "@context":"https://schema.org",
 "@graph":[
  {"@type":"WebSite","@id":base+"/#website","name":"The Pensieve OSINT","url":base+"/","description":"Analyst second brain for Open-Source Intelligence.","inLanguage":["en","pt-BR"],"keywords":["OSINT","SOCMINT","GEOINT","IMINT","CTI","open-source intelligence","knowledge graph","digital investigation","Brazil OSINT","LATAM OSINT"]},
  {"@type":"Dataset","@id":base+"/#dataset","name":"The Pensieve OSINT Knowledge Catalog","description":"Machine-readable catalog of OSINT tools, sources, inputs, outputs, playbooks, inference rules, projects and analytical relations.","url":base+"/ai-index.json","isAccessibleForFree":True,"distribution":[
   {"@type":"DataDownload","encodingFormat":"application/json","contentUrl":base+"/data/index.json"},
   {"@type":"DataDownload","encodingFormat":"application/json","contentUrl":base+"/data/playbooks.json"},
   {"@type":"DataDownload","encodingFormat":"application/json","contentUrl":base+"/data/graph.json"}
  ]}
 ]
}
dump(SITE_DATA/"schema-org.json",schema_org)
print(f"Built {len(tools)} tools, {len(playbooks)} playbooks, {len(nodes)} graph nodes and {len(edges)} edges.")
