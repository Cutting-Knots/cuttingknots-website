
(()=>{
"use strict";
const $=id=>document.getElementById(id);
const LANG=(document.documentElement.lang||"").slice(0,2)==="en"?"en":"it";
const L={it:{copied:"Copiato",selected:"Selezionato: premi Ctrl+C",enter:"Entra · ",talk:"Parla con Bit",cut:"Taglia il nodo",look:"Guarda il nodo tagliato",home:"/",
 done:"Villaggio esplorato. Il prossimo nodo è il tuo: scrivici dall'Ufficio Postale."},
 en:{copied:"Copied",selected:"Selected: press Ctrl+C",enter:"Enter · ",talk:"Talk to Bit",cut:"Cut the knot",look:"Look at the cut knot",home:"/en",
 done:"Village explored. The next knot is yours: write to us from the Post Office."}}[LANG];
/* ---------- brand mark (symbol paths from the CuttingKnots kit) ---------- */
const KNOT_D="M147.43,253.64C137.82,252.41 129.33,249.34 121.62,244.32C118.18,242.07 116.06,240.34 113.05,237.29C109.86,234.05 107.93,231.67 105.59,228.10C103.55,224.96 99.75,217.51 99.75,216.63C99.75,216.03 100.00,215.80 109.00,208.33C110.99,206.68 114.03,204.27 115.75,202.99C117.47,201.70 119.63,199.94 120.55,199.08C121.52,198.17 122.37,197.56 122.57,197.64C122.76,197.71 123.57,199.31 124.37,201.20C127.97,209.69 130.98,214.76 134.49,218.25C138.37,222.11 143.25,224.76 148.75,225.97C151.25,226.53 155.37,226.78 157.52,226.51C161.94,225.96 167.46,223.80 170.87,221.29C173.84,219.10 177.61,215.12 179.63,212.04C180.31,211.01 180.39,210.96 181.36,211.07C181.92,211.13 183.28,211.54 184.38,211.97C186.68,212.89 192.18,214.76 194.38,215.38C198.40,216.52 204.59,217.73 206.45,217.74C207.42,217.75 208.25,218.14 208.25,218.58C208.25,218.75 207.79,219.78 207.23,220.88C203.62,227.93 197.90,235.16 191.88,240.24C189.23,242.47 183.38,246.44 180.88,247.70C175.78,250.26 168.58,252.49 162.47,253.38C158.76,253.93 150.77,254.06 147.43,253.64ZM216.75,210.24C213.05,209.97 203.47,208.68 199.75,207.96C197.03,207.43 190.47,205.81 188.34,205.15C174.27,200.76 171.09,199.55 162.72,195.37C158.48,193.26 152.05,189.69 148.86,187.68C142.10,183.42 139.50,181.47 139.51,180.67C139.52,180.30 140.27,179.47 141.82,178.12C144.23,176.02 150.32,170.43 156.62,164.53C159.18,162.14 160.56,161.02 160.96,161.01C161.29,161.00 163.36,162.20 165.83,163.84C171.17,167.37 174.19,169.07 179.06,171.30C186.59,174.74 194.64,177.70 199.93,178.97C200.45,179.10 202.49,179.61 204.46,180.11C208.58,181.15 211.45,181.49 216.38,181.49C225.04,181.49 234.31,179.49 240.86,176.21C248.77,172.24 254.65,167.07 259.54,159.78C263.20,154.32 265.18,149.08 266.12,142.37C266.91,136.72 266.41,132.12 264.33,126.00C262.98,122.01 261.21,119.15 257.83,115.48C254.16,111.51 252.01,109.93 248.25,108.42C243.87,106.67 241.75,106.11 237.75,105.66C235.24,105.37 235.12,105.33 235.05,104.74C234.93,103.79 234.20,101.96 232.40,98.02C231.49,96.03 230.75,94.15 230.75,93.84C230.75,93.43 233.24,90.72 239.65,84.17C244.54,79.16 248.81,74.92 249.13,74.75C249.85,74.36 250.70,74.57 255.06,76.16C266.43,80.32 276.14,87.17 284.07,96.61C295.17,109.84 300.38,127.88 298.25,145.75C297.53,151.82 296.66,155.55 294.54,161.76C292.92,166.50 290.29,171.78 287.07,176.74C281.78,184.88 273.60,192.85 264.21,199.01C261.17,201.01 253.53,204.73 249.88,206.00C243.81,208.10 237.33,209.47 231.00,209.98C226.07,210.38 220.15,210.48 216.75,210.24ZM50.12,192.95C49.16,192.67 46.97,192.00 45.25,191.45C37.20,188.88 29.98,184.23 22.61,176.88C15.27,169.55 11.19,162.39 8.65,152.35C5.68,140.60 7.57,125.10 13.28,114.30C14.63,111.75 18.03,106.61 19.99,104.15C23.44,99.83 28.04,95.66 33.25,92.14C36.55,89.90 43.10,86.77 47.25,85.43C51.97,83.92 54.39,83.37 58.78,82.84C62.52,82.39 73.52,82.19 73.90,82.57C74.01,82.68 73.68,84.48 73.17,86.57C71.45,93.62 71.08,101.24 72.15,107.75C72.39,109.19 72.59,110.71 72.60,111.11L72.62,111.85L69.38,112.52C63.18,113.79 60.09,114.86 55.95,117.16C46.47,122.44 41.06,129.96 39.99,139.30C39.40,144.52 40.86,150.14 43.88,154.26C45.11,155.94 47.91,158.50 50.16,160.02C54.13,162.70 60.45,165.15 65.38,165.91C69.06,166.48 69.00,166.45 69.79,168.00C70.62,169.65 72.25,173.75 72.25,174.19C72.25,174.36 67.97,178.75 62.73,183.94C55.29,191.32 53.07,193.38 52.54,193.41C52.18,193.44 51.09,193.23 50.12,192.95ZM215.50,168.97C211.51,168.77 208.76,168.33 204.22,167.13C198.51,165.63 196.39,164.95 195.85,164.46C195.56,164.20 194.78,162.78 194.11,161.30C191.84,156.32 189.81,153.14 186.04,148.67C183.12,145.20 173.59,135.73 168.50,131.24C165.96,128.99 162.24,125.61 160.25,123.73C152.12,116.07 150.00,114.38 145.86,112.30C140.33,109.53 132.80,107.42 127.19,107.08C125.84,106.99 124.58,106.80 124.38,106.65C124.18,106.50 123.91,105.70 123.77,104.88C123.63,104.05 123.23,101.86 122.87,100.00C121.92,95.10 121.90,94.81 122.38,92.49C123.23,88.31 125.15,82.39 125.98,81.41C126.32,81.01 126.60,80.97 128.25,81.12C140.47,82.22 155.15,87.05 163.72,92.81C168.00,95.68 178.18,104.49 185.75,111.87C188.43,114.49 193.18,119.02 196.30,121.96C202.66,127.92 205.19,130.61 209.34,135.82C213.58,141.14 216.55,145.98 219.23,151.94C221.05,155.99 223.00,161.95 223.89,166.20C224.27,167.99 224.28,168.33 223.98,168.61C223.53,169.04 219.97,169.19 215.50,168.97ZM100.06,145.31C95.03,139.25 89.82,130.73 87.58,124.90C84.29,116.31 82.85,108.17 82.90,98.25C82.95,86.51 84.76,76.77 88.70,67.00C96.24,48.31 110.82,33.67 129.12,26.41C135.83,23.75 142.19,22.32 149.88,21.75C162.76,20.80 177.74,24.77 188.52,32.02C194.73,36.19 201.25,42.68 205.04,48.47C205.71,49.48 206.25,50.42 206.25,50.55C206.25,50.83 203.75,53.18 199.25,57.14C197.39,58.77 193.53,62.30 190.66,64.99C187.79,67.68 185.20,69.91 184.90,69.95C184.46,70.01 184.11,69.65 183.12,68.07C179.85,62.91 175.58,58.19 172.09,55.91C169.31,54.09 164.91,52.12 161.62,51.22C158.71,50.42 158.48,50.40 153.62,50.39C148.01,50.37 146.62,50.60 142.00,52.24C135.60,54.53 131.54,57.16 126.24,62.48C121.91,66.82 119.84,69.65 116.90,75.26C112.26,84.12 109.96,95.62 111.11,104.24C112.15,112.10 114.76,119.31 119.06,126.18C119.60,127.04 120.00,127.95 119.96,128.21C119.86,128.75 101.80,146.50 101.34,146.50C101.18,146.50 100.60,145.97 100.06,145.31Z";
const CUT_D="M19.40,246.06C19.05,245.72 19.30,245.00 19.94,244.50C20.32,244.21 38.12,226.51 59.50,205.17C109.58,155.19 131.63,133.32 134.12,131.16C135.22,130.20 137.03,128.57 138.12,127.52C140.93,124.86 142.34,123.75 142.94,123.75C143.51,123.75 144.94,124.82 147.65,127.27C148.63,128.15 150.80,130.11 152.48,131.62C156.42,135.17 159.50,138.41 159.50,139.00C159.50,139.28 157.14,141.70 153.49,145.17C150.19,148.31 128.79,169.59 105.93,192.47C52.00,246.46 52.47,246.00 52.28,246.01C51.06,246.12 19.50,246.17 19.40,246.06ZM192.64,104.42C191.68,103.57 189.48,101.53 187.75,99.88C186.01,98.22 183.28,95.69 181.68,94.25C179.60,92.38 178.76,91.46 178.76,91.06C178.75,90.44 182.16,86.58 185.66,83.25C194.61,74.72 222.94,46.29 247.24,21.43C258.42,10.00 261.25,7.23 261.86,7.13C262.84,6.98 293.52,6.79 293.94,6.93C294.40,7.10 294.31,7.94 293.78,8.44C293.52,8.68 279.13,22.99 261.80,40.25C244.47,57.51 226.43,75.42 221.71,80.05C216.99,84.68 209.14,92.42 204.26,97.24C198.27,103.16 195.23,106.00 194.89,105.99C194.60,105.98 193.59,105.28 192.64,104.42Z";
document.querySelectorAll(".mark").forEach(el=>{const s=+el.dataset.size||28;el.innerHTML=`<svg viewBox="7 6 292 248" width="${s}" height="${Math.round(s*248/292)}" aria-hidden="true"><path fill="#FFFFFF" d="${KNOT_D}"/><path fill="#FD3F03" d="${CUT_D}"/></svg>`});

/* ---------- pixel icons ---------- */
const ICONS={
tower:[".....oo.....",".....##.....","....####....","....#..#....","....####....","....#..#....","....####....","...######...","...#.##.#...","...######...","...#.##.#...","..########.."],
gear:[".....##.....","..#.####.#..","..########..","...##..##...",".###....###.",".##..oo..##.",".##..oo..##.",".###....###.","...##..##...","..########..","..#.####.#..",".....##....."],
house:[".....oo.....","....####....","...######...","..########..",".##########.","..#......#..","..#.##.#.#..","..#.##.#.#..","..#....#.#..","..#.oo.#.#..","..#.oo.#.#..","..########.."],
scroll:["............",".##########.","#.########.#",".#........#.",".#.######.#.",".#........#.",".#.####...#.",".#........#.",".#.#####..#.",".#.....oo.#.","#.#######o.#",".##########."],
mail:["............","############","##........##","#.#......#.#","#..#....#..#","#...#oo#...#","#....##....#","#..........#","#..........#","############"]
};
document.querySelectorAll("[data-icon]").forEach(el=>{const g=ICONS[el.dataset.icon],s=+el.dataset.px||5;let r="";
 g.forEach((row,y)=>[...row].forEach((c,x)=>{if(c!==".")r+=`<rect x="${x}" y="${y}" width="1" height="1" fill="${c==="o"?"#FD3F03":"#F2F3F5"}"/>`}));
 el.innerHTML=`<svg viewBox="0 0 ${g[0].length} ${g.length}" width="${g[0].length*s}" height="${g.length*s}" shape-rendering="crispEdges" aria-hidden="true">${r}</svg>`});

/* ---------- site: ticker, reveal, menu, copy ---------- */
const track=$("track");
if(track){const KN=LANG==="en"?["MANUAL PROCESSES","SYSTEMS THAT DON'T TALK","SCATTERED DATA","REPORTS BUILT BY HAND","EMAILS SORTED ONE BY ONE","TEN VERSIONS OF ONE EXCEL FILE","SOFTWARE NOBODY DARES TOUCH"]:["PROCESSI MANUALI","SISTEMI CHE NON SI PARLANO","DATI SPARSI","REPORT FATTI A MANO","EMAIL SMISTATE UNA PER UNA","FILE EXCEL IN DIECI VERSIONI","SOFTWARE CHE NESSUNO OSA TOCCARE"];track.innerHTML=[...KN,...KN].map(k=>`<span>${k}</span><i></i>`).join("")}
if("IntersectionObserver" in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}}),{rootMargin:"0px 0px -10% 0px"});
 document.querySelectorAll(".reveal").forEach(el=>{if(el.getBoundingClientRect().top>innerHeight)io.observe(el)})}
