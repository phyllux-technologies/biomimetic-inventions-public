(function() {
  function attachLightbox(img) {
    if (img.hasAttribute('data-lightbox-attached')) return;
    if (img.getAttribute('data-reveal-fact')) return;
    if (img.src && img.src.indexOf('favicon') >= 0) return;
    if (img.closest('header') || img.closest('nav')) return;
    img.setAttribute('data-lightbox-attached', '1');
    img.style.cursor = 'pointer';
    img.setAttribute('title', 'Click to expand');
    img.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      var overlay = document.getElementById('image-lightbox-overlay');
      if (overlay) overlay.remove();
      overlay = document.createElement('div');
      overlay.id = 'image-lightbox-overlay';
      overlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.9);z-index:9998;display:flex;align-items:center;justify-content:center;padding:2rem;cursor:pointer;animation:imageLightboxFadeIn 0.2s ease;';
      var big = document.createElement('img');
      big.src = this.currentSrc || this.src;
      big.alt = this.alt || '';
      big.style.cssText = 'max-width:95vw;max-height:95vh;object-fit:contain;border-radius:8px;box-shadow:0 0 80px rgba(0,0,0,0.5);pointer-events:none;';
      overlay.appendChild(big);
      overlay.addEventListener('click', function() { overlay.remove(); document.body.style.overflow = ''; });
      document.body.style.overflow = 'hidden';
      document.body.appendChild(overlay);
      document.addEventListener('keydown', function esc(ev) {
        if (ev.key === 'Escape') { overlay.remove(); document.body.style.overflow = ''; document.removeEventListener('keydown', esc); }
      });
    });
  }
  function run() {
    document.querySelectorAll('img:not([data-reveal-fact])').forEach(attachLightbox);
  }
  function init() {
    run();
    var obs = new MutationObserver(function(mutations) {
      mutations.forEach(function(m) {
        [].slice.call(m.addedNodes).forEach(function(n) {
          if (n.nodeType === 1) {
            if (n.tagName === 'IMG') attachLightbox(n);
            if (n.querySelectorAll) n.querySelectorAll('img:not([data-reveal-fact])').forEach(attachLightbox);
          }
        });
      });
    });
    obs.observe(document.body, { childList: true, subtree: true });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
  var style = document.createElement('style');
  style.textContent = '@keyframes imageLightboxFadeIn{from{opacity:0}to{opacity:1}}';
  document.head.appendChild(style);
})();
