// Fingerprint Defender - Content Script
// Injects protection into page context BEFORE any page scripts run
(function() {
    'use strict';
    // Default settings
    const defaultSettings = {
        enabled: true,
        webrtc: true
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

  // settings.webrtc obfuscation
  if (settings.webrtc && typeof RTCPeerConnection !== 'undefined') {
    const OrigRTC = RTCPeerConnection;
    window.RTCPeerConnection = function(cfg = {}) {
      cfg.iceServers = [];
      cfg.iceTransportPolicy = 'relay';
      return new OrigRTC(cfg);
    };
    Object.setPrototypeOf(window.RTCPeerConnection, OrigRTC);
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