const menuBtn=$("menu-btn"),nav=$("site-nav");
if(menuBtn&&nav){menuBtn.addEventListener("click",()=>{const o=nav.classList.toggle("open");menuBtn.setAttribute("aria-expanded",o);menuBtn.textContent=o?"✕ Chiudi":"☰ Menu"})}
document.addEventListener("click",e=>{
 const c=e.target.closest("[data-copy]");if(!c)return;const v=c.dataset.copy,old=c.textContent;
 const done=()=>{c.textContent=L.copied;setTimeout(()=>c.textContent=old,1600)};
 const sel=()=>{const a=c.parentElement.querySelector(".addr");if(!a)return;const r=document.createRange();r.selectNodeContents(a);const s=getSelection();s.removeAllRanges();s.addRange(r);c.textContent=L.selected};
 try{navigator.clipboard.writeText(v).then(done,sel)}catch(err){sel()}
});

/* ---------- hero: pixel knot being cut ---------- */
const KCV=$("knot-canvas");
if(KCV){
 const g=KCV.getContext("2d"),W=96,H=72,S=64;KCV.width=W;KCV.height=H;
 const kImg=rasterize(KNOT_D,"#F2F3F5",S),cImg=rasterize(CUT_D,"#FD3F03",S),kh=kImg.height,kx=(W-S)/2|0,ky=(H-kh)/2|0;
 const rm=matchMedia("(prefers-reduced-motion: reduce)").matches;let bits=[],fired=false,last=performance.now(),tt=0;
 const frame=now=>{
  const dt=Math.min(.05,(now-last)/1000);last=now;tt+=dt;
  const ph=rm?3:tt%5;g.clearRect(0,0,W,H);
  const shake=!rm&&ph<1.6&&Math.floor(tt*6)%7===0?1:0;
  g.drawImage(kImg,kx+shake,ky);
  let p=ph<1.6?0:Math.min(1,(ph-1.6)/.25);
  if(ph>4.6)p=Math.floor(tt*8)%2;
  if(p>0){const w=Math.ceil(S*p);g.drawImage(cImg,S-w,0,w,kh,kx+S-w,ky,w,kh)}
  if(!rm&&ph>=1.85&&!fired){fired=true;for(let i=0;i<26;i++){const a=Math.random()*6.28,v=20+Math.random()*50;bits.push({x:W/2,y:H/2,vx:Math.cos(a)*v,vy:Math.sin(a)*v-20,l:.6+Math.random()*.6,c:i%3?"#FD3F03":"#F2F3F5"})}}
  if(ph<1)fired=false;
  bits=bits.filter(b=>(b.l-=dt)>0);bits.forEach(b=>{b.x+=b.vx*dt;b.y+=b.vy*dt;b.vy+=90*dt;g.fillStyle=b.c;g.fillRect(b.x|0,b.y|0,1,1)});
  if(!rm)requestAnimationFrame(frame);
 };
 requestAnimationFrame(frame);
}

