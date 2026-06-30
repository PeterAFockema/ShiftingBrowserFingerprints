// Fingerprint Defender - Content Script
// Injects protection into page context BEFORE any page scripts run
(function() {
    'use strict';
    // Default settings
    const defaultSettings = {
        enabled: true,
        canvas: true
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
  function randInt(min, max, s) {
    const r = seededRandom(sessionSeed + s);
    return Math.floor(min + r() * (max - min + 1));
  }

  const map = new WeakMap();

const revertValue = canvas => {
  const { width, height } = canvas;
  const canvasContext = canvas.getContext('2d', { willReadFrequently: true });
  const matt = getImageData.apply(canvasContext, [0, 0, width, height]);
  matt.data.set(map.get(canvas));
  map.delete(canvas);

  canvasContext.putImageData(matt, 0, 0);
};

let gshift;

const getImageData = CanvasRenderingContext2D.prototype.getImageData;
const manipulateTheRGB = canvas => {
  port.dispatchEvent(new Event('manipulateTheRGB'));

  if (map.has(canvas)) {
      // If this has already manipulated
    return;
  }
  const { width, height } = canvas;
  const canvasContext = canvas.getContext('2d', { willReadFrequently: true });
  const matt = getImageData.apply(canvasContext, [0, 0, width, height]);
  map.set(canvas, matt.data);

  const shift = (port.dataset.mode === 'session' && gshift) ? gshift : {
    'r': port.dataset.mode === 'random' ? Math.floor(Math.random() * 10) - 5 : Number(port.dataset.red),
    'g': port.dataset.mode === 'random' ? Math.floor(Math.random() * 10) - 5 : Number(port.dataset.green),
    'b': port.dataset.mode === 'random' ? Math.floor(Math.random() * 10) - 5 : Number(port.dataset.blue)
  };
  gshift = gshift || shift;

  for (let i = 0; i < height; i += Math.max(1, parseInt(height / 10))) {
    for (let j = 0; j < width; j += Math.max(1, parseInt(width / 10))) {
      const n = ((i * (width * 4)) + (j * 4));
      matt.data[n + 0] = matt.data[n + 0] + shift.r;
      matt.data[n + 1] = matt.data[n + 1] + shift.g;
      matt.data[n + 2] = matt.data[n + 2] + shift.b;
    }
  }
  canvasContext.putImageData(matt, 0, 0);

  setTimeout(revertValue, 0, canvas);
};

  // canvas toBlob obfuscation
  if (settings.canvas) {
    const origGetImageData = HTMLCanvasElement.prototype.toBlob;
    HTMLCanvasElement.prototype.toBlob = function(...a) {
    const img = origGetImageData.apply(this, a);
    for (let i = 0; i < img.data.length; i += 4) {
        img.data[i] = Math.max(0, Math.min(255, img.data[i] + randInt(-3, 3, 'g' + i)));
      }
      return img;
    };
   
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