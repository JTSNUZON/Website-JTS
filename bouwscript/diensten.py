# Dienstpagina's, bedrijven en ons verhaal. Uitgevoerd vanuit paginas.py (helpers in bouw.py).

REGIO = 'Soest, Baarn, Amersfoort, Zeist, De Bilt, Bilthoven, Utrecht, Hilversum, Bussum, Leusden en de rest van regio Utrecht en het Gooi'
REV_DAMEN = ('Wij zijn heel tevreden van JTS. Echt vriendelijke, meedenkende, professionele en eerlijke werkers, die hun afspraken na kwamen.', 'Ria en Henny Damen')
REV_WILLEKENS = ('Netjes op tijd, communicatief geweldig, professioneel en denken met je mee.', 'Jordy Willekens')
REV_BOSSCHA = ('Alles mooi weggewerkt , nieuwe stoppenkast en een aansluiting voor een eventuele generator.', 'jonas Bosscha')
REV_WEGER = ('Deze jonge en zeer professionele mannen, met heel goede omgangsvormen, kwamen in eerste instantie omvormers van onze zonnepanelen vervangen. Dit werd snel en professioneel uitgevoerd.', 'Edith De Weger-Dahmen')

def dienstpagina(bestand, slug, naam, soort, titel, omschrijving, hero, splitdeel, artikel, review, vragen, extra=''):
    faq_html, faq_schema = faq(vragen, titel=f'Veelgestelde vragen over {naam.lower()}')
    inhoud = hero + splitdeel + lang(artikel, slug, review) + extra + faq_html + WAAROM
    pagina(bestand, titel, omschrijving, slug, inhoud,
           schema=[dienst_schema(naam, omschrijving, soort), kruimel_schema(naam, bestand), faq_schema])

# ============================== ELEKTRICIEN ==============================
dienstpagina('elektricien.html', 'elektricien', 'Elektricien', 'Elektrotechnische installaties',
  'Elektricien in Soest en regio Utrecht | JTS Installatietechniek',
  'Erkende elektricien in Soest en regio Utrecht voor groepenkast vervangen, extra groepen, stopcontacten, verlichting en storingen. Werkt volgens NEN 1010. Gratis inspectie.',
  dienst_hero('elektricien', 'Elektricien', 'Elektricien in Soest en regio Utrecht.',
    'Op zoek naar een ervaren elektricien voor uw installatieklus? JTS Installatietechniek helpt particulieren en bedrijven met groepenkasten, extra stopcontacten, verlichting en storingen. Betrouwbaar, betaalbaar en altijd volgens de geldende normen.',
    'elektricien-groepenkast.jpg', 'Elektricien van JTS vervangt een groepenkast in een woning', 'Werkt volgens', 'NEN 1010', 'en NEN 3140 · alle certificeringen in huis', 1125, 1500),
  split('Elektricien diensten', 'Van lamp tot groepenkast.',
    'Wij bieden een breed scala aan elektricien diensten aan voor zowel particulieren als bedrijven. Hier zijn enkele van onze diensten:',
    ['Het ophangen van lampen', 'Nieuwbouw en renovatie', 'Installatie van netwerkkabels', 'Plaatsen van buitenverlichting', 'Installatie van groepenkasten',
     'Uitbreiding van groepen in de groepenkast', 'Aanleggen van extra stopcontacten', 'Oplossen van stroomstoringen en kortsluitingen', 'Aarding en veiligheidsinspecties'],
    'elektricien-buiten.jpg', 'Monteur van JTS sluit een buitenkast aan in de tuin', 844, 1500, 'Vraag een elektricien aan', 'elektricien'),
  f'''<p class="lead">Een goede elektricien herkent u niet aan een mooie offerte, maar aan een installatie die jaren later nog steeds veilig en logisch in elkaar zit. Dat is precies hoe wij werken: eerst kijken, dan eerlijk advies, en daarna vakwerk volgens NEN 1010.</p>
<h2>Uw elektricien voor woning en bedrijf</h2>
<p>JTS Installatietechniek is een erkend installatiebedrijf uit Soest. Onze monteurs werken dagelijks aan elektrische installaties in woningen, bedrijfspanden en nieuwbouwprojecten. Van één extra stopcontact in de woonkamer tot de complete hoofdverdeling van een bedrijfspand: wij doen het met dezelfde zorg. U heeft één aanspreekpunt, vaste monteurs en duidelijke afspraken over planning en prijs.</p>
<p>Omdat wij ook <a href="zonnepanelen.html">zonnepanelen</a>, <a href="laadpalen.html">laadpalen</a> en <a href="thuisbatterijen.html">thuisbatterijen</a> installeren, kijken we verder dan de klus van vandaag. Wilt u over een paar jaar een warmtepomp, een laadpaal of een inductiekookplaat? Dan houden we daar nu al rekening mee in de groepenkast. Zo hoeft er later niet opnieuw gebroken te worden.</p>
<h2>Groepenkast vervangen of uitbreiden</h2>
<p>Veel woningen hebben nog een oude groepenkast met te weinig groepen of zonder goede aardlekbeveiliging. Dat merkt u vaak pas als er iets bij komt: een inductiekookplaat, een laadpaal, een thuisbatterij of een warmtepomp. Een meterkast die “vol” zit, is niet alleen onhandig, maar kan ook onveilig worden als groepen overbelast raken.</p>
<p>Wij vervangen uw groepenkast door een moderne, overzichtelijke kast die voldoet aan NEN 1010. Daarbij kijken we naar:</p>
<ul>
<li>het aantal groepen dat u nu en straks nodig heeft;</li>
<li>de juiste aardlekbeveiliging, zodat een storing niet uw hele huis uitschakelt;</li>
<li>de overstap van 1-fase naar een 3-fase aansluiting als dat nodig is;</li>
<li>een duidelijke en logische indeling, zodat u later altijd weet welke groep waarvoor is.</li>
</ul>
<p>Heeft u alleen een extra groep nodig, bijvoorbeeld voor een laadpaal, kookplaat of wasmachine? Dan breiden we uw bestaande kast uit, als die daar technisch geschikt voor is. Is dat niet zo, dan zeggen we dat eerlijk.</p>
{cta('Groepenkast te vol of te oud? Wij komen gratis kijken.', 'Plan een gratis inspectie', 'elektricien')}
<h2>Stopcontacten, verlichting en netwerkkabels</h2>
<p>Ook voor kleinere elektra-klussen bent u bij ons aan het goede adres. Wij leggen extra stopcontacten en schakelaars aan, hangen lampen op, plaatsen buitenverlichting en tuinverlichting en trekken netwerkkabels voor een stabiele internetverbinding in huis of op kantoor. Leidingen werken we netjes weg, zodat u er na afloop niets meer van ziet.</p>
<h2>Storing of kortsluiting oplossen</h2>
<p>Springt de aardlekschakelaar steeds uit, valt de stroom in een deel van het huis weg of ruikt u een brandlucht bij een stopcontact? Wacht dan niet te lang. Wij sporen de oorzaak van stroomstoringen en kortsluiting op, meten de installatie door en lossen het probleem bij de bron op. Zo voorkomt u dat een kleine storing een gevaarlijke situatie wordt.</p>
<h2>Nieuwbouw, renovatie en veiligheidsinspecties</h2>
<p>Bij nieuwbouw en renovatie verzorgen wij de complete elektrische installatie: van de aansluiting en de groepenkast tot de laatste wandcontactdoos. Voor bedrijven voeren wij inspecties uit volgens NEN 3140, zodat u aantoonbaar veilig werkt. Ook aarding en veiligheidsinspecties in woningen behoren tot de mogelijkheden, bijvoorbeeld bij aankoop van een ouder huis.</p>
<h2>Waarom kiezen voor JTS als elektricien?</h2>
<ul>
<li><strong>Gecertificeerd vakwerk:</strong> wij werken volgens NEN 1010 en NEN 3140 en zijn VCA-gecertificeerd.</li>
<li><strong>Gratis inspectie:</strong> we komen eerst kijken, zodat de offerte klopt en er geen verrassingen zijn.</li>
<li><strong>Transparante prijzen:</strong> heldere offertes en geen onverwachte meerwerkposten achteraf.</li>
<li><strong>Vaste monteurs:</strong> dezelfde mensen van begin tot eind, die ook na oplevering bereikbaar blijven.</li>
</ul>
<h2>Elektricien in uw regio</h2>
<p>Wij werken vanuit Soest en zijn dagelijks actief in {REGIO}. Voor bedrijven en grotere projecten werken we door heel Nederland. Twijfelt u of wij bij u in de buurt komen? Bel gerust, vaak kan het gewoon.</p>''',
  REV_BOSSCHA,
  [('Wat kost een elektricien?', 'Dat hangt af van de klus. Een extra stopcontact is iets anders dan een complete groepenkast. Wij komen gratis kijken en sturen daarna een duidelijke offerte, zonder verrassingen achteraf.'),
   ('Wanneer moet ik mijn groepenkast vervangen?', 'Als uw groepenkast vol zit, geen goede aardlekbeveiliging heeft, of als u een laadpaal, warmtepomp, thuisbatterij of inductiekookplaat wilt aansluiten. Ook bij oude bedrading of herhaaldelijke storingen is vervangen vaak verstandig.'),
   ('Heb ik een 3-fase aansluiting nodig?', 'Niet altijd. Voor een snelle laadpaal, een grote warmtepomp of een thuisbatterij kan 3-fase wel verstandig zijn. Wij bekijken uw situatie en adviseren eerlijk of de overstap nodig is.'),
   ('Werken jullie ook voor bedrijven?', 'Ja. Wij doen elektrotechniek voor bedrijfspanden, van verdeelinrichtingen tot NEN 3140-inspecties. Lees meer op onze pagina <a href="bedrijven.html">voor bedrijven</a>.'),
   ('In welke regio werken jullie?', 'Vanuit Soest werken wij in regio Utrecht, Eemland en het Gooi, onder meer in Baarn, Amersfoort, Zeist, De Bilt en Hilversum. Voor bedrijven werken we door heel Nederland.')])

