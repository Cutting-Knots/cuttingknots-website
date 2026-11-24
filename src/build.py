#!/usr/bin/env python3
"""Cutting Knots site generator.

Run from the repository root:  python3 src/build.py
Writes every page (Italian and English) into the repository root, plus
site.css / site.js (copied with a content hash), sitemap.xml and llms.txt.
The village pages (villaggio.html, village.html), game.css and ck.js are not touched.
"""
import hashlib, html, json, os, shutil
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')
SITE = 'https://www.cuttingknots.com'
EMAIL = 'info@cuttingknots.com'
LINKEDIN = 'https://www.linkedin.com/company/cutting-knots'
LASTMOD = '2026-11-18'
KN = json.load(open(os.path.join(SRC, 'knot.json')))
LOGO = open(os.path.join(SRC, 'logo.svg')).read()

# page key -> (Italian path, English path)
URL = {
    'home': ('/', '/en'),
    'enterprise': ('/enterprise', '/en/enterprise'),
    'consulting': ('/consulting', '/en/consulting'),
    'small': ('/small-solutions', '/en/small-solutions'),
    'prodotti': ('/prodotti', '/products'),
    'esperienze': ('/esperienze', '/experience'),
    'chi': ('/chi-siamo', '/about'),
    'contatti': ('/contatti', '/contact'),
    'villaggio': ('/villaggio', '/village'),
}
L = 'it'
def T(it, en): return it if L == 'it' else en
def u(key, lang=None): return URL[key][0 if (lang or L) == 'it' else 1]
def esc(s): return html.escape(s, quote=True)
def mailto(subject): return f'mailto:{EMAIL}?subject={quote(subject)}'
def hsh(path): return hashlib.sha1(open(path, 'rb').read()).hexdigest()[:8]

ARROW = '<svg aria-hidden="true" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
PLUS = '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>'
SUN = '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
MARK = f'<svg class="mark" aria-hidden="true" viewBox="0 0 310 260"><path class="k" d="{KN["REST"]}{KN["MID"]}"/><path class="c" d="{KN["CUT"]}"/></svg>'

# ------------------------------------------------------------------ shared data
def products():
    return [
        dict(id='forma', name='Forma Simplifier', logo='/img/forma-simplifier-negativo.svg', stage=3,
             cat=T('Ottimizzazione modelli 3D', '3D model optimisation'),
             former=T('Prima si chiamava 3D STEP Simplifier.', 'Formerly 3D STEP Simplifier.'),
             short=T('Modelli 3D STEP più leggeri, con forma e dimensioni intatte.', 'Lighter 3D STEP models, with shape and dimensions intact.'),
             img='/img/step-simplified.jpg', w=600, h=570, contain=True,
             alt=T('Modello 3D di un robot KUKA semplificato', 'Simplified 3D model of a KUKA robot'),
             cap=T('Test su un robot KUKA: da 55,98 a 3,21 MB', 'Test on a KUKA robot: 55.98 to 3.21 MB'),
             who=T('Uffici tecnici e commerciali che gestiscono librerie di modelli 3D, layout di offerta e scambio di file con clienti e fornitori.',
                   'Engineering and sales teams that manage 3D model libraries, quotation layouts and file exchange with clients and suppliers.'),
             problem=T('Modelli 3D troppo pesanti per librerie tecniche, layout di offerta e condivisione con clienti e fornitori.',
                       '3D models too heavy for technical libraries, quotation layouts and sharing with clients and suppliers.'),
             today=T('Semplifica la geometria dei file STEP ed esporta modelli più leggeri, mantenendo forma e dimensioni. In un test su un robot KUKA il file è passato da 55,98 a 3,21 MB.',
                     'It simplifies the geometry of STEP files and exports lighter models, keeping shape and dimensions. In one test on a KUKA robot the file went from 55.98 to 3.21 MB.'),
             next=T('Concludere la fase pilota prima del rilascio.', 'Complete the pilot before release.'),
             can=T('Raccontarci su quali modelli lavorate (dimensioni tipiche, uso): valutiamo insieme se il vostro caso si presta a una prova.',
                   "Tell us which models you work with (typical size, use): we'll assess together whether your case suits a trial."),
             cta=T('Chiedi informazioni', 'Ask for information'), subj=T('Forma Simplifier – richiesta informazioni', 'Forma Simplifier – information request')),
        dict(id='vigil', name='VIGIL', stage=2,
             cat=T('Computer vision industriale', 'Industrial computer vision'),
             short=T('Dai video delle linee a cicli, fermate e OEE.', 'From line video to cycles, stops and OEE.'),
             img='/img/vigil-dashboard.jpg', w=1200, h=713,
             alt=T('Interfaccia dimostrativa di VIGIL', 'VIGIL demo interface'),
             cap=T('Interfaccia dimostrativa, dati simulati', 'Demo interface, simulated data'),
             who=T('Responsabili di produzione e manutenzione che vogliono misurare cicli, fermate e OEE di linee e macchine.',
                   'Production and maintenance managers who want to measure cycles, stops and OEE on lines and machines.'),
             problem=T('Monitorare linee e macchine richiede dati affidabili su cicli, fermate, KPI e OEE. Individuare i segnali di deterioramento è ancora più complesso.',
                       'Monitoring lines and machines needs reliable data on cycles, stops, KPIs and OEE. Spotting early signs of wear is harder still.'),
             today=T("Esistono un'interfaccia dimostrativa, con dati simulati, e i test preliminari del motore di visione. Le funzioni predittive sono ancora da validare su impianti reali.",
                     'There is a demo interface, with simulated data, and preliminary tests of the vision engine. The predictive functions still have to be validated on real plants.'),
             next=T('Un test su una linea selezionata, con misure confrontate con riferimenti verificabili.', 'A test on a selected line, with measurements compared against verifiable references.'),
             can=T("Chiederci una dimostrazione dell'interfaccia, con dati simulati, o informazioni sulla validazione sul campo.",
                   'Ask us for a demo of the interface, with simulated data, or for information on field validation.'),
             cta=T('Chiedi una dimostrazione', 'Ask for a demo'), subj=T('VIGIL – richiesta dimostrazione', 'VIGIL – demo request'),
             img2='/img/vigil-detection.jpg', w2=1000, h2=750, cap2=T('Test preliminare: riconoscimento e conteggio sul nastro', 'Preliminary test: recognition and counting on the conveyor')),
        dict(id='aida', name='AIDA', stage=1,
             cat=T('Agenda e organizzazione', 'Planning and organisation'),
             short=T("Email, appunti e impegni trasformati nell'agenda della giornata.", 'Email, notes and appointments turned into a plan for the day.'),
             img='/img/aida-calendar.jpg', w=1200, h=596,
             alt=T('Calendario settimanale organizzato da AIDA', 'Weekly calendar organised by AIDA'),
             cap=T('Versione in sviluppo', 'Version in development'),
             who=T('Chi deve tenere insieme email, appunti, impegni e scadenze tra lavoro e vita privata.',
                   'People who have to keep email, notes, appointments and deadlines together across work and private life.'),
             problem=T('Email, appunti, impegni e scadenze sparsi tra mille strumenti: organizzare la giornata diventa un lavoro a sé.',
                       'Email, notes, appointments and deadlines spread across countless tools: organising the day becomes a job in itself.'),
             today=T("È in sviluppo. L'obiettivo: ricevere email, appunti e cose da fare, mettere tutto in ordine, preparare la giornata e ricordare i dettagli utili per i report.",
                     "It's in development. The goal: take in email, notes and to-dos, put everything in order, plan the day and remember the details that matter for reports."),
             next=T('Collegamento dei calendari Outlook e Gmail per ogni utente.', 'Connecting Outlook and Gmail calendars for each user.'),
             can=T('Scriverci se ti interessa: ti diciamo come procede lo sviluppo.', "Write to us if you're interested: we'll tell you how development is going."),
             cta=T('Chiedi informazioni', 'Ask for information'), subj=T('AIDA – richiesta informazioni', 'AIDA – information request')),
    ]

def stages():
    return [(T('In sviluppo', 'In development'), T('Lo stiamo costruendo: non si può ancora provare.', "We are building it: it can't be tried yet.")),
            (T('Prototipo', 'Prototype'), T('Esiste una versione dimostrativa; la prova in un contesto reale è ancora da fare.', 'A demo version exists; trying it in a real setting is still to come.')),
            (T('Pilota', 'Pilot'), T('Lo stiamo provando su casi reali, prima del rilascio.', 'We are trying it on real cases, before release.')),
            (T('In uso', 'In use'), T('Disponibile e in uso.', 'Available and in use.'))]

