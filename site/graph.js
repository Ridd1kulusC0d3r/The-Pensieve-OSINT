const NS="http://www.w3.org/2000/svg";
const esc=s=>String(s??"");
async function init(){
 const g=await fetch("data/graph.json").then(r=>r.json());
 const sel=document.querySelector("#graphInput");
 const inputNodes=g.nodes.filter(n=>n.type==="input").sort((a,b)=>a.label.localeCompare(b.label));
 for(const n of inputNodes){const o=document.createElement("option");o.value=n.id;o.textContent=n.label;sel.appendChild(o);}
 const preferred=inputNodes.find(n=>n.id==="input:domain");if(preferred)sel.value=preferred.id;
 function draw(){
  const center=sel.value;
  const edgeSet=g.edges.filter(e=>e.to===center&&e.type==="accepts").slice(0,42);
  const toolIds=new Set(edgeSet.map(e=>e.from));
  const tools=g.nodes.filter(n=>toolIds.has(n.id));
  const box=document.querySelector("#graph");box.innerHTML="";
  const svg=document.createElementNS(NS,"svg");svg.setAttribute("viewBox","0 0 1000 680");box.appendChild(svg);
  const cx=500,cy=340,r=260;
  edgeSet.forEach((e,i)=>{const a=2*Math.PI*i/Math.max(edgeSet.length,1)-Math.PI/2,x=cx+r*Math.cos(a),y=cy+r*Math.sin(a);const line=document.createElementNS(NS,"line");line.setAttribute("x1",cx);line.setAttribute("y1",cy);line.setAttribute("x2",x);line.setAttribute("y2",y);line.setAttribute("class","edge");svg.appendChild(line);});
  function node(x,y,label,cls,rad=35){
   const c=document.createElementNS(NS,"circle");c.setAttribute("cx",x);c.setAttribute("cy",y);c.setAttribute("r",rad);c.setAttribute("class","node "+cls);svg.appendChild(c);
   const t=document.createElementNS(NS,"text");t.setAttribute("x",x);t.setAttribute("y",y+rad+16);t.setAttribute("text-anchor","middle");t.setAttribute("class","node-label");t.textContent=label.length>24?label.slice(0,22)+"…":label;svg.appendChild(t);
  }
  node(cx,cy,inputNodes.find(n=>n.id===center)?.label||center,"input",46);
  tools.forEach((n,i)=>{const a=2*Math.PI*i/Math.max(tools.length,1)-Math.PI/2;node(cx+r*Math.cos(a),cy+r*Math.sin(a),n.label,"tool",24);});
  document.querySelector("#graphNote").textContent=`${tools.length} resources accept this input in the current catalog. Graph edges are routing metadata, not proof of any real-world relationship.`;
 }
 sel.onchange=draw;draw();
}
init().catch(e=>document.querySelector("#graph").textContent="Could not load graph: "+esc(e.message));
