# Inhoud per pagina. Wordt uitgevoerd vanuit bouw.py (helpers staan daar).

# ============================== HOME ==============================
dienst_rijen = {
  'elektricien': ('Elektricien op maat', 'Van tuinverlichting tot stopcontacten, en van stroomuitval tot meterkasten.'),
  'zonnepanelen': ('Zonnepanelen', 'Het volledige proces, van één zonnepaneel tot grootschalige installaties.'),
  'laadpalen': ('Laadpalen', 'Uw auto voor de deur opladen? Wij vertellen u wat er bij u thuis mogelijk is.'),
  'thuisbatterijen': ('Thuisbatterij', 'Noodstroom, niet meer terugleveren en slim energiebeheer. Alle merken, tot off-grid.'),
  'de-hermontage': ('De/Hermontage', 'Panelen tijdelijk van het dak voor de dakdekker of schilder, en daarna weer terug.'),
  'onderhoud': ('Onderhoud', 'Onderhoud en storingen, ook als uw oude installateur niet meer bereikbaar is.'),
}
rijen_html = ''.join(
  f'''<a class="rij" href="{s}.html"><span class="icoon">{ic(s)}</span><div><div class="titel">{t}</div><div class="uitleg">{u}</div></div></a>'''
  for s,(t,u) in dienst_rijen.items())

STER = '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>'
STERREN = f'<span class="sterren" aria-label="5 van 5 sterren">{STER*5}</span>'

# Reviews: letterlijk zoals de klant ze op Google schreef — niet corrigeren.
REVIEWS = [
  ("Deze jonge en zeer professionele mannen, met heel goede omgangsvormen, kwamen in eerste instantie omvormers van onze zonnepanelen vervangen. Dit werd snel en professioneel uitgevoerd. Zij kwamen er achter dat een aantal van onze nokpannen stuk waren. Snel en professioneel hebben zij de hele nok vernieuwd. Er was nog net geen lekkage ontstaan en wij zijn zeer blij dat zij dit op tijd ontdekten en voor zover zien kwaliteit goed.",
   "Edith De Weger-Dahmen", "de-weger-dakwerk.jpg", "Monteurs van JTS aan het werk op het dak en de nok van een woning"),
  ("Deze jonge mannen hebben bij ons de zonnepanelen gedemonteerd en later, na de nieuwe dakpannen weer hermonteerd.\nWij zijn heel tevreden van JTS. Echt vriendelijke, meedenkende, professionele en eerlijke werkers, die hun afspraken na kwamen.\nDe kosten waren heel transparant en wij kwamen niet voor verassingen te staan. Ga zo door en succes met jullie bedrijf!",
   "Ria en Henny Damen", "damen-zonnepanelen.jpg", "Monteurs die zonnepanelen terugplaatsen op een pannendak"),
  ("Deze getalenteerde en jonge heren hebben mijn dak voorzien van een prachtige set zonnepanelen. Netjes op tijd, communicatief geweldig, professioneel en denken met je mee. Het resultaat mag er zeker zijn, zoals het netjes verwerken van de omvormer in de ombouwkast van de CV.\n\nIk zie ze graag nog eens terug voor wat andere klussen in de nabije toekomst!",
   "Jordy Willekens", "willekens-omvormer.jpg", "Omvormer netjes weggewerkt in de ombouwkast naast de cv-ketel"),
  ("Wij hebben 48 zonnepanelen en wilde een 50 KW batterij laten installeren. Dat hebben ze snel en zeer professioneel gedaan!! Alles mooi weggewerkt , nieuwe stoppenkast en een aansluiting voor een eventuele generator. Buiten het feit dat w hun werk zeer goed hebben gedaan zijn het ook nog aardige jongens !!! Zeer aan te bevelen",
   "jonas Bosscha", None, None),
]
def review(t, naam, foto, alt):
    img = f'<img src="assets/reviews/{foto}" alt="{alt}" loading="lazy">' if foto else ''
    return f'''<figure class="review{'' if foto else ' zonder-foto'}" style="margin:0"><div>{STERREN}<blockquote>{t}</blockquote><figcaption class="wie">{naam} <span>· Google-review</span></figcaption></div>{img}</figure>'''
reviews_html = ''.join(review(*r) for r in REVIEWS)

