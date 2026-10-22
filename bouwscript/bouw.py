"""Bouwt de statische pagina's van de JTS-site (topbalk/footer identiek op elke pagina)."""
import sys, os, json
UIT = sys.argv[1]
V = '4'
DOMEIN = 'https://www.jtstechniek.nl'  # cachebuster css/js

ICOON = {
  'elektricien': '<path d="M9 2v6M15 2v6M6 8h12v3a6 6 0 0 1-12 0zM12 17v5"/>',
  'zonnepanelen': '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>',
  'laadpalen': '<path d="M5 21V5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v16M3 21h14M15 9h2a2 2 0 0 1 2 2v4a1.5 1.5 0 0 0 3 0V8l-3-3M10.5 7 8 11h4l-2.5 4"/>',
  'thuisbatterijen': '<rect x="3" y="7" width="15" height="10" rx="2"/><path d="M21 11v2M7 11v2M11 11v2"/>',
  'de-hermontage': '<path d="M7 4v13M3 13l4 4 4-4M17 20V7M13 11l4-4 4 4"/>',
  'onderhoud': '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.2L3 17.8V21h3.2l6.3-6.3a4 4 0 0 0 5.2-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/>',
  'bedrijven': '<path d="M3 21h18M5 21V8l7-5 7 5v13M9 21v-6h6v6"/>',
  'service': '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.2L3 17.8V21h3.2l6.3-6.3a4 4 0 0 0 5.2-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/>',
  'advies': '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.4A8 8 0 1 1 21 12z"/>',
  'prijs': '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
  'inspectie': '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
  'bolt': '<path d="M13 2 4 14h6l-1 8 9-12h-6z"/>',
  'schild': '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
  'vink': '<path d="m5 12 5 5 9-10"/>',
}
def ic(naam, maat=15, kleur='#5C9BE8', dikte='2'):
    return f'<svg width="{maat}" height="{maat}" viewBox="0 0 24 24" fill="none" stroke="{kleur}" stroke-width="{dikte}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICOON[naam]}</svg>'

DIENSTEN = [
  ('elektricien', 'Elektricien', 'Groepenkasten, stopcontacten, storingen'),
  ('zonnepanelen', 'Zonnepanelen', 'Van één paneel tot honderden'),
  ('laadpalen', 'Laadpalen', 'Thuis en op de zaak'),
  ('thuisbatterijen', 'Thuisbatterijen', 'Noodstroom, niet terugleveren, EMS'),
  ('de-hermontage', 'De/Hermontage', 'Panelen eraf en weer terug'),
  ('onderhoud', 'Onderhoud', 'Inspectie, reiniging, storingen'),
]

def topbalk(actief):
    paneel = ''.join(
        f'<a href="{s}.html"{" class=\"actief\" aria-current=\"page\"" if s==actief else ""}><span class="icoon">{ic(s,14)}</span><span>{n}<span class="klein">{k}</span></span></a>'
        for s,n,k in DIENSTEN)
    def a(href, tekst, sleutel):
        cls = ' class="actief" aria-current="page"' if sleutel == actief else ''
        return f'<a href="{href}"{cls}>{tekst}</a>'
    dienst_actief = ' actief' if actief in [d[0] for d in DIENSTEN] else ''
    return f'''<header class="topbalk" id="topbalk">
  <a class="logo" href="index.html" aria-label="JTS Installatietechniek — naar de homepage">
    <img src="assets/logo/jts-logo-op-donker.png" alt="JTS Installatietechniek" width="421" height="178">
  </a>
  <div class="rechts">
    <nav class="menu" id="menu" aria-label="Hoofdmenu">
      <div class="menu-groep">
        <button class="menu-knop{dienst_actief}" type="button" aria-expanded="false" aria-controls="dienstenpaneel">Diensten <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></button>
        <div class="paneel" id="dienstenpaneel">{paneel}</div>
      </div>
      {a("bedrijven.html","Bedrijven","bedrijven")}
      {a("projecten.html","Projecten","projecten")}
      {a("kennisbank.html","Kennisbank","kennisbank")}
      {a("ons-verhaal.html","Ons verhaal","ons-verhaal")}
    </nav>
    <a class="knop knop--klein" href="aanvragen.html">Offerte aanvragen</a>
    <button class="hamburger" id="hamburger" type="button" aria-label="Menu openen" aria-expanded="false" aria-controls="menu"><span></span><span></span></button>
  </div>
</header>'''

