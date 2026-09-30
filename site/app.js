const $=s=>document.querySelector(s);
let db={tools:[],inputs:[],projects:[],taxonomy:[]}, playbooks=[];
let activeInput="", pins=new Set(JSON.parse(localStorage.getItem("pensievePins")||"[]"));

function esc(s){return String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}
function uniq(a){return [...new Set(a.filter(Boolean))].sort((a,b)=>a.localeCompare(b));}
function optionize(el,vals){for(const v of uniq(vals)){const o=document.createElement("option");o.value=v;o.textContent=v;el.appendChild(o);}}
function searchText(t){return [t.name,t.category,t.region,t.access,...(t.inputs||[]),...(t.outputs||[]),...(t.stages||[]),...(t.use_when||[]),...(t.caveats||[])].join(" ").toLowerCase();}
function savePins(){localStorage.setItem("pensievePins",JSON.stringify([...pins]));}

function card(t){
 const caveat=(t.caveats||[])[0]||"Verify important findings with independent or primary evidence.";
 return `<article class="card">
   <button class="pin ${pins.has(t.id)?"active":""}" data-pin="${esc(t.id)}" title="Pin locally">★</button>
   <span class="kicker">${esc(t.category)}</span>
   <h3>${esc(t.name)}</h3>
   <div class="meta">
     ${(t.inputs||[]).slice(0,4).map(x=>`<span class="tag">in: ${esc(x)}</span>`).join("")}
     ${(t.stages||[]).slice(0,3).map(x=>`<span class="tag">${esc(x)}</span>`).join("")}
     <span class="tag">${esc(t.region)}</span>
     <span class="tag">${esc(t.access)}</span>
   </div>
   <p>${esc(caveat)}</p>
   <a class="url" href="${esc(t.url)}" rel="noopener noreferrer">Open canonical source ↗</a>
 </article>`;
}
function render(){
 const q=$("#search").value.trim().toLowerCase(), cat=$("#category").value, reg=$("#region").value, access=$("#access").value, pinned=$("#pinnedOnly").checked;
 let arr=db.tools.filter(t=>(!activeInput||(t.inputs||[]).includes(activeInput))&&(!cat||t.category===cat)&&(!reg||t.region===reg)&&(!access||t.access===access)&&(!pinned||pins.has(t.id))&&(!q||searchText(t).includes(q)));
 $("#results").innerHTML=arr.slice(0,120).map(card).join("")||'<p class="graph-note">No matching records. Clear filters or choose a broader input.</p>';
 $("#stats").textContent=`${arr.length} matching · ${db.tools.length} catalog records · ${db.projects.length} ecosystem projects`;
 document.querySelectorAll("[data-pin]").forEach(b=>b.onclick=()=>{const id=b.dataset.pin;pins.has(id)?pins.delete(id):pins.add(id);savePins();render();});
}
function showPlaybook(input){
 const p=playbooks.find(x=>x.input===input);
 const box=$("#playbook");
 if(!p){box.classList.add("hidden");return;}
 box.classList.remove("hidden");
 box.innerHTML=`<span class="kicker">RECOMMENDED METHOD</span><h2>${esc(p.title)}</h2><p>${esc(p.intent)}</p><ol>${p.steps.map(s=>`<li>${esc(s)}</li>`).join("")}</ol><p class="warning"><strong>Failure modes:</strong> ${p.failure_modes.map(esc).join(" · ")}</p>`;
}
function setInput(id){
 activeInput=activeInput===id?"":id;
 document.querySelectorAll("[data-input]").forEach(b=>b.classList.toggle("active",b.dataset.input===activeInput));
 activeInput?showPlaybook(activeInput):$("#playbook").classList.add("hidden");
 render();
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
