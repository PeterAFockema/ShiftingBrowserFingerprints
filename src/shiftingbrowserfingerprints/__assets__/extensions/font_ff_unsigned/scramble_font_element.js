// Fingerprint Defender - Content Script
// Injects protection into page context BEFORE any page scripts run
(function() {
    'use strict';
    // Default settings
    const defaultSettings = {
        enabled: true,
        fonts: true
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

  function randFloat(min, max, s) {
    const r = seededRandom(sessionSeed + s);
    return min + r() * (max - min);
  }

  // fonts obfuscation
  if (settings.fonts) {
    // These are the common fonts we'll pretend ARE installed in order to blend in
    const commonFonts = [
      'Arial', 'Arial Black', 'Courier', 'Courier New', 'Georgia',
      'Helvetica', 'Times', 'Times New Roman', 'Verdana', 'Tahoma'
    ];
    // Common fonts that we'll pretend are not installed so as to reduce or change the fingerprint
    const hiddenFonts = [
      'Segoe UI', 'Segoe Print', 'Segoe Script', 'Segoe UI Light', 'Segoe UI Semibold', 'Segoe UI Symbol',
      'Calibri', 'Cambria', 'Cambria Math', 'Consolas',
      'Lucida Console', 'Lucida Sans Unicode',
      'Palatino Linotype', 'MS Gothic', 'MS PGothic', 'MS Sans Serif', 'MS Serif',
      'Comic Sans MS', 'Impact', 'Trebuchet MS'
    ];
    // Check if font should be hidden
    function shouldHideFont(fontFamily) {
      const lower = fontFamily.toLowerCase();
      for (const f of hiddenFonts) {
        if (lower.includes(f.toLowerCase())) return true;
      }
      return false;
    }
    // Add noise to offsetWidth
    const origW = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetWidth');
    if (origW) {
      Object.defineProperty(HTMLElement.prototype, 'offsetWidth', {
        get: function() {
          const w = origW.get.call(this);
          // Add noise for elements with font-family set (font detection)
          if (this.style.fontFamily) {
            // If testing a hidden font, return baseline width (as if font not installed)
            if (shouldHideFont(this.style.fontFamily)) {
              return w + randFloat(-1, 1, 'fwh');
            }
            return w + randFloat(-3, 3, 'fw' + w);
          }
          if (this.tagName === 'SPAN' && w < 500) {
            return w + randFloat(-2, 2, 'fws' + w);
          }
          return w;
        }
      });
    }
    // Add noise to offsetHeight
    const origH = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetHeight');
    if (origH) {
      Object.defineProperty(HTMLElement.prototype, 'offsetHeight', {
        get: function() {
          const h = origH.get.call(this);
          if (this.style.fontFamily) {
            if (shouldHideFont(this.style.fontFamily)) {
              return h + randFloat(-1, 1, 'fhh');
            }
            return h + randFloat(-3, 3, 'fh' + h);
          }
          if (this.tagName === 'SPAN' && h < 100) {
            return h + randFloat(-2, 2, 'fhs' + h);
          }
          return h;
        }
      });
    }
    // Spoof document.fonts API
    if ('fonts' in document) {
      const origCheck = document.fonts.check.bind(document.fonts);
      document.fonts.check = function(font, text) {
        // Here we parse font family from the font string
        const match = font.match(/[\\d.]+(?:px|pt|em|rem)?\\s+(.+)/i);
        const fontFamily = match ? match[1] : font;
        // Now return false for hidden fonts
        if (shouldHideFont(fontFamily)) {
          return false;
        }
        // Return true for common fonts (even if not installed)
        for (const f of commonFonts) {
          if (fontFamily.toLowerCase().includes(f.toLowerCase())) {
            return true;
          }
        }
        // For the other fonts we will use seeded random so as to be consistent but varied
        const r = seededRandom(sessionSeed + 'fc' + fontFamily);
        if (r() > 0.6) return false;
        return origCheck(font, text);
      };
      // Spoof fonts.forEach / fonts iteration
      const origForEach = document.fonts.forEach.bind(document.fonts);
      document.fonts.forEach = function(callback, thisArg) {
        origForEach(function(font, idx, set) {
          // Filter out hidden fonts from enumeration
          if (!shouldHideFont(font.family)) {
            callback.call(thisArg, font, idx, set);
          }
        }, thisArg);
      };
    }
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