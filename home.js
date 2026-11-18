(function(){
  var root=document.documentElement;
  /* theme toggle (remembered per viewer when storage is available) */
  try{var t=localStorage.getItem('ck-theme');if(t==='dark'||t==='light')root.setAttribute('data-theme',t)}catch(e){}
  document.querySelectorAll('[data-theme-toggle]').forEach(function(b){b.addEventListener('click',function(){
    var cur=root.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
    var next=cur==='dark'?'light':'dark';root.setAttribute('data-theme',next);try{localStorage.setItem('ck-theme',next)}catch(e){}
  })});
  /* phone menu */
  var mb=document.getElementById('menu-btn'),sheet=document.getElementById('sheet');
  function setMenu(o){sheet.hidden=!o;mb.setAttribute('aria-expanded',String(o));mb.setAttribute('aria-label',o?'Chiudi il menu':'Apri il menu');document.body.style.overflow=o?'hidden':''}
  mb.addEventListener('click',function(){setMenu(sheet.hidden)});
  sheet.addEventListener('click',function(e){if(e.target.closest('a'))setMenu(false)});
  addEventListener('keydown',function(e){if(e.key==='Escape'&&!sheet.hidden){setMenu(false);mb.focus()}});
  /* copy address */
  var cb=document.getElementById('copy'),cs=document.getElementById('copy-status');
  cb.addEventListener('click',function(){var done=function(t){cb.textContent=t;cs.textContent=t;setTimeout(function(){cb.textContent="Copia l'indirizzo";cs.textContent=''},2200)};
    try{navigator.clipboard.writeText('info@cuttingknots.com').then(function(){done('Copiato')},function(){sel()})}catch(e){sel()}
    function sel(){var r=document.createRange();r.selectNodeContents(document.querySelector('.mail'));var s=getSelection();s.removeAllRanges();s.addRange(r);done('Indirizzo selezionato')}
  });

  /* the scene: everything is driven by scroll position */
  var scene=document.querySelector('.scene'),sym=document.getElementById('sym'),cutp=document.getElementById('cutp'),bar=document.getElementById('bar');
  var th=['t1','t2','t3','t4'].map(function(i){return document.getElementById(i)}),tl=document.getElementById('tl'),hint=document.getElementById('hint');
  var P0=[19,246],N=[0.6563,0.7551],D=[0.7548,-0.6559],TIP=364.3,REACH=420;  /* the cut line, its normal and direction; TIP = far end of the bar along the cut */
  var clamp=function(v){return v<0?0:v>1?1:v},ease=function(t){return t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2};
  var RM=matchMedia('(prefers-reduced-motion: reduce)');
  function pt(a,s){return (P0[0]+D[0]*a+N[0]*s).toFixed(1)+','+(P0[1]+D[1]*a+N[1]*s).toFixed(1)}
  var ha=document.getElementById('ha'),hb=document.getElementById('hb');
  var out3=function(t){return 1-Math.pow(1-t,3)};
  function render(p){
    /* form 0–.24 · fast cut .27–.37 · halves kick apart and settle .33–.5 · threads .42–.62 */
    var form=out3(clamp(p/.24)),cut=out3(clamp((p-.27)/.10)),thr=clamp((p-.42)/.2);
    sym.style.setProperty('--draw',(1-form).toFixed(4));
    sym.style.setProperty('--fill',(.12+.88*clamp((form-.3)/.7)).toFixed(3));
    sym.style.setProperty('--olo',(1-clamp(cut*6)).toFixed(3));
    var b=REACH*(1-cut),tip=TIP-b;
    bar.setAttribute('transform','translate('+(-D[0]*b).toFixed(2)+','+(-D[1]*b).toFixed(2)+')');
    cutp.setAttribute('points',[pt(tip,-2000),pt(3000,-2000),pt(3000,2000),pt(tip,2000)].join(' '));
    var k=clamp((p-.33)/.17),g=7*Math.sin(Math.PI*k)*(1-k*.4);
    ha.setAttribute('transform','translate('+(-N[0]*g).toFixed(2)+','+(-N[1]*g).toFixed(2)+')');
    hb.setAttribute('transform','translate('+(N[0]*g).toFixed(2)+','+(N[1]*g).toFixed(2)+')');
    th.forEach(function(el,i){var v=clamp(thr*1.3-i*.1);el.style.strokeDashoffset=(100*(1-v)).toFixed(2);el.style.visibility=v>0?'visible':'hidden'});
    tl.style.setProperty('--labels',clamp((p-.56)/.08).toFixed(3));
    tl.style.pointerEvents=p>.6?'auto':'none';
    hint.style.setProperty('--hint',(1-clamp(p/.1)).toFixed(3));
  }
  var raf=0;
  function update(){raf=0;if(RM.matches){render(1);return}var r=scene.getBoundingClientRect(),total=scene.offsetHeight-innerHeight;render(total>0?clamp(-r.top/total):1)}
  addEventListener('scroll',function(){if(!raf)raf=requestAnimationFrame(update)},{passive:true});
  addEventListener('resize',update);
  if(RM.addEventListener)RM.addEventListener('change',update);
  update();
})();