const HERO_CV=$("hero-canvas"),GAME_EL=$("game");
if(!HERO_CV&&!GAME_EL)return;

/* ---------- game content (IT / EN) ---------- */
const SEC={
it:{
casa:{eyebrow:"Chi siamo",title:"La Base",html:`<p class="lead">CuttingKnots è una società di consulenza IT e automazione con l'intelligenza artificiale.</p><p>Prendiamo un problema aggrovigliato, lo guardiamo da vicino e lo risolviamo con un intervento netto.</p><dl class="facts"><div><dt>Fondatori</dt><dd>Luca, Luca e Antonio</dd></div><div><dt>Per chi</dt><dd>PMI e team aziendali con processi da semplificare</dd></div><div><dt>Come</dt><dd>Analisi, prototipo, produzione</dd></div></dl>`},
torre:{eyebrow:"Consulenza IT",title:"Torre della Consulenza",html:`<p class="lead">Dall'alto si vede tutto il sistema. Partiamo da lì.</p><ul class="list"><li><span><b>Architettura di soluzione</b>Come applicazioni, dati e persone si collegano, prima di scrivere codice.</span></li><li><span><b>Sviluppo low-code</b>Applicazioni gestionali su piattaforme come Mendix, in settimane.</span></li><li><span><b>Modernizzazione</b>Software datato portato su basi che si possono mantenere.</span></li><li><span><b>Settori regolati</b>Esperienza su progetti bancari e finanziari.</span></li></ul>`},
officina:{eyebrow:"Automazione con IA",title:"Officina dell'Automazione",html:`<p class="lead">Qui si costruiscono gli strumenti che lavorano al posto vostro.</p><ul class="list"><li><span><b>Agenti e assistenti IA</b>Leggono documenti, email e dati e preparano risposte e riepiloghi.</span></li><li><span><b>Automazione dei processi</b>Fatture, report e richieste diventano flussi automatici.</span></li><li><span><b>IA nei vostri sistemi</b>Modelli collegati agli strumenti che usate già, via API e server MCP.</span></li><li><span><b>Formazione</b>Il team impara a usare questi strumenti in sicurezza.</span></li></ul>`},
archivio:{eyebrow:"Progetti",title:"Archivio Progetti",html:`<p class="lead">Ogni progetto è un nodo tagliato.</p><div class="cases"><article class="case"><span class="tag">Esempio</span><h3>Richieste clienti smistate da un assistente</h3><p class="knot-line">Nodo: 40 email al giorno smistate a mano</p></article><article class="case"><span class="tag">Esempio</span><h3>Report mensile senza copia-incolla</h3><p class="knot-line">Nodo: due giorni di lavoro al mese</p></article><article class="case"><span class="tag">Esempio</span><h3>Gestionale low-code per un ufficio operativo</h3><p class="knot-line">Nodo: versioni diverse dello stesso dato</p></article></div>`},
posta:{eyebrow:"Contatti",title:"Ufficio Postale",html:`<p class="lead">Hai un nodo da sciogliere? Raccontacelo in poche righe.</p><div class="mail"><span class="addr">info@cuttingknots.com</span><button class="pxbtn small" data-copy="info@cuttingknots.com">Copia indirizzo</button></div><p>Rispondiamo entro due giorni lavorativi.</p>`},
bit:{eyebrow:"Guida",title:"Bit",html:`<p class="lead">Ciao, sono Bit. Hai trovato il villaggio segreto di CuttingKnots.</p><p>Ogni edificio racconta una parte di noi. Avvicinati a una porta e interagisci per entrare.</p><ul class="list compact"><li><span><b>La Base</b>chi siamo, a nord-ovest</span></li><li><span><b>Torre della Consulenza</b>a nord-est, oltre il lago</span></li><li><span><b>Officina dell'Automazione</b>a sud-ovest</span></li><li><span><b>Archivio Progetti</b>a sud-est</span></li><li><span><b>Ufficio Postale</b>appena a sud della piazza</span></li></ul><p>In mezzo alla piazza c'è un nodo. Prova a tagliarlo.</p>`},
knotCut:{eyebrow:"Piazza",title:"Il nodo tagliato",html:`<p class="headline">Sciogliamo <span>nodi.</span></p><p>Consulenza IT e automazione con l'intelligenza artificiale.</p>`},
knot:{eyebrow:"Piazza",title:"Il Nodo",html:`<p class="lead">Processi, sistemi e dati, tutti aggrovigliati.</p><p>Si possono passare mesi a scioglierlo, oppure lo si taglia con un colpo solo.</p><button class="pxbtn" id="cut-btn">Taglia il nodo</button>`}
},
en:{
casa:{eyebrow:"About us",title:"The Base",html:`<p class="lead">CuttingKnots is an IT consulting and AI automation company.</p><p>We take a tangled problem, look at it closely and solve it with one clean intervention.</p><dl class="facts"><div><dt>Founders</dt><dd>Luca, Luca and Antonio</dd></div><div><dt>For</dt><dd>SMEs and company teams with processes to simplify</dd></div><div><dt>How</dt><dd>Analysis, prototype, production</dd></div></dl>`},
torre:{eyebrow:"IT consulting",title:"Consulting Tower",html:`<p class="lead">From up here you can see the whole system. That's where we start.</p><ul class="list"><li><span><b>Solution architecture</b>How applications, data and people connect, before any code is written.</span></li><li><span><b>Low-code development</b>Business applications on platforms such as Mendix, in weeks.</span></li><li><span><b>Modernisation</b>Legacy software moved onto foundations you can maintain.</span></li><li><span><b>Regulated sectors</b>Experience on banking and finance projects.</span></li></ul>`},
officina:{eyebrow:"AI automation",title:"Automation Workshop",html:`<p class="lead">This is where we build the tools that do the work for you.</p><ul class="list"><li><span><b>AI agents and assistants</b>They read documents, email and data and draft replies and summaries.</span></li><li><span><b>Process automation</b>Invoices, reports and requests become automatic flows.</span></li><li><span><b>AI in your systems</b>Models connected to the tools you already use, via APIs and MCP servers.</span></li><li><span><b>Training</b>Your team learns to use these tools safely.</span></li></ul>`},
archivio:{eyebrow:"Projects",title:"Project Archive",html:`<p class="lead">Every project is a knot that got cut.</p><div class="cases"><article class="case"><span class="tag">Example</span><h3>Customer requests routed by an assistant</h3><p class="knot-line">Knot: 40 emails a day sorted by hand</p></article><article class="case"><span class="tag">Example</span><h3>Monthly report without copy-paste</h3><p class="knot-line">Knot: two working days every month</p></article><article class="case"><span class="tag">Example</span><h3>Low-code app for an operations office</h3><p class="knot-line">Knot: different versions of the same data</p></article></div>`},
posta:{eyebrow:"Contact",title:"Post Office",html:`<p class="lead">Got a knot to untie? Tell us in a few lines.</p><div class="mail"><span class="addr">info@cuttingknots.com</span><button class="pxbtn small" data-copy="info@cuttingknots.com">Copy address</button></div><p>We reply within two working days.</p>`},
bit:{eyebrow:"Guide",title:"Bit",html:`<p class="lead">Hi, I'm Bit. You found the secret CuttingKnots village.</p><p>Each building tells part of our story. Walk up to a door and interact to go in.</p><ul class="list compact"><li><span><b>The Base</b>about us, to the north-west</span></li><li><span><b>Consulting Tower</b>north-east, past the lake</span></li><li><span><b>Automation Workshop</b>to the south-west</span></li><li><span><b>Project Archive</b>to the south-east</span></li><li><span><b>Post Office</b>just south of the square</span></li></ul><p>There's a knot in the middle of the square. Try cutting it.</p>`},
knotCut:{eyebrow:"Square",title:"The cut knot",html:`<p class="headline">We cut <span>knots.</span></p><p>IT consulting and automation with artificial intelligence.</p>`},
knot:{eyebrow:"Square",title:"The Knot",html:`<p class="lead">Processes, systems and data, all tangled up.</p><p>You can spend months untying it, or cut it in one stroke.</p><button class="pxbtn" id="cut-btn">Cut the knot</button>`}
}}[LANG];
const SECTIONS=SEC;
const knotSection=()=>cut?SEC.knotCut:SEC.knot;
const NAMES={it:{casa:"La Base",torre:"Torre della Consulenza",officina:"Officina dell'Automazione",archivio:"Archivio Progetti",posta:"Ufficio Postale"},
 en:{casa:"The Base",torre:"Consulting Tower",officina:"Automation Workshop",archivio:"Project Archive",posta:"Post Office"}}[LANG];

