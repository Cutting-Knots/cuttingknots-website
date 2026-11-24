# cuttingknots-website

Sito statico di Cutting Knots, pubblicato su Vercel.

Le pagine si generano con `python3 src/build.py` (dalla radice del repository):
testi, struttura e dati per Google stanno in `src/build.py`, stili e script in
`src/site.css` e `src/site.js`. La cartella `src` non viene pubblicata (`.vercelignore`).

Il villaggio (`villaggio.html`, `village.html`, `game.css`, `ck.js`) è a parte e non viene rigenerato.