def experiences():
    X = lambda id, sector, title, ctx, prob, did, res, note=None: dict(id=id, sector=sector, title=title, ctx=ctx, prob=prob, did=did, res=res, note=note)
    return [
        X('sap-teamcenter', 'Automotive', T('Far dialogare SAP e Teamcenter', 'Making SAP and Teamcenter talk'),
          T("In un'azienda automotive, ufficio tecnico e gestionale lavoravano su due sistemi separati: Teamcenter per i progetti, SAP per la gestione.", 'In an automotive company, engineering and management worked on two separate systems: Teamcenter for projects, SAP for management.'),
          T('Le informazioni andavano passate a mano da un sistema all\'altro, con molto lavoro di coordinamento.', 'Information had to be moved by hand from one system to the other, with a lot of coordination work.'),
          T("Un'applicazione che collega i due sistemi e trasferisce le informazioni in automatico.", 'An application that connects the two systems and transfers information automatically.'),
          T('Avanzamento dei progetti, distinte base e report sempre allineati, in un unico posto.', 'Project progress, bills of materials and reports always aligned, in one place.')),
        X('omniqual', T('Sanità', 'Healthcare'), T("OmniQual Engine: l'IA che scrive i test", 'OmniQual Engine: the AI that writes tests'),
          T('Un software medicale certificato va provato simulando quello che fa un utente. Questi test venivano scritti a mano.', 'Certified medical software has to be tested by simulating what a user does. These tests were written by hand.'),
          T("Scrivere e controllare i test a mano era lento, e non c'era modo di sapere se coprivano tutti i casi.", 'Writing and checking tests by hand was slow, and there was no way to know whether they covered every case.'),
          T("Un'applicazione che legge il codice e un test di esempio, capisce come è fatto e ne scrive di nuovi da sola.", 'An application that reads the code and a sample test, understands how it works and writes new ones on its own.'),
          T('Test generati in automatico, bug individuati, controllo dei casi mancanti e proposte di nuovi test.', 'Tests generated automatically, bugs found, missing cases checked and new tests proposed.')),
        X('cronofest', T('Eventi', 'Events'), T("CronoFest: un'app per organizzare un evento", 'CronoFest: an app to run an event'),
          T('Un evento con molte aree e ruoli diversi: amministratori, organizzatori, responsabili di area e persone che devono solo consultare.', 'An event with many areas and roles: administrators, organisers, area leads and people who only need to look things up.'),
          T('Programma, attività e materiali erano sparsi tra le aree, e ognuno doveva poter modificare solo la propria parte.', 'Schedule, activities and materials were scattered across areas, and everyone had to edit only their own part.'),
          T("Un'app con il programma di ogni area, un assistente vocale per aggiungere attività parlando e la gestione del magazzino.", "An app with each area's schedule, a voice assistant to add activities by speaking, and inventory management."),
          T("Un'unica dashboard: ognuno vede quello che gli serve e modifica solo la propria area.", 'A single dashboard: everyone sees what they need and edits only their own area.')),
        X('omop', T('Sanità', 'Healthcare'), T('Dati clinici in uno standard internazionale', 'Clinical data in an international standard'),
          T('Le prestazioni di un pronto soccorso, registrate dal 2008 con codici interni, andavano convertite nello standard internazionale OMOP.', 'Emergency department records, coded internally since 2008, had to be converted to the international OMOP standard.'),
          T('Bisognava abbinare termini in italiano a oltre 2 milioni di voci dello standard.', 'Italian terms had to be matched to more than 2 million entries in the standard.'),
          T('Un gruppo di agenti IA che traduce i termini e trova la voce corrispondente nello standard.', 'A group of AI agents that translates the terms and finds the matching entry in the standard.'),
          T('Nel test del progetto la voce corretta è tra le prime 5 proposte in circa il 97% dei casi; per i software tradizionali il materiale di progetto indica il 67%.', 'In the project test the correct entry was among the top 5 suggestions in about 97% of cases; the project material gives 67% for traditional software.'),
          T('Nota sul dato: il 97% indica quante volte la voce corretta compare tra le prime 5 proposte nel test del progetto. Il materiale di progetto non descrive come è stato misurato il 67% dei software tradizionali.', "About this figure: 97% is how often the correct entry appeared among the top 5 suggestions in the project test. The project material doesn't describe how the 67% for traditional software was measured.")),
        X('biblioteca', T('Ricerca', 'Research'), T("Catalogare i documenti di una biblioteca con l'IA", 'Cataloguing library documents with AI'),
          T('Progetto di ricerca in corso: documenti di biblioteca, anche in arabo, che un esperto doveva catalogare e controllare a mano.', 'Ongoing research project: library documents, some in Arabic, that an expert had to catalogue and check by hand.'),
          T('Catalogare a mano richiede moltissimo tempo, e la lettura automatica del testo (OCR) introduce errori.', 'Manual cataloguing takes a great deal of time, and automatic text recognition (OCR) introduces errors.'),
          T("Più agenti IA riconoscono l'opera anche da un testo letto male e recuperano i dati corretti da cataloghi affidabili.", 'Several AI agents recognise the work even from poorly read text and retrieve correct data from reliable catalogues.'),
          T("Schede già compilate con dati verificati: meno lavoro per l'esperto e meno errori.", 'Records already filled in with verified data: less work for the expert and fewer errors.')),
        X('sql', T('Ricerca', 'Research'), T('Fare domande a un database, in italiano', 'Asking a database questions in plain language'),
          T('Filone di ricerca: ottenere dati da un database facendo domande con parole di tutti i giorni.', 'Research track: getting data out of a database by asking questions in everyday words.'),
          T('Per estrarre dati da un database bisogna saper scrivere codice SQL. Esempio: «Chi è stato il pilota di Formula 1 che ha vinto nel 1998?»', 'Getting data out of a database means writing SQL. Example: “Which Formula 1 driver won in 1998?”'),
          T("L'IA trasforma la domanda in codice SQL, lo esegue e restituisce la risposta.", 'The AI turns the question into SQL, runs it and returns the answer.'),
          T('Chiunque può ottenere i dati con una semplice domanda, senza scrivere codice.', 'Anyone can get the data with a simple question, without writing code.')),
    ]

def xp_link(id):
    t = {e['id']: e['title'] for e in experiences()}[id]
    return f'<a href="{u("esperienze")}#{id}">{esc(t)}</a>'

# ------------------------------------------------------------------ layout
def head(key, title, desc, jsonld, extra=''):
    path = u(key)
    it, en = URL[key]
    css = f'/site.css?v={hsh(os.path.join(ROOT, "site.css"))}'
    data = json.dumps(jsonld, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    return f'''<!doctype html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Outfit:wght@500;600;700&display=swap">
<link rel="stylesheet" href="{css}">
<script>try{{var t=localStorage.getItem("ck-theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}{path}">
<link rel="alternate" hreflang="it" href="{SITE}{it}">
<link rel="alternate" hreflang="en" href="{SITE}{en}">
<link rel="alternate" hreflang="x-default" href="{SITE}{it}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Cutting Knots">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Cutting Knots">
<meta property="og:locale" content="{T('it_IT', 'en_US')}">
<meta property="og:locale:alternate" content="{T('en_US', 'it_IT')}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0B1015">
{extra}<script type="application/ld+json">{data}</script>
</head>
<body>
<a class="skip" href="#main">{T('Vai al contenuto', 'Skip to content')}</a>
'''

def nav_items():
    return [('enterprise', 'Enterprise'), ('consulting', 'Consulting'), ('prodotti', T('Prodotti', 'Products')),
            ('esperienze', T('Esperienze', 'Experience')), ('chi', T('Chi siamo', 'About'))]

def header(key):
    other = 'en' if L == 'it' else 'it'
    alt = u(key, other)
    cur = lambda k: ' aria-current="page"' if k == key else ''
    links = ''.join(f'<a href="{u(k)}"{cur(k)}>{n}</a>' for k, n in nav_items())
    big = ''.join(f'<a class="big" href="{u(k)}"{cur(k)}>{n}</a>' for k, n in nav_items())
    lang = (f'<b>IT</b> · <a href="{alt}" lang="en" hreflang="en">EN</a>' if L == 'it'
            else f'<a href="{alt}" lang="it" hreflang="it">IT</a> · <b>EN</b>')
    return f'''<header class="hd">
  <div class="hd-in">
    <a class="logo" href="{u('home')}" aria-label="{T('Cutting Knots, pagina iniziale', 'Cutting Knots, home page')}"><img src="/img/ck-logo-white.svg" alt="Cutting Knots" width="152" height="28"></a>
    <nav class="hd-links" aria-label="{T('Principale', 'Main')}">{links}</nav>
    <div class="hd-tools">
      <span class="lang">{lang}</span>
      <button class="iconbtn" type="button" data-theme-toggle aria-label="{T('Cambia tema', 'Switch theme')}">{SUN}</button>
    </div>
    <a class="btn cta-sm" href="{u('contatti')}">{T('Contattaci', 'Contact us')}</a>
    <button class="iconbtn menubtn" type="button" id="menu-btn" aria-expanded="false" aria-controls="sheet" aria-label="{T('Apri il menu', 'Open the menu')}">
      <svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 8h16M4 16h16"/></svg>
    </button>
  </div>
</header>
<nav class="sheet" id="sheet" aria-label="Menu" hidden>
  {big}<a class="big" href="{u('small')}"{cur('small')}>Small Solutions</a>
  <div class="sheet-foot">
    <div style="display:flex;justify-content:space-between;align-items:center"><span class="lang" style="padding:0;font-size:15px">{lang}</span>
      <button class="btn btn-ghost" type="button" data-theme-toggle style="min-height:44px">{T('Cambia tema', 'Switch theme')}</button></div>
    <a class="btn btn-accent" href="{u('contatti')}">{T('Contattaci', 'Contact us')}</a>
  </div>
</nav>
'''

def footer():
    col = lambda title, items: f'<div><h2>{title}</h2>' + ''.join(f'<a href="{h}"{a}>{t}</a>' for t, h, a in items) + '</div>'
    return f'''<footer class="site-foot">
  <div class="wrap">
    <div class="f-brand"><a href="{u('home')}" style="color:var(--fg);display:block;width:180px">{LOGO.replace('<svg ', '<svg style="width:100%;height:auto;display:block" ', 1)}</a>
      <p>{T('Cutting Knots: software, intelligenza artificiale e consulenza per le aziende.', 'Cutting Knots: software, artificial intelligence and consulting for companies.')}</p></div>
    <div class="f-cols">
      {col('Cutting Knots', [('Enterprise', u('enterprise'), ''), ('Consulting', u('consulting'), ''), ('Small Solutions', u('small'), '')])}
      {col(T('Azienda', 'Company'), [(T('Prodotti', 'Products'), u('prodotti'), ''), (T('Esperienze', 'Experience'), u('esperienze'), ''), (T('Chi siamo', 'About'), u('chi'), '')])}
      {col(T('Contatti', 'Contact'), [(EMAIL, 'mailto:' + EMAIL, ''), ('LinkedIn', LINKEDIN, ' rel="noopener"'), (T('Scrivici', 'Write to us'), u('contatti'), '')])}
    </div>
    <div class="f-bottom">
      <span>© 2026 Cutting Knots</span>
      <div class="themes" role="group" aria-label="{T('Tema', 'Theme')}"><button type="button" data-theme-set="auto" aria-pressed="true">{T('Automatico', 'Auto')}</button><button type="button" data-theme-set="light" aria-pressed="false">{T('Chiaro', 'Light')}</button><button type="button" data-theme-set="dark" aria-pressed="false">{T('Scuro', 'Dark')}</button></div>
      <a class="egg" href="{u('villaggio')}">▶ {T('PREMI START', 'PRESS START')}</a>
    </div>
  </div>
</footer>
<script src="/site.js?v={hsh(os.path.join(ROOT, 'site.js'))}" defer></script>
</body>
</html>
'''

def band(eyebrow, h1, lead, acts='', cls=''):
    return f'''<section class="band {cls}">
  {MARK}
  <div class="wrap">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    {f'<div class="acts">{acts}</div>' if acts else ''}
  </div>
</section>
'''

def close(title=None, text=None):
    title = title or T('Qual è il vostro nodo?', "What's your knot?")
    text = text or T('Raccontatecelo in poche righe. Rispondiamo entro due giorni lavorativi.', 'Tell us in a few lines. We reply within two working days.')
    return f'''<section class="sec" style="padding-top:24px">
  <div class="wrap">
    <div class="close">
      <h2 class="h2" style="font-size:clamp(28px,4vw,44px)">{title}</h2>
      <p>{text}</p>
      <p class="mail">{EMAIL}</p>
      <div class="acts">
        <button class="btn btn-accent" type="button" data-copy="{EMAIL}">{T("Copia l'indirizzo", 'Copy the address')}</button>
        <a class="btn btn-ghost" href="mailto:{EMAIL}">{T("Scrivi un'email", 'Send an email')}</a>
      </div>
      <p class="sr" role="status" id="copy-status"></p>
    </div>
  </div>
</section>
'''

def webpage(key, title, desc, crumbs=True):
    g = [] if key == 'home' else [org()]
    g += [{"@type": "WebPage", "@id": f"{SITE}{u(key)}#page", "url": f"{SITE}{u(key)}", "name": title, "description": desc,
          "inLanguage": L, "isPartOf": {"@id": f"{SITE}/#website"}, "about": {"@id": f"{SITE}/#org"}}]
    if crumbs and key != 'home':
        g.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Cutting Knots", "item": f"{SITE}{u('home')}"},
            {"@type": "ListItem", "position": 2, "name": title.split(' · ')[0], "item": f"{SITE}{u(key)}"}]})
    return g

