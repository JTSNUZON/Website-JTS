# Website JTS Installatietechniek

Statische site, geen frameworks of buildstap: de HTML-bestanden in de hoofdmap zijn wat er live komt (Vercel, `cleanUrls` via `vercel.json`).

## Pagina's aanpassen

Topbalk, footer en alle pagina-inhoud worden gegenereerd door `bouwscript/`. Pas daar de tekst aan en bouw opnieuw:

```bash
python3 bouwscript/bouw.py .
```

- `bouw.py` — topbalk, footer, gedeelde blokken, SEO-tags en gestructureerde data
- `paginas.py` — homepage en aanvraagpagina
- `diensten.py` — dienstpagina's, bedrijven en ons verhaal
- `extra.py` — projecten, kennisbank en privacy

Wijzig je `css/site.css` of een bestand in `js/`, verhoog dan `V` in `bouw.py` (cachebuster) en bouw opnieuw.

## Instellingen

- `js/site.js` — `WHATSAPP_NUMMER` en `GA_ID` (Google Analytics, leeg = uit)
- `js/aanvragen.js` — `FORMULIER.sleutel` (Web3Forms access key, leeg = mail-fallback)

## Lokaal bekijken

```bash
python3 -m http.server 4173
```
