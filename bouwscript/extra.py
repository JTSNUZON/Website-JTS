# Projecten, kennisbank (+ artikelen) en privacy. Uitgevoerd vanuit paginas.py.
import json as _json

DATUM = '2026-10-22'
DATUM_NL = '22 oktober 2026'

def paginakop(badge, h1, intro, kruimel):
    return f'''<section class="pagina-kop">
  <nav class="kruimel" aria-label="Kruimelpad"><a href="index.html">Home</a>{kruimel}</nav>
  <div class="badge"><span class="stip">{ic("zonnepanelen",10,"#fff","2.4")}</span><span class="tekst">{badge}</span></div>
  <h1>{h1}</h1>
  <p class="intro">{intro}</p>
</section>'''

# ============================== PROJECTEN ==============================
PROJ = _json.load(open(os.path.join(os.path.dirname(UIT_SCRIPT), 'projecten.json'), encoding='utf-8'))
SOORTEN = [('alle', 'Alle'), ('zonnepanelen', 'Zonnepanelen'), ('elektra', 'Elektra'), ('laadpalen', 'Laadpalen'), ('batterijen', 'Omvormers &amp; batterijen'), ('hermontage', 'De/hermontage'), ('onderhoud', 'Onderhoud')]
LABEL = dict(SOORTEN)
tel = {s: sum(1 for p in PROJ if p[1] == s) for s, _ in SOORTEN}
tel['alle'] = len(PROJ)
filters = ''.join(f'<button type="button" class="filter" data-filter="{s}" aria-pressed="{"true" if s == "alle" else "false"}">{n}<span>{tel[s]}</span></button>' for s, n in SOORTEN if tel[s])
fotos = ''.join(f'<button type="button" data-soort="{c}" data-groot="assets/foto/projecten/{n}" aria-label="Vergroot: {a}"><img src="assets/foto/projecten/{n}" alt="{a}" width="{w}" height="{h}" loading="lazy"><span class="soort">{LABEL[c]}</span></button>' for n, c, a, (w, h) in PROJ)
proj = paginakop('Afgeronde projecten', 'Onze projecten.',
  'Van een woning in Soest tot honderden panelen op een bedrijfsdak: een selectie uit ons werk. Meer dan 10.000 zonnepanelen, meterkasten tot 3×250 ampère, laadpalen en thuisbatterijen. Mede mogelijk gemaakt door onze partners.',
  '<span>/</span><span>Projecten</span>')
proj += f'''<section class="galerij-sectie">
  <div class="filters" role="group" aria-label="Filter op soort project">{filters}</div>
  <div class="galerij" id="galerij">{fotos}</div>
</section>
<dialog class="lightbox" id="lightbox" aria-label="Projectfoto">
  <img src="" alt="">
  <div class="onder"><span id="lb-tekst"></span><div class="knoppen"><button type="button" id="lb-vorige" aria-label="Vorige foto">←</button><button type="button" id="lb-volgende" aria-label="Volgende foto">→</button><button type="button" id="lb-sluit" aria-label="Sluiten">✕</button></div></div>
</dialog>
<section class="vragen">
  <div class="twee">
    <div><div class="eyebrow">Uw project</div><h2>Zelf zo’n project?</h2><p class="vragen-sub">Beantwoord een paar korte vragen. Wij komen gratis kijken en maken een offerte op maat.</p></div>
    <div><div class="cta-blok" style="margin:0"><p>Offerte in twee minuten aangevraagd.</p><a class="knop" href="aanvragen.html">Offerte aanvragen</a></div></div>
  </div>
</section>
''' + WAAROM
pagina('projecten.html', 'Projecten: zonnepanelen, elektra en laadpalen | JTS Installatietechniek',
  'Bekijk projecten van JTS Installatietechniek: zonnepanelen op woningen en bedrijfsdaken, meterkasten, laadpalen, thuisbatterijen en de/hermontage.',
  'projecten', proj, extra_js=f'\n<script src="js/projecten.js?v={V}"></script>', schema=[kruimel_schema('Projecten', 'projecten.html')])

