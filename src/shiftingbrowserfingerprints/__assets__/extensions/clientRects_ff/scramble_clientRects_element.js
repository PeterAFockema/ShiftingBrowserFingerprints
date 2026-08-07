(function() {
	'use strict';

	const settingsForPage = {
		enabled: true,
		clientRects: true
	};
	// Generate the session seed
	const sessionSeed = 'fp-' + Math.random()
		.toString(36)
		.substr(2, 9) + '-' + Date.now();
	// Inject randomness in as an inline script
	const injectRandomness = (settings) => {
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

  // settings.clientRects obfuscation
  if (settings.clientRects) {
    const origRect = Element.prototype.getBoundingClientRect;
    Element.prototype.getBoundingClientRect = function() {
      const r = origRect.call(this);
      const n = randFloat(-0.001, 0.001, 'rect');
      return new DOMRect(r.x + n, r.y + n, r.width + n, r.height + n);
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

	injectRandomness(settingsForPage);

	if (typeof browser !== 'undefined') {
		browser.runtime.sendMessage({
			type: 'getSettings'
		})
			.then(response => { 
				// A refresh would then be required
			})
			.catch(() => {});
	}
})();
