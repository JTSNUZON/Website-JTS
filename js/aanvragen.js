/* =====================================================================
   Aanvraagfunnel (aanvragen.html)

   FORMULIER — waar de aanvraag naartoe gaat. Standaard Web3Forms:
   maak een gratis account op web3forms.com met info@jtstechniek.nl,
   en zet de 'Access Key' hieronder bij sleutel. Zolang sleutel leeg is,
   opent de laatste stap het mailprogramma van de klant met de complete
   aanvraag erin (en kan de klant de tekst kopiëren).

   De vragen staan in STAPPEN. Een vraag met 'als' verschijnt alleen
   wanneer die functie true geeft voor de antwoorden tot nu toe.
   ===================================================================== */
var FORMULIER = {
  url: 'https://api.web3forms.com/submit',
  sleutel: ''
};
var ONTVANGER = 'info@jtstechniek.nl';
var WHATSAPP  = '31307816767';

var DIENSTEN = {
  'elektricien':     'Elektricien',
  'zonnepanelen':    'Zonnepanelen',
  'laadpalen':       'Laadpaal',
  'thuisbatterijen': 'Thuisbatterij',
  'de-hermontage':   'De/hermontage van panelen',
  'onderhoud':       'Onderhoud of storing',
  'bedrijven':       'Piekbesparing / energieadvies',
  'anders':          'Iets anders'
};

function heeft(a, dienst) { return (a.dienst || []).indexOf(dienst) > -1; }
function heeftEen(a, lijst) { return lijst.some(function (d) { return heeft(a, d); }); }
function opties(lijst) { return lijst.map(function (o) { return typeof o === 'string' ? { w: o, t: o } : o; }); }