def org():
    return {"@type": "Organization", "@id": f"{SITE}/#org", "name": "Cutting Knots", "alternateName": ["CuttingKnots", "Cutting Knots Enterprise", "Cutting Knots Consulting"], "url": f"{SITE}/",
            "areaServed": {"@type": "Country", "name": "Italia"},
            "logo": f"{SITE}/android-chrome-512x512.png", "image": f"{SITE}/og-image.png", "email": EMAIL, "sameAs": [LINKEDIN],
            "slogan": "Sciogliamo nodi.",
            "description": T("Prodotti e progetti software con Cutting Knots Enterprise. Corsi sull'intelligenza artificiale e consulenza tecnica con Cutting Knots Consulting.",
                             'Software products and projects with Cutting Knots Enterprise. AI courses and technical consulting with Cutting Knots Consulting.'),
            "department": [{"@type": "Organization", "name": "Cutting Knots Enterprise", "url": f"{SITE}{u('enterprise')}"},
                           {"@type": "Organization", "name": "Cutting Knots Consulting", "url": f"{SITE}{u('consulting')}"},
                           {"@type": "Organization", "name": "Cutting Knots Small Solutions", "url": f"{SITE}{u('small')}"}],
            "knowsAbout": ["Intelligenza artificiale", "Formazione sull'intelligenza artificiale", "Solution Architecture", "Integrazione di sistemi",
                           "ERP", "PLM", "SAP", "Teamcenter", "Mendix", "Low-code", "Computer vision", "Modelli 3D", "Simulazioni", "Sviluppo software su misura", "OMOP", "MCP"],
            "contactPoint": {"@type": "ContactPoint", "email": EMAIL, "contactType": "sales", "availableLanguage": ["Italian", "English"]}}

def faq_block(items, title):
    q = ''.join(f'<details name="faq"><summary>{esc(a)}{PLUS}</summary><p>{esc(b)}</p></details>' for a, b in items)
    return f'''<section id="faq" class="sec">
  <div class="wrap faq-grid">
    <h2 class="h2" style="margin-bottom:12px">{title}</h2>
    <div class="faq">{q}</div>
  </div>
</section>
'''

def faq_ld(items, key):
    return {"@type": "FAQPage", "@id": f"{SITE}{u(key)}#faq", "inLanguage": L,
            "mainEntity": [{"@type": "Question", "name": a, "acceptedAnswer": {"@type": "Answer", "text": b}} for a, b in items]}

def prod_cards(link_to_page=True):
    out = []
    for p in products():
        fig = (f'<figure><img src="{p["img"]}" alt="{esc(p["alt"])}" width="{p["w"]}" height="{p["h"]}" loading="lazy"'
               + (' style="object-fit:contain;background:#262626"' if p.get('contain') else '') + f'><figcaption>{esc(p["cap"])}</figcaption></figure>')
        name = (f'<img src="{p["logo"]}" alt="{p["name"]}" width="142" height="24" style="height:24px;width:auto;align-self:flex-start">'
                if p.get('logo') else f'<h3>{p["name"]}</h3>')
        st = stages()[p['stage'] - 1][0]
        cls = {3: 'pilot', 2: 'proto'}.get(p['stage'], '')
        out.append(f'''<li class="prod">{fig}<div class="prod-b">{name}<p>{esc(p["short"])}</p><span class="st {cls}"><i></i>{T('Stato', 'Status')}: {st.lower()}</span>
          <a href="{u('prodotti')}#{p['id']}">{T('Scheda del prodotto', 'Product details')}</a></div></li>''')
    return '<ul class="prods">' + ''.join(out) + '</ul>'

def consulting_items():
    return [
        ('courses', '<path d="M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/>',
         T("Corsi sull'intelligenza artificiale", 'AI courses'), T('Per i team aziendali, costruiti sui vostri casi d\'uso.', 'For company teams, built on your own use cases.')),
        ('industrial', '<path d="M12 2l9 5v10l-9 5-9-5V7z"/><path d="M12 22V12M21 7l-9 5-9-5"/>',
         T('Consulenza industriale', 'Industrial consulting'), T('Modelli 3D, simulazioni e sistemi gestionali.', '3D models, simulations and management systems.')),
        ('architect', '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="8.5" y="14" width="7" height="7" rx="1.5"/><path d="M6.5 10v2h11v-2M12 12v2"/>',
         T('Solution Architect per voi', 'A Solution Architect for you'), T('Architettura e scelte tecnologiche, dalla vostra parte del tavolo.', 'Architecture and technology choices, on your side of the table.')),
        ('rnd', '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.7 3h10.6a2 2 0 0 0 1.7-3l-5-9V3"/>',
         T('Ricerca e sviluppo IA end-to-end', 'End-to-end AI research and development'), T('Dall\'idea al prototipo funzionante, con il vostro team.', 'From the idea to a working prototype, with your team.')),
    ]

def ico(path): return f'<span class="ico" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{path}</svg></span>'

def more(href, text): return f'<a class="more" href="{href}">{text} {ARROW}</a>'

# ------------------------------------------------------------------ pages
def home_faq():
    return [
        (T('Cosa fa Cutting Knots?', 'What does Cutting Knots do?'),
         T("Cutting Knots è un'azienda italiana di software, intelligenza artificiale e consulenza. Lavoriamo su due fronti. Con Cutting Knots Enterprise sviluppiamo prodotti software nostri e progetti su misura per le aziende. Con Cutting Knots Consulting formiamo i team sull'intelligenza artificiale e offriamo consulenza tecnica.",
           'Cutting Knots is an Italian software, artificial intelligence and consulting company. We work on two fronts. With Cutting Knots Enterprise we build our own software products and custom projects for companies. With Cutting Knots Consulting we train teams on artificial intelligence and provide technical consulting.')),
        (T("Che differenza c'è tra Enterprise e Consulting?", "What's the difference between Enterprise and Consulting?"),
         T('Enterprise consegna software: un nostro prodotto o un progetto costruito per voi. Consulting mette a disposizione competenze: corsi, consulenza industriale, un Solution Architect, ricerca e sviluppo. Si possono scegliere separatamente o insieme.',
           'Enterprise delivers software: one of our products or a project built for you. Consulting provides expertise: courses, industrial consulting, a Solution Architect, research and development. You can choose them separately or together.')),
        (T('I vostri prodotti si possono già usare?', 'Can I already use your products?'),
         T('Dipende dal prodotto: Forma Simplifier è in fase pilota, VIGIL è un prototipo e AIDA è in sviluppo. Per ognuno indichiamo lo stato reale e cosa si può fare oggi.',
           'It depends on the product: Forma Simplifier is in pilot, VIGIL is a prototype and AIDA is in development. For each one we state its real status and what can be done today.')),
        (T("Fate corsi sull'intelligenza artificiale per le aziende?", 'Do you run AI courses for companies?'),
         T('Sì, con Cutting Knots Consulting. I corsi sono pensati per i team aziendali e partono dai vostri casi d\'uso.',
           'Yes, with Cutting Knots Consulting. The courses are designed for company teams and start from your own use cases.')),
        (T('Come si comincia?', 'How do we start?'),
         T('Scriveteci in poche righe cosa vi serve. Rispondiamo entro due giorni lavorativi e, se possiamo aiutarvi, vi proponiamo una prima conversazione.',
           'Write to us in a few lines about what you need. We reply within two working days and, if we can help, suggest a first conversation.')),
    ]

