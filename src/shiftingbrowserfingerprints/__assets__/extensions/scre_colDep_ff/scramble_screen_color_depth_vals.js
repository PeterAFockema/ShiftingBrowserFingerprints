(function() {
	'use strict';

	const settingsForPage = {
		enabled: true,
		screen: true
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

  // screen obfuscation/ spoofing- to common resolution (1920x1080 is most common)
  // This is re-enabled because unusual resolutions like 2867x1200 contribute to a more unique fingerprint
  if (settings.screen) {
    const spoofedScreen = { width: 1920, height: 1080, availWidth: 1920, availHeight: 1040, colorDepth: 24, pixelDepth: 24 };
    Object.defineProperty(window, 'screen', {
      get: () => ({
	colorDepth: spoofedScreen.colorDepth,
	pixelDepth: spoofedScreen.pixelDepth,
	orientation: { type: 'landscape-primary', angle: 0 }
      })
    });
    Object.defineProperty(window, 'colorDepth', { get: () => spoofedScreen.colorDepth });
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
