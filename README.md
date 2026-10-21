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
- `404.html`: pagina di errore bilingue.
- `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `android-chrome-*.png`, `site.webmanifest`: icone.
- `og-image.png`: anteprima per i link condivisi (1200×630).
- `sitemap.xml`, `robots.txt`: per i motori di ricerca. Il villaggio è escluso dall'indicizzazione.
- `vercel.json`: URL senza `.html`, header di sicurezza, cache.

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
3. Imposta `www.cuttingknots.com` come redirect verso `cuttingknots.com`.

Attenzione: la posta `info@cuttingknots.com` usa i record `MX` del dominio. Quando modifichi i DNS **non toccare i record MX** (e gli eventuali TXT di SPF/DKIM), altrimenti l'email smette di funzionare.

Se il sito andrà su un dominio diverso, cerca e sostituisci `https://cuttingknots.com` in tutti i file `.html`, in `sitemap.xml` e in `robots.txt`.

## Provare in locale

Gli URL sono "puliti" (`/servizi` invece di `/servizi.html`), quindi serve un server che li gestisca:

```bash
npx serve .          # http://localhost:3000
# oppure, con la configurazione Vercel completa:
vercel dev
```

## Modificare i testi

I testi sono direttamente nei file HTML: ogni pagina esiste in due versioni (italiano e inglese), quindi una modifica va fatta in entrambe. I testi del villaggio sono in `ck.js` (oggetto `SEC`, una sezione `it` e una `en`).