def page_home():
    title = T('Cutting Knots · Software, IA e consulenza', 'Cutting Knots · Software, AI and consulting')
    desc = T("Cutting Knots: prodotti e progetti software con Cutting Knots Enterprise, corsi sull'intelligenza artificiale e consulenza tecnica con Cutting Knots Consulting.",
             'Cutting Knots: software products and projects with Cutting Knots Enterprise, AI courses and technical consulting with Cutting Knots Consulting.')
    faq = home_faq()
    ld = {"@context": "https://schema.org", "@graph": [org(), {"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/", "name": "Cutting Knots", "inLanguage": ["it", "en"], "publisher": {"@id": f"{SITE}/#org"}}]
          + webpage('home', title, desc) + [faq_ld(faq, 'home')]}
    pre = '<link rel="preload" as="image" href="/img/horizon-1200.jpg" imagesrcset="/img/horizon-1200.jpg 1200w, /img/horizon-2400.jpg 2400w" imagesizes="100vw" fetchpriority="high">\n'
    cons = ''.join(f'<li>{ico(p)}<div><h3>{t}</h3><p>{d}</p></div></li>' for _, p, t, d in consulting_items())
    body = f'''<main id="main" tabindex="-1">
<section class="scene" id="top" aria-label="{T('Introduzione', 'Introduction')}">
  <div class="pin">
    <img class="sky" src="/img/horizon-1200.jpg" srcset="/img/horizon-1200.jpg 1200w, /img/horizon-2400.jpg 2400w" sizes="100vw" alt="" fetchpriority="high">
    <div class="wrap copy">
      <p class="eyebrow">{T('Software, intelligenza artificiale, consulenza', 'Software, artificial intelligence, consulting')}</p>
      <h1>{T('Tagliamo i nodi che rallentano la tua azienda.', 'We cut the knots that slow your company down.')}</h1>
      <p class="sub">{T("Prodotti e progetti software con Cutting Knots Enterprise. Formazione sull'intelligenza artificiale e consulenza con Cutting Knots Consulting.", 'Software products and projects with Cutting Knots Enterprise. AI training and consulting with Cutting Knots Consulting.')}</p>
    </div>
    <svg class="sym" id="sym" role="img" aria-label="{T('Il nodo di Cutting Knots, tagliato dalla sua barra arancione', 'The Cutting Knots knot, cut by its orange bar')}" viewBox="-12 -12 330 284">
      <defs>
        <clipPath id="cutclip"><polygon id="cutp" points="-2000,-2000 2000,-2000 2000,2000 -2000,2000"/></clipPath>
        <path id="kp" d="{KN['REST']}"/>
        <path id="bp" clip-path="url(#cutclip)" d="{KN['BR']}"/>
        <clipPath id="cpA"><polygon points="-600,-600 844,-471 -531,724"/></clipPath>
        <clipPath id="cpB"><polygon points="843,-472.1 900,900 -532,722.9"/></clipPath>
      </defs>
      <path id="bar" class="bar" d="{KN['CUT']}"/>
      <g class="body">
        <g id="ha"><g clip-path="url(#cpA)"><use href="#kp"/><use href="#bp"/></g></g>
        <g id="hb"><g clip-path="url(#cpB)"><use href="#kp"/><use href="#bp"/></g></g>
        <path d="{KN['MID']}"/>
      </g>
      <path class="ol" id="ol" pathLength="1" d="{KN['U']}"/>
    </svg>
    <div class="threads wrap">
      <svg viewBox="0 0 400 120" preserveAspectRatio="none" aria-hidden="true">
        <path id="t4" pathLength="100" d="M200 0 C 190 70, 40 50, 24 118" stroke="#9AA4AE" stroke-width="1" opacity=".5"/>
        <path id="t1" pathLength="100" d="M200 0 C 200 70, 140 50, 140 118" stroke="#FD3F03" stroke-width="5"/>
        <path id="t2" pathLength="100" d="M200 0 C 200 70, 260 50, 260 118" stroke="#FFFFFF" stroke-width="3"/>
        <path id="t3" pathLength="100" d="M200 0 C 210 70, 360 50, 376 118" stroke="#9AA4AE" stroke-width="1.5"/>
      </svg>
      <div class="tl" id="tl">
        <a href="{u('villaggio')}" aria-label="{T('Un filo nascosto', 'A hidden thread')}" title="{T('Un filo nascosto', 'A hidden thread')}" style="left:6%;transform:translateX(-50%);width:44px;height:44px;display:grid;place-items:center"><span aria-hidden="true" style="width:7px;height:7px;border-radius:50%;background:#5B6670"></span></a>
        <a class="pill" href="{u('enterprise')}" style="left:35%;background:var(--accent);color:var(--on-accent)">Enterprise</a>
        <a class="pill" href="{u('consulting')}" style="left:65%;background:#fff;color:#0F151B">Consulting</a>
        <a href="{u('small')}" style="right:max(16px,env(safe-area-inset-right,0px));max-width:84px;min-height:44px;display:flex;align-items:center;text-align:right;font-size:12px;line-height:1.25;color:#C9D0D6;text-decoration:none">Small Solutions</a>
      </div>
    </div>
    <p class="hint" id="hint" aria-hidden="true">{T('Scorri', 'Scroll')}
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 5v14M6 13l6 6 6-6"/></svg></p>
  </div>
</section>

<section id="enterprise" class="sec ent">
  <div class="wrap stack">
    <p class="eyebrow">Cutting Knots Enterprise</p>
    <h2 class="h2">{T('Prodotti e progetti software per le aziende.', 'Software products and projects for companies.')}</h2>
    <p class="lead">{T('Prodotti nostri per i problemi più comuni, e progetti costruiti sul vostro processo quando serve qualcosa che non esiste ancora.', "Our own products for common problems, and projects built around your process when you need something that doesn't exist yet.")}</p>
    <h3 class="sub-h" id="prodotti">{T('Prodotti · ognuno con il suo stato reale', 'Products · each with its real status')}</h3>
    {prod_cards()}
    <h3 class="sub-h">{T('Progetti', 'Projects')}</h3>
    <ul class="projs">
      <li class="proj"><h3>{T('Progetti su misura', 'Custom projects')}</h3><p>{T('Integrazioni tra ERP, PLM e gestionali, applicazioni web e low-code costruite sul vostro processo.', 'Integrations between ERP, PLM and business systems, web and low-code applications built around your process.')}</p></li>
      <li class="proj"><h3>{T("Progetti di intelligenza artificiale", 'AI projects')}</h3><p>{T('Lettura e controllo dei documenti, computer vision, dati interrogabili in linguaggio naturale.', 'Reading and checking documents, computer vision, data you can query in plain language.')}</p></li>
    </ul>
    <div class="acts" style="margin-top:8px"><a class="btn btn-white" href="{u('enterprise')}">{T('Scopri Cutting Knots Enterprise', 'Explore Cutting Knots Enterprise')}</a></div>
  </div>
</section>

<section id="consulting" class="sec">
  <div class="wrap stack">
    <p class="eyebrow" style="color:var(--accent-text)">Cutting Knots Consulting</p>
    <h2 class="h2">{T('Formazione e consulenza, dove servono competenze in più.', 'Training and consulting, where you need extra expertise.')}</h2>
    <p class="lead">{T("Portiamo l'intelligenza artificiale nei vostri team e vi affianchiamo su progetti tecnici, dall'architettura alla ricerca.", 'We bring artificial intelligence into your teams and support you on technical projects, from architecture to research.')}</p>
    <ul class="cons">{cons}</ul>
    <div class="acts" style="margin-top:8px">
      <a class="btn btn-ink" href="{u('consulting')}">{T('Scopri Cutting Knots Consulting', 'Explore Cutting Knots Consulting')}</a>
      <a class="btn btn-soft" href="{mailto(T('Corso sull’intelligenza artificiale per il team', 'AI course for our team'))}">{T('Chiedi un corso per il team', 'Ask about a course for your team')}</a>
    </div>
  </div>
</section>

<section id="small"><div class="wrap"><p class="small"><span aria-hidden="true"></span>{T('Per realtà più piccole: siti web, e-commerce e microgestionali con', 'For smaller organisations: websites, e-commerce and small management apps with')}&nbsp;<a href="{u('small')}" style="font-weight:600">Cutting Knots Small Solutions</a></p></div></section>
'''
    return head('home', title, desc, ld, pre) + header('home') + body + faq_block(faq, T('Domande', 'Questions')).replace('class="sec"', 'class="sec"', 1) + close() + '</main>\n' + footer()

def problems():
    P = lambda t, p, d, o, xps: dict(t=t, p=p, d=d, o=o, xps=xps)
    return [
        P(T('Attività manuali e ripetitive', 'Manual, repetitive work'),
          T('Dati copiati da un documento all\'altro, report fatti a mano, controlli ripetuti ogni giorno.', 'Data copied from one document to another, reports built by hand, the same checks every day.'),
          T("Automazione, anche con l'intelligenza artificiale: lettura dei documenti, estrazione e controllo dei dati.", 'Automation, with artificial intelligence where useful: reading documents, extracting and checking data.'),
          T('Meno lavoro manuale e meno errori di trascrizione.', 'Less manual work and fewer transcription errors.'), ['biblioteca', 'omniqual']),
        P(T('Sistemi che non si parlano', "Systems that don't talk"),
          T('ERP, PLM e gestionali separati: le informazioni passano a mano da un sistema all\'altro.', 'Separate ERP, PLM and business systems: information moves by hand from one to the other.'),
          T('Integrazione tra le piattaforme che avete già, senza doppio lavoro.', 'Integration between the platforms you already have, without double work.'),
          T('Informazioni allineate in un unico posto.', 'Information aligned in one place.'), ['sap-teamcenter']),
        P(T('Un processo che nessuno strumento copre', 'A process no tool covers'),
          T('Fogli condivisi, email e telefonate tengono insieme un processo con molti ruoli.', 'Shared sheets, email and phone calls hold together a process with many roles.'),
          T('Software su misura: applicazioni web o piattaforme low-code come Mendix, costruite su ruoli e passaggi reali.', 'Custom software: web applications or low-code platforms such as Mendix, built around real roles and steps.'),
          T('Ognuno vede quello che gli serve e modifica solo la propria parte.', 'Everyone sees what they need and edits only their own part.'), ['cronofest']),
        P(T('Dati difficili da trovare o interrogare', "Data that's hard to find or query"),
          T('Per ottenere un dato serve chi sa scrivere query, oppure i dati sono in formati e codici diversi.', 'Getting a figure needs someone who writes queries, or the data sits in different formats and codes.'),
          T('Accesso ai dati con domande in linguaggio naturale; conversione verso standard comuni.', 'Access to data by asking in plain language; conversion to common standards.'),
          T('Dati consultabili da chi ne ha bisogno.', 'Data available to the people who need it.'), ['sql', 'omop']),
    ]