# ============================== ZONNEPANELEN ==============================
dienstpagina('zonnepanelen.html', 'zonnepanelen', 'Zonnepanelen', 'Installatie van zonnepanelen',
  'Zonnepanelen laten installeren in regio Utrecht | JTS Installatietechniek',
  'Zonnepanelen laten installeren door een ervaren installateur uit Soest. Meer dan 10.000 panelen gelegd, voor woningen en bedrijven. Advies op maat en gratis dakcheck.',
  dienst_hero('zonnepanelen', 'Zonnepanelen', 'Zonnepanelen laten installeren.',
    'Wij regelen het complete proces van A tot Z: van één zonnepaneel tot honderden bij elkaar. Met meer dan 10.000 gelegde panelen in het portfolio staan wij klaar om uw wensen te realiseren, voor zowel woningen als bedrijven.',
    'zonnepanelen-pannendak.jpg', 'Zwarte zonnepanelen door JTS geïnstalleerd op een pannendak', 'In het portfolio', '10.000+', 'gelegde zonnepanelen', 1500, 1125),
  split('Waarom kiezen voor ons', 'Ervaren in het leggen van zonnepanelen.',
    'Onze ervaren installateurs zorgen voor een veilige en efficiënte installatie, zodat u direct kunt profiteren van duurzame energie.',
    [('Advies op maat', 'Beste opstelling en type zonnepanelen voor maximaal rendement.'),
     ('Veilige montage', 'Stevige bevestiging van zonnepanelen met oog voor veiligheid.'),
     ('Professionele aansluiting', 'Veilig aansluiten van omvormer en elektrisch systeem.'),
     ('Monitoring', 'Inzicht in uw energieopbrengst.')],
    'zonnepanelen-dakkapel.jpg', 'Zonnepanelen geïntegreerd in een nieuw dakvlak met dakkapel', 1500, 1125, 'Vraag een offerte aan', 'zonnepanelen'),
  f'''<p class="lead">Zonnepanelen laten installeren is een investering voor vele jaren. Het verschil zit niet alleen in de panelen, maar vooral in het ontwerp, de montage en de aansluiting op uw meterkast. Daar maken wij het verschil.</p>
<h2>Installateur van zonnepanelen met ruime ervaring</h2>
<p>JTS Installatietechniek heeft inmiddels meer dan 10.000 zonnepanelen gelegd: op pannendaken, platte daken, staaldaken van bedrijfshallen en in grondopstellingen. Veel van die installaties zijn gekeurd volgens Scope 12, de inspectie die verzekeraars steeds vaker vragen voor zakelijke zonnestroominstallaties. Die ervaring gebruiken we bij elke woning, of het nu om acht panelen gaat of om tachtig.</p>
<p>U heeft bij ons één aanspreekpunt en vaste monteurs. Geen onderaannemers die uw dak niet kennen, maar het team dat ook uw dakcheck deed en na oplevering bereikbaar blijft.</p>
<h2>Zo verloopt de installatie van zonnepanelen</h2>
<h3>1. Gratis dakcheck en advies op maat</h3>
<p>We komen langs om uw dak, de ligging, eventuele schaduw en uw meterkast te bekijken. Op basis van uw jaarverbruik adviseren we hoeveel panelen zinvol zijn, welk type paneel past en welke omvormer daarbij hoort. Soms is het eerlijke advies: minder panelen, of eerst iets aan de meterkast doen.</p>
<h3>2. Heldere offerte</h3>
<p>U ontvangt een duidelijke offerte met alle onderdelen: panelen, montagemateriaal, omvormer, bekabeling en de aansluiting in de meterkast. Onze tarieven hangen af van de omvang en uw wensen. Wat in de offerte staat, is wat u betaalt.</p>
<h3>3. Veilige montage en aansluiting</h3>
<p>Onze monteurs plaatsen de panelen met stevige bevestiging en oog voor uw dak. Zonnepanelen op een woning liggen er meestal binnen één werkdag. We sluiten de omvormer veilig aan op een eigen groep en werken de bekabeling netjes weg.</p>
<h3>4. Oplevering en monitoring</h3>
<p>Na de installatie testen we het systeem en richten we de monitoring in. Zo ziet u in een app precies wat uw panelen opwekken. Valt de opbrengst onverwacht terug, dan ziet u dat direct.</p>
{cta('Benieuwd hoeveel panelen er op uw dak passen?', 'Vraag een gratis dakcheck aan', 'zonnepanelen')}
<h2>Zonnepanelen na het einde van de salderingsregeling</h2>
<p>Per 1 januari 2027 stopt de salderingsregeling. Stroom die u teruglevert aan het net, kunt u dan niet meer wegstrepen tegen stroom die u afneemt. Zonnepanelen blijven interessant, maar het wordt belangrijker om uw eigen stroom zelf te gebruiken. Daarom kijken wij bij elk advies ook naar uw verbruikspatroon, en naar slimme combinaties met een <a href="thuisbatterijen.html">thuisbatterij</a>, <a href="laadpalen.html">laadpaal</a> of energiemanagementsysteem. Zo haalt u na 2027 het meeste uit uw panelen.</p>
<h2>Zonnepanelen voor bedrijven</h2>
<p>Voor bedrijfspanden ontwerpen en installeren wij grotere zonnestroominstallaties op platte daken en staaldaken. Daarbij letten we op dakbelasting, brandveiligheid, kabeltracés en de capaciteit van uw aansluiting. Ons eerste grote project was 400 zonnepanelen bij een bedrijf in Nieuwveen; inmiddels zijn dat er vele duizenden. Lees meer over <a href="bedrijven.html">zonnepanelen en energie voor bedrijven</a>.</p>
<h2>Bestaande zonnepanelen?</h2>
<p>Ook als u al zonnepanelen heeft, kunt u bij ons terecht. Moeten de panelen tijdelijk van het dak voor een dakrenovatie? Dan verzorgen wij de <a href="de-hermontage.html">demontage en hermontage</a>. Doet uw installatie het niet meer goed of is uw oude installateur niet meer bereikbaar? Dan helpt onze <a href="onderhoud.html">onderhoudsservice</a> u verder.</p>
<h2>Zonnepanelen in uw regio</h2>
<p>Wij installeren zonnepanelen vanuit Soest in {REGIO}. Zakelijke projecten voeren we door heel Nederland uit.</p>''',
  REV_WILLEKENS,
  [('Wat kosten zonnepanelen?', 'De prijs hangt af van het aantal panelen, het type dak, de omvormer en de aansluiting in uw meterkast. Na een gratis dakcheck krijgt u een duidelijke offerte op maat.'),
   ('Hoe lang duurt het installeren van zonnepanelen?', 'Zonnepanelen op een woning liggen er meestal binnen één werkdag. Grotere installaties en bedrijfsdaken plannen we in overleg.'),
   ('Zijn zonnepanelen na 2027 nog rendabel?', 'Ja, vaak wel, maar de manier waarop u ze gebruikt wordt belangrijker. Na het einde van de salderingsregeling loont het om zoveel mogelijk zelf te verbruiken, eventueel met een thuisbatterij of slimme sturing. Wij rekenen het voor uw situatie door.'),
   ('Kan ik zonnepanelen op een plat dak laten leggen?', 'Ja. Op platte daken plaatsen wij de panelen op een onderconstructie onder de juiste hoek, met aandacht voor ballast, dakbelasting en windbelasting.'),
   ('Heb ik een 3-fase aansluiting nodig voor zonnepanelen?', 'Bij een kleine installatie is dat meestal niet nodig. Bij grotere aantallen panelen kan een 3-fase omvormer verstandig of noodzakelijk zijn. Dat bekijken we tijdens de dakcheck.')])

