/* Projectengalerij: filteren op soort en foto's vergroten (pijltjestoetsen werken ook). */
(function () {
  var knoppen = document.querySelectorAll('.filter');
  var fotos = Array.prototype.slice.call(document.querySelectorAll('#galerij button'));
  var lb = document.getElementById('lightbox');
  var lbImg = lb.querySelector('img');
  var huidig = 0;

  knoppen.forEach(function (k) {
    k.addEventListener('click', function () {
      var f = k.getAttribute('data-filter');
      knoppen.forEach(function (x) { x.setAttribute('aria-pressed', x === k ? 'true' : 'false'); });
      fotos.forEach(function (b) { b.hidden = f !== 'alle' && b.getAttribute('data-soort') !== f; });
    });
  });

  function zichtbaar() { return fotos.filter(function (b) { return !b.hidden; }); }
  function toon(b) {
    var img = b.querySelector('img');
    lbImg.src = b.getAttribute('data-groot'); lbImg.alt = img.alt;
    document.getElementById('lb-tekst').textContent = img.alt;
    huidig = zichtbaar().indexOf(b);
  }
  function stap(n) { var z = zichtbaar(); toon(z[(huidig + n + z.length) % z.length]); }

  fotos.forEach(function (b) {
    b.addEventListener('click', function () { toon(b); if (lb.showModal) lb.showModal(); else lb.setAttribute('open', ''); });
  });
  document.getElementById('lb-vorige').addEventListener('click', function () { stap(-1); });
  document.getElementById('lb-volgende').addEventListener('click', function () { stap(1); });
  document.getElementById('lb-sluit').addEventListener('click', function () { lb.close(); });
  lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
  lb.addEventListener('keydown', function (e) { if (e.key === 'ArrowLeft') stap(-1); if (e.key === 'ArrowRight') stap(1); });
})();