def steps(items):
    return '<ol class="steps">' + ''.join(f'<li><h3>{a}</h3><p>{b}</p></li>' for a, b in items) + '</ol>'

def start_steps():
    return steps([
        (T('Ci scrivete', 'You write to us'), T('Bastano tre righe: cosa fate, dov\'è il nodo, cosa vorreste ottenere.', "Three lines are enough: what you do, where the knot is, what you'd like to achieve.")),
        (T('Vi rispondiamo', 'We reply'), T('Entro due giorni lavorativi. Se possiamo aiutarvi, vi proponiamo una prima conversazione.', 'Within two working days. If we can help, we suggest a first conversation.')),
        (T('Analizziamo insieme', 'We analyse it together'), T('Obiettivi, processo di oggi e sistemi coinvolti.', "Goals, today's process and the systems involved.")),
        (T('Scegliamo la strada', 'We choose the path'), T('Sviluppare, integrare o adottare una soluzione esistente, con indicatori concordati per capire se il nodo è stato tagliato.', 'Build, integrate or adopt an existing solution, with agreed indicators to know whether the knot was cut.')),
    ])

def page_enterprise():
    title = T('Cutting Knots Enterprise · Prodotti e progetti software', 'Cutting Knots Enterprise · Software products and projects')
    desc = T('Prodotti software nostri e progetti su misura per le aziende: integrazione di ERP e PLM, applicazioni web e low-code, progetti di intelligenza artificiale.',
             'Our own software products and custom projects for companies: ERP and PLM integration, web and low-code applications, AI projects.')
    rows = ''
    for i, p in enumerate(problems(), 1):
        xp = ' · '.join(xp_link(x) for x in p['xps'])
        rows += f'''<li class="row"><h3><span>{i:02d}</span>{p["t"]}</h3>
      <div><dl><div><dt>{T('Il problema', 'The problem')}</dt><dd>{p["p"]}</dd></div><div><dt>{T('Cosa facciamo', 'What we do')}</dt><dd>{p["d"]}</dd></div><div><dt>{T('Obiettivo', 'The aim')}</dt><dd>{p["o"]}</dd></div></dl>
      <p class="xp" style="margin-top:12px">{T('Esperienze del team', 'Team experience')}: {xp}</p></div></li>'''
    ai = [(T('Documenti che si leggono da soli', 'Documents that read themselves'), T('Lettura, estrazione e controllo dei dati da PDF, email e moduli, con una persona che verifica.', 'Reading, extracting and checking data from PDFs, email and forms, with a person checking.')),
          (T('Computer vision', 'Computer vision'), T('Telecamere che riconoscono oggetti, eventi e tempi su linee e magazzini.', 'Cameras that recognise objects, events and times on lines and in warehouses.')),
          (T('Dati in linguaggio naturale', 'Data in plain language'), T('Domande ai database con parole di tutti i giorni, senza scrivere query.', 'Questions to databases in everyday words, without writing queries.')),
          (T('Agenti e assistenti', 'Agents and assistants'), T('Più agenti IA che si dividono un lavoro complesso, collegati ai vostri sistemi anche via MCP.', 'Several AI agents sharing a complex job, connected to your systems, including via MCP.'))]
    body = band('Cutting Knots Enterprise', T('Software che <em>lavora</em> per la vostra azienda.', 'Software that <em>works</em> for your company.'),
                T('Prodotti nostri per i problemi più comuni, e progetti costruiti sul vostro processo quando serve qualcosa che non esiste ancora.', "Our own products for common problems, and projects built around your process when you need something that doesn't exist yet."),
                f'<a class="btn btn-white" href="{mailto(T("Cutting Knots Enterprise – nuovo progetto", "Cutting Knots Enterprise – new project"))}">{T("Parliamo del vostro progetto", "Let’s talk about your project")}</a><a class="btn btn-ghost" href="#prodotti">{T("Vedi i prodotti", "See the products")}</a>')
    body += f'''<section class="sec ent" id="prodotti">
  <div class="wrap stack">
    <p class="eyebrow">{T('Prodotti', 'Products')}</p>
    <h2 class="h2">{T('Software nostro, ognuno con il suo stato reale.', 'Our own software, each with its real status.')}</h2>
    <p class="lead">{T('Nessuno è ancora un prodotto in uso: per ognuno diciamo a che punto è e cosa si può fare oggi.', "None is in general use yet: for each one we say where it stands and what can be done today.")}</p>
    {prod_cards()}
    {more(u('prodotti'), T('Tutti i dettagli dei prodotti', 'All product details'))}
  </div>
</section>
<section class="sec" id="progetti">
  <div class="wrap stack">
    <p class="kicker">{T('Progetti su misura', 'Custom projects')}</p>
    <h2 class="h2">{T('Dal problema <em>al risultato</em> atteso.', 'From the problem <em>to the expected</em> outcome.')}</h2>
    <p class="lead">{T('Partiamo da un problema concreto e scegliamo con voi se automatizzare, integrare i sistemi che avete o sviluppare quello che manca.', 'We start from a concrete problem and choose with you whether to automate, integrate the systems you have or build what\'s missing.')}</p>
    <ul class="rows">{rows}</ul>
  </div>
</section>
<section class="sec alt" id="ia">
  <div class="wrap stack">
    <p class="kicker">{T("Progetti di intelligenza artificiale", 'AI projects')}</p>
    <h2 class="h2">{T("L'intelligenza artificiale dove fa risparmiare tempo.", 'Artificial intelligence where it saves time.')}</h2>
    <p class="lead">{T('Progetti costruiti sui vostri dati e sui vostri sistemi, con un controllo umano dove serve.', 'Projects built on your data and your systems, with human checks where needed.')}</p>
    <ul class="grid g4">{''.join(f'<li class="card"><h3>{a}</h3><p>{b}</p></li>' for a, b in ai)}</ul>
  </div>
</section>
<section class="sec">
  <div class="wrap stack">
    <p class="kicker">{T('Come si comincia', 'How it starts')}</p>
    <h2 class="h2">{T('Dal primo messaggio alla strada da prendere.', 'From the first message to the path to take.')}</h2>
    {start_steps()}
    <p class="kicker" style="margin-top:20px">{T('Tecnologie su cui il team ha lavorato', 'Technologies our team has worked with')}</p>
    <ul class="chips">{''.join(f'<li>{t}</li>' for t in ['Mendix', 'SAP', 'Teamcenter', 'OMOP', 'SQL', 'MCP'])}</ul>
    {more(u('esperienze'), T('Vedi i progetti del team', "See the team's projects"))}
  </div>
</section>
'''
    ld = {"@context": "https://schema.org", "@graph": webpage('enterprise', title, desc)}
    return head('enterprise', title, desc, ld) + header('enterprise') + '<main id="main" tabindex="-1">\n' + body + close() + '</main>\n' + footer()