# ============================== KENNISBANK ==============================
ARTIKELEN = [
  {
    'bestand': 'salderingsregeling-2027.html', 'rubriek': 'Zonnepanelen',
    'titel': 'Einde salderingsregeling in 2027: wat betekent het voor uw zonnepanelen?',
    'kort': 'Per 1 januari 2027 stopt het salderen. Wat verandert er, wat betekent het voor uw opbrengst en wat kunt u nu al doen?',
    'beeld': 'assets/foto/diensten/zonnepanelen-pannendak.jpg', 'alt': 'Zonnepanelen op een pannendak', 'dienst': 'thuisbatterijen',
    'tekst': '''<p class="lead">Per 1 januari 2027 stopt de salderingsregeling. Dat is goed nieuws noch slecht nieuws: het verandert vooral hoe u het meeste uit uw zonnepanelen haalt. In dit artikel leggen we uit wat er verandert en wat u kunt doen.</p>
<h2>Wat is salderen?</h2>
<p>Zolang de salderingsregeling geldt, mag u de stroom die u met uw zonnepanelen teruglevert aan het net wegstrepen tegen de stroom die u afneemt. Levert u overdag 3.000 kWh terug en neemt u ’s avonds 3.000 kWh af, dan betaalt u per saldo bijna niets voor die stroom. Het net werkt dan als een gratis batterij.</p>
<h2>Wat verandert er per 1 januari 2027?</h2>
<p>Vanaf 2027 mag u niet meer salderen. Voor stroom die u teruglevert, krijgt u een terugleververgoeding van uw energieleverancier. Die vergoeding is in de regel lager dan de prijs die u betaalt voor stroom die u afneemt. Daarnaast rekenen veel leveranciers nu al terugleverkosten. Het gevolg: elke kWh die u zelf gebruikt, levert meer op dan een kWh die u teruglevert.</p>
<h2>Zijn zonnepanelen dan nog rendabel?</h2>
<p>Vaak wel. Stroom die u direct zelf verbruikt, hoeft u niet in te kopen, en dat blijft gewoon voordeel opleveren. Wat verandert, is dat de terugverdientijd meer afhangt van uw eigen verbruik op het moment dat de zon schijnt. Een huishouden dat overdag thuis is, of een bedrijf dat overdag draait, heeft daar een voorsprong.</p>
<h2>Vijf manieren om meer zonnestroom zelf te gebruiken</h2>
<ul>
<li><strong>Verschuif uw verbruik naar overdag.</strong> Laat de vaatwasser, wasmachine en droger draaien als de zon schijnt.</li>
<li><strong>Laad uw auto op zonnestroom.</strong> Met een slimme <a href="laadpalen.html">laadpaal</a> laadt de auto vooral als er zonne-energie over is.</li>
<li><strong>Plaats een thuisbatterij.</strong> Een <a href="thuisbatterijen.html">thuisbatterij</a> slaat uw overschot op voor de avond en kan ook als noodstroom dienen.</li>
<li><strong>Stuur alles slim aan met een EMS.</strong> Een energiemanagementsysteem laat zonnepanelen, batterij, laadpaal en warmtepomp samenwerken.</li>
<li><strong>Begrens de teruglevering.</strong> Met een energiemeter kan de omvormer worden afgeremd zodra u zou gaan terugleveren.</li>
</ul>
<h2>Wat is voor u verstandig?</h2>
<p>Dat hangt af van uw verbruik, het aantal panelen, uw aansluiting en uw energiecontract. Wij rekenen het vooraf eerlijk door. Soms is een thuisbatterij de beste stap, soms is slim schakelen genoeg, en soms is het advies: nog even wachten. Plan een gratis inspectie, dan kijken we samen naar uw situatie.</p>'''
  },
  {
    'bestand': 'groepenkast-vervangen.html', 'rubriek': 'Elektra',
    'titel': 'Groepenkast vervangen: wanneer is het nodig en waar let u op?',
    'kort': 'Een volle of verouderde groepenkast is onhandig en soms onveilig. Hoe herkent u dat het tijd is, en wat komt erbij kijken?',
    'beeld': 'assets/foto/diensten/elektricien-groepenkast.jpg', 'alt': 'Elektricien vervangt een groepenkast', 'dienst': 'elektricien',
    'tekst': '''<p class="lead">De groepenkast is het hart van uw elektrische installatie. Toch kijkt bijna niemand ernaar, tot er iets bij moet komen of de stroom steeds uitvalt. Wanneer is vervangen verstandig, en waar moet u op letten?</p>
<h2>Vijf signalen dat uw groepenkast aan vervanging toe is</h2>
<ul>
<li><strong>Alle groepen zijn bezet.</strong> Er is geen ruimte meer voor een laadpaal, inductiekookplaat, warmtepomp of thuisbatterij.</li>
<li><strong>De aardlekschakelaar slaat regelmatig af.</strong> Dat kan wijzen op overbelasting of een fout in de installatie.</li>
<li><strong>U heeft nog schroefzekeringen</strong> of een kast zonder goede aardlekbeveiliging.</li>
<li><strong>De kast wordt warm of u ruikt een brandlucht.</strong> Laat dit direct controleren.</li>
<li><strong>U gaat verduurzamen.</strong> Zonnepanelen, een thuisbatterij of een laadpaal vragen vaak om extra groepen of een 3-fase aansluiting.</li>
</ul>
<h2>Uitbreiden of vervangen?</h2>
<p>Heeft u alleen één extra groep nodig, en is uw kast in goede staat met voldoende ruimte? Dan is uitbreiden vaak voldoende. Is de kast verouderd, vol of niet meer volgens de huidige normen opgebouwd, dan is vervangen de veiligste en uiteindelijk vaak ook de voordeligste keuze.</p>
<h2>1-fase of 3-fase?</h2>
<p>Veel woningen hebben een 1-fase aansluiting. Voor een snelle laadpaal, een grotere warmtepomp, een thuisbatterij of een grotere zonnestroominstallatie kan een 3-fase aansluiting nodig of verstandig zijn. De aanvraag daarvoor loopt via uw netbeheerder. Wij adviseren eerlijk of het in uw situatie nodig is.</p>
<h2>Waar let een goede elektricien op?</h2>
<ul>
<li>Een opbouw volgens NEN 1010, met de juiste aardlekbeveiliging.</li>
<li>Voldoende reserve voor wat u de komende jaren wilt toevoegen.</li>
<li>Een logische indeling met duidelijke groepsaanduiding.</li>
<li>Een nette afwerking, zodat ook een volgende monteur meteen begrijpt hoe alles in elkaar zit.</li>
</ul>
<h2>Hoe gaat het in de praktijk?</h2>
<p>Wij komen eerst gratis kijken. We bekijken uw huidige kast, uw aansluiting en uw plannen, en maken daarna een duidelijke offerte. Het vervangen zelf gebeurt meestal binnen een dag; u zit dan een deel van die dag zonder stroom. Na afloop meten we de installatie door en leggen we uit welke groep waarvoor is. Meer weten? Lees over onze diensten als <a href="elektricien.html">elektricien</a>.</p>'''
  },
  {
    'bestand': 'thuisbatterij-noodstroom.html', 'rubriek': 'Thuisbatterij',
    'titel': 'Thuisbatterij als noodstroom: zo werkt het',
    'kort': 'Kan een thuisbatterij uw huis van stroom voorzien als het net uitvalt? Ja, als het goed is aangesloten. Dit moet u weten.',
    'beeld': 'assets/foto/diensten/thuisbatterij-bliq.jpg', 'alt': 'Thuisbatterij met noodstroomvoorziening', 'dienst': 'thuisbatterijen',
    'tekst': '''<p class="lead">Veel mensen denken dat een thuisbatterij automatisch stroom levert als het net uitvalt. Dat is niet zo. Zonder de juiste voorziening schakelt ook uw batterij uit. Met een goed ontworpen noodstroominstallatie blijven de lampen wél branden.</p>
<h2>Waarom gaat een gewone installatie uit bij stroomuitval?</h2>
<p>Omvormers van zonnepanelen en batterijen schakelen bij stroomuitval om veiligheidsredenen uit. Zo voorkomen ze dat ze stroom terugleveren op een net waar monteurs mogelijk aan het werk zijn. Wilt u noodstroom, dan moet uw installatie zich bij uitval veilig van het net kunnen loskoppelen en zelfstandig verder kunnen werken.</p>
<h2>Back-up met een ATS</h2>
<p>Wij koppelen de thuisbatterij aan een ATS: een Automatic Transfer Switch. Valt de netspanning weg, dan detecteert de ATS dat en schakelt de installatie automatisch over van netstroom naar de batterij. De aangesloten groepen blijven zonder onderbreking werken. Komt het net terug, dan schakelt het systeem weer terug. U hoeft er zelf niets voor te doen. Wij werken onder meer met batterijen van Bliq en Pylontech.</p>
<h2>Hele huis of alleen de belangrijkste groepen?</h2>
<p>U kunt kiezen welke groepen op de noodstroom komen. Vaak zijn dat de verlichting, de koelkast en vriezer, de cv-ketel of warmtepompregeling, internet en een paar stopcontacten. Hoe meer u aansluit, hoe groter de batterij en omvormer moeten zijn. Wij helpen u kiezen.</p>
<h2>Langdurige stroomuitval: de inverter generator</h2>
<p>Een batterij is een keer leeg. Voor langdurige uitval kunnen wij een inverter generator op het systeem aansluiten. Die laadt de batterij weer op en kan zo nodig direct stroom leveren. Inverter generatoren zijn relatief stil en zuinig, en daarmee geschikt voor langere inzet.</p>
<h2>Voor wie is noodstroom interessant?</h2>
<ul>
<li>Huishoudens die niet afhankelijk willen zijn van het net, bijvoorbeeld in het buitengebied.</li>
<li>Mensen die thuiswerken of thuis medische apparatuur gebruiken.</li>
<li>Bedrijven waar stroomuitval productieverlies of schade betekent.</li>
</ul>
<h2>Combineren met zonnepanelen en het einde van salderen</h2>
<p>Een noodstroombatterij doet in de praktijk vooral iets anders: elke dag uw zonnestroom opslaan voor de avond. Zeker na het einde van de salderingsregeling in 2027 is dat interessant. Lees meer over onze <a href="thuisbatterijen.html">thuisbatterijen</a>, of vraag gratis advies aan.</p>'''
  },
  {
    'bestand': 'installateur-failliet.html', 'rubriek': 'Onderhoud',
    'titel': 'Installateur van uw zonnepanelen failliet? Dit kunt u doen',
    'kort': 'Uw installateur is niet meer bereikbaar en er is iets mis met uw panelen of omvormer. Zo pakt u het aan.',
    'beeld': 'assets/foto/diensten/onderhoud-panelen.jpg', 'alt': 'Monteur controleert zonnepanelen', 'dienst': 'onderhoud',
    'tekst': '''<p class="lead">Het overkomt veel mensen: de omvormer geeft een foutmelding, de opbrengst valt terug, en het bedrijf dat de zonnepanelen plaatste, neemt niet meer op of is failliet. Gelukkig staat u niet met lege handen.</p>
<h2>Stap 1: breng uw installatie in kaart</h2>
<p>Zoek de gegevens van uw installatie op: de offerte of factuur, het merk en type van de panelen en de omvormer, en de datum van installatie. Maak een foto van het typeplaatje van de omvormer en van eventuele foutmeldingen op het display of in de app.</p>
<h2>Stap 2: check de fabrieksgarantie</h2>
<p>Ook als de installateur failliet is, kan de garantie van de fabrikant nog gelden. Omvormers en panelen hebben vaak een eigen fabrieksgarantie. Een nieuwe installateur kan namens u contact opnemen met de fabrikant. Bij oudere installaties is die garantie soms verlopen, of bestaat het merk niet meer. Dan kijken we naar een passend alternatief.</p>
<h2>Stap 3: laat de installatie controleren</h2>
<p>Veelvoorkomende problemen zijn een defecte omvormer, een losgeraakte of verbrande MC4-connector, beschadigde bekabeling of een kapotte optimizer. Een installateur meet het systeem door en vindt de oorzaak. Probeer zelf niets aan de bekabeling op het dak te doen: op de kabels tussen panelen en omvormer staat gelijkspanning.</p>
<h2>Stap 4: kies een vaste onderhoudspartner</h2>
<p>Wij nemen het onderhoud van installaties van andere bedrijven graag over. We beginnen met een inspectie, zodat we weten hoe uw systeem ervoor staat. Daarna kunt u kiezen voor losse service bij storingen, of voor een vast onderhoudscontract met een jaarlijkse controle. Zo weet u zeker dat er iemand is als er iets misgaat.</p>
<h2>Moet de hele installatie vervangen worden?</h2>
<p>Meestal niet. Zonnepanelen gaan lang mee; vaak is het de omvormer die na verloop van tijd vervangen moet worden. Soms is het wel verstandig om bij vervanging meteen te kijken naar een nieuwere omvormer die geschikt is voor een thuisbatterij, zeker met het einde van de salderingsregeling in 2027.</p>
<h2>Hulp nodig?</h2>
<p>Bekijk onze pagina over <a href="onderhoud.html">onderhoud en storingen</a>, of stuur ons een foto van de foutmelding via WhatsApp. Vaak kunnen we dan al inschatten wat er aan de hand is.</p>'''
  },
]

