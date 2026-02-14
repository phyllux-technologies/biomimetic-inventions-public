(function() {
  document.addEventListener('DOMContentLoaded', function() {
    var btn = document.querySelector('.nav-dropdown-btn');
    var panel = document.querySelector('.nav-dropdown-panel');
    if (!btn || !panel) return;
    btn.addEventListener('click', function(e) {
      e.stopPropagation();
      panel.classList.toggle('open');
      btn.setAttribute('aria-expanded', panel.classList.contains('open'));
    });
    document.addEventListener('click', function() {
      panel.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    });
    panel.addEventListener('click', function(e) { e.stopPropagation(); });
  });
})();