/* ---------- world ---------- */
const T=16,MW=48,MH=36;
const GROUND=0,PATH=1,TREE=2,BUILD=3,PLAZA=4,WATER=5,FLOWER=6;
const C={bg:"#0B1216",g1:"#18222A",g2:"#1D2932",g3:"#23313B",path:"#33404C",pathHi:"#3D4B58",pathDk:"#2A3540",
 plaza:"#2E3944",plazaDk:"#232D36",plazaHi:"#3A4652",water:"#132A3A",waterHi:"#2D5068",waterEdge:"#0D1E2A",
 tree:"#1F3A35",treeHi:"#2C5048",treeDk:"#152A26",trunk:"#3A2C25",shadow:"#0C1418",
 wall:"#2C3843",wallLine:"#26313B",roof:"#0F151B",roofLine:"#1D2731",win:"#FFB48F",winOff:"#3A4652",
 ink:"#0F151B",slate:"#5B6670",mist:"#F2F3F5",orange:"#FD3F03",orangeDk:"#7A2002",skin:"#F0C9A8",stone:"#46535F",stoneDk:"#323E4A",line:"#2E3A46"};
const B=[
 {id:"casa",name:"La Base",x:5,y:5,w:8,h:6,style:"house"},
 {id:"torre",name:"Torre della Consulenza",x:36,y:3,w:6,h:8,style:"tower"},
 {id:"officina",name:"Officina dell'Automazione",x:4,y:23,w:10,h:6,style:"workshop"},
 {id:"archivio",name:"Archivio Progetti",x:34,y:23,w:9,h:6,style:"archive"},
 {id:"posta",name:"Ufficio Postale",x:20,y:23,w:8,h:6,style:"post"}
];
B.forEach(b=>{b.name=NAMES[b.id];b.dx=b.x+Math.floor(b.w/2);b.fy=b.y+b.h});
const map=new Uint8Array(MW*MH),solid=new Uint8Array(MW*MH);
const idx=(x,y)=>y*MW+x,inMap=(x,y)=>x>=0&&y>=0&&x<MW&&y<MH;
const getT=(x,y)=>inMap(x,y)?map[idx(x,y)]:TREE,setT=(x,y,v)=>{if(inMap(x,y))map[idx(x,y)]=v};
function rng(seed){return()=>{seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function hash(x,y){let h=Math.imul(x,374761393)+Math.imul(y,668265263)|0;h=Math.imul(h^(h>>>13),1274126177);return(h^(h>>>16))>>>0}
function carve(x1,y1,x2,y2){for(let x=Math.min(x1,x2);x<=Math.max(x1,x2)+1;x++)for(let y=Math.min(y1,y2);y<=Math.max(y1,y2)+1;y++)if(getT(x,y)!==BUILD)setT(x,y,PATH)}
(function build(){
 const r=rng(7);
 for(let y=0;y<MH;y++)for(let x=0;x<MW;x++)setT(x,y,(x<2||y<2||x>=MW-2||y>=MH-2)?TREE:GROUND);
 for(let y=0;y<MH;y++)for(let x=0;x<MW;x++){const a=(x-24)/6.2,b=(y-6.5)/2.9;if(a*a+b*b<=1)setT(x,y,WATER)}
 B.forEach(b=>{for(let y=b.y;y<b.y+b.h;y++)for(let x=b.x;x<b.x+b.w;x++)setT(x,y,BUILD)});
 carve(9,17,40,17);carve(9,30,40,30);carve(17,17,17,30);carve(30,17,30,30);
 B.forEach(b=>carve(b.dx,b.fy,b.dx,b.y<17?17:30));
 for(let y=0;y<MH;y++)for(let x=0;x<MW;x++){const dx=x-23.5,dy=y-16.5;if(dx*dx+dy*dy<=4.8*4.8)setT(x,y,PLAZA)}
 for(let y=2;y<MH-2;y++)for(let x=2;x<MW-2;x++){
  if(getT(x,y)!==GROUND)continue;
  let clear=true;for(let j=-1;j<=1;j++)for(let i=-1;i<=1;i++){const v=getT(x+i,y+j);if(v!==GROUND&&v!==TREE)clear=false}
  const v=r();if(clear&&v<0.1)setT(x,y,TREE);else if(v>0.94)setT(x,y,FLOWER);
 }
 for(let i=0;i<MW*MH;i++){const v=map[i];solid[i]=(v===TREE||v===BUILD||v===WATER)?1:0}
 solid[idx(23,16)]=solid[idx(24,16)]=solid[idx(23,17)]=solid[idx(24,17)]=1;
 solid[idx(21,20)]=1;
})();
const BIT={x:21*T+8,y:21*T-2},KNOT={x:24*T,y:18*T+4};
const P={x:24*T+8,y:21*T+10,dir:"up",walk:0,moving:false};

/* ---------- state ---------- */
let visited=new Set(),cut=false,completeShown=false;
try{const s=JSON.parse(localStorage.getItem("ck-village")||"{}");visited=new Set(s.visited||[]);cut=!!s.cut;completeShown=!!s.done}catch(e){}
const save=()=>{try{localStorage.setItem("ck-village",JSON.stringify({visited:[...visited],cut,done:completeShown}))}catch(e){}};
const reduced=matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- views ---------- */
let ctx,cw=0,ch=0,vt=null,heroMode=false,t=0,cutting=false,cutStart=0,target=null;
const howto=$("howto"),dlg=$("dialog");
const GV=GAME_EL?{cv:$("world")}:null,HV=HERO_CV?{cv:HERO_CV}:null;
if(GV)GV.ctx=GV.cv.getContext("2d");if(HV)HV.ctx=HV.cv.getContext("2d");
function setCanvas(v,w,h,s){v.s=s;v.w=Math.ceil(w/s);v.h=Math.ceil(h/s);v.cv.width=v.w;v.cv.height=v.h;v.cv.style.width=v.w*s+"px";v.cv.style.height=v.h*s+"px"}
function sizeGame(){const w=innerWidth,h=innerHeight;setCanvas(GV,w,h,Math.max(2,Math.min(4,Math.floor(Math.min(w/(T*15),h/(T*11)))||2)))}
function sizeHero(){const r=HV.cv.parentElement.getBoundingClientRect();if(!r.width)return;setCanvas(HV,r.width,r.height,Math.max(2,Math.floor(r.width/(T*14))))}
let heroVisible=true;
if(HV){
 sizeHero();addEventListener("resize",sizeHero);
 if("ResizeObserver" in window)new ResizeObserver(sizeHero).observe(HV.cv.parentElement);
 if("IntersectionObserver" in window)new IntersectionObserver(es=>{heroVisible=es[0].isIntersecting}).observe(HV.cv.parentElement);
}
if(GV){sizeGame();addEventListener("resize",sizeGame)}

const px=(x,y,w,h,c)=>{ctx.fillStyle=c;ctx.fillRect(x|0,y|0,w|0,h|0)};
function rasterize(d,color,size){
 const h=Math.round(size*248/292),c=document.createElement("canvas");c.width=size;c.height=h;
 const g=c.getContext("2d"),s=size/292;g.setTransform(s,0,0,s,-7*s,-6*s);g.fillStyle=color;g.fill(new Path2D(d));
 const im=g.getImageData(0,0,size,h);for(let i=3;i<im.data.length;i+=4)im.data[i]=im.data[i]>100?255:0;g.putImageData(im,0,0);return c;
}
const KS=40,knotImg=rasterize(KNOT_D,"#F2F3F5",KS),cutImg=rasterize(CUT_D,"#FD3F03",KS),KH=knotImg.height;

/* ---------- drawing ---------- */
function ground(sx,sy,h){px(sx,sy,T,T,C.g1);if(h%4===0)px(sx+(h>>5)%13,sy+(h>>9)%13,2,1,C.g2);
 if(h%6===1){const ax=sx+(h>>3)%11+1,ay=sy+(h>>11)%10+3;px(ax,ay,1,2,C.g3);px(ax+2,ay-1,1,3,C.g3);px(ax+4,ay,1,2,C.g3)}}
function drawTile(x,y){
 const v=map[idx(x,y)],sx=x*T,sy=y*T,h=hash(x,y);
 if(v===GROUND||v===FLOWER){ground(sx,sy,h);if(v===FLOWER){
   const fx=sx+(h>>4)%9+3,fy=sy+(h>>12)%9+4,c=h%5===0?C.orange:(h%2?C.mist:C.slate);
   px(fx,fy-1,1,1,c);px(fx-1,fy,3,1,c);px(fx,fy+1,1,1,c);px(fx,fy+2,1,2,C.treeHi);
   const gx=sx+(h>>7)%9+2,gy=sy+(h>>15)%6+2;px(gx,gy,1,1,C.slate);px(gx,gy+1,1,2,C.treeHi)}}
 else if(v===PATH){px(sx,sy,T,T,C.path);if(h%3===0)px(sx+(h>>4)%12+1,sy+(h>>8)%12+1,3,2,C.pathHi);if(h%5===1)px(sx+(h>>6)%13,sy+(h>>10)%13,2,1,C.pathDk)}
 else if(v===PLAZA){px(sx,sy,T,T,C.plaza);px(sx,sy,T,1,C.plazaDk);px(sx,sy+8,T,1,C.plazaDk);
   px(sx+(y%2?4:12),sy,1,8,C.plazaDk);px(sx+(y%2?12:4),sy+8,1,8,C.plazaDk);px(sx+1+(y%2?4:0),sy+2,2,1,C.plazaHi)}
 else if(v===WATER){px(sx,sy,T,T,C.water);if(getT(x,y-1)!==WATER)px(sx,sy,T,2,C.waterEdge);
   const k=reduced?h%6:(Math.floor(t*1.6)+x*2+y*3)%7;if(k<2)px(sx+(h%7)+1,sy+5+k*5,5,1,C.waterHi)}
 else if(v===TREE){ground(sx,sy,h);const o=(h%3)-1;
   px(sx+3,sy+13,10,2,C.shadow);px(sx+7,sy+10,2,4,C.trunk);
   px(sx+3+o,sy+2,10,8,C.tree);px(sx+2+o,sy+4,12,5,C.tree);px(sx+5+o,sy+1,6,1,C.tree);
   px(sx+5+o,sy+3,4,2,C.treeHi);px(sx+4+o,sy+8,8,2,C.treeDk)}
 else if(v===BUILD)px(sx,sy,T,T,C.g1);
}
function windowAt(x,y,lit){px(x-1,y-1,10,10,C.ink);px(x,y,8,8,lit?C.win:C.winOff);px(x+3,y,2,8,C.ink);px(x,y+3,8,2,C.ink)}
function drawBuilding(b){
 const bx=b.x*T,by=b.y*T,bw=b.w*T,bh=b.h*T,roofH=2*T,wy=by+roofH,near=vt&&vt.b===b;
 const flick=i=>reduced||((Math.floor(t*0.5)+i*3+b.x)%11)!==0;
 px(bx+3,by+bh,bw,3,C.shadow);px(bx,wy,bw,bh-roofH,C.wall);
 for(let y=wy+5;y<by+bh;y+=6)px(bx,y,bw,1,C.wallLine);
 px(bx,by+bh-2,bw,2,C.roofLine);
 const doorX=b.dx*T;
 if(b.style==="house"){
  px(bx+bw-22,by-8,8,12,C.wall);px(bx+bw-23,by-9,10,2,C.slate);
  px(bx-3,by+2,bw+6,roofH-2,C.roof);for(let y=by+6;y<wy;y+=5)px(bx-3,y,bw+6,1,C.roofLine);px(bx-3,by,bw+6,3,C.orange);
  [[bx+12,0],[bx+28,1],[bx+bw-36,2],[bx+bw-20,3]].forEach(([x,i])=>windowAt(x,wy+14,flick(i)));
 }else if(b.style==="tower"){
  px(bx-2,by,bw+4,roofH,C.roof);px(bx-2,by,bw+4,2,C.slate);for(let x=bx-2;x<bx+bw+2;x+=8)px(x,by-4,4,4,C.roof);
  px(bx+bw/2-1,by-18,2,14,C.slate);px(bx+bw/2-2,by-21,4,4,(reduced||Math.floor(t*1.5)%2)?C.orange:C.orangeDk);
  for(let r=0;r<4;r++)for(let c=0;c<3;c++){if(r===3&&c===1)continue;windowAt(bx+10+c*28,wy+8+r*20,flick(r*3+c))}
 }else if(b.style==="workshop"){
  px(bx,by+8,bw,roofH-8,C.roof);
  for(let s=bx;s<bx+bw;s+=20){for(let k=0;k<10;k++)px(s,by+8-k,20-k*2,1,C.roof);px(s+19,by,1,9,C.slate);px(s+1,by+9,16,1,C.roofLine)}
  px(bx,wy-2,bw,2,C.orange);
  px(bx+12,wy+18,40,bh-roofH-20,C.ink);for(let y=wy+20;y<by+bh-2;y+=4)px(bx+12,y,40,1,C.pathDk);
  windowAt(bx+bw-40,wy+14,flick(1));windowAt(bx+bw-22,wy+14,flick(2));
  const gx=bx+32,gy=wy+8,c=reduced?0:Math.floor(t*4)%2;px(gx-3,gy-3,6,6,C.slate);px(gx-1,gy-5,2,10,C.slate);px(gx-5,gy-1,10,2,C.slate);px(gx-1,gy-1,2,2,c?C.orange:C.ink);
 }else if(b.style==="archive"){
  const W=bw+8;for(let r=0;r<roofH;r++){const inset=Math.floor((roofH-1-r)*(W/2)/roofH);px(bx-4+inset,by+r,W-inset*2,1,r%5===0?"#7E8893":"#9AA3AC")}
  px(bx-4,wy-3,bw+8,3,C.slate);
  for(let x=bx+6;x<bx+bw-6;x+=18){if(Math.abs(x+3-(doorX+8))<12)continue;px(x,wy+2,7,bh-roofH-4,"#8A949E");px(x+1,wy+2,1,bh-roofH-4,"#AEB6BE");px(x-1,wy,9,3,"#AEB6BE")}
  px(bx+bw/2-6,by+roofH-12,12,6,C.ink);px(bx+bw/2-4,by+roofH-11,8,1,C.orange);px(bx+bw/2-4,by+roofH-9,6,1,C.slate);
 }else if(b.style==="post"){
  px(bx-2,by+2,bw+4,roofH-2,C.roof);for(let y=by+7;y<wy;y+=5)px(bx-2,y,bw+4,1,C.roofLine);px(bx-2,wy-5,bw+4,4,C.orange);
  windowAt(bx+12,wy+14,flick(0));windowAt(bx+bw-20,wy+14,flick(1));
  px(bx+bw/2-8,by+8,16,11,C.mist);px(bx+bw/2-8,by+8,16,1,C.slate);for(let k=0;k<6;k++){px(bx+bw/2-7+k,by+9+k,1,1,C.slate);px(bx+bw/2+6-k,by+9+k,1,1,C.slate)}
  const mx=doorX+28,my=by+bh;px(mx+2,my-4,2,8,C.slate);px(mx-1,my-14,9,10,C.orange);px(mx-1,my-14,9,2,"#FF7A4D");px(mx+1,my-9,5,1,C.ink);
 }
 const fc=near?C.orange:C.slate;
 px(doorX+2,by+bh-17,12,1,fc);px(doorX+1,by+bh-17,1,17,fc);px(doorX+14,by+bh-17,1,17,fc);
 px(doorX+2,by+bh-16,12,16,C.ink);px(doorX+11,by+bh-8,1,1,C.mist);px(doorX,by+bh,16,2,"#3A4652");
}
function drawLabel(b){
 ctx.font='10px "Pixelify Sans",monospace';const vis=!heroMode&&visited.has(b.id);
 const tw=Math.ceil(ctx.measureText(b.name).width),w=tw+10+(vis?6:0),cx=b.x*T+b.w*T/2,top=b.y*T-(b.style==="tower"?36:b.style==="house"?24:16);
 const lx=Math.round(cx-w/2);px(lx,top,w,13,"rgba(15,21,27,.88)");px(lx,top+12,w,1,vis?C.orange:C.slate);
 if(vis)px(lx+5,top+5,3,3,C.orange);ctx.fillStyle=C.mist;ctx.textBaseline="alphabetic";ctx.fillText(b.name,lx+5+(vis?6:0),top+10);
}
function drawPlayer(){
 const x=Math.round(P.x),y=Math.round(P.y),f=P.moving?Math.floor(P.walk*8)%2:0,lift=P.moving&&f?1:0;
 px(x-5,y-1,10,2,C.shadow);
 if(f){px(x-3,y-3,2,2,C.slate);px(x+1,y-2,2,2,C.slate);px(x-3,y-1,2,1,C.ink);px(x+1,y,2,1,C.ink)}
 else{px(x-3,y-2,2,2,C.slate);px(x+1,y-2,2,2,C.slate);px(x-3,y,2,1,C.ink);px(x+1,y,2,1,C.ink)}
 const by=y-lift;
 px(x-5,by-8,10,6,C.mist);px(x-5,by-8,10,1,"#C9D0D6");px(x-5,by-3,10,1,"#C9D0D6");
 if(P.dir!=="up"){const l=P.dir==="left";px(x+(l?-3:0),by-7,1,1,C.orange);px(x+(l?-2:1),by-6,1,1,C.orange);px(x+(l?-1:2),by-5,1,1,C.orange)}
 px(x-4,by-14,8,6,C.skin);px(x-4,by-15,8,3,C.ink);
 if(P.dir==="up")px(x-4,by-13,8,4,C.ink);
 else if(P.dir==="down"){px(x-4,by-13,1,2,C.ink);px(x+3,by-13,1,2,C.ink);px(x-2,by-11,1,2,C.ink);px(x+1,by-11,1,2,C.ink)}
 else if(P.dir==="left"){px(x,by-13,4,3,C.ink);px(x-3,by-11,1,2,C.ink)}
 else{px(x-4,by-13,4,3,C.ink);px(x+2,by-11,1,2,C.ink)}
 if(vt){const b2=reduced?0:Math.round(Math.sin(t*6));px(x-1,by-24+b2,2,5,C.orange);px(x-1,by-18+b2,2,2,C.orange)}
}
function drawBit(){
 const x=BIT.x,y=BIT.y,b=reduced?0:(Math.sin(t*3)>0?1:0);
 px(x-5,y-1,10,2,C.shadow);px(x-3,y-3,6,2,C.line);
 px(x-4,y-9-b,8,6,C.slate);px(x-3,y-8-b,6,1,"#7A8590");px(x-6,y-8-b,2,4,C.slate);px(x+4,y-8-b,2,4,C.slate);
 px(x-4,y-15-b,8,6,"#C9D0D6");px(x-3,y-13-b,6,3,C.ink);
 if(reduced||Math.floor(t*1.3)%5!==0){px(x-2,y-12-b,1,1,C.orange);px(x+1,y-12-b,1,1,C.orange)}
 px(x,y-18-b,1,3,C.slate);px(x-1,y-20-b,3,2,(reduced||Math.floor(t*2)%2)?C.orange:C.orangeDk);
}
function drawMonument(){
 const x=23*T,y=16*T;
 px(x,y+31,32,2,C.shadow);px(x+1,y+16,30,16,C.stoneDk);px(x+1,y+12,30,5,C.stone);px(x+1,y+12,30,1,C.slate);
 px(x+5,y+21,22,1,"#3A4652");px(x+5,y+26,22,1,"#3A4652");
 const bob=reduced?0:Math.round(Math.sin(t*2)),kx=KNOT.x-KS/2,ky=y+11-KH+bob;
 if(vt&&vt.kind==="knot")px(kx+6,y+13,KS-12,2,C.orange);
 ctx.drawImage(knotImg,kx,ky);
 let p;
 if(heroMode){const ph=(t%6)/6;p=reduced?1:ph<0.4?0:Math.min(1,(ph-0.4)/0.08)}
 else p=cut?1:cutting?Math.min(1,(t-cutStart)/0.45):0;
 if(p>0){const w=Math.ceil(KS*p);ctx.drawImage(cutImg,KS-w,0,w,KH,kx+KS-w,ky,w,KH)}
}
let parts=[];
function burst(){for(let i=0;i<40;i++){const a=Math.random()*Math.PI*2,s=30+Math.random()*90;parts.push({x:KNOT.x,y:KNOT.y-28,vx:Math.cos(a)*s,vy:Math.sin(a)*s-40,life:0.8+Math.random()*0.7,c:i%3?C.orange:C.mist})}}

function renderView(v,camX,camY){
 ctx=v.ctx;cw=v.w;ch=v.h;ctx.imageSmoothingEnabled=false;
 px(0,0,cw,ch,C.bg);
 ctx.save();ctx.translate(-camX,-camY);
 const x0=Math.max(0,Math.floor(camX/T)),x1=Math.min(MW-1,Math.floor((camX+cw)/T)),y0=Math.max(0,Math.floor(camY/T)),y1=Math.min(MH-1,Math.floor((camY+ch)/T));
 for(let y=y0;y<=y1;y++)for(let x=x0;x<=x1;x++)drawTile(x,y);
 const objs=B.map(b=>({y:(b.y+b.h)*T,d:()=>drawBuilding(b)}));
 objs.push({y:P.y,d:drawPlayer},{y:BIT.y,d:drawBit},{y:18*T,d:drawMonument});
 objs.sort((a,b)=>a.y-b.y).forEach(o=>o.d());
 if(!heroMode)parts.forEach(p=>px(p.x,p.y,2,2,p.c));
 B.forEach(drawLabel);
 ctx.restore();
}
const clampCam=(c,size,view)=>size<=view?Math.round((size-view)/2):Math.round(Math.max(0,Math.min(size-view,c)));

/* hero attract camera: drifts between landmarks */
const WAY=[[24*T,15*T],[10*T,10*T],[24*T,7*T],[39*T,9*T],[38*T,26*T],[24*T,27*T],[9*T,26*T],[18*T,19*T]];
function heroCam(){
 const seg=5,i=Math.floor(t/seg)%WAY.length,f=(t%seg)/seg,a=WAY[i],b=WAY[(i+1)%WAY.length];
 let k=reduced?0:Math.max(0,(f-0.45)/0.55);k=k*k*(3-2*k);
 return[a[0]+(b[0]-a[0])*k,a[1]+(b[1]-a[1])*k];
}

/* ---------- input (village page) ---------- */
const keys={up:false,down:false,left:false,right:false};let run=false;
const MOVE={ArrowUp:"up",w:"up",W:"up",ArrowDown:"down",s:"down",S:"down",ArrowLeft:"left",a:"left",A:"left",ArrowRight:"right",d:"right",D:"right"};
const dlgOpen=()=>!!dlg&&!dlg.hidden;
const clearKeys=()=>{for(const k in keys)keys[k]=false;run=false;document.querySelectorAll(".dpad .held").forEach(b=>b.classList.remove("held"))};
function exitGame(){let to=L.home;try{const r=new URL(document.referrer);if(r.origin===location.origin&&!/villag/.test(r.pathname))to=r.pathname.split("/").pop()||"index.html"}catch(e){}location.href=to}
function openHowto(){clearKeys();howto.hidden=false;$("howto-go").focus({preventScroll:true})}
function closeHowto(){howto.hidden=true}
if(GAME_EL){
 document.body.classList.add("in-game");
 addEventListener("keydown",e=>{
  const k=e.key;
  if(!howto.hidden){if(k==="Escape"||MOVE[k]){e.preventDefault();closeHowto()}return}
  if(dlgOpen()){if(k==="Escape"||k==="e"||k==="E"){e.preventDefault();closeDialog()}return}
  if(k==="Escape"){exitGame();return}
  if(MOVE[k]){keys[MOVE[k]]=true;e.preventDefault()}
  if(k==="Shift")run=true;
  if(k==="e"||k==="E"||k==="Enter"||k===" "){e.preventDefault();interact()}
 });
 addEventListener("keyup",e=>{if(MOVE[e.key])keys[MOVE[e.key]]=false;if(e.key==="Shift")run=false});
 addEventListener("blur",clearKeys);
 const enableTouch=()=>{document.body.classList.add("touch");$("prompt-key").textContent="A";$("ctrl-keys").hidden=true;$("ctrl-touch").hidden=false};
 if(matchMedia("(pointer: coarse)").matches)enableTouch();
 addEventListener("touchstart",enableTouch,{once:true,passive:true});
 document.querySelectorAll(".dpad button").forEach(btn=>{
  const d=btn.dataset.dir,on=e=>{e.preventDefault();keys[d]=true;btn.classList.add("held")},off=()=>{keys[d]=false;btn.classList.remove("held")};
  btn.addEventListener("pointerdown",on);["pointerup","pointerleave","pointercancel"].forEach(ev=>btn.addEventListener(ev,off));
  btn.addEventListener("contextmenu",e=>e.preventDefault());
 });
 $("btn-a").addEventListener("pointerdown",e=>{e.preventDefault();if(dlgOpen())closeDialog();else interact()});
 $("howto-go").addEventListener("click",closeHowto);
 $("howto-open").addEventListener("click",openHowto);
 $("exit-game").addEventListener("click",e=>{e.preventDefault();exitGame()});
 const b=B.find(x=>x.id===location.hash.slice(1));if(b){P.x=b.dx*T+8;P.y=(b.fy+1)*T+2;P.dir="up"}
 setTimeout(()=>{updateHud();openHowto()},0);
}

/* ---------- interaction ---------- */
function findTarget(){
 let best=null,bd=1e9;const fx=P.x,fy=P.y-3;
 const consider=(o,x,y,r)=>{const d=Math.hypot(fx-x,fy-y);if(d<r&&d<bd){bd=d;best=o}};
 B.forEach(b=>consider({kind:"door",b,id:b.id,label:L.enter+b.name},b.dx*T+8,b.fy*T+6,16));
 consider({kind:"npc",id:"bit",label:L.talk},BIT.x,BIT.y+4,22);
 consider({kind:"knot",id:"knot",label:cut?L.look:L.cut},KNOT.x,KNOT.y+6,24);
 return best;
}
function interact(){if(target)openDialog(target.id)}
function openDialog(id){
 clearKeys();const s=id==="knot"?knotSection():SECTIONS[id];
 $("dlg-eyebrow").textContent=s.eyebrow;$("dlg-title").textContent=s.title;$("dlg-body").innerHTML=s.html;
 dlg.hidden=false;dlg.scrollTop=0;
 const cb=$("cut-btn");if(cb)cb.addEventListener("click",()=>{closeDialog();startCut()});
 (cb||$("dlg-close")).focus({preventScroll:true});
 if(B.some(b=>b.id===id)&&!visited.has(id)){visited.add(id);save();updateHud()}
}
function closeDialog(silent){if(dlg.hidden)return;dlg.hidden=true;if(!silent)checkComplete()}
if(GAME_EL)$("dlg-close").addEventListener("click",()=>closeDialog());
function startCut(){
 if(cut||cutting)return;cutting=true;cutStart=t;
 if(!reduced){const f=$("flash");f.classList.add("on");requestAnimationFrame(()=>requestAnimationFrame(()=>f.classList.remove("on")))}
 burst();
 setTimeout(()=>{cutting=false;cut=true;save();const bn=$("banner");bn.classList.add("show");setTimeout(()=>bn.classList.remove("show"),3200);checkComplete()},460);
}
let toastTimer;
function toast(msg){const el=$("toast");el.textContent=msg;el.hidden=false;clearTimeout(toastTimer);toastTimer=setTimeout(()=>el.hidden=true,4500)}
function checkComplete(){if(!completeShown&&cut&&visited.size===B.length){completeShown=true;save();toast(L.done)}}

/* ---------- HUD ---------- */
function updateHud(){$("count").textContent=visited.size;[...$("pips").children].forEach((p,i)=>p.classList.toggle("on",i<visited.size))}
const mm=GAME_EL?$("minimap").getContext("2d"):null;
const MMC={[GROUND]:"#1D2932",[FLOWER]:"#1D2932",[PATH]:"#3D4B58",[TREE]:"#1F3A35",[PLAZA]:"#4A5763",[WATER]:"#1F4058",[BUILD]:"#5B6670"};
function drawMinimap(){
 for(let y=0;y<MH;y++)for(let x=0;x<MW;x++){mm.fillStyle=MMC[map[idx(x,y)]];mm.fillRect(x*2,y*2,2,2)}
 B.forEach(b=>{if(visited.has(b.id)){mm.fillStyle=C.orange;mm.fillRect(b.x*2,b.y*2,b.w*2,b.h*2)}});
 mm.fillStyle=cut?C.orange:C.mist;mm.fillRect(47,33,2,2);
 if(reduced||Math.floor(t*3)%2){mm.fillStyle=C.mist;mm.fillRect(Math.floor(P.x/T)*2-1,Math.floor(P.y/T)*2-1,3,3)}
}

/* ---------- loop ---------- */
function blocked(x,y){
 const s=(a,b)=>{const tx=Math.floor(a/T),ty=Math.floor(b/T);return!inMap(tx,ty)||solid[idx(tx,ty)]===1};
 return s(x-4,y-5)||s(x+4,y-5)||s(x-4,y)||s(x+4,y);
}
function update(dt){
 const paused=dlgOpen()||!howto.hidden;
 let mx=0,my=0;
 if(!paused){if(keys.left)mx--;if(keys.right)mx++;if(keys.up)my--;if(keys.down)my++}
 P.moving=!!(mx||my);
 if(P.moving){
  if(mx&&my){mx*=0.7071;my*=0.7071}
  const sp=(run?118:72)*dt;
  P.dir=my<0&&Math.abs(my)>=Math.abs(mx)?"up":my>0&&Math.abs(my)>=Math.abs(mx)?"down":mx<0?"left":"right";
  if(!blocked(P.x+mx*sp,P.y))P.x+=mx*sp;
  if(!blocked(P.x,P.y+my*sp))P.y+=my*sp;
  P.walk+=dt*(run?1.5:1);
 }
 target=paused?null:findTarget();
 const pr=$("prompt");if(target){$("prompt-text").textContent=target.label;pr.hidden=false}else pr.hidden=true;
 parts=parts.filter(p=>(p.life-=dt)>0);parts.forEach(p=>{p.x+=p.vx*dt;p.y+=p.vy*dt;p.vy+=140*dt});
}
let last=performance.now();
function loop(now){
 const dt=Math.min(0.05,(now-last)/1000);last=now;t+=dt;
 if(GV){
  update(dt);heroMode=false;vt=target;
  renderView(GV,clampCam(P.x-GV.w/2,MW*T,GV.w),clampCam(P.y-8-GV.h/2,MH*T,GV.h));
  drawMinimap();
 }else if(HV&&heroVisible&&HV.w){
  heroMode=true;vt=null;const[cx,cy]=heroCam();
  renderView(HV,clampCam(cx-HV.w/2,MW*T,HV.w),clampCam(cy-HV.h/2,MH*T,HV.h));
 }
 requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
document.fonts&&document.fonts.load('10px "Pixelify Sans"').catch(()=>{});
})();
