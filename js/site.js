/* =====================================================================
   JTS Installatietechniek — gedeeld script voor alle pagina's:
   menu (hamburger + Diensten-paneel), actief menu-item, WhatsApp-knop
   en het jaartal in de footer.

   WHATSAPP_NUMMER — landcode zonder +, zonder spaties of streepjes.
   GA_ID           — Google Analytics 4 meet-ID ("G-XXXXXXXXXX"). Leeg =
                     geen Analytics en geen cookiebalk. Analytics laadt pas
                     nadat de bezoeker toestemming geeft.
   ===================================================================== */
var WHATSAPP_NUMMER  = "31307816767";
var WHATSAPP_BERICHT = "Hallo JTS, ik heb een vraag over ";
var GA_ID            = "";

(function () {
  var balk = document.getElementById('topbalk');
  var hamburger = document.getElementById('hamburger');

  /* ---- hamburger (telefoon) ---- */
  function zetMenu(open) {
    balk.classList.toggle('open', open);
    hamburger.setAttribute('aria-expanded', open ? 'true' : 'false');
    hamburger.setAttribute('aria-label', open ? 'Menu sluiten' : 'Menu openen');
  }
  hamburger.addEventListener('click', function () { zetMenu(!balk.classList.contains('open')); });
  document.querySelectorAll('#menu a').forEach(function (a) {
    a.addEventListener('click', function () { zetMenu(false); zetPaneel(false); });
  });

  /* ---- Diensten-paneel: hover opent, klik wisselt, Escape sluit ---- */
  var groep = document.querySelector('.menu-groep');
  var knop = groep && groep.querySelector('.menu-knop');
  function zetPaneel(open) {
    if (!groep) return;
    groep.classList.toggle('open', open);
    knop.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (groep) {
    var hoverMag = window.matchMedia('(hover: hover) and (min-width: 701px)');
    groep.addEventListener('mouseenter', function () { if (hoverMag.matches) zetPaneel(true); });
    groep.addEventListener('mouseleave', function () { if (hoverMag.matches) zetPaneel(false); });
    knop.addEventListener('click', function () { zetPaneel(!groep.classList.contains('open')); });
    groep.addEventListener('focusout', function (e) { if (!groep.contains(e.relatedTarget)) zetPaneel(false); });
    document.addEventListener('click', function (e) { if (!groep.contains(e.target)) zetPaneel(false); });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (groep && groep.classList.contains('open')) { zetPaneel(false); knop.focus(); }
    zetMenu(false);
  });

  /* ---- actief menu-item: per pagina vast, op de homepage per sectie ---- */
  var sectieLinks = Array.prototype.filter.call(document.querySelectorAll('#menu > a'), function (a) {
    var h = a.getAttribute('href');
    return h.indexOf('#') > -1 && document.getElementById(h.split('#')[1]);
  });
  if (sectieLinks.length && document.body.classList.contains('home')) {
    var markeer = function () {
      var y = window.scrollY + 140, actief = -1;
      sectieLinks.forEach(function (a, i) {
        var s = document.getElementById(a.getAttribute('href').split('#')[1]);
        if (s.offsetTop <= y) actief = i;
      });
      sectieLinks.forEach(function (a, i) { a.classList.toggle('actief', i === actief); });
      if (knop) knop.classList.toggle('actief', actief === -1 && window.scrollY > 300 && window.scrollY < document.getElementById('diensten').offsetTop + document.getElementById('diensten').offsetHeight);
    };
    window.addEventListener('scroll', markeer, { passive: true });
    markeer();
  }

  /* ---- WhatsApp-knop ---- */
  var wa = document.createElement('a');
  wa.className = 'wa-knop';
  wa.href = 'https://wa.me/' + WHATSAPP_NUMMER + (WHATSAPP_BERICHT ? '?text=' + encodeURIComponent(WHATSAPP_BERICHT) : '');
  wa.target = '_blank';
  wa.rel = 'noopener';
  wa.setAttribute('aria-label', 'Stuur JTS een WhatsApp-bericht');
  wa.innerHTML = '<svg width="22" height="22" viewBox="0 0 24 24" fill="#08371C" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.4-.3z"/></svg><span class="wa-tekst">WhatsApp</span>';
  document.body.appendChild(wa);

  /* ---- Analytics met toestemming ---- */
  var COOKIE_SLEUTEL = 'jts-cookies';
  var geladen = false;
  function keuze() { try { return localStorage.getItem(COOKIE_SLEUTEL); } catch (e) { return null; } }
  function bewaarKeuze(w) { try { localStorage.setItem(COOKIE_SLEUTEL, w); } catch (e) {} }
  function laadAnalytics() {
    if (geladen || !GA_ID) return;
    geladen = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag('js', new Date());
    gtag('config', GA_ID, { anonymize_ip: true });
    var s = document.createElement('script');
    s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
  }
  // meet een gebeurtenis; doet niets zonder toestemming
  window.jtsMeet = function (naam, data) { if (geladen && window.gtag) gtag('event', naam, data || {}); };

  function toonBalk() {
    if (document.getElementById('cookiebalk')) return;
    var balk = document.createElement('div');
    balk.id = 'cookiebalk'; balk.className = 'cookiebalk'; balk.setAttribute('role', 'dialog'); balk.setAttribute('aria-label', 'Cookies');
    balk.innerHTML = '<p>Wij gebruiken analytische cookies van Google om te zien hoe de site wordt gebruikt en hem te verbeteren. <a href="privacy.html">Meer weten</a></p>' +
      '<div class="cookieknoppen"><button type="button" class="knop knop--rand knop--klein" data-keuze="nee">Weigeren</button><button type="button" class="knop knop--klein" data-keuze="ja">Accepteren</button></div>';
    document.body.appendChild(balk);
    balk.addEventListener('click', function (e) {
      var w = e.target.getAttribute('data-keuze'); if (!w) return;
      bewaarKeuze(w); balk.remove();
      if (w === 'ja') laadAnalytics();
    });
  }
  if (GA_ID) {
    var k = keuze();
    if (k === 'ja') laadAnalytics(); else if (k !== 'nee') toonBalk();
    var inst = document.getElementById('cookie-instellingen');
    if (inst) { inst.hidden = false; inst.addEventListener('click', function () { try { localStorage.removeItem(COOKIE_SLEUTEL); } catch (e) {} toonBalk(); }); }
  }

  /* ---- kliks die tot contact leiden ---- */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]'); if (!a) return;
    var h = a.getAttribute('href');
    if (h.indexOf('tel:') === 0) window.jtsMeet('klik_bellen');
    else if (h.indexOf('wa.me') > -1) window.jtsMeet('klik_whatsapp');
    else if (h.indexOf('mailto:') === 0) window.jtsMeet('klik_mail');
    else if (h.indexOf('aanvragen.html') > -1) window.jtsMeet('start_aanvraag', { vanaf: location.pathname });
  });

  /* ---- jaartal ---- */
  var jaar = document.getElementById('jaar');
  if (jaar) jaar.textContent = new Date().getFullYear();
})();