FOOTER = '''<footer class="voet" id="contact">
  <div class="voet-raster">
    <div>
      <h2>Op zoek naar een betrouwbare partner voor al uw installaties?</h2>
      <a class="knop" href="aanvragen.html">Gratis offerte aanvragen</a>
    </div>
    <div class="kolommen">
      <div class="kolom">
        <div class="naam">Contact</div>
        <div class="inhoud"><a href="mailto:info@jtstechniek.nl">info@jtstechniek.nl</a><br><a href="tel:+31307816767">030 781 6767</a><br><a href="https://wa.me/31307816767" target="_blank" rel="noopener">WhatsApp</a></div>
      </div>
      <div class="kolom">
        <div class="naam">Gevestigd te</div>
        <div class="inhoud">Weteringpad 13A<br>3762 EN Soest<br><a href="https://www.nuzon.nl/" target="_blank" rel="noopener">Zusterbedrijf van NuZon&nbsp;B.V.</a></div>
      </div>
    </div>
  </div>
  <div class="onderbalk">
    <span>© <span id="jaar">2026</span> JTS Installatietechniek · KvK 88475751 · BTW NL864642727B01</span>
    <span class="voetlinks"><a href="projecten.html">Projecten</a><a href="kennisbank.html">Kennisbank</a><a href="ons-verhaal.html">Ons verhaal</a><a href="privacy.html">Privacy &amp; cookies</a><button type="button" id="cookie-instellingen" hidden>Cookie-instellingen</button></span>
  </div>
</footer>'''

WAAROM = '''<section class="woordmerk">
  <div class="groot-merk" aria-hidden="true">JTS INSTALLATIETECHNIEK</div>
  <div class="kader">
    <img class="beeld" src="assets/foto/team-jts-bus.jpg" alt="Het team van JTS Installatietechniek bij de bedrijfsbus" width="1500" height="1298" loading="lazy" style="object-position:50% 40%">
  </div>
  <div class="bij">
    <div class="zin">Vertrouwen is de reden waarom klanten voor JTS kiezen.</div>
    <div class="klein">Eerlijk advies, duidelijke afspraken en transparante offertes. Wij blijven aanspreekbaar en nemen verantwoordelijkheid voor ons werk.</div>
  </div>
</section>'''

def pagina(bestand, titel, omschrijving, actief, inhoud, body_klasse='', extra_js='', schema=None, og_beeld='assets/foto/hero-daken-zonnepanelen.jpg'):
    pad = '' if bestand == 'index.html' else bestand[:-5]
    url = f'{DOMEIN}/{pad}'
    blokken = [BEDRIJF_SCHEMA] + (schema or [])
    ld = ''.join('<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + '</script>\n' for s in blokken)
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titel}</title>
<meta name="description" content="{omschrijving}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="JTS Installatietechniek">
<meta property="og:title" content="{titel}">
<meta property="og:description" content="{omschrijving}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMEIN}/{og_beeld}">
<link rel="icon" href="assets/logo/jts-logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css?v={V}">
{ld}</head>
<body{f' class="{body_klasse}"' if body_klasse else ''}>

{topbalk(actief)}

<main id="top">
{inhoud}
</main>

{FOOTER}

<script src="js/site.js?v={V}"></script>{extra_js}
</body>
</html>
'''
    open(os.path.join(UIT, bestand), 'w').write(html)

USPS = f'''<div class="usps">
  <div class="usp"><span class="icoon">{ic("service",14)}</span>Professionele service</div>
  <div class="usp"><span class="icoon">{ic("advies",14)}</span>Deskundig advies</div>
  <div class="usp"><span class="icoon">{ic("prijs",14)}</span>Uitstekende prijs/kwaliteit</div>
  <div class="usp"><span class="icoon">{ic("inspectie",14)}</span>Gratis inspectie</div>