home = f'''
<!-- ============ HERO ============ -->
<section class="hero">
  <div class="hero-raster">
    <div class="hero-tekst">
      <div class="badge">
        <span class="stip">{ic("bolt",10,"#fff","2.6")}</span>
        <span class="tekst">Elektrotechniek &amp; duurzame energie</span>
      </div>
      <h1>Techniek die klopt.</h1>
      <p class="intro">Bij JTS Installatietechniek draait het om techniek die klopt. Wij realiseren complete, technische en duurzame installaties voor zowel particulieren als bedrijven. Altijd veilig, netjes en met oog op de toekomst.</p>
      <div class="knoppen">
        <a class="knop" href="aanvragen.html">Gratis offerte aanvragen</a>
        <a class="knop knop--rand" href="#diensten">Bekijk diensten</a>
      </div>
    </div>

    <div class="hero-beeld">
      <div class="kader">
        <img class="beeld" src="assets/foto/hero-daken-zonnepanelen.jpg" alt="Zonnepanelen door JTS gelegd op een groot bedrijfsdak" width="1500" height="1125" fetchpriority="high">
      </div>
      <div class="label"><span class="stip">{ic("zonnepanelen",10,"#fff","2.4")}</span>Uit eigen werk</div>
      <div class="glas glas--links">
        <div class="kop"><span class="icoon">{ic("bolt",11,"#fff","2.4")}</span><span class="naam">Zonnepanelen</span></div>
        <div class="waarde">10.000+</div>
        <div class="balk"><div></div></div>
        <div class="onder">geïnstalleerd, met vele foutloze Scope-12-keuringen</div>
      </div>
      <div class="glas glas--onder">
        <div class="kop"><span class="icoon">{ic("schild",11,"#fff","2.4")}</span><span class="naam">Werkt volgens</span></div>
        <div class="waarde">NEN 1010</div>
        <div class="onder">en NEN 3140 · VCA-gecertificeerd</div>
      </div>
    </div>
  </div>
</section>

<!-- ============ DIENSTEN ============ -->
<section class="diensten" id="diensten">
  <div class="diensten-raster">
    <div>
      <div class="eyebrow">Diensten</div>
      <h2>Wat wij doen.</h2>
      <p class="inleiding">Bij nieuwbouw, renovatie, uitbreiding of verduurzaming zorgen wij dat de elektrotechnische en duurzame installaties kloppen — nu én later.</p>
      <div class="lijst">{rijen_html}</div>
    </div>
    <div class="kader">
      <img class="beeld" src="assets/foto/monteurs-op-dak.jpg" alt="Monteurs van JTS bevestigen zonnepanelen op een schuin bedrijfsdak" width="1500" height="844" loading="lazy">
      <a class="knop" href="aanvragen.html">Vraag een offerte aan</a>
    </div>
  </div>
</section>

<!-- ============ BEDRIJVEN / PIEKBESPARING ============ -->
<section class="wit" id="bedrijven">
  <div class="twee">
    <div>
      <div class="eyebrow">Bedrijven</div>
      <h2>Besparen op pieken en ruimte maken voor groei.</h2>
    </div>
    <div style="padding-top:8px">
      <p>Bij veel bedrijven zit de pijn niet in het jaarverbruik, maar in korte pieken: alles tegelijk aan en je installatie “zit vol”. Dat merk je aan beperkingen, zoals geen ruimte voor extra machines, koeling, keuken of laders.</p>
      <p>Wij maken het simpel: waar komt de piek vandaan, en wat is de goedkoopste, veilige oplossing? Vaak is dat eerst slimmer schakelen, en soms een batterij die tijdelijk bijspringt — alleen als het klopt.</p>
      <div class="feiten">
        <div><div class="groot">NEN 1010 / NEN 3140</div><div class="klein">Vakwerk volgens de geldende normen</div></div>
        <div><div class="groot">Vrijblijvende inspectie</div><div class="klein">Wij komen graag langs op locatie</div></div>
      </div>
    </div>
  </div>
  <div class="situaties">
    <div class="situatie"><div class="nr">Situatie 1</div><h3>Alles start tegelijk</h3><p>Machines, koeling, keuken, compressor: ’s ochtends of rond de lunch gaat alles aan. Startmomenten spreiden en prioriteiten instellen geeft rust én voorkomt dat je te snel aan verzwaring denkt.</p></div>
    <div class="situatie"><div class="nr">Situatie 2</div><h3>Laden zonder sturing</h3><p>Zonder load balancing trekken laadmomenten je piek onnodig omhoog. Wij ontwerpen een laadplein schaalbaar, met sturing zodat je installatie niet “op slot” gaat.</p></div>
    <div class="situatie"><div class="nr">Situatie 3</div><h3>Netcapaciteit is de rem</h3><p>Uitbreiden kan vaak wél, maar niet zomaar “erbij”. Met fasebalans, reserves, logische groepen en slimme sturing maken we je installatie groei-proof.</p></div>
  </div>
  <div class="rekenvoorbeeld">
    <div class="groot-getal">30 kW <span>≈ ±€200</span></div>
    <p><strong>Nuchter rekenvoorbeeld.</strong> 30 kW structureel lager kan, afhankelijk van de tariefcategorie, grofweg ±€200 per maand schelen aan netbeheer-transportcomponenten. Wij beloven dit nooit zomaar: we bepalen het op basis van jouw meetdata en tariefindeling.</p>
    <a class="knop" href="bedrijven.html">Meer voor bedrijven</a>
  </div>
</section>

<!-- ============ BEELDBAND ============ -->
<div class="band">
  <img class="beeld" src="assets/foto/luchtfoto-zonnepanelen-flat.jpg" alt="Luchtfoto van een appartementencomplex met zonnepanelen van JTS op het dak" width="1500" height="844" loading="lazy">
</div>

<!-- ============ ONS VERHAAL ============ -->
<section class="over" id="ons-verhaal">
  <div class="over-raster">
    <div>
      <div class="eyebrow">Ons verhaal</div>
      <h2>Een nuchter, technisch sterk installatiebedrijf.</h2>
      <p>JTS Installatietechniek is opgericht door Jesse Odijk, Tjark Boot en Stijn Ronner. In december 2022 schreven wij ons in bij de Kamer van Koophandel, met één duidelijke ambitie: bouwen aan iets van onszelf.</p>
      <p>Vandaag bestaat JTS uit een hecht en groeiend team. Naast de oprichters werken Ruben Striekwold en Sebastiaan Odijk bij ons. Samen staan we voor kwaliteit, verantwoordelijkheid en oplossingen die klaar zijn voor de toekomst.</p>
      <a class="meer" href="ons-verhaal.html">Lees ons hele verhaal →</a>
    </div>
    <div class="globe">
      <svg viewBox="0 0 200 200" fill="none" stroke="rgba(120,170,230,.42)" stroke-width=".7" aria-hidden="true">
        <circle cx="100" cy="100" r="78" stroke="rgba(120,170,230,.6)"/>
        <ellipse cx="100" cy="100" rx="20" ry="78"/><ellipse cx="100" cy="100" rx="42" ry="78"/><ellipse cx="100" cy="100" rx="62" ry="78"/>
        <ellipse cx="100" cy="100" rx="78" ry="20"/><ellipse cx="100" cy="100" rx="78" ry="42"/><ellipse cx="100" cy="100" rx="78" ry="62"/>
        <circle cx="100" cy="100" r="78" stroke="rgba(0,74,173,.5)" stroke-width="1.4" stroke-dasharray="3 6"/>
        <circle cx="152" cy="66" r="3" fill="#004AAD" stroke="none"/><circle cx="62" cy="136" r="3" fill="#5C9BE8" stroke="none"/><circle cx="118" cy="158" r="2.4" fill="#5C9BE8" stroke="none"/>
      </svg>
      <div class="glas">
        <div class="kop"><span class="naam">Het team van JTS</span><span class="groen"></span></div>
        <div class="waarde" style="font-size:28px">5 vakmensen</div>
        <div class="grafiek" aria-hidden="true"><div style="height:38%"></div><div style="height:56%"></div><div style="height:44%"></div><div class="uit" style="height:78%"></div><div style="height:62%"></div><div style="height:88%"></div><div style="height:70%"></div></div>
      </div>
    </div>
  </div>
</section>

<!-- ============ CIJFERS ============ -->
<section class="cijfers" id="cijfers">
  <div class="cijfers-raster">
    <div>
      <div class="getallen">
        <div><div class="getal">10K+</div><div class="getal-uitleg">Zonnepanelen geïnstalleerd, met vele foutloze Scope-12-keuringen</div></div>
        <div><div class="getal">2022</div><div class="getal-uitleg">Opgericht in Soest — sindsdien gegroeid naar zwaardere en technisch uitdagendere projecten</div></div>
      </div>
      <a class="knop knop--pijl" href="#reviews">
        <span class="rondje"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>
        Wat klanten zeggen
      </a>
    </div>
    <div class="telefoon">
      <div class="scherm">
        <img class="beeld" src="assets/foto/elektricien-verdeelkast.jpg" alt="Elektricien van JTS aan het werk in een grote verdeelkast" width="1500" height="2000" loading="lazy">
        <div class="notch"></div>
      </div>
    </div>
  </div>
</section>

<!-- ============ REVIEWS ============ -->
<section class="reviews" id="reviews">
  <div class="reviews-kop">
    <div>
      <div class="eyebrow">Reviews</div>
      <h2>Wat klanten zeggen.</h2>
    </div>
    <div class="score">{STERREN} Letterlijk overgenomen van Google</div>
  </div>
  <div class="review-raster">{reviews_html}</div>
</section>

<!-- ============ PARTNERS & CERTIFICATEN ============ -->
<section class="partners" id="partners">
  <div class="eyebrow">Partners &amp; certificaten</div>
  <h2>Gecertificeerd vakwerk, met partners die we al jaren kennen.</h2>
  <div class="certificaten">
    <div class="certificaat"><img src="assets/certificaten/nen-1010.png" alt="NEN 1010" loading="lazy"><div><div class="groot">NEN 1010</div><div class="klein">Veiligheid van laagspanningsinstallaties</div></div></div>
    <div class="certificaat"><img src="assets/certificaten/nen-3140.png" alt="NEN 3140" loading="lazy"><div><div class="groot">NEN 3140</div><div class="klein">Veilig werken aan en bij elektrische installaties</div></div></div>
    <div class="certificaat"><img src="assets/certificaten/vca.png" alt="VCA" loading="lazy"><div><div class="groot">VCA</div><div class="klein">Veiligheid, gezondheid en milieu op de werkplek</div></div></div>
  </div>
  <div class="partner-raster">
    <article class="partner partner--zus">
      <img src="assets/partners/nuzon-logo.png" alt="NuZon" loading="lazy">
      <span class="rol">Zusterbedrijf</span>
      <h3>NuZon B.V.</h3>
      <p>NuZon plaatst sinds 2012 zonnepanelen vanuit Soest. NuZon en JTS zijn twee zelfstandige bedrijven met dezelfde eigenaren: NuZon is de naam, de historie en de klanten — JTS doet het werk.</p>
      <a class="door" href="https://www.nuzon.nl/" target="_blank" rel="noopener">Bezoek NuZon →</a>
    </article>
    <article class="partner">
      <span class="rol">Grote projecten</span>
      <h3>East Connect</h3>
      <p>Partner in duurzame installatietechniek en energiemanagement met ruim 25 jaar ervaring. Bij grote projecten, zoals opslag en laadpleinen, werken we samen; de uitvoering ligt bij JTS.</p>
      <a class="door" href="https://eastconnect.nl/" target="_blank" rel="noopener">Over East Connect →</a>
    </article>
    <article class="partner">
      <span class="rol">Energiebeheer thuis</span>
      <h3>Jullix</h3>
      <p>Stuurt zon, batterij, laadpaal en verbruik thuis slim aan. JTS is gecertificeerd Jullix-partner.</p>
    </article>
    <article class="partner">
      <span class="rol">Energiebeheer zakelijk</span>
      <h3>Embion</h3>
      <p>Voor zakelijke installaties werken wij met Embion: laadpalen, klimaat en machines efficiënt op elkaar afgestemd, zonder piekbelasting.</p>
    </article>
  </div>
</section>

<!-- ============ WOORDMERK ============ -->
{WAAROM}
'''
pagina('index.html', 'Energieoplossingen Soest | JTS Installatietechniek',
  'JTS Installatietechniek uit Soest realiseert complete, technische en duurzame installaties voor particulieren en bedrijven: meterkasten, zonnepanelen, laadpalen, batterijsystemen en onderhoud.',
  'home', home, body_klasse='home')