# ============================== LAADPALEN ==============================
dienstpagina('laadpalen.html', 'laadpalen', 'Laadpalen', 'Installatie van laadpalen',
  'Laadpaal laten installeren, thuis of zakelijk | JTS Installatietechniek',
  'Laadpaal laten installeren door gecertificeerde monteurs uit Soest. Laadpaal thuis of op de zaak, met load balancing en e-flux. Gratis advies en vrijblijvende offerte.',
  dienst_hero('laadpalen', 'Laadpalen', 'Laadpaal laten installeren.',
    'Uw elektrische auto opladen voor de deur of op de zaak? JTS Installatietechniek levert en installeert laadpalen, volledig afgestemd op uw auto, uw meterkast en uw situatie. Neem vandaag nog contact op voor gratis advies.',
    'laadpalen-kantoor.jpg', 'Laadpalen door JTS geplaatst bij een kantoorpand', 'Laadoplossing', 'Thuis &amp; zakelijk', 'met e-flux kunnen bedrijven er geld mee verdienen', 1125, 1500),
  split('Waarom een laadpaal van JTS', 'Altijd klaar om te laden.',
    'Onze gecertificeerde installateurs zorgen voor een veilige en snelle installatie, zodat u altijd klaar bent om uw elektrische auto op te laden.',
    [('Advies op maat', 'De beste laadpaal voor uw situatie, passend bij uw auto en laadsnelheid.'),
     ('Veilige installatie', 'Inclusief aansluiting op uw elektrische systeem en een eigen groep.'),
     ('Toekomstbestendig', 'Voorbereid op uitbreiding. Met e-flux kunnen bedrijven ook geld verdienen met hun laadoplossing.'),
     ('Thuis en zakelijk', 'Van één laadpunt op de oprit tot een compleet laadplein.')],
    'laadpalen-kabeltrace.jpg', 'Kabeltracé in de grond naar een nieuwe laadpaal', 1125, 1500, 'Vraag een laadpaal aan', 'laadpalen'),
  f'''<p class="lead">Een laadpaal thuis is de makkelijkste manier om elektrisch te rijden: ’s avonds aansluiten, ’s ochtends vol. Maar welke laadpaal past bij uw auto, en kan uw meterkast het aan? Daar helpen wij u bij.</p>
<h2>Laadpaal thuis laten installeren</h2>
<p>Een goede laadpaal installatie begint bij uw meterkast. Wij bekijken eerst of uw huidige aansluiting voldoende ruimte heeft en of er een extra groep bij kan. Daarna adviseren wij een laadpaal die past bij uw auto, uw rijgedrag en uw budget. Geen laadpaal die meer kan dan uw auto, en ook geen laadpaal die u over twee jaar alweer moet vervangen.</p>
<h3>Welke laadsnelheid heeft u nodig?</h3>
<p>Het laadvermogen hangt af van uw aansluiting en van wat uw auto aankan. Op een 1-fase aansluiting laadt u doorgaans met 3,7 kW. Met een 3-fase aansluiting is 11 kW mogelijk, waarmee de meeste elektrische auto’s in een nacht ruim vol zijn. Een snellere laadpaal heeft alleen zin als uw auto en uw aansluiting dat ook ondersteunen. Wij rekenen het voor u uit.</p>
<h3>Load balancing: slim laden zonder overbelasting</h3>
<p>Staan de wasmachine, de oven en de laadpaal tegelijk aan? Dan kan uw hoofdzekering het zwaar krijgen. Met load balancing (dynamische vermogensregeling) past de laadpaal zijn vermogen automatisch aan op wat er in huis wordt gebruikt. Zo laadt u altijd zo snel als veilig kan, zonder dat de stroom uitvalt.</p>
<h3>Laden op zonne-energie</h3>
<p>Heeft u <a href="zonnepanelen.html">zonnepanelen</a>? Dan is het slim om uw auto vooral op eigen zonnestroom te laden, zeker nu de salderingsregeling per 2027 stopt. Met een <a href="thuisbatterijen.html">energiemanagementsysteem</a> laadt de auto automatisch wanneer er zonne-energie over is.</p>
{cta('Wilt u weten welke laadpaal bij uw auto en meterkast past?', 'Vraag gratis advies aan', 'laadpalen')}
<h2>Laadpalen voor bedrijven</h2>
<p>Voor bedrijven ontwerpen wij laadoplossingen van een paar laadpunten op het eigen terrein tot complete laadpleinen. Zakelijk laden werkt prima, als u het slim verdeelt. Zonder sturing trekken laadmomenten uw piekvermogen onnodig omhoog, en dat kost geld of zet uw installatie “op slot”.</p>
<ul>
<li><strong>Schaalbaar ontwerp:</strong> begin met een paar laadpunten en breid later eenvoudig uit.</li>
<li><strong>Load balancing over meerdere laadpalen:</strong> meer laadpunten op uw bestaande aansluiting.</li>
<li><strong>Verdienen met laden:</strong> wij werken met e-flux, waarmee bedrijven ook geld kunnen verdienen met hun laadpalen, bijvoorbeeld door bezoekers of medewerkers te laten betalen.</li>
<li><strong>AC en waar passend DC:</strong> van gewone laadpalen tot snelladers voor bijvoorbeeld een wagenpark.</li>
</ul>
<p>Lees meer over <a href="bedrijven.html">laadinfrastructuur en piekbesparing voor bedrijven</a>.</p>
<h2>Wat kost een laadpaal laten installeren?</h2>
<p>Onze tarieven zijn afhankelijk van uw wensen en de technische situatie: het type laadpaal, de afstand van de meterkast tot de parkeerplek, of er gegraven moet worden en of uw groepenkast aangepast moet worden. Neem contact met ons op voor een vrijblijvende offerte en ontdek hoe wij u kunnen helpen met de overstap naar elektrisch rijden.</p>
<h2>Laadpaal installateur in uw regio</h2>
<p>Wij installeren laadpalen vanuit Soest in {REGIO}. Laadoplossingen voor bedrijven realiseren wij door heel Nederland.</p>''',
  REV_WILLEKENS,
  [('Wat kost een laadpaal met installatie?', 'Dat hangt af van de laadpaal, de afstand tot de meterkast, eventueel graafwerk en of uw groepenkast aangepast moet worden. Wij komen gratis kijken en maken een duidelijke offerte.'),
   ('Heb ik 3-fase nodig voor een laadpaal?', 'Niet per se. Op 1-fase laadt u doorgaans met 3,7 kW, op 3-fase is 11 kW mogelijk. Of 3-fase zinvol is, hangt af van uw auto en hoeveel kilometers u rijdt.'),
   ('Wat is load balancing?', 'Load balancing regelt het laadvermogen automatisch op basis van het verbruik in huis of in het pand. Zo voorkomt u overbelasting van uw aansluiting en kunt u veilig laden.'),
   ('Kan ik mijn auto laden op zonne-energie?', 'Ja. Met een slimme laadpaal of een energiemanagementsysteem laadt uw auto vooral wanneer uw zonnepanelen stroom over hebben.'),
   ('Plaatsen jullie ook laadpalen voor bedrijven?', 'Ja, van een paar laadpunten tot complete laadpleinen met load balancing. Met e-flux kunnen bedrijven ook geld verdienen met hun laadpalen.')])