def kaart(a, kop='h2'):
    return f'''<a class="kennis-kaart" href="{a['bestand']}"><img src="{a['beeld']}" alt="{a['alt']}" loading="lazy"><div class="binnen"><span class="rubriek">{a['rubriek']}</span><{kop}>{a['titel']}</{kop}><p>{a['kort']}</p><span class="lees">Lees artikel →</span></div></a>'''

kb = paginakop('Kennisbank', 'Kennisbank.',
  'Heldere uitleg over zonnepanelen, thuisbatterijen, laadpalen en elektra. Geschreven door de monteurs van JTS, zonder verkooppraatjes.',
  '<span>/</span><span>Kennisbank</span>')
kb += f'<section class="kennis-sectie"><div class="kennis-raster">{"".join(kaart(a) for a in ARTIKELEN)}</div></section>' + WAAROM
pagina('kennisbank.html', 'Kennisbank: zonnepanelen, thuisbatterij en elektra | JTS Installatietechniek',
  'Uitleg over het einde van de salderingsregeling, thuisbatterijen als noodstroom, groepenkast vervangen en meer. Door de monteurs van JTS Installatietechniek.',
  'kennisbank', kb, schema=[kruimel_schema('Kennisbank', 'kennisbank.html')])

for a in ARTIKELEN:
    kop = f'''<section class="pagina-kop">
  <nav class="kruimel" aria-label="Kruimelpad"><a href="index.html">Home</a><span>/</span><a href="kennisbank.html">Kennisbank</a><span>/</span><span>{a['rubriek']}</span></nav>
  <div class="badge"><span class="stip">{ic("advies",10,"#fff","2.4")}</span><span class="tekst">{a['rubriek']}</span></div>
  <h1 style="font-size:clamp(34px,5vw,56px);max-width:22ch">{a['titel']}</h1>
  <p class="intro">{a['kort']}</p>
  <div class="artikel-meta"><span>Door JTS Installatietechniek</span><span>Bijgewerkt op {DATUM_NL}</span></div>
</section>'''
    artikel = f'<figure class="artikel-beeld"><img src="{a["beeld"]}" alt="{a["alt"]}"></figure>' + a['tekst'] + cta('Vragen over uw situatie? Wij komen gratis kijken.', 'Vraag gratis advies aan', a['dienst'])
    ander = [x for x in ARTIKELEN if x is not a][:3]
    ook = f'<section class="lees-ook"><h2>Lees ook</h2><div class="kennis-raster">{"".join(kaart(x, "h3") for x in ander)}</div></section>'
    schema = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a['titel'], "description": a['kort'],
              "image": DOMEIN + '/' + a['beeld'], "datePublished": DATUM, "dateModified": DATUM, "inLanguage": "nl-NL",
              "author": {"@id": DOMEIN + "/#bedrijf"}, "publisher": {"@id": DOMEIN + "/#bedrijf"},
              "mainEntityOfPage": DOMEIN + '/' + a['bestand'][:-5]}
    kruimel = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMEIN + "/"},
      {"@type": "ListItem", "position": 2, "name": "Kennisbank", "item": DOMEIN + "/kennisbank"},
      {"@type": "ListItem", "position": 3, "name": a['titel'], "item": DOMEIN + '/' + a['bestand'][:-5]}]}
    pagina(a['bestand'], a['titel'] + ' | JTS', a['kort'], 'kennisbank', kop + lang(artikel, a['dienst']) + ook,
           schema=[schema, kruimel], og_beeld=a['beeld'])