def page_consulting():
    title = T("Cutting Knots Consulting · Corsi sull'IA e consulenza tecnica", 'Cutting Knots Consulting · AI courses and technical consulting')
    desc = T("Corsi sull'IA per i team aziendali, consulenza su modelli 3D, simulazioni e gestionali, Solution Architect e ricerca e sviluppo IA, da consulenti esterni.",
             'AI courses for company teams, consulting on 3D models, simulations and management systems, a Solution Architect and AI R&D, as external consultants.')
    detail = {
        'courses': ([T('Dal livello introduttivo per tutti ai laboratori pratici per ruolo', 'From an introduction for everyone to hands-on labs by role'),
                     T("Esempi presi dal vostro lavoro, non casi generici", 'Examples taken from your work, not generic cases'),
                     T("Uso sicuro e consapevole degli strumenti di intelligenza artificiale", 'Safe, informed use of AI tools')],
                    T('Chiedi un corso per il team', 'Ask about a course for your team'), T("Corso sull'intelligenza artificiale per il team", 'AI course for our team')),
        'industrial': ([T('Modelli 3D: preparazione, semplificazione e scambio dei file', '3D models: preparing, simplifying and exchanging files'),
                        T('Simulazioni a supporto delle decisioni di progetto e di produzione', 'Simulations to support design and production decisions'),
                        T('Gestionali, ERP e PLM: analisi, scelta e integrazione', 'Management systems, ERP and PLM: analysis, choice and integration')],
                       T('Chiedi una consulenza', 'Ask for a consultation'), T('Consulenza industriale', 'Industrial consulting')),
        'architect': ([T('Architettura delle soluzioni e scelta delle tecnologie', 'Solution architecture and technology choices'),
                       T('Valutazione di fornitori e offerte, con una scelta motivata', 'Assessing vendors and offers, with a reasoned choice'),
                       T("Coordinamento dell'implementazione fino al rilascio", 'Coordinating the implementation through to release')],
                      T('Chiedi un Solution Architect', 'Ask for a Solution Architect'), T('Solution Architect esterno', 'External Solution Architect')),
        'rnd': ([T('Studio di fattibilità e scelta dei modelli', 'Feasibility study and model choice'),
                 T('Prototipo funzionante sui vostri dati', 'A working prototype on your data'),
                 T('Passaggio di competenze al vostro team', 'Handing the know-how over to your team')],
                T('Parliamo del progetto', "Let's talk about the project"), T('Ricerca e sviluppo IA', 'AI research and development')),
    }
    cards = ''
    for k, p, t, d in consulting_items():
        ticks, cta, subj = detail[k]
        cards += f'''<li class="card" id="{k}">{ico(p)}<h3>{t}</h3><p>{d}</p><ul class="ticks">{''.join(f'<li>{x}</li>' for x in ticks)}</ul>
      <a class="more" href="{mailto(subj)}">{cta} {ARROW}</a></li>'''
    how = [(T('Consulenti esterni', 'External consultants'), T('Lavoriamo accanto al vostro team, senza sostituirlo: le decisioni restano vostre.', 'We work alongside your team without replacing it: the decisions stay yours.')),
           (T('Dagli obiettivi', 'From your goals'), T("Partiamo da cosa l'azienda vuole ottenere, non da una tecnologia da vendere.", 'We start from what the company wants to achieve, not from a technology to sell.')),
           (T('Indipendenti da Enterprise', 'Independent of Enterprise'), T('Una consulenza non vi impegna a comprare i nostri prodotti o progetti.', "A consultation doesn't commit you to buying our products or projects.")),
           (T('Competenze che restano', 'Skills that stay'), T('Ogni attività lascia documenti, decisioni motivate e persone formate.', 'Every engagement leaves documents, reasoned decisions and trained people.'))]
    faq = [(T('I corsi sono uguali per tutti?', 'Are the courses the same for everyone?'),
            T("No. Partiamo dai vostri casi d'uso e dai ruoli del team, e adattiamo contenuti e livello.", 'No. We start from your use cases and the roles in your team, and adapt content and level.')),
           (T('Dobbiamo usare i vostri prodotti?', 'Do we have to use your products?'),
            T('No. Consulting e Enterprise si possono scegliere separatamente o insieme.', 'No. Consulting and Enterprise can be chosen separately or together.')),
           (T('Lavorate in sede o da remoto?', 'Do you work on site or remotely?'),
            T('Entrambe le cose, a seconda dell\'attività: lo concordiamo all\'inizio.', 'Both, depending on the work: we agree on it at the start.'))]
    body = band('Cutting Knots Consulting', T('Competenze in più, <em>quando servono</em>.', 'Extra expertise, <em>when you need it</em>.'),
                T("Formiamo i vostri team sull'intelligenza artificiale e vi affianchiamo come consulenti esterni su progetti tecnici, dall'architettura alla ricerca.",
                  'We train your teams on artificial intelligence and support you as external consultants on technical projects, from architecture to research.'),
                f'<a class="btn btn-white" href="{mailto(T("Cutting Knots Consulting – richiesta", "Cutting Knots Consulting – enquiry"))}">{T("Chiedi una consulenza", "Ask for a consultation")}</a>')
    body += f'''<section class="sec">
  <div class="wrap stack">
    <p class="kicker">{T('Cosa facciamo', 'What we do')}</p>
    <h2 class="h2">{T('Quattro modi di <em>affiancarvi</em>.', 'Four ways to <em>support</em> you.')}</h2>
    <ul class="grid g2">{cards}</ul>
  </div>
</section>
<section class="sec alt">
  <div class="wrap stack">
    <p class="kicker">{T('Come lavoriamo', 'How we work')}</p>
    <h2 class="h2">{T('Dalla vostra parte del tavolo.', 'On your side of the table.')}</h2>
    <ul class="grid g4">{''.join(f'<li class="card"><h3>{a}</h3><p>{b}</p></li>' for a, b in how)}</ul>
  </div>
</section>
''' + faq_block(faq, T('Domande', 'Questions'))
    ld = {"@context": "https://schema.org", "@graph": webpage('consulting', title, desc) + [faq_ld(faq, 'consulting')]}
    return head('consulting', title, desc, ld) + header('consulting') + '<main id="main" tabindex="-1">\n' + body + close() + '</main>\n' + footer()

def page_small():
    title = T('Cutting Knots Small Solutions · Siti, e-commerce, gestionali', 'Cutting Knots Small Solutions · Websites, shops, small apps')
    desc = T('Siti web, e-commerce e microgestionali per realtà più piccole, con lo stesso metodo e la stessa cura dei progetti più grandi.',
             'Websites, e-commerce and small management apps for smaller organisations, with the same method and care as larger projects.')
    items = [(T('Siti web', 'Websites'), T('Veloci, leggibili da telefono, pronti per i motori di ricerca e facili da aggiornare.', 'Fast, readable on phones, ready for search engines and easy to update.')),
             ('E-commerce', T('Un negozio online con catalogo, pagamenti e spedizioni, costruito sui vostri prodotti.', 'An online shop with catalogue, payments and shipping, built around your products.')),
             (T('Microgestionali', 'Small management apps'), T('Piccole applicazioni per prenotazioni, iscrizioni, magazzino o turni, al posto di fogli e messaggi.', 'Small apps for bookings, sign-ups, stock or shifts, instead of spreadsheets and messages.'))]
    how = [(T('Un preventivo chiaro', 'A clear quote'), T('Cosa facciamo, in quanto tempo e a che prezzo, prima di cominciare.', 'What we do, how long it takes and what it costs, before we start.')),
           (T('Lo stesso standard', 'The same standard'), T('Strumenti e cura dei progetti più grandi, in proporzione.', 'The tools and care of larger projects, in proportion.')),
           (T('Autonomi dopo il rilascio', 'Independent after launch'), T('Vi lasciamo in grado di aggiornare contenuti e dati da soli.', 'We leave you able to update content and data yourselves.'))]
    body = band('Cutting Knots Small Solutions', T('Siti web, e-commerce e <em>microgestionali</em>.', 'Websites, e-commerce and <em>small management apps</em>.'),
                T('Per associazioni, studi, negozi e piccole imprese che hanno bisogno di uno strumento digitale fatto bene, senza un grande progetto.',
                  'For associations, practices, shops and small businesses that need a well-made digital tool, without a big project.'),
                f'<a class="btn btn-white" href="{mailto("Cutting Knots Small Solutions – " + T("richiesta", "enquiry"))}">{T("Chiedi un preventivo", "Ask for a quote")}</a>', 'small')
    body += f'''<section class="sec">
  <div class="wrap stack">
    <h2 class="kicker">{T('Cosa facciamo', 'What we do')}</h2>
    <ul class="grid g3">{''.join(f'<li class="card"><h3>{a}</h3><p>{b}</p></li>' for a, b in items)}</ul>
  </div>
</section>
<section class="sec alt">
  <div class="wrap stack">
    <h2 class="kicker">{T('Come lavoriamo', 'How we work')}</h2>
    <ul class="grid g3">{''.join(f'<li class="card"><h3>{a}</h3><p>{b}</p></li>' for a, b in how)}</ul>
    <p class="note">{T('Per progetti più grandi o integrati con i sistemi aziendali, guardate', 'For larger projects, or ones integrated with company systems, see')} <a href="{u('enterprise')}">Cutting Knots Enterprise</a>.</p>
  </div>
</section>
'''
    ld = {"@context": "https://schema.org", "@graph": webpage('small', title, desc)}
    return head('small', title, desc, ld) + header('small') + '<main id="main" tabindex="-1">\n' + body + close(T('Raccontateci cosa vi serve.', 'Tell us what you need.')) + '</main>\n' + footer()

def page_prodotti():
    title = T('Prodotti · Cutting Knots Enterprise', 'Products · Cutting Knots Enterprise')
    desc = T('Forma Simplifier, VIGIL e AIDA: a chi servono, cosa fanno oggi, a che punto sono e qual è il prossimo passo.',
             "Forma Simplifier, VIGIL and AIDA: who they're for, what they do today, where they stand and what comes next.")
    leg = ''.join(f'<li><b>{a}</b>{b}</li>' for a, b in stages())
    secs = ''
    for p in products():
        stg = ''.join(f'<li{" aria-current=\"step\"" if i + 1 == p["stage"] else ""}>{s[0]}</li>' for i, s in enumerate(stages()))
        name = (f'<h2><img src="/img/forma-simplifier-colore.svg" alt="" width="200" height="34" style="height:34px;width:auto" class="logo-ink"><img src="{p["logo"]}" alt="" width="200" height="34" style="height:34px;width:auto" class="logo-ink-dark"><span class="sr">{p["name"]}</span></h2>'
                if p.get('logo') else f'<h2>{p["name"]}</h2>')
        fig = f'<figure class="shot"><img src="{p["img"]}" alt="{esc(p["alt"])}" width="{p["w"]}" height="{p["h"]}" loading="lazy"{" style=\"background:#262626\"" if p.get("contain") else ""}><figcaption>{esc(p["cap"])}</figcaption></figure>'
        extra = ''
        if p['id'] == 'forma':
            extra = f'''<div class="metrics"><div><b>−94,3%</b><span>{T('dimensione del file', 'file size')}</span></div><div><b>{T('86,1 s', '86.1 s')}</b><span>{T('tempo di elaborazione', 'processing time')}</span></div></div>
            <p class="subj">{T('Risultato di un singolo test su un robot KUKA, non una media.', 'Result of a single test on a KUKA robot, not an average.')}</p>'''
            if L == 'en': extra = extra.replace('−94,3%', '−94.3%')
        if p.get('img2'):
            extra += f'<figure class="shot"><img src="{p["img2"]}" alt="{esc(p["cap2"])}" width="{p["w2"]}" height="{p["h2"]}" loading="lazy"><figcaption>{esc(p["cap2"])}</figcaption></figure>'
        secs += f'''<article class="pd" id="{p['id']}">
  <div class="stack" style="gap:14px">
    <p class="cat">{p['cat']}</p>{name}{f'<p class="former">{p["former"]}</p>' if p.get('former') else ''}
    <ol class="stages" aria-label="{T('Stato', 'Status')}">{stg}</ol>
    <dl><div><dt>{T('A chi serve', "Who it's for")}</dt><dd>{p['who']}</dd></div><div><dt>{T('Il problema', 'The problem')}</dt><dd>{p['problem']}</dd></div>
      <div><dt>{T('Cosa fa oggi', 'What it does today')}</dt><dd>{p['today']}</dd></div><div><dt>{T('Prossimo passo', 'Next step')}</dt><dd>{p['next']}</dd></div></dl>
    <div class="note"><strong>{T('Cosa puoi fare oggi', 'What you can do today')}</strong> · {p['can']}</div>
    <div class="acts"><a class="btn btn-ink" href="{mailto(p['subj'])}">{p['cta']}</a></div>
    <p class="subj">{T("L'oggetto dell'email è già compilato.", 'The email subject is already filled in.')}</p>
  </div>
  <div class="stack" style="gap:14px">{fig}{extra}</div>
</article>'''
    body = band('Cutting Knots Enterprise', T('I nostri <em>prodotti</em>.', 'Our <em>products</em>.'),
                T('Software nostro per problemi ricorrenti. Nessuno è ancora un prodotto in uso: per ognuno trovi a che punto è e cosa si può fare oggi.',
                  "Our own software for recurring problems. None is in general use yet: for each one you'll find where it stands and what can be done today."), cls='small')
    body += f'''<section class="sec" style="padding-bottom:0">
  <div class="wrap stack">
    <p class="kicker">{T('Come leggere lo stato', 'How to read the status')}</p>
    <ul class="legend">{leg}</ul>
  </div>
</section>
<section class="sec" style="padding-top:24px"><div class="wrap">{secs}</div></section>
'''
    apps = [{"@type": "SoftwareApplication", "name": p['name'], "description": p['short'], "applicationCategory": "BusinessApplication",
             "url": f"{SITE}{u('prodotti')}#{p['id']}", "publisher": {"@id": f"{SITE}/#org"}} for p in products()]
    ld = {"@context": "https://schema.org", "@graph": webpage('prodotti', title, desc) + apps}
    return head('prodotti', title, desc, ld) + header('prodotti') + '<main id="main" tabindex="-1">\n' + body + close() + '</main>\n' + footer()