var STAPPEN = [
  {
    sleutel: 'wie', kort: 'Wie bent u?',
    titel: 'Voor wie is de aanvraag?',
    vragen: [
      { id: 'wie', type: 'radio', groot: true, verplicht: true, opties: [
        { w: 'Particulier', t: 'Particulier', u: 'Voor mijn woning' },
        { w: 'Bedrijf', t: 'Bedrijf', u: 'Voor een bedrijfspand, VvE of vastgoed' }
      ]}
    ]
  },
  {
    sleutel: 'dienst', kort: 'Waarmee?',
    titel: 'Waar kunnen we u mee helpen?',
    toelichting: 'Kies alles wat van toepassing is.',
    vragen: [
      { id: 'dienst', type: 'check', groot: true, verplicht: true, opties: function (a) {
        return Object.keys(DIENSTEN).filter(function (k) { return k !== 'bedrijven' || a.wie === 'Bedrijf'; })
          .map(function (k) { return { w: k, t: DIENSTEN[k] }; });
      }}
    ]
  },
  {
    sleutel: 'situatie', kort: 'Uw situatie',
    titel: 'Vertel iets over de situatie.',
    toelichting: 'Weet u iets niet zeker? Kies “Weet ik niet”, dan kijken we het samen na.',
    vragen: [
      /* zonnepanelen */
      { id: 'daktype', label: 'Op wat voor dak of plek komen de panelen?', type: 'radio', verplicht: true, als: function (a) { return heeft(a, 'zonnepanelen'); },
        opties: opties(['Schuin pannendak', 'Plat dak', 'Staal- of golfplaatdak', 'Grondopstelling', 'Weet ik niet']) },
      { id: 'verbruik', label: 'Jaarverbruik in kWh', type: 'tekst', invoer: 'numeric', hint: 'Staat op uw jaarafrekening, bijv. 3500', als: function (a) { return heeft(a, 'zonnepanelen'); } },
      { id: 'bestaand', label: 'Liggen er al zonnepanelen?', type: 'radio', verplicht: true, als: function (a) { return heeftEen(a, ['zonnepanelen', 'thuisbatterijen']); },
        opties: opties(['Ja', 'Nee']) },
      { id: 'aantalBestaand', label: 'Hoeveel panelen liggen er?', type: 'tekst', invoer: 'numeric', als: function (a) { return heeftEen(a, ['zonnepanelen', 'thuisbatterijen']) && a.bestaand === 'Ja'; } },
      /* thuisbatterij */
      { id: 'batterijDoel', label: 'Wat wilt u met de batterij bereiken?', type: 'check', verplicht: true, als: function (a) { return heeft(a, 'thuisbatterijen'); },
        opties: opties(['Noodstroom bij stroomuitval', 'Niet meer terugleveren', 'Slim energiebeheer (EMS)', 'Off-grid', 'Weet ik nog niet']) },
      /* laadpaal */
      { id: 'laadpunten', label: 'Hoeveel laadpunten?', type: 'radio', verplicht: true, als: function (a) { return heeft(a, 'laadpalen'); },
        opties: opties(['1', '2 tot 4', '5 of meer']) },
      { id: 'afstand', label: 'Afstand van meterkast tot parkeerplek', type: 'radio', verplicht: true, als: function (a) { return heeft(a, 'laadpalen'); },
        opties: opties(['Minder dan 10 meter', '10 tot 25 meter', 'Meer dan 25 meter', 'Weet ik niet']) },
      { id: 'auto', label: 'Welke auto(’s)?', type: 'tekst', hint: 'Bijv. Tesla Model 3', als: function (a) { return heeft(a, 'laadpalen'); } },
      /* elektricien */
      { id: 'klus', label: 'Wat voor klus is het?', type: 'check', verplicht: true, als: function (a) { return heeft(a, 'elektricien'); },
        opties: opties(['Groepenkast vervangen of uitbreiden', 'Extra stopcontacten', 'Verlichting (binnen of buiten)', 'Netwerkkabels', 'Storing of kortsluiting', 'Nieuwbouw of renovatie', 'Aarding of veiligheidsinspectie', 'Iets anders']) },
      /* de/hermontage */
      { id: 'aantalPanelen', label: 'Om hoeveel panelen gaat het?', type: 'tekst', invoer: 'numeric', verplicht: true, als: function (a) { return heeft(a, 'de-hermontage'); } },
      { id: 'reden', label: 'Waarom moeten de panelen eraf?', type: 'radio', verplicht: true, als: function (a) { return heeft(a, 'de-hermontage'); },
        opties: opties(['Dakrenovatie', 'Schilderwerk', 'Nieuwe dakkapel', 'Lekkage', 'Verhuizing', 'Anders']) },
      { id: 'datumDak', label: 'Wanneer komt de dakdekker of schilder?', type: 'tekst', soort: 'date', als: function (a) { return heeft(a, 'de-hermontage'); } },
      /* onderhoud */
      { id: 'onderhoudWat', label: 'Waarvoor is het onderhoud?', type: 'check', verplicht: true, als: function (a) { return heeft(a, 'onderhoud'); },
        opties: opties(['Zonnepanelen', 'Laadpaal', 'Elektrische installatie']) },
      { id: 'probleem', label: 'Wat speelt er?', type: 'radio', verplicht: true, als: function (a) { return heeft(a, 'onderhoud'); },
        opties: opties(['Storing of foutmelding', 'Opbrengst lager dan normaal', 'Periodiek onderhoud', 'Onderhoudscontract (€299 per jaar)', 'Oude installateur niet meer bereikbaar']) },
      { id: 'omvormer', label: 'Merk van de omvormer', type: 'tekst', hint: 'Bijv. SolarEdge, Growatt, SMA', als: function (a) { return heeft(a, 'onderhoud'); } },
      /* bedrijven */
      { id: 'verbruikers', label: 'Wat zijn de grootste verbruikers?', type: 'check', verplicht: true, als: function (a) { return heeft(a, 'bedrijven'); },
        opties: opties(['Machines', 'Koeling', 'Keuken', 'Compressor', 'Laadpalen', 'Warmtepompen', 'Weet ik niet']) },
      { id: 'meetdata', label: 'Zijn er meetdata of kwartierwaarden beschikbaar?', type: 'radio', verplicht: true, als: function (a) { return heeft(a, 'bedrijven'); },
        opties: opties(['Ja', 'Nee', 'Weet ik niet']) },
      { id: 'aansluitwaarde', label: 'Aansluitwaarde', type: 'tekst', hint: 'Bijv. 3x80A of 160 kVA', als: function (a) { return heeft(a, 'bedrijven'); } },
      /* algemeen */
      { id: 'fase', label: 'Wat voor aansluiting heeft u?', type: 'radio', verplicht: true,
        als: function (a) { return heeftEen(a, ['zonnepanelen', 'laadpalen', 'thuisbatterijen', 'elektricien']); },
        opties: [{ w: '1-fase', t: '1-fase', u: 'Eén hoofdschakelaar met één draad' }, { w: '3-fase', t: '3-fase', u: 'Brede hoofdschakelaar, vaak 3x25A' }, { w: 'Weet ik niet', t: 'Weet ik niet' }] },
      { id: 'omschrijving', label: 'Omschrijf kort uw situatie of vraag', type: 'tekstvak', hint: 'Alles wat ons helpt om u goed te adviseren.', verplicht: function (a) { return heeft(a, 'anders'); } }
    ]
  },
  {
    sleutel: 'planning', kort: 'Planning & budget',
    titel: 'Planning en budget.',
    vragen: [
      { id: 'wanneer', label: 'Wanneer wilt u het geregeld hebben?', type: 'radio', verplicht: true,
        opties: opties(['Zo snel mogelijk', 'Binnen 3 maanden', 'Binnen een jaar', 'Ik oriënteer me nog']) },
      { id: 'budget', label: 'Heeft u al een budget in gedachten?', type: 'radio', verplicht: true,
        opties: opties(['Tot €2.500', '€2.500 – €10.000', '€10.000 – €25.000', 'Meer dan €25.000', 'Weet ik nog niet']) },
      { id: 'elders', label: 'Heeft u al een offerte van een ander bedrijf?', type: 'radio', verplicht: true,
        opties: opties(['Ja', 'Nee']) }
    ]
  },
  {
    sleutel: 'contact', kort: 'Contactgegevens',
    titel: 'Hoe bereiken we u?',
    toelichting: 'We gebruiken uw gegevens alleen om contact op te nemen over deze aanvraag.',
    vragen: [
      { type: 'velden', velden: [
        { id: 'naam', label: 'Naam', verplicht: true, auto: 'name' },
        { id: 'bedrijf', label: 'Bedrijfsnaam', verplicht: true, auto: 'organization', als: function (a) { return a.wie === 'Bedrijf'; } },
        { id: 'email', label: 'E-mailadres', soort: 'email', verplicht: true, auto: 'email' },
        { id: 'telefoon', label: 'Telefoonnummer', soort: 'tel', verplicht: true, auto: 'tel' },
        { id: 'postcode', label: 'Postcode', verplicht: true, auto: 'postal-code' },
        { id: 'huisnummer', label: 'Huisnummer', verplicht: true },
        { id: 'plaats', label: 'Plaats', auto: 'address-level2' }
      ]},
      { id: 'voorkeur', label: 'Hoe wilt u het liefst contact?', type: 'radio', verplicht: true, opties: opties(['Bellen', 'E-mail', 'WhatsApp']) },
      { id: 'fotos', label: 'Foto’s van de meterkast of het dak', type: 'radio', verplicht: true, opties: [
        { w: 'Ik stuur foto’s via WhatsApp', t: 'Via WhatsApp', u: 'Na het versturen krijgt u een knop om ze te sturen' },
        { w: 'Ik stuur foto’s via e-mail', t: 'Via e-mail', u: 'Naar ' + ONTVANGER },
        { w: 'Liever geen foto’s, kom kijken', t: 'Kom liever kijken', u: 'Gratis inspectie op locatie' }
      ]}
    ]
  },
  { sleutel: 'controle', kort: 'Controleren', titel: 'Klopt alles?', toelichting: 'Controleer uw antwoorden en verstuur de aanvraag.', vragen: [] }
];

