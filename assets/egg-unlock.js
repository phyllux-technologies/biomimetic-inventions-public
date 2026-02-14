/**
 * Phyllux Vault — Easter egg unlock mechanism
 * Find and click all 5 key fragments across the site to unlock the vault.
 */
(function() {
  const STORAGE_KEY = 'phyllux_vault_keys';
  const VAULT_URL = 'vault.html';
  const REQUIRED_KEYS = 5;

  function getKeys() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) { return {}; }
  }

  function setKey(id) {
    const keys = getKeys();
    keys['k' + id] = true;
    localStorage.setItem(STORAGE_KEY, JSON.stringify(keys));
    return Object.keys(keys).length;
  }

  function isUnlocked() {
    return Object.keys(getKeys()).length >= REQUIRED_KEYS;
  }

  function checkUnlock() {
    if (isUnlocked()) {
      window.location.href = VAULT_URL;
    }
  }

  window.PhylluxEgg = {
    click: function(keyId) {
      const count = setKey(keyId);
      if (count >= REQUIRED_KEYS) {
        checkUnlock();
      }
    },
    isUnlocked: isUnlocked,
    getCount: function() { return Object.keys(getKeys()).length; }
  };

  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('[data-egg-key]').forEach(function(el) {
      el.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        const id = this.getAttribute('data-egg-key');
        if (id) PhylluxEgg.click(id);
      });
      el.style.cursor = 'pointer';
    });
  });
})();
