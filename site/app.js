const $=s=>document.querySelector(s);
let db={tools:[],inputs:[],projects:[],taxonomy:[],synonyms:[]}, playbooks=[];
let activeInput="", pins=new Set(JSON.parse(localStorage.getItem("pensievePins")||"[]"));

function esc(s){return String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}
function uniq(a){return [...new Set(a.filter(Boolean))].sort((a,b)=>a.localeCompare(b));}
function optionize(el,vals){for(const v of uniq(vals)){const o=document.createElement("option");o.value=v;o.textContent=v;el.appendChild(o);}}
function savePins(){localStorage.setItem("pensievePins",JSON.stringify([...pins]));}

function expandQuery(q){
  const terms=new Set([q]);
  for(const g of db.synonyms||[]){
    const all=[g.canonical,...(g.terms||[])].map(x=>x.toLowerCase());
    if(all.some(x=>q.includes(x)||x.includes(q))) all.forEach(x=>terms.add(x));
  }
  return [...terms];
}
function score(t,q){
  if(!q) return 1;
  const terms=expandQuery(q);
  let s=0;
  for(const term of terms){
    if(t.name.toLowerCase().includes(term)) s+=12;
    if(String(t.category).toLowerCase().includes(term)) s+=8;
    if((t.inputs||[]).some(x=>x.toLowerCase().includes(term))) s+=9;
    if((t.outputs||[]).some(x=>x.toLowerCase().includes(term))) s+=6;
    if((t.stages||[]).some(x=>x.toLowerCase().includes(term))) s+=4;
    if((t.use_when||[]).some(x=>x.toLowerCase().includes(term))) s+=5;
    if((t.caveats||[]).some(x=>x.toLowerCase().includes(term))) s+=2;
    if(String(t.region).toLowerCase().includes(term)) s+=5;
  }
  return s;
}
function card(t){
 const caveat=(t.caveats||[])[0]||"Verify important findings with independent or primary evidence.";
 return `<article class="card">
   <button class="pin ${pins.has(t.id)?"active":""}" data-pin="${esc(t.id)}" title="Pin locally">★</button>
   <span class="kicker">${esc(t.category)}</span><h3>${esc(t.name)}</h3>
   <div class="meta">
     ${(t.inputs||[]).slice(0,4).map(x=>`<span class="tag">in: ${esc(x)}</span>`).join("")}
     ${(t.stages||[]).slice(0,3).map(x=>`<span class="tag">${esc(x)}</span>`).join("")}
     <span class="tag">${esc(t.region)}</span><span class="tag">${esc(t.access)}</span>
   </div>
   <p>${esc(caveat)}</p><a class="url" href="${esc(t.url)}" rel="noopener noreferrer">Open canonical source ↗</a>
 </article>`;
}
function render(){
 const q=$("#search").value.trim().toLowerCase(), cat=$("#category").value, reg=$("#region").value, access=$("#access").value, pinned=$("#pinnedOnly").checked;
 let arr=db.tools
   .filter(t=>(!activeInput||(t.inputs||[]).includes(activeInput))&&(!cat||t.category===cat)&&(!reg||t.region===reg)&&(!access||t.access===access)&&(!pinned||pins.has(t.id)))
   .map(t=>({t,s:score(t,q)})).filter(x=>!q||x.s>0).sort((a,b)=>b.s-a.s||a.t.name.localeCompare(b.t.name)).map(x=>x.t);
 $("#results").innerHTML=arr.slice(0,120).map(card).join("")||'<p class="graph-note">No matching records. Clear filters or choose a broader input.</p>';
 $("#stats").textContent=`${arr.length} matching · ${db.tools.length} catalog records · ${db.projects.length} ecosystem projects`;
 document.querySelectorAll("[data-pin]").forEach(b=>b.onclick=()=>{const id=b.dataset.pin;pins.has(id)?pins.delete(id):pins.add(id);savePins();render();});
}
function showPlaybook(input){
 const p=playbooks.find(x=>x.input===input); const box=$("#playbook");
 if(!p){box.classList.add("hidden");return;}
 box.classList.remove("hidden");
 box.innerHTML=`<span class="kicker">RECOMMENDED METHOD</span><h2>${esc(p.title)}</h2><p>${esc(p.intent)}</p><ol>${p.steps.map(s=>`<li>${esc(s)}</li>`).join("")}</ol><p class="warning"><strong>Failure modes:</strong> ${p.failure_modes.map(esc).join(" · ")}</p>`;
}
function setInput(id){
 activeInput=activeInput===id?"":id;
 document.querySelectorAll("[data-input]").forEach(b=>b.classList.toggle("active",b.dataset.input===activeInput));
 activeInput?showPlaybook(activeInput):$("#playbook").classList.add("hidden"); render();
}
async function init(){
 const [i,p]=await Promise.all([fetch("data/index.json").then(r=>r.json()),fetch("data/playbooks.json").then(r=>r.json())]);
 db=i;playbooks=p.playbooks||[];
 const preferred=["username","email","phone","domain","ip","url","image","company","document","location","hash","ioc","keyword"];
 const labels=Object.fromEntries(db.inputs.map(x=>[x.id,x.label]));
 $("#inputChips").innerHTML=preferred.map(id=>`<button class="chip" data-input="${id}">${esc(labels[id]||id)}</button>`).join("");
 document.querySelectorAll("[data-input]").forEach(b=>b.onclick=()=>setInput(b.dataset.input));
 optionize($("#category"),db.tools.map(t=>t.category));optionize($("#region"),db.tools.map(t=>t.region));optionize($("#access"),db.tools.map(t=>t.access));
 ["search","category","region","access","pinnedOnly"].forEach(id=>$("#"+id).addEventListener(id==="search"?"input":"change",render));
 $("#clear").onclick=()=>{activeInput="";$("#search").value="";$("#category").value="";$("#region").value="";$("#access").value="";$("#pinnedOnly").checked=false;document.querySelectorAll(".chip").forEach(x=>x.classList.remove("active"));$("#playbook").classList.add("hidden");render();};
 render();
}
init().catch(e=>{$("#results").innerHTML=`<p>Could not load the local knowledge index: ${esc(e.message)}</p>`;});