# ============================== PRIVACY ==============================
pv = paginakop('Privacy &amp; cookies', 'Privacyverklaring.', 'Hoe JTS Installatietechniek omgaat met uw persoonsgegevens en welke cookies deze website gebruikt.', '<span>/</span><span>Privacy</span>')
pv += f'''<section class="lang"><div class="lang-raster"><article class="tekst">
<p class="lead">JTS Installatietechniek gaat zorgvuldig om met uw gegevens. We vragen alleen wat we nodig hebben om u te helpen, en we verkopen niets door.</p>
<h2>Wie zijn wij?</h2>
<p>JTS Installatietechniek, Weteringpad 13A, 3762 EN Soest. KvK 88475751. E-mail: info@jtstechniek.nl, telefoon 030 781 6767.</p>
<h2>Welke gegevens verwerken wij?</h2>
<p>Als u een offerte aanvraagt, contact opneemt of klant bij ons wordt, verwerken wij de gegevens die u zelf invult of doorgeeft: uw naam, eventueel bedrijfsnaam, adres, e-mailadres, telefoonnummer, uw antwoorden over de situatie ter plekke en eventuele foto’s die u stuurt.</p>
<h2>Waarvoor gebruiken wij uw gegevens?</h2>
<ul><li>om contact met u op te nemen over uw aanvraag;</li><li>om een offerte te maken en de werkzaamheden uit te voeren;</li><li>om te factureren en te voldoen aan onze wettelijke (fiscale) verplichtingen;</li><li>om service en onderhoud te kunnen verlenen na oplevering.</li></ul>
<h2>Met wie delen wij gegevens?</h2>
<p>Aanvragen via het formulier op deze website worden verstuurd via een formulierdienst die de gegevens naar ons e-mailadres doorstuurt. Stuurt u ons een bericht via WhatsApp, dan verloopt dat via WhatsApp (Meta). Verder delen wij uw gegevens alleen met partijen die nodig zijn om de opdracht uit te voeren, zoals een netbeheerder of leverancier, of als de wet dat verplicht.</p>
<h2>Hoe lang bewaren wij uw gegevens?</h2>
<p>Niet langer dan nodig. Aanvragen die niet tot een opdracht leiden, verwijderen wij na afhandeling. Gegevens van klanten bewaren wij zolang dat nodig is voor service en garantie, en facturen zeven jaar, zoals de wet voorschrijft.</p>
<h2>Cookies en Google Analytics</h2>
<p>Deze website gebruikt Google Analytics om te meten hoe de site wordt gebruikt, bijvoorbeeld hoeveel bezoekers een offerte aanvragen. Analytics wordt pas geladen nadat u daar in de cookiebalk toestemming voor geeft. IP-adressen worden geanonimiseerd. Uw keuze bewaren wij in uw browser; via “Cookie-instellingen” onderaan elke pagina kunt u die keuze altijd wijzigen. Daarnaast onthoudt het aanvraagformulier tijdelijk uw antwoorden in uw browser, zodat u niets kwijtraakt als u even terugbladert. Die gegevens verdwijnen als u het tabblad sluit.</p>
<h2>Uw rechten</h2>
<p>U heeft het recht om uw gegevens in te zien, te laten corrigeren of te laten verwijderen, en om bezwaar te maken tegen het gebruik ervan. Stuur daarvoor een e-mail naar info@jtstechniek.nl. Bent u het niet eens met hoe wij met uw gegevens omgaan, dan kunt u een klacht indienen bij de Autoriteit Persoonsgegevens.</p>
<p><em>Laatst bijgewerkt: {DATUM_NL}.</em></p>
</article><aside class="lang-zij"></aside></div></section>'''
pagina('privacy.html', 'Privacyverklaring en cookies | JTS Installatietechniek', 'Hoe JTS Installatietechniek omgaat met persoonsgegevens en cookies.', 'privacy', pv)
