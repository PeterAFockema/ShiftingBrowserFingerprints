// Fingerprint Defender - Content Script
// Injects protection into page context BEFORE any page scripts run
(function() {
    'use strict';
    // Default settings
    const defaultSettings = {
        enabled: true,
        webgl: true
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
     
                return function() { h = Math.sin(h) * 10000; return h - Math.floor(h); };
              }
            
              // For WebGL obfuscation we want to add noise to the WebGL canvas rendering
              if (settings.webgl) {
                // WebGL fingerprint noise is added via canvas noise which affects WebGL too
                // No static spoofing is implemented and we instead will let the real GPU info 
                // through, as it otherwise makes the browser fingerprint more unique.
              }

            })();
                `;
        const script = document.createElement('script');
        script.textContent = code;
        const parent = document.documentElement || document.head || document.body; // We want to inject to documentElement and run this before the page scripts
        parent.insertBefore(script, parent.firstChild);
        script.remove();
    };
    injectProtection(defaultSettings); // Now inject with default settings immediately (sync)
    
    if (typeof browser !== 'undefined') {
        browser.runtime.sendMessage({
                type: 'getSettings' // Get settings from background
            })
            .then(response => {
                // The settings are loaded and already injected with defaults
                // For new setting s the user would need to refresh
            })
            .catch(() => {});
    }
})();