exec(open(os.path.join(os.path.dirname(UIT_SCRIPT), 'diensten.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(UIT_SCRIPT), 'extra.py'), encoding='utf-8').read())

# ============================== AANVRAGEN ==============================
aanvraag = '''<section class="funnel-pagina">
  <div class="funnel-raster">
    <aside class="funnel-zij">
      <div class="badge"><span class="stip">''' + ic("vink",10,"#fff","3") + '''</span><span class="tekst">Gratis en vrijblijvend</span></div>
      <h1>Offerte aanvragen.</h1>
      <p>Beantwoord een paar korte vragen. Dan weten wij precies wat u nodig heeft en kunnen we gericht advies geven of een inspectie inplannen. Het duurt ongeveer twee minuten.</p>
      <ol class="stappen" id="stappenlijst"></ol>
    </aside>
    <div class="funnel-kaart" id="funnel" aria-live="polite">
      <noscript><p>Deze aanvraag werkt met JavaScript. Mail ons gerust op info@jtstechniek.nl of bel 030 781 6767.</p></noscript>
    </div>
  </div>
</section>'''
pagina('aanvragen.html', 'Offerte aanvragen | JTS Installatietechniek',
  'Vraag gratis en vrijblijvend een offerte aan bij JTS Installatietechniek. Beantwoord een paar korte vragen, dan nemen wij snel contact met u op.',
  'aanvragen', aanvraag, extra_js=f'\n<script src="js/aanvragen.js?v={V}"></script>')
print('klaar')