</div>'''

def dienst_hero(slug, badge, h1, intro, foto, alt, kaart_naam, kaart_waarde, kaart_onder, w, h):
    return f'''<section class="hero hero--dienst">
  <div class="hero-raster">
    <div class="hero-tekst">
      <nav class="kruimel" aria-label="Kruimelpad"><a href="index.html">Home</a><span>/</span><a href="index.html#diensten">Diensten</a><span>/</span><span>{badge}</span></nav>
      <div class="badge"><span class="stip">{ic(slug,10,"#fff","2.4")}</span><span class="tekst">{badge}</span></div>
      <h1>{h1}</h1>
      <p class="intro">{intro}</p>
      <div class="knoppen">
        <a class="knop" href="aanvragen.html?dienst={slug}">Gratis offerte aanvragen</a>
        <a class="knop knop--rand" href="tel:+31307816767">Bel 030 781 6767</a>
      </div>
    </div>
    <div class="hero-beeld">
      <div class="kader"><img class="beeld" src="assets/foto/diensten/{foto}" alt="{alt}" width="{w}" height="{h}" fetchpriority="high"></div>
      <div class="label"><span class="stip">{ic("zonnepanelen",10,"#fff","2.4")}</span>Uit eigen werk</div>
      <div class="glas glas--onder">
        <div class="kop"><span class="icoon">{ic("schild",11,"#fff","2.4")}</span><span class="naam">{kaart_naam}</span></div>
        <div class="waarde">{kaart_waarde}</div>
        <div class="onder">{kaart_onder}</div>
      </div>
    </div>
  </div>
</section>
{USPS}'''

def vinklijst(items):
    rijen = []
    for it in items:
        if isinstance(it, tuple):
            rijen.append(f'<li>{ic("vink",16)}<span><strong>{it[0]}</strong><span class="uitleg">{it[1]}</span></span></li>')
        else:
            rijen.append(f'<li>{ic("vink",16)}<span>{it}</span></li>')
    return '<ul class="vinklijst">' + ''.join(rijen) + '</ul>'

def split(eyebrow, h2, inleiding, items, foto, alt, w, h, knoptekst, slug):
    return f'''<section class="diensten">
  <div class="diensten-raster">
    <div>
      <div class="eyebrow">{eyebrow}</div>
      <h2>{h2}</h2>
      {f'<p class="inleiding">{inleiding}</p>' if inleiding else ''}
      {vinklijst(items)}
    </div>
    <div class="kader">
      <img class="beeld" src="assets/foto/diensten/{foto}" alt="{alt}" width="{w}" height="{h}" loading="lazy">
      <a class="knop" href="aanvragen.html?dienst={slug}">{knoptekst}</a>
    </div>
  </div>
</section>'''

def wit(eyebrow, h2, rechts, id_=''):
    return f'''<section class="wit"{f' id="{id_}"' if id_ else ''}>
  <div class="twee">
    <div><div class="eyebrow">{eyebrow}</div><h2>{h2}</h2></div>
    <div class="artikel" style="padding-top:8px">{rechts}</div>
  </div>
