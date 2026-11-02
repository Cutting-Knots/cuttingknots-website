# CuttingKnots — sito web

Sito statico (HTML, CSS, JS, nessun build step) in italiano e inglese, pronto per Vercel.

## Struttura

| Pagina | Italiano | English |
|---|---|---|
| Home | `/` (index.html) | `/en` (en.html) |
| Chi siamo / About | `/chi-siamo` | `/about` |
| Servizi / Services | `/servizi` | `/services` |
| Prodotti / Products | `/prodotti` | `/products` |
| Esperienze / Experience | `/esperienze` | `/experience` |
| Contatti / Contact | `/contatti` | `/contact` |
| Easter egg | `/villaggio` | `/village` |

Altri file:

- `style.css`: stile del sito. `game.css`: stile pixel del solo easter egg. `ck.js`: script condiviso.
- `img/`: il cielo del brand (`horizon-1200.jpg`, `horizon-2400.jpg`) e le schermate dei prodotti.
- `404.html`: pagina di errore bilingue.
- `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `android-chrome-*.png`, `site.webmanifest`: icone.
- `og-image.png`: anteprima per i link condivisi (1200×630).
- `sitemap.xml`, `robots.txt`: per i motori di ricerca e gli assistenti IA (crawler elencati in modo esplicito). Il villaggio è escluso dall'indicizzazione.
- `llms.txt`: riassunto del sito per gli assistenti IA (ChatGPT, Claude, Perplexity…). Va aggiornato quando cambiano servizi o stato dei prodotti.
- Ogni pagina contiene dati strutturati schema.org (JSON-LD): organizzazione, sito, servizi, prodotti, domande frequenti.
- `vercel.json`: URL senza `.html`, header di sicurezza, cache.

## Tema chiaro e scuro

Il sito segue l'impostazione chiaro/scuro del sistema. Il pulsante sole/luna nella barra in alto cambia tema, e nel footer si può scegliere Automatico, Chiaro o Scuro. La scelta resta salvata nel browser (`localStorage`, chiave `ck-theme`). I colori dei due temi sono i token del design system CuttingKnots (vedi le linee guida del brand, sezione "Web themes").

## Deploy su Vercel

### Opzione A: da GitHub (consigliata)

1. Crea un repository su GitHub e carica il contenuto di questa cartella:
   ```bash
   git init
   git add .
   git commit -m "Sito CuttingKnots"
   git branch -M main
   git remote add origin https://github.com/<utente>/cuttingknots-web.git
   git push -u origin main
   ```
2. Su [vercel.com/new](https://vercel.com/new) importa il repository.
3. Impostazioni del progetto:
   - **Framework Preset:** Other
   - **Build Command:** lascia vuoto
   - **Output Directory:** lascia vuoto (la radice del repo)
4. Premi **Deploy**. Ogni `git push` su `main` pubblica una nuova versione; ogni altro branch crea un'anteprima.

### Opzione B: da terminale

```bash
npm i -g vercel        # una volta sola
vercel                 # primo deploy (anteprima); rispondi alle domande, va bene tutto di default
vercel --prod          # pubblica in produzione
```

## Dominio cuttingknots.com

1. Vercel → progetto → **Settings → Domains** → aggiungi `cuttingknots.com` e `www.cuttingknots.com`.
2. Dal pannello del registrar del dominio imposta i record DNS che Vercel mostra (di solito un record `A` per il dominio principale e un `CNAME` per `www`).
3. Usa `www.cuttingknots.com` come dominio principale e imposta `cuttingknots.com` come redirect permanente verso `www.cuttingknots.com`, conservando percorso e query string.

Il dominio canonico del sito è `https://www.cuttingknots.com`. La regola in `vercel.json` reindirizza soltanto l'host `cuttingknots.com` con stato **308**; gli URL di anteprima Vercel non sono coinvolti. Controlla che anche **Settings → Domains** abbia lo stesso verso: un redirect di dominio configurato al contrario può creare un ciclo.

Attenzione: la posta `info@cuttingknots.com` usa i record `MX` del dominio. Quando modifichi i DNS **non toccare i record MX** (e gli eventuali TXT di SPF/DKIM), altrimenti l'email smette di funzionare.

Se il sito andrà su un dominio diverso, aggiorna insieme canonical, hreflang, metadati social e JSON-LD nei file `.html`, gli URL in `sitemap.xml`, il riferimento Sitemap in `robots.txt`, i link in `llms.txt` e la regola host in `vercel.json`.

Dopo il deploy, verifica che `https://cuttingknots.com/servizi?check=seo` arrivi a `https://www.cuttingknots.com/servizi?check=seo` con un redirect permanente e che la destinazione risponda **200**. Controlla anche homepage, versione inglese e sitemap. Le condizioni `has` dei redirect non sono supportate da `vercel dev`: il controllo HTTP va eseguito sul deploy.

In Google Search Console invia `https://www.cuttingknots.com/sitemap.xml` usando una proprietà Dominio oppure la proprietà con prefisso `https://www.cuttingknots.com/`. Usa Controllo URL sulla homepage con `www` per verificare il canonical dichiarato e quello scelto da Google, poi richiedi l'indicizzazione dopo la correzione. Una sitemap letta correttamente non garantisce l'indicizzazione né una data di comparsa nei risultati.

## Provare in locale

Gli URL sono "puliti" (`/servizi` invece di `/servizi.html`), quindi serve un server che li gestisca:

```bash
npx serve .          # http://localhost:3000
# oppure, con la configurazione Vercel completa:
vercel dev
```

## Modificare i testi

I testi sono direttamente nei file HTML: ogni pagina esiste in due versioni (italiano e inglese), quindi una modifica va fatta in entrambe. I testi del villaggio sono in `ck.js` (oggetto `SEC`, una sezione `it` e una `en`).