# ============================== THUISBATTERIJEN ==============================
dienstpagina('thuisbatterijen.html', 'thuisbatterijen', 'Thuisbatterij', 'Installatie van thuisbatterijen',
  'Thuisbatterij laten installeren met noodstroom | JTS Installatietechniek',
  'Thuisbatterij laten installeren in regio Utrecht. Noodstroom met ATS, niet meer terugleveren na 2027 en slim energiemanagement. Bliq, Pylontech en meer. Gratis advies.',
  dienst_hero('thuisbatterijen', 'Thuisbatterij', 'Thuisbatterij laten installeren.',
    'Bent u op zoek naar een thuisbatterij? Wij zorgen voor een totaalpakket: noodstroom, energiemanagement en integratie op uw huidige installatie. Alle merken en opties zijn mogelijk, van reguliere systemen tot off-grid.',
    'thuisbatterij-bliq.jpg', 'Bliq-thuisbatterij door JTS geïnstalleerd in een bijkeuken', 'Werkt met', 'Bliq &amp; Pylontech', 'gekoppeld aan een ATS voor noodstroom', 1125, 1500),
  split('Onze slimme batterijoplossingen', 'Drie redenen voor een thuisbatterij.', '',
    [('Noodstroom', 'Valt de netstroom weg, dan blijven bij u thuis de lampen branden. Ook kunnen wij een back-upgenerator op het systeem aansluiten.'),
     ('Niet meer terugleveren', 'Terugleveren wordt steeds minder aantrekkelijk. Hiervoor hebben wij drie passende oplossingen.'),
     ('Energiemanagement', 'Bij elk systeem bieden wij een passend energiemanagementsysteem (EMS) aan, zodat uw hele installatie met elkaar communiceert.')],
    'thuisbatterij-installatie.jpg', 'Monteurs van JTS installeren een thuisbatterij', 1125, 1500, 'Vraag een thuisbatterij aan', 'thuisbatterijen'),
  f'''<p class="lead">Een thuisbatterij slaat uw overschot aan zonnestroom op, zodat u die ’s avonds zelf gebruikt in plaats van goedkoop terug te leveren. Met de juiste installatie wordt diezelfde batterij ook uw noodstroomvoorziening.</p>
<h2>Waarom nu een thuisbatterij?</h2>
<p>Per 1 januari 2027 stopt de salderingsregeling. Wat u teruglevert aan het net, mag u dan niet meer wegstrepen tegen wat u afneemt. Veel energieleveranciers rekenen nu al terugleverkosten. Hoe meer zonnestroom u zelf gebruikt, hoe meer u aan uw zonnepanelen overhoudt. Een thuisbatterij is daarvoor de meest complete oplossing, zeker in combinatie met slim energiemanagement of een dynamisch energiecontract.</p>
<h2>Noodstroom: stroom, ook als het net wegvalt</h2>
<h3>Back-up via batterij met ATS (automatische omschakeling)</h3>
<p>Wij werken met hoogwaardige energieopslagsystemen, zoals Bliq- en Pylontech-batterijen. Deze koppelen wij aan een ATS (Automatic Transfer Switch). Zodra de netspanning wegvalt, detecteert de ATS de stroomuitval en schakelt het systeem automatisch over van netstroom naar batterij. De aangesloten installatie blijft zonder onderbreking werken: volledig automatisch, stil en zeer betrouwbaar.</p>
<h3>Uitbreiding met een inverter generator</h3>
<p>Bij langdurige stroomuitval, of wanneer de batterij leeg raakt, kan een inverter generator de batterij opnieuw opladen en zo nodig direct stroom leveren. Zo bent u niet alleen beschermd tegen korte onderbrekingen, maar ook voorbereid op situaties waarin het elektriciteitsnet langere tijd niet beschikbaar is.</p>
{cta('Wilt u weten welke thuisbatterij bij uw verbruik past?', 'Vraag gratis advies aan', 'thuisbatterijen')}
<h2>Niet meer terugleveren: drie oplossingen</h2>
<h3>1. Energiemeter als terugleverbegrenzer</h3>
<p>Een energiemeter stuurt de omvormer automatisch aan, zodat er geen energie meer wordt teruggeleverd aan het net. Eenvoudig en betaalbaar, maar overtollige zonnestroom wordt dan niet opgewekt.</p>
<h3>2. Thuisbatterij met energiemeter (onze aanrader)</h3>
<p>Overtollige zonne-energie gaat eerst de batterij in. Is die (bijna) vol, dan remt de energiemeter de omvormer, zodat er niet wordt teruggeleverd. Tegelijk gebruikt het systeem de opgewekte energie optimaal. Dit is de oplossing die wij in de meeste gevallen aanraden, omdat u hiermee het maximale rendement uit uw installatie haalt.</p>
<h3>3. Omvormer uitschakelen</h3>
<p>De omvormer gaat uit op momenten dat er wordt teruggeleverd. Het nadeel: op dat moment wordt er helemaal geen energie meer opgewekt en gaat rendement verloren. Dit is de minst wenselijke optie.</p>
<h2>Energiemanagement (EMS): alles werkt samen</h2>
<p>Met een energiemanagementsysteem laten wij zonnepanelen, thuisbatterij, <a href="laadpalen.html">laadpaal</a> en warmtepomp met elkaar communiceren. De auto laadt als er genoeg zonne-energie is, de warmtepomp schakelt in wanneer dat het gunstigst is en de batterij laadt slim bij. Alles gebeurt automatisch. JTS is gecertificeerd Jullix-partner. Voor bedrijven werken wij met het EMS van Embion, dat piekbelasting voorkomt en grotere installaties aanstuurt.</p>
<h2>Welke thuisbatterij past bij u?</h2>
<p>De juiste capaciteit hangt af van uw verbruik, het aantal <a href="zonnepanelen.html">zonnepanelen</a>, uw aansluiting (1-fase of 3-fase) en of u noodstroom wilt. Alle merken en opties zijn mogelijk, van reguliere systemen tot off-grid. Wij kijken samen met u naar uw energiebehoefte en adviseren een systeem dat technisch én financieel klopt. Soms betekent dat: nog even wachten. Dat zeggen we dan ook.</p>
<h2>Thuisbatterij installateur in uw regio</h2>
<p>Wij installeren thuisbatterijen vanuit Soest in {REGIO}. Batterijopslag voor bedrijven realiseren wij door heel Nederland, bij grote projecten samen met East Connect.</p>''',
  REV_BOSSCHA,
  [('Is een thuisbatterij rendabel?', 'Dat hangt af van uw verbruik, het aantal zonnepanelen en uw energiecontract. Na het einde van de salderingsregeling in 2027 wordt zelf verbruiken belangrijker. Wij rekenen vooraf eerlijk door of het voor u loont.'),
   ('Werkt een thuisbatterij als noodstroom?', 'Ja, als de installatie daarvoor is ingericht. Wij koppelen de batterij aan een ATS die bij stroomuitval automatisch omschakelt, eventueel aangevuld met een inverter generator.'),
   ('Welke merken thuisbatterij installeren jullie?', 'Wij werken onder meer met Bliq en Pylontech, maar alle merken en opties zijn mogelijk, van reguliere systemen tot off-grid.'),
   ('Kan een thuisbatterij bij mijn bestaande zonnepanelen?', 'In de meeste gevallen wel. Wij integreren de batterij op uw huidige installatie en kijken of omvormer en meterkast geschikt zijn.'),
   ('Heb ik een 3-fase aansluiting nodig?', 'Niet altijd. Voor grotere batterijen en noodstroom van het hele huis kan 3-fase nodig zijn. Dat bekijken we tijdens de gratis inspectie.')])