def page_esperienze():
    title = T('Esperienze · Cutting Knots', 'Experience · Cutting Knots')
    desc = T('Sei progetti realizzati dalle persone del team in automotive, sanità, eventi e ricerca: contesto, problema, intervento e risultato.',
             'Six projects delivered by people on the team in automotive, healthcare, events and research: context, problem, what was done and result.')
    cards = ''
    for e in experiences():
        cards += f'''<li class="xpc" id="{e['id']}"><span class="sector">{e['sector']}</span><h2>{e['title']}</h2>
      <dl><div><dt>{T('Contesto', 'Context')}</dt><dd>{e['ctx']}</dd></div><div><dt>{T('Problema', 'Problem')}</dt><dd>{e['prob']}</dd></div>
      <div><dt>{T('Intervento', 'What was done')}</dt><dd>{e['did']}</dd></div><div><dt>{T('Risultato', 'Result')}</dt><dd>{e['res']}</dd></div></dl>
      {f'<small>{e["note"]}</small>' if e['note'] else ''}</li>'''
    body = band(T('Esperienze', 'Experience'), T('Nodi già <em>tagliati</em>.', 'Knots already <em>cut</em>.'),
                T('Sei progetti realizzati dalle persone del team, in automotive, sanità, eventi e ricerca.', 'Six projects delivered by people on our team, across automotive, healthcare, events and research.'), cls='small')
    body += f'''<section class="sec">
  <div class="wrap stack">
    <p class="note">{T('Questi progetti sono stati realizzati in <strong>precedenti realtà lavorative</strong>: non sono clienti né progetti commissionati a Cutting Knots. Li mostriamo perché raccontano cosa sappiamo fare.',
                       'These projects were delivered in <strong>previous roles</strong>: they are not Cutting Knots clients or commissions. We show them because they tell you what we can do.')}</p>
    <ul class="xps">{cards}</ul>
  </div>
</section>
'''
    ld = {"@context": "https://schema.org", "@graph": webpage('esperienze', title, desc)}
    return head('esperienze', title, desc, ld) + header('esperienze') + '<main id="main" tabindex="-1">\n' + body + close() + '</main>\n' + footer()

def page_chi():
    title = T('Chi siamo · Cutting Knots', 'About · Cutting Knots')
    desc = T('Cutting Knots è un partner tecnologico per le aziende: prodotti e progetti software, formazione e consulenza. Tre fondatori, competenze complementari.',
             'Cutting Knots is a technology partner for companies: software products and projects, training and consulting. Three founders, complementary skills.')
    facts = [(T('Cosa facciamo', 'What we do'), T('Prodotti e progetti software · formazione e consulenza', 'Software products and projects · training and consulting')),
             (T('Dove ha lavorato il team', 'Where our team has worked'), T('Automotive, sanità, eventi, ricerca, banca e finanza', 'Automotive, healthcare, events, research, banking and finance')),
             (T('Come', 'How'), T("Dall'analisi all'implementazione, con un solo interlocutore", 'From analysis to implementation, with one point of contact'))]
    skills = [(T('Sviluppo software e low-code', 'Software and low-code development'), T('Applicazioni web e piattaforme come Mendix.', 'Web applications and platforms such as Mendix.')),
              (T('Intelligenza artificiale', 'Artificial intelligence'), T('Analisi documentale, automazione, computer vision.', 'Document analysis, automation, computer vision.')),
              (T('Integrazione di sistemi', 'Systems integration'), T('ERP, PLM e sistemi operativi che si parlano.', 'ERP, PLM and operational systems that talk.')),
              (T('Processi aziendali', 'Business processes'), T('Analisi dei flussi e indicatori misurabili.', 'Flow analysis and measurable indicators.'))]
    way = [(T('Dagli obiettivi', 'From your goals'), T("Partiamo da cosa l'azienda vuole ottenere e da come lavora oggi, non da una tecnologia da vendere.", 'We start from what the company wants to achieve and how it works today, not from a technology to sell.')),
           (T('Sviluppo condiviso', 'Shared development'), T('Definiamo il percorso insieme al cliente e lo portiamo avanti con lui, passo dopo passo.', 'We define the path together with the client and move it forward with them, step by step.')),
           (T('Attenzione ai risultati', 'Focus on results'), T("Indicatori concordati fin dall'inizio, per sapere se il nodo è stato davvero tagliato.", 'Indicators agreed from the start, so you know whether the knot was really cut.'))]
    body = band(T('Chi siamo', 'About'), T('Il nome è il <em>metodo</em>.', 'The name is the <em>method</em>.'),
                T('Cutting Knots è un partner tecnologico per le aziende: prodotti e progetti software, formazione e consulenza.', 'Cutting Knots is a technology partner for companies: software products and projects, training and consulting.'), cls='small')
    body += f'''<section class="sec">
  <div class="wrap stack">
    <h2 class="h2">{T('Tagliare, non sciogliere un filo alla volta.', "Cut it, don't untie it thread by thread.")}</h2>
    <p class="lead">{T('Cutting Knots vuol dire «tagliare i nodi». È il nome della nostra azienda di software, intelligenza artificiale e consulenza, con le divisioni Cutting Knots Enterprise, Cutting Knots Consulting e Cutting Knots Small Solutions.', 'Cutting Knots is the name of our software, artificial intelligence and consulting company, with the divisions Cutting Knots Enterprise, Cutting Knots Consulting and Cutting Knots Small Solutions.')}</p>
    <p class="lead">{T("In ogni azienda c'è un nodo: un processo fatto a mano da anni, due sistemi che non si parlano, dati sparsi in troppi posti. Spesso si prova a scioglierlo un filo alla volta, e passano mesi.", "Every company has a knot: a process done by hand for years, two systems that don't talk, data spread across too many places. People often try to untie it one thread at a time, and months go by.")}</p>
    <p class="lead">{T("Noi partiamo dagli obiettivi dell'azienda e scegliamo il percorso più netto: sviluppare una soluzione, integrare le tecnologie giuste o adottarne una esistente. E restiamo al vostro fianco dall'analisi iniziale all'implementazione.", 'We start from the company\'s goals and choose the cleanest path: build a solution, integrate the right technologies or adopt an existing one. And we stay with you from first analysis to implementation.')}</p>
    <ul class="grid g3" style="margin-top:12px">{''.join(f'<li class="card"><p class="kicker">{a}</p><h3>{b}</h3></li>' for a, b in facts)}</ul>
  </div>
</section>
<section class="sec alt">
  <div class="wrap stack">
    <p class="kicker">{T('Il team', 'The team')}</p>
    <h2 class="h2">{T('Tre fondatori, competenze complementari.', 'Three founders, complementary skills.')}</h2>
    <p class="lead">{T('Abbiamo maturato la nostra esperienza in precedenti realtà lavorative, su progetti in automotive, sanità, eventi, ricerca e banca. Ogni progetto ha accanto le competenze che servono.', 'We built our experience in previous roles, on projects in automotive, healthcare, events, research and banking. Every project gets the skills it needs.')}</p>
    <ul class="grid g4">{''.join(f'<li class="card"><h3>{a}</h3><p>{b}</p></li>' for a, b in skills)}</ul>
    {more(u('esperienze'), T('Vedi i progetti del team', "See the team's projects"))}
  </div>
</section>
<section class="sec">
  <div class="wrap stack">
    <p class="kicker">{T('Come lavoriamo', 'How we work')}</p>
    <h2 class="h2">{T('Insieme, <em>dall\'inizio</em>.', 'Together, <em>from the start</em>.')}</h2>
    <ul class="grid g3">{''.join(f'<li class="card"><h3>{a}</h3><p>{b}</p></li>' for a, b in way)}</ul>
  </div>
</section>
'''
    ld = {"@context": "https://schema.org", "@graph": webpage('chi', title, desc)}
    return head('chi', title, desc, ld) + header('chi') + '<main id="main" tabindex="-1">\n' + body + close() + '</main>\n' + footer()