</section>'''

def tarieven(titel, rijen, noot=''):
    dl = ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a,b in rijen)
    return f'<div class="tarieven"><div class="naam">{titel}</div><dl>{dl}</dl>{f"<p class=\"noot\">{noot}</p>" if noot else ""}</div>'


BEDRIJF_SCHEMA = {
  "@context": "https://schema.org", "@type": "Electrician", "@id": DOMEIN + "/#bedrijf",
  "name": "JTS Installatietechniek", "url": DOMEIN + "/", "logo": DOMEIN + "/assets/logo/jts-logo.png",
  "image": DOMEIN + "/assets/foto/hero-daken-zonnepanelen.jpg",
  "email": "info@jtstechniek.nl", "telephone": "+31307816767",
  "address": {"@type": "PostalAddress", "streetAddress": "Weteringpad 13A", "postalCode": "3762 EN", "addressLocality": "Soest", "addressCountry": "NL"},
  "areaServed": ["Soest", "Baarn", "Amersfoort", "Zeist", "De Bilt", "Utrecht", "Hilversum", "Het Gooi", "Provincie Utrecht", "Nederland"],
  "foundingDate": "2022-12", "vatID": "NL864642727B01",
  "founder": [{"@type": "Person", "name": "Jesse Odijk"}, {"@type": "Person", "name": "Tjark Boot"}, {"@type": "Person", "name": "Stijn Ronner"}]
}

def kruimel_schema(naam, bestand):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMEIN + "/"},
      {"@type": "ListItem", "position": 2, "name": naam, "item": DOMEIN + "/" + bestand[:-5]}]}

def dienst_schema(naam, omschrijving, soort):
    return {"@context": "https://schema.org", "@type": "Service", "name": naam, "serviceType": soort, "description": omschrijving,
            "provider": {"@id": DOMEIN + "/#bedrijf"}, "areaServed": BEDRIJF_SCHEMA["areaServed"]}

def faq(vragen, titel='Veelgestelde vragen', eyebrow='Vragen'):
    """Geeft (html, schema) terug. vragen = [(vraag, antwoord-html), ...]"""
    import re as _re
    items = ''.join(f'<details{" open" if i == 0 else ""}><summary>{v}</summary><p>{a}</p></details>' for i, (v, a) in enumerate(vragen))
    html = f"""<section class="vragen">
  <div class="twee">
    <div><div class="eyebrow">{eyebrow}</div><h2>{titel}</h2><p class="vragen-sub">Staat uw vraag er niet tussen? Bel <a href="tel:+31307816767">030 781 6767</a> of stuur een <a href="https://wa.me/31307816767" target="_blank" rel="noopener">WhatsApp-bericht</a>.</p></div>
    <div class="faq">{items}</div>
  </div>
</section>"""
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
      {"@type": "Question", "name": v, "acceptedAnswer": {"@type": "Answer", "text": _re.sub(r'<[^>]+>', '', a)}} for v, a in vragen]}
    return html, schema

def lang(artikel, slug, review=None):
    """Lange SEO-tekst met een meescrollende offertekaart ernaast."""
    rev = ''
    if review:
        rev = f'<figure class="zij-review">{STERREN_KLEIN}<blockquote>“{review[0]}”</blockquote><figcaption>{review[1]} · Google-review</figcaption></figure>'
    return f"""<section class="lang">
  <div class="lang-raster">
    <article class="tekst">{artikel}</article>
    <aside class="lang-zij">
      <div class="zij-kaart">
        <div class="eyebrow" style="color:var(--accent-tint)">Gratis en vrijblijvend</div>
        <div class="zij-titel">Offerte in twee minuten</div>
        <p>Beantwoord een paar korte vragen, dan nemen wij binnen twee werkdagen contact op.</p>
        <a class="knop" href="aanvragen.html?dienst={slug}">Offerte aanvragen</a>
        <div class="zij-contact"><a href="tel:+31307816767">030 781 6767</a><a href="https://wa.me/31307816767" target="_blank" rel="noopener">WhatsApp</a></div>
        <ul class="zij-lijst"><li>{ic("vink",14)}Gratis inspectie op locatie</li><li>{ic("vink",14)}Werkt volgens NEN 1010 en NEN 3140</li><li>{ic("vink",14)}Vaste monteurs, één aanspreekpunt</li></ul>
      </div>
      {rev}
    </aside>
  </div>
</section>"""

def cta(tekst, knop, slug):
    return f'<div class="cta-blok"><p>{tekst}</p><a class="knop" href="aanvragen.html?dienst={slug}">{knop}</a></div>'

STERREN_KLEIN = '<span class="sterren" aria-label="5 van 5 sterren">' + ('<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>' * 5) + '</span>'

UIT_SCRIPT = os.path.abspath(__file__)
exec(open(os.path.join(os.path.dirname(__file__), 'paginas.py'), encoding='utf-8').read())