# ============================== DE/HERMONTAGE ==============================
dh_tarieven = '<section class="wit"><div class="twee"><div><div class="eyebrow">Tarieven</div><h2>Duidelijke prijzen, vooraf.</h2></div><div class="artikel" style="padding-top:8px"><p>U weet vooraf waar u aan toe bent. Bij vijf panelen of meer rekenen wij geen voorrijkosten.</p>' + tarieven('Tarieven de- en hermontage', [('Montage en hermontage per paneel', '€100 excl. · €121 incl. btw'), ('Voorrijkosten vanaf 5 panelen', 'Gratis'), ('Voorrijkosten bij minder dan 5 panelen', '€75')], 'Defecte onderdelen die we tegenkomen, vervangen we na overleg. Neem contact op voor een offerte op maat.') + '</div></div></section>'
dienstpagina('de-hermontage.html', 'de-hermontage', 'De/hermontage', 'Demontage en hermontage van zonnepanelen',
  'Zonnepanelen demonteren en hermonteren | JTS Installatietechniek',
  'Zonnepanelen tijdelijk verwijderen voor dakrenovatie, schilderwerk of dakkapel en daarna terugplaatsen. €121 per paneel incl. btw, gratis voorrijden vanaf 5 panelen.',
  dienst_hero('de-hermontage', 'De/Hermontage', 'Zonnepanelen demonteren en hermonteren.',
    'Lekkage, een defect of toe aan een nieuwe dakkapel? Komt de dakdekker of schilder langs en moeten uw panelen tijdelijk van het dak af? Wij komen voor de klus langs en monteren na de werkzaamheden alles weer terug zoals het was.',
    'hermontage-na.jpg', 'Zonnepanelen netjes teruggeplaatst op een pannendak met dakramen', 'Tarief', '€121 per paneel', 'incl. btw · gratis voorrijden vanaf 5 panelen', 1500, 1125),
  split('Wat wij doen', 'Van demontage tot nacontrole.', '',
    ['Complete demontage, inclusief het verwijderen van de frames, stringen en dakhaken',
     'Hermontage naar de huidige standaard: complete herinstallatie van het systeem',
     'Nacontrole of alles naar de huidige normen is teruggeplaatst en of het materiaal nog in orde is',
     'Zijn er punten in het systeem niet in orde, dan vervangen wij de defecte onderdelen',
     'Goed contact met alle partijen die bij u aan het werk zijn'],
    'hermontage-voor.jpg', 'Hetzelfde dak met de zonnepanelen tijdelijk verwijderd', 1500, 1125, 'Plan de/hermontage in', 'de-hermontage'),
  f'''<p class="lead">Zonnepanelen liggen er voor twintig jaar of langer. Maar uw dak heeft in die tijd ook onderhoud nodig. Dan moeten de panelen er tijdelijk af, en daarna weer veilig terug. Dat is specialistisch werk, en precies waar wij goed in zijn.</p>
<h2>Wanneer moeten zonnepanelen tijdelijk van het dak?</h2>
<p>Er zijn verschillende situaties waarin zonnepanelen gedemonteerd en opnieuw gemonteerd moeten worden:</p>
<ul>
<li><strong>Dakrenovatie of nieuwe dakpannen:</strong> de dakdekker kan pas aan de slag als de panelen eraf zijn.</li>
<li><strong>Lekkage:</strong> om de oorzaak van een lekkage te vinden en te herstellen.</li>
<li><strong>Een nieuwe dakkapel of dakraam:</strong> de indeling van het dak verandert, en de panelen moeten opnieuw worden geplaatst.</li>
<li><strong>Schilderwerk of gevelonderhoud:</strong> als panelen het werk in de weg zitten.</li>
<li><strong>Verhuizing:</strong> u wilt uw zonnepanelen meenemen naar uw nieuwe woning.</li>
</ul>
<h2>Waarom geen dakdekker of klusjesman?</h2>
<p>Zonnepanelen zijn een elektrische installatie. Bij het loskoppelen van de stringen staat er gelijkspanning op de kabels, en een verkeerd teruggezette MC4-connector of beschadigde kabel kan later tot storingen, opbrengstverlies of zelfs brand leiden. Daarom laat u de- en hermontage over aan een installateur die dagelijks met zonnepanelen werkt. Wij koppelen het systeem veilig af, bewaren alles zorgvuldig en sluiten het na afloop weer correct aan.</p>
<h2>Zo werken wij</h2>
<h3>Demontage</h3>
<p>Voorbereiding en veilige verwijdering van de panelen, inclusief bekabeling, frames, stringen, dakhaken en bevestigingsmaterialen. We stemmen de planning af met uw dakdekker of aannemer, zodat het werk naadloos op elkaar aansluit.</p>
<h3>Hermontage naar de huidige standaard</h3>
<p>Na de werkzaamheden plaatsen wij de zonnepanelen terug met een zorgvuldige inspectie van alle componenten, zoals de omvormer en de bekabeling. We monteren naar de huidige standaard, ook als de oorspronkelijke installatie dat niet was.</p>
<h3>Controle en testen</h3>
<p>Na hermontage testen wij het volledige systeem, zodat alles naar behoren functioneert en u weer het maximale rendement uit uw zonnepanelen haalt. Komen we defecte onderdelen tegen, dan bespreken we dat met u en vervangen we ze.</p>
{cta('Komt de dakdekker binnenkort? Plan de demontage op tijd in.', 'Plan de/hermontage in', 'de-hermontage')}
<h2>Flexibele planning, goed contact</h2>
<p>Of het nu gaat om een renovatie, onderhoud of verhuizing: wij passen ons aan uw planning aan, zodat u zo min mogelijk hinder ondervindt en uw panelen zo kort mogelijk stilliggen. We houden contact met alle partijen die bij u aan het werk zijn. Dat is ook precies wat klanten over ons zeggen: afspraken nakomen en transparante kosten, zonder verrassingen.</p>
<h2>Meteen uw installatie laten nakijken</h2>
<p>Liggen de panelen er toch af? Dan is het een goed moment om uw systeem te laten controleren. Doet uw omvormer het nog goed, is de bekabeling in orde? Wij kijken het na tijdens de hermontage. Voor structureel onderhoud kunt u terecht bij onze <a href="onderhoud.html">onderhoudsservice</a>. Overweegt u meer panelen? Bij de hermontage kunnen we uw installatie ook <a href="zonnepanelen.html">uitbreiden</a>.</p>
<h2>De/hermontage in uw regio</h2>
<p>Wij demonteren en hermonteren zonnepanelen vanuit Soest in {REGIO}.</p>''',
  REV_DAMEN,
  [('Wat kost het demonteren en hermonteren van zonnepanelen?', 'Montage en hermontage kost €100 per paneel exclusief btw (€121 inclusief btw). Vanaf vijf panelen rekenen wij geen voorrijkosten, bij minder dan vijf panelen is dat €75.'),
   ('Hoe lang liggen mijn zonnepanelen eraf?', 'Dat hangt af van de werkzaamheden van uw dakdekker of aannemer. Wij stemmen de planning met hen af, zodat de panelen zo kort mogelijk stilliggen.'),
   ('Waar blijven de panelen tijdens de werkzaamheden?', 'In overleg bewaren we de panelen veilig op locatie, zodat ze direct klaarliggen voor de hermontage.'),
   ('Wat als er onderdelen kapot zijn?', 'Tijdens de nacontrole kijken we of al het materiaal nog in orde is. Defecte onderdelen vervangen we na overleg met u.'),
   ('Kunnen jullie ook panelen van een ander bedrijf hermonteren?', 'Ja. Wij demonteren en hermonteren zonnepanelen ongeacht wie ze oorspronkelijk heeft geplaatst.')],
  extra=dh_tarieven)

