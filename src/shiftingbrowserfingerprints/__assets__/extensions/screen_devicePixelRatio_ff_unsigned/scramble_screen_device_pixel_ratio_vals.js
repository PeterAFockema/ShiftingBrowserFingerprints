// Fingerprint Defender - Content Script
// Injects protection into page context BEFORE any page scripts run
(function() {
    'use strict';
    // Default settings
    const defaultSettings = {
        enabled: true,
        screen: true
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

  // screen obfuscation/ spoofing- to common resolution (1920x1080 is most common)
  // This is re-enabled because unusual resolutions like 2867x1200 contribute to a more unique fingerprint
  if (settings.screen) {
    const spoofedScreen = { width: 1920, height: 1080, availWidth: 1920, availHeight: 1040, colorDepth: 24, pixelDepth: 24 };
    Object.defineProperty(window, 'screen', {
      get: () => ({
        pixelDepth: spoofedScreen.pixelDepth,
        orientation: { type: 'landscape-primary', angle: 0 }
      })
    });
    Object.defineProperty(window, 'pixelDepth', { get: () => spoofedScreen.pixelDepth });
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