/* ------------------------------------------------------------------ */

(function () {
  var doos = document.getElementById('funnel');
  var lijst = document.getElementById('stappenlijst');
  var OPSLAG = 'jts-aanvraag';
  var a = {}, stap = 0, verstuurd = false;

  try { var bewaard = JSON.parse(sessionStorage.getItem(OPSLAG) || 'null'); if (bewaard) { a = bewaard.a || {}; stap = bewaard.stap || 0; } } catch (e) {}
  try {
    var vooraf = new URLSearchParams(location.search).get('dienst');
    if (vooraf && DIENSTEN[vooraf] && !(a.dienst && a.dienst.length)) {
      a.dienst = [vooraf];
      if (vooraf === 'bedrijven') a.wie = 'Bedrijf';
    }
  } catch (e) {}

  function bewaar() { try { sessionStorage.setItem(OPSLAG, JSON.stringify({ a: a, stap: stap })); } catch (e) {} }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function zichtbaar(v) { return !v.als || v.als(a); }
  function isVerplicht(v) { return typeof v.verplicht === 'function' ? v.verplicht(a) : !!v.verplicht; }
  function optiesVan(v) { return typeof v.opties === 'function' ? v.opties(a) : v.opties; }
  function leeg(w) { return w == null || w === '' || (Array.isArray(w) && !w.length); }

  /* ---- alle zichtbare vragen van een stap, velden-groepen uitgevouwen ---- */
  function vragenVan(s) {
    var uit = [];
    s.vragen.forEach(function (v) {
      if (!zichtbaar(v)) return;
      if (v.type === 'velden') v.velden.forEach(function (f) { if (zichtbaar(f)) uit.push(f); });
      else uit.push(v);
    });
    return uit;
  }

  /* ---- antwoorden opruimen die bij verborgen vragen horen ---- */
  function ruimOp() {
    STAPPEN.forEach(function (s) {
      s.vragen.forEach(function (v) {
        var alle = v.type === 'velden' ? v.velden : [v];
        alle.forEach(function (f) { if ((!zichtbaar(v) || !zichtbaar(f)) && f.id in a) delete a[f.id]; });
      });
    });
  }

  /* ---- tekenen ---- */
  function tekenLijst() {
    lijst.innerHTML = STAPPEN.map(function (s, i) {
      return '<li class="' + (i < stap ? 'klaar' : i === stap ? 'nu' : '') + '"' + (i === stap ? ' aria-current="step"' : '') + '>' + esc(s.kort) + '</li>';
    }).join('');
  }

  function vraagHtml(v) {
    var vp = isVerplicht(v);
    var opt = vp ? '' : ' <span class="optioneel">(optioneel)</span>';
    if (v.type === 'radio' || v.type === 'check') {
      var soort = v.type === 'radio' ? 'radio' : 'checkbox';
      var w = a[v.id];
      var knoppen = optiesVan(v).map(function (o, i) {
        var aan = soort === 'radio' ? w === o.w : (w || []).indexOf(o.w) > -1;
        return '<label class="keuze"><input type="' + soort + '" name="' + v.id + '" id="' + v.id + '-' + i + '" value="' + esc(o.w) + '"' + (aan ? ' checked' : '') + '><span class="vink"></span><span><span class="k-titel">' + esc(o.t) + '</span>' + (o.u ? '<span class="k-uitleg">' + esc(o.u) + '</span>' : '') + '</span></label>';
      }).join('');
      return '<fieldset class="vraag" data-vraag="' + v.id + '">' + (v.label ? '<legend>' + esc(v.label) + opt + '</legend>' : '<legend class="sr">' + esc(STAPPEN[stap].titel) + '</legend>') +
        '<div class="keuzes' + (v.groot ? ' keuzes--groot' : '') + '">' + knoppen + '</div></fieldset>';
    }
    if (v.type === 'tekstvak') {
      return '<div class="vraag veld" data-vraag="' + v.id + '"><label for="' + v.id + '">' + esc(v.label) + opt + '</label><textarea id="' + v.id + '" name="' + v.id + '" placeholder="' + esc(v.hint || '') + '">' + esc(a[v.id] || '') + '</textarea></div>';
    }
    return '<div class="vraag veld" data-vraag="' + v.id + '">' + veldHtml(v, opt) + '</div>';
  }

  function veldHtml(f, opt) {
    return '<label for="' + f.id + '">' + esc(f.label) + (opt != null ? opt : (isVerplicht(f) ? '' : ' <span class="optioneel">(optioneel)</span>')) + '</label>' +
      '<input id="' + f.id + '" name="' + f.id + '" type="' + (f.soort || 'text') + '"' + (f.invoer ? ' inputmode="' + f.invoer + '"' : '') + (f.auto ? ' autocomplete="' + f.auto + '"' : '') +
      ' value="' + esc(a[f.id] || '') + '" placeholder="' + esc(f.hint || '') + '">';
  }

  function teken() {
    tekenLijst();
    var s = STAPPEN[stap];
    var html = '<div class="voortgang" aria-hidden="true"><div style="width:' + Math.round((stap + 1) / STAPPEN.length * 100) + '%"></div></div>' +
      '<div class="stap-label">Stap ' + (stap + 1) + ' van ' + STAPPEN.length + ' · ' + esc(s.kort) + '</div>' +
      '<h2 id="staptitel" tabindex="-1">' + esc(s.titel) + '</h2>' + (s.toelichting ? '<p class="toelichting">' + esc(s.toelichting) + '</p>' : '');

    if (s.sleutel === 'controle') {
      html += overzichtHtml();
    } else {
      s.vragen.forEach(function (v) {
        if (!zichtbaar(v)) return;
        if (v.type === 'velden') {
          html += '<div class="vraag velden">' + v.velden.filter(zichtbaar).map(function (f) {
            return '<div class="veld' + (f.id === 'naam' || f.id === 'bedrijf' ? '' : '') + '" data-vraag="' + f.id + '">' + veldHtml(f) + '</div>';
          }).join('') + '</div>';
        } else html += vraagHtml(v);
      });
    }
    html += '<div id="fout"></div><div class="funnel-knoppen">' +
      (stap > 0 ? '<button type="button" class="knop knop--rand" id="terug">Terug</button>' : '<span></span>') +
      '<button type="button" class="knop" id="verder">' + (s.sleutel === 'controle' ? 'Aanvraag versturen' : 'Volgende') + '</button></div>';
    doos.innerHTML = html;

    doos.querySelectorAll('input, textarea').forEach(function (el) {
      el.addEventListener(el.type === 'radio' || el.type === 'checkbox' ? 'change' : 'input', function () {
        var vorige = JSON.stringify(vragenVan(STAPPEN[stap]).map(function (v) { return v.id; }));
        lees(el);
        if (el.type === 'radio' || el.type === 'checkbox') {
          ruimOp();
          // komen er door dit antwoord vragen bij of af, teken de stap opnieuw
          if (JSON.stringify(vragenVan(STAPPEN[stap]).map(function (v) { return v.id; })) !== vorige) { bewaar(); teken(); var z = document.getElementById(el.id); if (z) z.focus(); return; }
        }
        var blok = el.closest('[data-vraag]'); if (blok) blok.querySelectorAll('.ongeldig').forEach(function (x) { x.classList.remove('ongeldig'); });
        bewaar();
      });
    });
    doos.querySelectorAll('.wijzig').forEach(function (k) {
      k.addEventListener('click', function () { stap = +k.getAttribute('data-stap'); bewaar(); teken(); focusTitel(); });
    });
    var terug = document.getElementById('terug');
    if (terug) terug.addEventListener('click', function () { stap--; bewaar(); teken(); focusTitel(); });
    document.getElementById('verder').addEventListener('click', verder);
    doos.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && e.target.tagName === 'INPUT' && e.target.type !== 'radio' && e.target.type !== 'checkbox') { e.preventDefault(); verder(); }
    });
  }

  function focusTitel() {
    var t = document.getElementById('staptitel');
    if (t) t.focus({ preventScroll: true });
    var top = doos.getBoundingClientRect().top + window.scrollY - 110;
    if (window.scrollY > top) window.scrollTo({ top: top, behavior: 'smooth' });
  }

  function lees(el) {
    if (el.type === 'checkbox') {
      a[el.name] = Array.prototype.map.call(doos.querySelectorAll('input[name="' + el.name + '"]:checked'), function (x) { return x.value; });
    } else if (el.type === 'radio') {
      if (el.checked) a[el.name] = el.value;
    } else a[el.name] = el.value.trim();
  }

  /* ---- controleren ---- */
  function fouten() {
    var uit = [];
    vragenVan(STAPPEN[stap]).forEach(function (v) {
      var w = a[v.id];
      if (isVerplicht(v) && leeg(w)) uit.push({ id: v.id, tekst: v.label ? 'Vul in: ' + v.label.toLowerCase() : 'Maak een keuze' });
      else if (v.soort === 'email' && w && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(w)) uit.push({ id: v.id, tekst: 'Dit e-mailadres klopt niet helemaal.' });
      else if (v.soort === 'tel' && w && w.replace(/\D/g, '').length < 10) uit.push({ id: v.id, tekst: 'Vul een telefoonnummer van 10 cijfers in.' });
      else if (v.id === 'postcode' && w && !/^\d{4}\s?[a-zA-Z]{2}$/.test(w)) uit.push({ id: v.id, tekst: 'Vul een postcode in zoals 3762 EN.' });
    });
    return uit;
  }

  function verder() {
    if (STAPPEN[stap].sleutel === 'controle') return verstuur();
    var f = fouten();
    if (f.length) {
      document.getElementById('fout').innerHTML = '<div class="foutmelding" role="alert">' + f.map(function (x) { return esc(x.tekst); }).join('<br>') + '</div>';
      f.forEach(function (x) {
        var blok = doos.querySelector('[data-vraag="' + x.id + '"]');
        if (blok) blok.querySelectorAll('input, textarea, .keuze').forEach(function (el) { el.classList.add('ongeldig'); });
      });
      var eerste = doos.querySelector('[data-vraag="' + f[0].id + '"] input, [data-vraag="' + f[0].id + '"] textarea');
      if (eerste) eerste.focus();
      return;
    }
    stap++; bewaar(); teken(); focusTitel();
  }

  /* ---- overzicht en versturen ---- */
  function waarde(v) {
    var w = a[v.id];
    if (v.id === 'dienst') return (w || []).map(function (k) { return DIENSTEN[k]; }).join(', ');
    return Array.isArray(w) ? w.join(', ') : w;
  }
  function regels() {
    var uit = [];
    STAPPEN.forEach(function (s, i) {
      if (s.sleutel === 'controle') return;
      vragenVan(s).forEach(function (v) {
        if (leeg(a[v.id])) return;
        uit.push({ stap: i, label: v.label || s.titel.replace(/[.?]$/, ''), waarde: waarde(v) });
      });
    });
    return uit;
  }
  function overzichtHtml() {
    var html = '';
    STAPPEN.forEach(function (s, i) {
      if (s.sleutel === 'controle') return;
      var r = regels().filter(function (x) { return x.stap === i; });
      html += '<dl class="overzicht">' + r.map(function (x) { return '<dt>' + esc(x.label) + '</dt><dd>' + esc(x.waarde) + '</dd>'; }).join('') +
        '<button type="button" class="wijzig" data-stap="' + i + '">' + esc(s.kort) + ' wijzigen</button></dl>';
    });
    return html;
  }
  function onderwerp() {
    return 'Aanvraag ' + (a.dienst || []).map(function (k) { return DIENSTEN[k]; }).join(', ') + ' — ' + (a.bedrijf || a.naam || '') + ', ' + (a.postcode || '');
  }
  function platteTekst() {
    return regels().map(function (x) { return x.label + ': ' + x.waarde; }).join('\n');
  }

  function verstuur() {
    if (verstuurd) return;
    var knop = document.getElementById('verder');
    if (!FORMULIER.sleutel) { if (window.jtsMeet) jtsMeet('generate_lead', { diensten: (a.dienst || []).join(','), klant: a.wie, via: 'mail' }); return klaar(false); }
    knop.disabled = true; knop.textContent = 'Bezig met versturen…';
    var data = { access_key: FORMULIER.sleutel, subject: onderwerp(), from_name: 'Website JTS — aanvraag', replyto: a.email, botcheck: '' };
    regels().forEach(function (x) { data[x.label] = x.waarde; });
    fetch(FORMULIER.url, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().then(function (j) { if (!r.ok || j.success === false) throw new Error(j.message || r.status); }); })
      .then(function () { verstuurd = true; if (window.jtsMeet) jtsMeet('generate_lead', { diensten: (a.dienst || []).join(','), klant: a.wie }); klaar(true); })
      .catch(function () {
        knop.disabled = false; knop.textContent = 'Opnieuw proberen';
        document.getElementById('fout').innerHTML = '<div class="foutmelding" role="alert">Versturen lukte niet. Controleer uw internetverbinding en probeer het opnieuw, of mail de aanvraag naar ' + ONTVANGER + '.</div>';
      });
  }

  function klaar(gelukt) {
    var tekst = platteTekst();
    var mail = 'mailto:' + ONTVANGER + '?subject=' + encodeURIComponent(onderwerp()) + '&body=' + encodeURIComponent(tekst);
    var waTekst = 'Hallo JTS, hierbij de foto’s bij mijn aanvraag (' + (a.naam || '') + ', ' + (a.postcode || '') + ' ' + (a.huisnummer || '') + ').';
    var wa = 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(waTekst);
    var fotoKnop = a.fotos && a.fotos.indexOf('WhatsApp') > -1
      ? '<a class="knop knop--wa" href="' + wa + '" target="_blank" rel="noopener">Foto’s sturen via WhatsApp</a>'
      : a.fotos && a.fotos.indexOf('e-mail') > -1 ? '<a class="knop knop--rand" href="mailto:' + ONTVANGER + '?subject=' + encodeURIComponent('Foto’s bij aanvraag — ' + (a.naam || '')) + '">Foto’s mailen</a>' : '';
    var html = '<div class="klaar-scherm">';
    if (gelukt) {
      html += '<div class="groot-vink"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#3DD68C" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"/></svg></div>' +
        '<h2 id="staptitel" tabindex="-1" style="margin-top:22px">Bedankt, ' + esc((a.naam || '').split(' ')[0]) + '!</h2>' +
        '<p class="toelichting">Uw aanvraag is binnen. We nemen binnen twee werkdagen contact met u op' + (a.voorkeur ? ' via ' + esc(a.voorkeur.toLowerCase()) : '') + '.</p>' +
        '<div class="knoppen">' + fotoKnop + '<a class="knop knop--rand" href="index.html">Terug naar de homepage</a></div>';
      try { sessionStorage.removeItem(OPSLAG); } catch (e) {}
    } else {
      html += '<h2 id="staptitel" tabindex="-1">Nog één klik.</h2>' +
        '<p class="toelichting">Druk op de knop hieronder. Uw mailprogramma opent met de complete aanvraag erin; u hoeft alleen nog op verzenden te drukken. Opent er niets? Kopieer de tekst en mail die naar <strong>' + ONTVANGER + '</strong>.</p>' +
        '<div class="knoppen"><a class="knop" href="' + mail + '">Aanvraag mailen</a><button type="button" class="knop knop--rand" id="kopieer">Tekst kopiëren</button>' + fotoKnop + '</div>' +
        '<pre class="kopie-blok" id="kopietekst">' + esc(tekst) + '</pre>' +
        '<div class="funnel-knoppen"><button type="button" class="knop knop--rand" id="terug">Terug</button><span></span></div>';
    }
    html += '</div>';
    doos.innerHTML = html;
    lijst.querySelectorAll('li').forEach(function (li) { li.className = 'klaar'; });
    var k = document.getElementById('kopieer');
    if (k) k.addEventListener('click', function () {
      var gekopieerd = function () { k.textContent = 'Gekopieerd'; };
      if (navigator.clipboard) navigator.clipboard.writeText(tekst).then(gekopieerd, selecteer); else selecteer();
      function selecteer() { var r = document.createRange(); r.selectNodeContents(document.getElementById('kopietekst')); var s = getSelection(); s.removeAllRanges(); s.addRange(r); }
    });
    var t = document.getElementById('terug');
    if (t) t.addEventListener('click', function () { teken(); focusTitel(); });
    focusTitel();
  }

  if (stap >= STAPPEN.length) stap = 0;
  teken();
})();