# ============================== ONDERHOUD ==============================
oh_tarieven = '<section class="wit"><div class="twee"><div><div class="eyebrow">Tarieven</div><h2>Onderhoud zonder verrassingen.</h2></div><div class="artikel" style="padding-top:8px"><p>Kies voor een vast onderhoudscontract, of laat ons komen als er iets speelt.</p>' + tarieven('Vast onderhoudscontract', [('Jaarlijkse controle', '€299 per jaar incl. btw')], 'Exclusief materiaalkosten voor onderhoud. Vergoedt tot 10 uur aan werkzaamheden.') + tarieven('Onderhoud en storingen', [('Uurtarief', '€70 incl. btw'), ('Voorrijkosten (verder dan 20 km vanaf Lage Vuursche)', '€75')]) + '</div></div></section>'
dienstpagina('onderhoud.html', 'onderhoud', 'Onderhoud', 'Onderhoud van zonnepanelen, laadpalen en elektrische installaties',
  'Onderhoud en storing zonnepanelen | JTS Installatietechniek',
  'Onderhoud en storingen van zonnepanelen, omvormers, laadpalen en elektrische installaties. Ook als uw installateur failliet is. Onderhoudscontract €299 per jaar.',
  dienst_hero('onderhoud', 'Onderhoud', 'Onderhoud en storing zonnepanelen.',
    'Vertrouwt u het niet meer en is uw huidige installateur niet meer te bereiken? Neem contact met ons op voor alle vragen over onderhoud. Wij vervangen alles en zorgen ervoor dat uw systeem optimaal blijft draaien.',
    'onderhoud-panelen.jpg', 'Monteur van JTS controleert de bekabeling onder zonnepanelen', 'Onderhoudscontract', '€299 per jaar', 'incl. btw · jaarlijkse controle', 844, 1500),
  split('Wat valt er onder ons onderhoud', 'Zonnepanelen, laadpalen en elektra.',
    'Wij onderhouden zonnepanelen, laadpalen en andere elektrische systemen, voor particulieren en zakelijke klanten.',
    [('Vervangen van kapotte onderdelen', 'Omvormers, connectoren, bekabeling en optimizers.'),
     ('Visuele inspecties', 'Van panelen, bevestiging, dakdoorvoeren en bekabeling.'),
     ('Doormeten van het hele systeem', 'Zodat we fouten vinden voordat ze opbrengst kosten.'),
     ('Reiniging en coating', 'Reinigen van panelen en opnieuw aanbrengen van een coatinglaag.')],
    'onderhoud-bedrijfsdak.jpg', 'Monteurs van JTS aan het werk op een bedrijfsdak', 844, 1500, 'Vraag onderhoud aan', 'onderhoud'),
  f'''<p class="lead">Zonnepanelen hebben weinig onderhoud nodig, maar niet géén onderhoud. Een omvormer die stilletjes uitvalt of een losse connector kost u maandenlang opbrengst zonder dat u het doorheeft. Met goed onderhoud voorkomt u dat.</p>
<h2>Onderhoud van zonnepanelen</h2>
<p>Regelmatig onderhoud zorgt ervoor dat uw zonnepanelen optimaal blijven werken en voorkomt storingen of onnodige slijtage. Wij reinigen en inspecteren de panelen, controleren de bevestiging en de bekabeling, meten het systeem door en kijken of de omvormer naar behoren werkt. Zo verlengt u de levensduur van uw zonne-installatie en haalt u een betere return on investment.</p>
<h2>Storing aan zonnepanelen of omvormer?</h2>
<p>Geeft uw omvormer een foutmelding, ziet u in de app ineens een veel lagere opbrengst, of doet de installatie helemaal niets meer? Dan is er vaak sprake van een defecte omvormer, een losgeraakte of verbrande connector, of een probleem met de bekabeling. Wij sporen de storing op, vervangen defecte onderdelen en zorgen dat uw installatie weer volledig werkt. Ook als iemand anders uw installatie heeft geplaatst.</p>
<h2>Installateur failliet of niet meer bereikbaar?</h2>
<p>Helaas komt het regelmatig voor: de installateur die uw zonnepanelen plaatste, bestaat niet meer of neemt de telefoon niet op. Bent u op zoek naar een nieuwe onderhoudspartner omdat uw zonnepanelenbedrijf failliet is gegaan? Wij nemen graag het onderhoud van uw installaties over en zorgen voor continuïteit en kwaliteit. Bij oudere installaties is er soms geen fabrieksgarantie meer, of zijn onderdelen niet meer leverbaar. Dan zeggen we dat eerlijk en kijken we samen naar wat wél kan.</p>
{cta('Doet uw installatie het niet meer goed? Wij komen langs.', 'Vraag onderhoud aan', 'onderhoud')}
<h2>Onderhoud van laadpalen en elektrische systemen</h2>
<p>Ook uw laadpaal en elektrische installatie verdienen aandacht. Wij voeren periodieke controles uit op laadpalen om de efficiëntie te waarborgen en problemen vroegtijdig op te lossen. Daarnaast inspecteren en onderhouden wij groepenkasten, stopcontacten en bedrading, voor een veilige en betrouwbare werking. Is er meer nodig, dan helpt onze <a href="elektricien.html">elektricien</a> u verder.</p>
<h2>Vast onderhoudscontract</h2>
<p>Wilt u zich er niet meer druk om maken? Met een vast onderhoudscontract komen wij jaarlijks langs voor een volledige controle. Het contract kost €299 per jaar inclusief btw, vergoedt tot 10 uur aan werkzaamheden en is exclusief materiaalkosten. Zo weet u zeker dat uw installatie elk jaar wordt nagekeken.</p>
<h2>Ervaren en gecertificeerde monteurs</h2>
<p>Onze technici hebben jarenlange ervaring met zonne-energiesystemen en elektrische installaties. Wij werken volgens NEN 1010 en NEN 3140 en staan garant voor kwaliteit en veiligheid. Liggen uw panelen op een dak dat gerenoveerd moet worden? Dan verzorgen we ook de <a href="de-hermontage.html">demontage en hermontage</a>. Overweegt u uw installatie uit te breiden met een <a href="thuisbatterijen.html">thuisbatterij</a>? Ook daarover adviseren wij graag.</p>
<h2>Onderhoud in uw regio</h2>
<p>Onze onderhoudsdiensten zijn beschikbaar in heel Nederland, met een sterke focus op de regio Utrecht: {REGIO}.</p>''',
  REV_WEGER,
  [('Hoe vaak moeten zonnepanelen onderhouden worden?', 'Wij adviseren een jaarlijkse controle. Zo vindt u storingen, losse connectoren of een haperende omvormer op tijd, voordat het opbrengst kost.'),
   ('Mijn installateur is failliet. Kunnen jullie helpen?', 'Ja. Wij nemen het onderhoud van installaties van andere bedrijven graag over. We beginnen met een inspectie, zodat we weten hoe uw systeem ervoor staat.'),
   ('Wat kost onderhoud aan zonnepanelen?', 'Het vaste onderhoudscontract kost €299 per jaar inclusief btw. Voor losse storingen en onderhoud rekenen wij €70 per uur inclusief btw, plus €75 voorrijkosten als we verder dan 20 km moeten rijden.'),
   ('Mijn omvormer geeft een foutmelding. Wat nu?', 'Noteer de foutmelding of maak er een foto van en neem contact met ons op. Vaak kunnen we op basis daarvan al inschatten wat er aan de hand is.'),
   ('Reinigen jullie ook zonnepanelen?', 'Ja. Reiniging is onderdeel van ons onderhoud, net als het opnieuw aanbrengen van een coatinglaag.')],
  extra=oh_tarieven)

# ============================== BEDRIJVEN ==============================
bd = dienst_hero('bedrijven', 'Bedrijven', 'Zakelijke elektrotechniek &amp; energie.',
  'JTS Installatietechniek ondersteunt bedrijven bij elektrotechnische installaties en duurzame energieoplossingen. Van elektra en meterkasten tot zonnepanelen, batterijopslag en laadinfrastructuur. Altijd veilig, met oog voor toekomstige uitbreiding.',
  'bedrijven-plat-dak.jpg', 'Monteur van JTS draagt een zonnepaneel over een groot plat bedrijfsdak', 'Rekenvoorbeeld', '30 kW lager', '≈ ±€200 per maand minder netkosten', 1500, 1125)
bd += split('Waar wij bedrijven mee helpen', 'Concreet, nuchter en klaar voor groei.', '',
  [('Elektra &amp; verdelers/meterkasten', 'Uitbreiden, aanpassen, netjes en veilig opbouwen, klaar voor groei.'),
   ('Zonnepanelen op bedrijfspanden', 'Ontwerp en plaatsing met focus op veiligheid, monitoring en onderhoud.'),
   ('Batterijopslag &amp; energiesturing (EMS)', 'Interessant bij terugkerende pieken of beter benutten van eigen opwek — alleen als het technisch én financieel klopt.'),
   ('Laadinfrastructuur (AC en waar passend DC)', 'Schaalbaar laadplein, load balancing, voorbereiding op uitbreiding.'),
   ('Onderhoud &amp; service', 'Continuïteit, overzicht en snelle opvolging bij issues.')],
  'bedrijven-dakvlak.jpg', 'Groot bedrijfsdak met zonnepanelen onder een blauwe lucht', 1500, 1125, 'Plan een kennismaking', 'bedrijven')
