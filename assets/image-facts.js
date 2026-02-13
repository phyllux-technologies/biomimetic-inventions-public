(function() {
  var facts = {
    'david-desk-mastermind-hero': 'MASTERMIND was built with Cursor AI — coordination that improves all systems. One idea propagates to many improvements.',
    'david-phyllux-presenting': 'David presents Phyllux at workshops and to partners. 30-min onboarding. Evaluation → License → Prototype.',
    'david-coding-hands-on-keyboard': 'Systems thinker. Creator of MASTERMIND, this site, and the propagation engine. Documents are memory.',
    'david-explaining-whiteboard': 'Quality Hierarchy: Pirsig levels from inorganic → intellectual. One concept per module.',
    'david-nature-tech-outdoor': 'Nature-inspired innovation. Four billion years of R&D. One golden angle — 137.508°. Biomimetic systems.',
    'david-celebrating-success': 'ENGENICA: +157.7% performance. Meta-iterative polish. Entropy, symmetry, fractal convergence.',
    'david-about-page-headshot': 'David Edward Sproule. Edmonton, Alberta. Founder & Inventor. Mission: mutual flourishing for AI, human, nature, technology.',
    'phyllux-hero-banner': 'Phyllux: Wave, Mesh, Vault, Core. Golden-angle biomimetic tech across four domains.',
    'phyllux-embellishment': 'The golden angle appears in sunflowers, pinecones, and Phyllux. Nature\'s optimal packing.',
    'index-hub-card': 'One hub. Products. Vision. Path. Proof. Partners. All voluntary, transparent, free to leave.',
    'phyllux-footer-divider': 'Phyllux Technologies · Mutual flourishing · phyllux.io'
  };
  function getFact(src) {
    var m = src.match(/([^/\\]+)(?:\.[^.]+)?$/);
    var key = m ? m[1].replace(/\.[^.]+$/, '') : '';
    return facts[key] || facts[Object.keys(facts).find(function(k) { return src.indexOf(k) >= 0; })] || 'Phyllux Technologies — Golden-angle biomimetic systems. Mutual flourishing.';
  }
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('img[data-reveal-fact]').forEach(function(img) {
      img.style.cursor = 'pointer';
      img.title = 'Click to reveal';
      img.addEventListener('click', function() {
        var fact = this.getAttribute('data-fact') || getFact(this.src);
        var el = document.getElementById('image-fact-overlay');
        if (el) el.remove();
        el = document.createElement('div');
        el.id = 'image-fact-overlay';
        el.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.7);z-index:9999;display:flex;align-items:center;justify-content:center;padding:2rem;animation:fadeIn 0.2s ease;';
        el.innerHTML = '<div style="max-width:420px;background:#0c0f14;border:1px solid rgba(94,234,212,0.3);border-radius:12px;padding:1.5rem;color:#f0f4f8;font-size:0.95rem;line-height:1.6;position:relative;">' +
          '<button onclick="this.closest(\'#image-fact-overlay\').remove()" style="position:absolute;top:8px;right:8px;background:none;border:none;color:#94a3b8;cursor:pointer;font-size:1.2rem;">×</button>' +
          '<p style="margin:0;color:#5eead4;font-weight:600;margin-bottom:0.5rem;">✨</p><p style="margin:0;">' + fact.replace(/</g,'&lt;').replace(/>/g,'&gt;') + '</p></div>';
        el.addEventListener('click', function(ev) { if (ev.target === el) el.remove(); });
        document.body.appendChild(el);
      });
    });
  });
})();
