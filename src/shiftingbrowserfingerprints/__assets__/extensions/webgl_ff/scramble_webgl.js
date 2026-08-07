(function() {
	'use strict';

	const settingsForPage = {
		enabled: true,
		webgl: true
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

		return function() { h = Math.sin(h) * 10000; return h - Math.floor(h); };
	      }

	      // For WebGL obfuscation add noise to the WebGL canvas rendering
	      if (settings.webgl) {
		// WebGL fingerprint noise is added via canvas noise which affects WebGL too
		// No static spoofing is implemented and we instead will let the real GPU info 
		// through, as it otherwise makes the browser fingerprint more unique.
	      }

	    })();
		`;
		const script = document.createElement('script');
		script.textContent = code;
		const parent = document.documentElement || document.head || document.body; 
		parent.insertBefore(script, parent.firstChild);
		script.remove();
	};
	injectRandomness(settingsForPage);

	if (typeof browser !== 'undefined') {
		browser.runtime.sendMessage({
			type: 'getSettings' // Get settings from background
		})
			.then(response => {   
				// A refresh would then be required
			})
			.catch(() => {});
	}
})();