bd += '''<section class="wit">
  <div class="twee">
    <div><div class="eyebrow">Piek en peak shaving</div><h2>Besparen op pieken en ruimte maken voor groei.</h2></div>
    <div class="artikel" style="padding-top:8px">
      <p>Bij veel bedrijven zit de pijn niet in het jaarverbruik, maar in korte pieken: alles tegelijk aan en je installatie “zit vol”. Dat merk je aan beperkingen, zoals geen extra machines, koeling, keuken of laders, of gedoe in de verdeler. Bij grootzakelijk kan het bovendien doorwerken in netwerkkosten.</p>
      <h3>Wat bedoelen we met piek?</h3><p><strong>Piek (kW)</strong> is het hoogste moment dat je tegelijk afneemt; vaak zie je dit terug in kwartierwaarden. <strong>Peak shaving</strong> is die piek lager maken door slimmer te schakelen (eerste stap) en soms met een batterij die tijdelijk bijspringt (alleen als het klopt).</p>
    </div>
  </div>
  <div class="situaties">
    <div class="situatie"><div class="nr">Situatie 1</div><h3>Alles start tegelijk</h3><p>’s Ochtends of rond de lunch gaat alles aan: machines, koeling, keuken, compressor. De piek wordt dan bepaald door timing, niet door je echte behoefte. Startmomenten spreiden, prioriteiten instellen en de verdeling in de meterkast netjes maken geeft rust én voorkomt dat je te snel aan verzwaring denkt.</p></div>
    <div class="situatie"><div class="nr">Situatie 2</div><h3>Laden zonder sturing</h3><p>Zakelijk laden werkt prima — als je het slim verdeelt. Zonder load balancing trekken laadmomenten je piek onnodig omhoog. Wij ontwerpen een laadplein schaalbaar, van enkele laadpalen tot grotere installaties, met sturing zodat je installatie niet “op slot” gaat.</p></div>
    <div class="situatie"><div class="nr">Situatie 3</div><h3>Netcapaciteit is de rem</h3><p>Meer machines, extra koeling, warmtepompen of een DC-lader: het kan vaak wél, maar niet zomaar “erbij”. Met fasebalans, reserves, logische groepen, kabeltrajecten en slimme sturing maken we je installatie groei-proof: meer bruikbare capaciteit op het juiste moment.</p></div>
  </div>
  <div class="rekenvoorbeeld">
    <div class="groot-getal">30 kW <span>≈ ±€200</span></div>
    <p><strong>Wat levert dit op in euro’s?</strong> Bij sommige grootzakelijke tariefstructuren tellen pieken mee in de netwerkkosten. 30 kW structureel lager kan, afhankelijk van de tariefcategorie, grofweg ±€200 per maand schelen aan netbeheer-transportcomponenten. Wij beloven dit nooit zomaar: we bepalen het op basis van jouw meetdata en tariefindeling.</p>
    <a class="knop" href="aanvragen.html?dienst=bedrijven">Laat het doorrekenen</a>
  </div>
</section>
<section class="over">
  <div class="twee">
    <div><div class="eyebrow">Voor aannemers &amp; vastgoed</div><h2>Samen verduurzamen.</h2>
      <p>We zijn actief op zoek naar aannemers, vastgoedpartijen en ontwikkelaars om langdurig mee samen te werken aan elektrische renovaties en verduurzamingsprojecten: meterkasten en verdeelinrichtingen, voorbereiding op elektrificatie, laadinfrastructuur, PV en waar passend energieopslag.</p>
      <p>Wij houden het nuchter: duidelijke afspraken, strakke uitvoering en een planning waar je op kunt bouwen. Bij grote projecten werken we samen met East Connect, met ruim 25 jaar ervaring in installatietechniek en energiemanagement; de uitvoering ligt bij JTS.</p>
    </div>
    <div class="artikel" style="padding-top:8px"><div class="cta-blok" style="margin-top:0"><p>Interesse om samen te werken? Plan een kennismaking.</p><a class="knop" href="aanvragen.html?dienst=bedrijven">Neem contact op</a></div></div>
  </div>
</section>
'''
bd_vragen = [('Moet ik altijd verzwaren als ik uitbreid?', 'Niet altijd. Vaak kun je eerst winst pakken met verdeling, fasebalans en slimme sturing. Verzwaren is soms nodig, maar niet de eerste stap.'),
  ('Is een batterij altijd rendabel?', 'Nee. Soms wel, soms niet. Als pieken kort en regelmatig zijn, of als je veel eigen opwek beter wil benutten, kan het interessant worden. We rekenen het door.'),
  ('Kunnen we meer laadpalen plaatsen op de bestaande aansluiting?', 'Vaak wel, mits je het slim ontwerpt. Load balancing en een goede verdeleropbouw zijn het verschil tussen “gedoe” en “werkt gewoon”.'),
  ('Wat is de eerste stap?', 'We starten met inzicht: meetdata en kwartierwaarden, piekmomenten, de grootste verbruikers en je uitbreidingsplannen. Daarna krijg je een plan dat technisch klopt én uitvoerbaar is.')]
bd_faq, bd_schema = faq(bd_vragen, titel='Veelgestelde vragen, kort en eerlijk')
pagina('bedrijven.html', 'Zakelijke elektrotechniek en peak shaving | JTS Installatietechniek',
  'Elektra, meterkasten, zonnepanelen, batterijopslag en laadinfrastructuur voor bedrijven. Besparen op pieken (peak shaving) en ruimte maken voor groei.',
  'bedrijven', bd + bd_faq + WAAROM,
  schema=[dienst_schema('Zakelijke elektrotechniek en energieoplossingen', 'Elektra, meterkasten, zonnepanelen, batterijopslag, laadinfrastructuur en peak shaving voor bedrijven.', 'Zakelijke elektrotechniek'), kruimel_schema('Bedrijven', 'bedrijven.html'), bd_schema])