def page_contatti():
    title = T('Contatti · Cutting Knots', 'Contact · Cutting Knots')
    desc = T('Scrivete a info@cuttingknots.com per un progetto, un corso, una consulenza o uno dei nostri prodotti. Rispondiamo entro due giorni lavorativi.',
             'Write to info@cuttingknots.com about a project, a course, a consultation or one of our products. We reply within two working days.')
    topics = [('Cutting Knots Enterprise', T('Cutting Knots Enterprise – nuovo progetto', 'Cutting Knots Enterprise – new project'), T('Un prodotto o un progetto su misura', 'A product or a custom project')),
              ('Cutting Knots Consulting', T('Cutting Knots Consulting – richiesta', 'Cutting Knots Consulting – enquiry'), T('Un corso o una consulenza', 'A course or a consultation')),
              ('Cutting Knots Small Solutions', 'Cutting Knots Small Solutions – ' + T('richiesta', 'enquiry'), T('Un sito, un e-commerce o un microgestionale', 'A website, an online shop or a small app'))]
    topics += [(p['name'], p['subj'], stages()[p['stage'] - 1][0]) for p in products()]
    tl = ''.join(f'<li class="card" style="padding:18px 20px;gap:4px"><a class="more" style="min-height:0" href="{mailto(s)}">{n} {ARROW}</a><p style="font-size:14px">{d}</p></li>' for n, s, d in topics)
    what = [(T('Cosa fate', 'What you do'), T('Il settore e quante persone sono coinvolte nel processo.', 'Your sector and how many people are involved in the process.')),
            (T("Dov'è il nodo", 'Where the knot is'), T('Il passaggio che richiede più tempo o crea più errori.', 'The step that takes the most time or causes the most errors.')),
            (T('Cosa vorreste', "What you'd like"), T('Come sarebbe la giornata se il problema non ci fosse più.', 'What the day would look like without the problem.'))]
    body = band(T('Contatti', 'Contact'), T('Hai un nodo da <em>tagliare</em>?', 'Got a knot to <em>cut</em>?'),
                T('Scriveteci per un progetto, un corso, una consulenza o uno dei nostri prodotti. Rispondiamo entro due giorni lavorativi.', 'Write to us about a project, a course, a consultation or one of our products. We reply within two working days.'), cls='small')
    body += close(T('Scriveteci', 'Write to us'), T('Una persona del team vi risponde entro due giorni lavorativi.', 'A person from the team replies within two working days.')).replace('style="padding-top:24px"', '')
    body += f'''<section class="sec alt">
  <div class="wrap stack">
    <p class="kicker">{T("L'oggetto dell'email è già pronto", 'The email subject is ready')}</p>
    <h2 class="h2">{T('Di cosa volete parlarci?', 'What would you like to talk about?')}</h2>
    <ul class="grid g3">{tl}</ul>
  </div>
</section>
<section class="sec">
  <div class="wrap stack">
    <p class="kicker">{T('Cosa scriverci', 'What to write')}</p>
    <h2 class="h2">{T('Tre righe bastano.', 'Three lines are enough.')}</h2>
    <ul class="grid g3">{''.join(f'<li class="card"><h3>{a}</h3><p>{b}</p></li>' for a, b in what)}</ul>
    <p class="kicker" style="margin-top:20px">{T('Cosa succede dopo', 'What happens next')}</p>
    {steps([(T('Vi rispondiamo', 'We reply'), T('Entro due giorni lavorativi, da una persona del team.', 'Within two working days, from a person on the team.')),
            (T('Ne parliamo', 'We talk'), T('Se possiamo aiutarvi, vi proponiamo una prima conversazione per capire meglio.', 'If we can help, we suggest a first conversation to understand better.'))]).replace('class="steps"', 'class="steps" style="max-width:720px"')}
    <p>{T('Ci trovate anche su', 'You can also find us on')} <a href="{LINKEDIN}" rel="noopener">LinkedIn</a>.</p>
  </div>
</section>
'''
    ld = {"@context": "https://schema.org", "@graph": webpage('contatti', title, desc)}
    return head('contatti', title, desc, ld) + header('contatti') + '<main id="main" tabindex="-1">\n' + body + '</main>\n' + footer()

def page_404():
    global L
    L = 'it'
    title = 'Cutting Knots · Pagina non trovata'
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": title}
    h = head('home', title, 'La pagina che cerchi non c\'è.', ld).replace(f'<link rel="canonical" href="{SITE}/">\n', '').replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">')
    body = band('404', 'Questo nodo <em>non esiste</em>.', 'La pagina che cerchi non c\'è. <span lang="en">This page doesn\'t exist.</span>',
                '<a class="btn btn-white" href="/">Torna alla home</a><a class="btn btn-ghost" href="/en" lang="en">English site</a>')
    return h + header('home') + '<main id="main" tabindex="-1">\n' + body + '</main>\n' + footer()

PAGES = {'home': page_home, 'enterprise': page_enterprise, 'consulting': page_consulting, 'small': page_small,
         'prodotti': page_prodotti, 'esperienze': page_esperienze, 'chi': page_chi, 'contatti': page_contatti}

def out_file(path):
    if path == '/': return 'index.html'
    return path.strip('/') + '.html'

def main():
    global L
    for f in ('site.css', 'site.js'):
        shutil.copy(os.path.join(SRC, f), os.path.join(ROOT, f))
    for lang in ('it', 'en'):
        L = lang
        for key, fn in PAGES.items():
            p = os.path.join(ROOT, out_file(u(key)))
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, 'w').write(fn())
    open(os.path.join(ROOT, '404.html'), 'w').write(page_404())
    # sitemap with language alternates
    rows = []
    for key in PAGES:
        it, en = URL[key]
        alts = f'<xhtml:link rel="alternate" hreflang="it" href="{SITE}{it}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}{en}"/><xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{it}"/>'
        for path in (it, en):
            rows.append(f'  <url><loc>{SITE}{path}</loc><lastmod>{LASTMOD}</lastmod>{alts}</url>')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(rows) + '\n</urlset>\n')
    open(os.path.join(ROOT, 'llms.txt'), 'w').write(llms())

def llms():
    L_ = globals()
    global L
    L = 'en'
    prods = '\n'.join(f"  - {p['name']} — {stages()[p['stage']-1][0].lower()}. {p['short']}" for p in products())
    L = 'it'
    return f'''# Cutting Knots

> Cutting Knots (two words; the domain is cuttingknots.com, so it is sometimes written "Cutting Knots") is an Italian technology company for businesses, with its website at https://www.cuttingknots.com, organised in divisions. Cutting Knots Enterprise builds its own software products and custom software and AI projects. Cutting Knots Consulting offers AI courses for company teams, industrial consulting (3D models, simulations, management systems), Solution Architect services and end-to-end AI research and development, always as external consultants. Enterprise and Consulting can be chosen separately or together. Cutting Knots Small Solutions builds websites, e-commerce and small management apps for smaller organisations. The site is bilingual (Italian at /, English at /en). Contact: {EMAIL} (reply within two working days). LinkedIn: {LINKEDIN}

Key facts, stated as on the site:
- Name: Cutting Knots, two words, like "Bending Spoons". It is a company name, unrelated to knot theory, knot-tying or the "cut the knot" idiom. Official website: https://www.cuttingknots.com · LinkedIn: {LINKEDIN} · Email: {EMAIL}
- Custom projects address: manual and repetitive work (automation, also with AI); systems that don't talk (ERP, PLM and business systems such as SAP and Teamcenter); processes no tool covers (custom web applications and Mendix low-code); data that is hard to query (plain-language questions to databases, conversion to standards such as OMOP).
- Products and real status (none is in general use yet):
{prods}
  - Forma Simplifier test on a KUKA robot model: 55.98 MB to 3.21 MB (−94.3%) in 86.1 s. Single test, not an average.
- Experience: six projects delivered by people on the team in previous roles (not Cutting Knots clients or commissions), in automotive, healthcare, events and research. Team background also includes banking and finance projects.

## Pages (English)
- [Home](https://www.cuttingknots.com/en): the divisions, products, FAQ and contact
- [Enterprise](https://www.cuttingknots.com/en/enterprise): products, custom projects, AI projects, how it starts
- [Consulting](https://www.cuttingknots.com/en/consulting): AI courses, industrial consulting, Solution Architect, AI R&D
- [Small Solutions](https://www.cuttingknots.com/en/small-solutions): websites, e-commerce and small management apps
- [Products](https://www.cuttingknots.com/products): who each product is for, what it does today, status, next step
- [Experience](https://www.cuttingknots.com/experience): six team projects with context, problem, what was done and result
- [About](https://www.cuttingknots.com/about): the team and how it works
- [Contact](https://www.cuttingknots.com/contact): email and what to write

## Pagine (italiano)
- [Home](https://www.cuttingknots.com/): le divisioni, i prodotti, domande frequenti e contatti
- [Enterprise](https://www.cuttingknots.com/enterprise): prodotti, progetti su misura, progetti di IA, come si comincia
- [Consulting](https://www.cuttingknots.com/consulting): corsi sull'IA, consulenza industriale, Solution Architect, ricerca e sviluppo
- [Small Solutions](https://www.cuttingknots.com/small-solutions): siti web, e-commerce e microgestionali
- [Prodotti](https://www.cuttingknots.com/prodotti): a chi serve ogni prodotto, cosa fa oggi, stato e prossimo passo
- [Esperienze](https://www.cuttingknots.com/esperienze): sei progetti del team in precedenti realtà lavorative
- [Chi siamo](https://www.cuttingknots.com/chi-siamo): il team e come lavora
- [Contatti](https://www.cuttingknots.com/contatti): email e cosa scrivere

## Optional
- [Sitemap](https://www.cuttingknots.com/sitemap.xml)
'''

if __name__ == '__main__':
    main()
