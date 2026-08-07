(function() {
	'use strict';

	const settingsForPage = {
		enabled: true,
		canvas: true
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
  function randInt(min, max, s) {
    const r = seededRandom(sessionSeed + s);
    return Math.floor(min + r() * (max - min + 1));
  }

  // canvas obfuscation
  if (settings.canvas) {
    const origToDataURL = HTMLCanvasElement.prototype.toDataURL;
    HTMLCanvasElement.prototype.toDataURL = function(...a) {
      try {
	const ctx = this.getContext('2d');
	if (ctx && this.width && this.height) {
	  const img = ctx.getImageData(0, 0, this.width, this.height);
	  for (let i = 0; i < img.data.length; i += 4) {
	    img.data[i] = Math.max(0, Math.min(255, img.data[i] + randInt(-3, 3, 'c' + i)));
	  }
	  ctx.putImageData(img, 0, 0);
	}
      } catch(e) {}
      return origToDataURL.apply(this, a);
    };

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
