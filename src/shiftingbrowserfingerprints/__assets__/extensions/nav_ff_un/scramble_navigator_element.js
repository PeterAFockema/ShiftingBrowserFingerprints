// Fingerprint Defender - Content Script
// Injects protection into page context BEFORE any page scripts run
(function() {
    'use strict';
    // Default settings
    const defaultSettings = {
        enabled: true,
        navigator: true
    };
    // Generate session seed
    const sessionSeed = 'fp-' + Math.random()
        .toString(36)
        .substr(2, 9) + '-' + Date.now();
    // Inject immediately using inline script (synchronous, runs before page scripts)
    const injectProtection = (settings) => {
        const code = `
(function() {
  'use strict';
  const settings = ${JSON.stringify(settings)};
  const sessionSeed = "${sessionSeed}";
  if (settings.enabled === false) return;
  // Seeded random
  function seededRandom(seed) {
    let h = 0;
    for (let i = 0; i < seed.length; i++) {
      h = ((h << 5) - h) + seed.charCodeAt(i);
      h = h & h;
    }
    return function() { h = Math.sin(h) * 10000; return h - Math.floor(h); };
  }

  // settings.navigator obfuscation - Static spoofing DISABLED
  if (settings.navigator) {
    // Here we follow the method demonstrated and discussed by Fingerprint Defender,
    // where we disable the static spoofing as spoofing UA/ platform creates unique
    // fingerprints, instead of blending in- as navigator values are typically common.
    // By letting real navigator values through to match other users with the same browser
    // and we only the hide plugins list as a privacy measure we don't create a unique fingerprint.
    Object.defineProperty(navigator, 'plugins', {get:()=>[]});
  }

})();
    `;
        const script = document.createElement('script');
        script.textContent = code;
        // Must inject to documentElement to run before page scripts
        const parent = document.documentElement || document.head || document.body;
        parent.insertBefore(script, parent.firstChild);
        script.remove();
    };
    // Inject with default settings immediately (sync)
    injectProtection(defaultSettings);
    // Try to get settings from background (for future use)
    if (typeof browser !== 'undefined') {
        browser.runtime.sendMessage({
                type: 'getSettings'
            })
            .then(response => {
                // Settings loaded but already injected with defaults
                // User needs to refresh for new settings
            })
            .catch(() => {});
    }
})();