# ============================== ONS VERHAAL ==============================
ov = f'''<section class="hero hero--dienst">
  <div class="hero-raster">
    <div class="hero-tekst">
      <nav class="kruimel" aria-label="Kruimelpad"><a href="index.html">Home</a><span>/</span><span>Ons verhaal</span></nav>
      <div class="badge"><span class="stip">{ic("zonnepanelen",10,"#fff","2.4")}</span><span class="tekst">Opgericht in december 2022</span></div>
      <h1>Ons verhaal.</h1>
      <p class="intro">JTS Installatietechniek is opgericht door Jesse Odijk, Tjark Boot en Stijn Ronner, met één duidelijke ambitie: bouwen aan iets van onszelf. Wat begon als een spannend avontuur, is uitgegroeid tot een bedrijf waar we elke dag met trots aan werken.</p>
      <div class="knoppen">
        <a class="knop" href="aanvragen.html">Offerte aanvragen</a>
        <a class="knop knop--rand" href="#hoe-het-begon">Lees het verhaal</a>
      </div>
    </div>
    <div class="hero-beeld">
      <div class="kader"><img class="beeld" src="assets/foto/verhaal/jts-team-hero.jpg" alt="Het team van JTS Installatietechniek bij de bedrijfsbus" width="1600" height="1384" fetchpriority="high" style="object-position:50% 35%"></div>
      <div class="label"><span class="stip">{ic("schild",10,"#fff","2.4")}</span>Het team van JTS</div>
      <div class="glas glas--onder">
        <div class="kop"><span class="icoon">{ic("bolt",11,"#fff","2.4")}</span><span class="naam">Sinds 2022</span></div>
        <div class="waarde">10.000+</div>
        <div class="onder">zonnepanelen geïnstalleerd</div>
      </div>
    </div>
  </div>
</section>
<section class="lang" id="hoe-het-begon">
  <div class="lang-raster">
    <article class="tekst">
      <p class="lead">In december 2022 schreven wij ons in bij de Kamer van Koophandel. De afgelopen jaren hebben we enorme stappen gezet. Soms sta je daar te weinig bij stil, terwijl het bijzonder is om te zien hoe ver je kunt komen door te doen, te leren en steeds beter te worden.</p>
      <p>Hoewel we nog niet staan waar we uiteindelijk naartoe willen, kijken we met vertrouwen vooruit. Onze focus ligt niet op de korte termijn. We denken in jaren: in groei, ontwikkeling en duurzame relaties met onze klanten en partners. De komende jaren staan in het teken van verdere professionalisering, innovatie en het blijven leveren van kwaliteit waar wij volledig achter staan.</p>
      <h2>Hoe het begon</h2>
      <p>Jesse Odijk en Tjark Boot begonnen hun carrière in de duurzaamheidssector bij Greenlink Nederland B.V., een solarbedrijf waar zij veel praktijkervaring opdeden. Daar leerden zij de eigenaren Maarten Strengers en Jaap de Jong goed kennen — prachtige mensen die dicht bij ons hart staan.</p>
      <p>Stijn Ronner werkte in die periode in de horeca en volgde zijn eigen pad. We kenden elkaar al langere tijd, maar het samen ondernemen kwam pas later. Toen duidelijk werd dat onze ambities en mentaliteit goed bij elkaar pasten, besloten we de krachten te bundelen.</p>
      <p>In de beginfase maakten we letterlijk onze handen vuil. We deden alles wat nodig was, met een sterke focus op het schoonmaken en onderhouden van zonnepanelen. Vanuit daar groeiden we stap voor stap door naar waar onze echte passie lag: het installeren en realiseren van grotere zonnestroominstallaties.</p>
      <h2>Groeien door te doen</h2>
      <p>Na verloop van tijd kwam DenG Solar op ons pad, een betrouwbare energiepartner waar we inmiddels al jaren mee samenwerken. Binnen DenG leerden we Theo Mostert en Paul van Scharrenburg goed kennen. Zij zagen onze motivatie, leergierigheid en oog voor kwaliteit, en gaven ons het vertrouwen om verder te groeien. Daar zijn wij zeer dankbaar voor.</p>
      <p>Ons eerste grote project binnen deze samenwerking was de installatie van 400 zonnepanelen bij JdB Groep in Nieuwveen: ons eerste project als onderaannemer en een belangrijk moment in onze ontwikkeling. Door onze inzet en focus op kwaliteit groeide het vertrouwen snel. Met én dankzij DenG Solar hebben wij inmiddels meer dan 10.000 zonnepanelen mogen installeren, met vele foutloze Scope-12-keuringen. Een prestatie waar we trots op zijn en die veel zegt over de manier waarop wij werken.</p>
      <div class="projecten">
        <figure class="project"><img src="assets/foto/verhaal/odilliapeel-2025.jpg" alt="Monteurs van JTS leggen zonnepanelen op een bedrijfsdak in Odilliapeel" loading="lazy"><figcaption>Odilliapeel · 2025</figcaption></figure>
        <figure class="project"><img src="assets/foto/verhaal/raadsheeren-2025.jpg" alt="Nieuwe meterkast van 3×250 ampère bij Raadsheeren" loading="lazy"><figcaption>Raadsheeren · 2025</figcaption></figure>
        <figure class="project"><img src="assets/foto/verhaal/middenbeemster-2024.jpg" alt="Zonnepanelen op een groot bedrijfsdak in Middenbeemster" loading="lazy"><figcaption>Middenbeemster · 2024</figcaption></figure>
        <figure class="project"><img src="assets/foto/verhaal/nieuwveen-2023.jpg" alt="400 zonnepanelen op een bedrijfsdak in Nieuwveen" loading="lazy"><figcaption>Nieuwveen · 2023</figcaption></figure>
      </div>
      <p>Naast zonnepanelen breidden we onze werkzaamheden stap voor stap uit. Ons eerste laadpalenproject mochten we uitvoeren voor Willem Boot. Hij gaf ons in een vroege fase het vertrouwen en de ruimte om te leren, te groeien en verantwoordelijkheid te nemen, iets wat wij enorm waarderen.</p>
      <p>Natuurlijk ging niet alles in één keer perfect. Sommige keuzes hadden achteraf beter gekund en sommige oplossingen zijn nog altijd work in progress. Wat wél altijd vaststond: wij draaien ervoor op, nemen verantwoordelijkheid en laten zien dat we er staan — ook als het ingewikkeld wordt.</p>
      <p>Die ontwikkeling leidde uiteindelijk tot steeds zwaardere en technisch uitdagendere projecten, waaronder het vervangen van een 3×250 ampère meterkast bij Raadsheeren. Een project dat laat zien hoe ver we inmiddels zijn gekomen en waar we als team trots op zijn. Tegelijkertijd hebben we onze kennis steeds verder verbreed. Naast <a href="zonnepanelen.html">zonnepanelen</a> zijn we ons gaan specialiseren in <a href="thuisbatterijen.html">batterijsystemen</a>, <a href="laadpalen.html">laadpalen</a>, meterkasten, verlichting en elektrische renovaties. We werken volgens de NEN 1010- en NEN 3140-normen en blijven ons continu ontwikkelen.</p>
      <h2>Waar we nu staan</h2>
      <p>Vandaag bestaat JTS Installatietechniek uit een hecht en groeiend team. Naast de oprichters werken Ruben Striekwold en Sebastiaan Odijk bij ons in dienst. Ruben is er vrijwel vanaf het begin bij en heeft zich ontwikkeld tot een echte vakman; het is super leuk om als team elkaar te zien groeien. Sebastiaan, de broer van Jesse, versterkt het team met dezelfde inzet en mentaliteit.</p>
      <div class="team">
        <div><strong>Jesse Odijk</strong><span>Oprichter</span></div>
        <div><strong>Tjark Boot</strong><span>Oprichter</span></div>
        <div><strong>Stijn Ronner</strong><span>Oprichter</span></div>
        <div><strong>Ruben Striekwold</strong><span>Monteur</span></div>
        <div><strong>Sebastiaan Odijk</strong><span>Monteur</span></div>
      </div>
      <p>Samen bouwen we verder aan JTS Installatietechniek: een nuchter, technisch sterk installatiebedrijf dat staat voor kwaliteit, verantwoordelijkheid en oplossingen die klaar zijn voor de toekomst. De komende jaren staan in het teken van verdere groei en ontwikkeling. Er zijn veel nieuwe stappen in voorbereiding, en dat zal zichtbaar worden. Wij zijn nog lang niet klaar in deze sector.</p>
      <h2>JTS en NuZon</h2>
      <p>Sinds januari zijn wij ook de eigenaren van NuZon B.V., dat sinds 2012 zonnepanelen plaatst vanuit Soest. NuZon en JTS zijn twee zelfstandige bedrijven met dezelfde eigenaren: NuZon is de naam, de historie en de klanten, JTS Installatietechniek doet het werk. <a href="https://www.nuzon.nl/" target="_blank" rel="noopener">Bezoek NuZon</a>.</p>
    </article>
    <aside class="lang-zij">
      <div class="zij-kaart">
        <div class="eyebrow" style="color:var(--accent-tint)">Werken met JTS</div>
        <div class="zij-titel">Benieuwd wat wij voor u kunnen doen?</div>
        <p>Beantwoord een paar korte vragen, dan nemen wij binnen twee werkdagen contact op.</p>
        <a class="knop" href="aanvragen.html">Offerte aanvragen</a>
        <div class="zij-contact"><a href="tel:+31307816767">030 781 6767</a><a href="https://wa.me/31307816767" target="_blank" rel="noopener">WhatsApp</a></div>
        <ul class="zij-lijst"><li>{ic("vink",14)}Opgericht in december 2022</li><li>{ic("vink",14)}10.000+ zonnepanelen geïnstalleerd</li><li>{ic("vink",14)}NEN 1010 · NEN 3140 · VCA</li></ul>
      </div>
    </aside>
  </div>
</section>
''' + WAAROM
pagina('ons-verhaal.html', 'Ons verhaal | JTS Installatietechniek uit Soest',
  'JTS Installatietechniek is in 2022 opgericht door Jesse Odijk, Tjark Boot en Stijn Ronner. Van het reinigen van zonnepanelen naar 10.000+ geïnstalleerde panelen en complete elektrotechniek.',
  'ons-verhaal', ov, schema=[kruimel_schema('Ons verhaal', 'ons-verhaal.html')], og_beeld='assets/foto/verhaal/jts-team-hero.jpg')
