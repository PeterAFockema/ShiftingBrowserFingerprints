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

	    // WebGL spoofing- this version has been updated so that 
	    we no add noise to WebGL canvas rendering and don't spoof vendor/renderer
	    // Static vendor/renderer spoofing disabled - it makes fingerprint MORE unique
	    if (settings.webgl) {
	      // WebGL fingerprint noise is added via canvas noise which affects WebGL too
	      // No static spoofing here - let real GPU info through to blend in
	    }

	    if (settings.canvas) {
	      const bufferData = proto.bufferData;
	      proto.bufferData = function(...a) {
	      const target = bufferData.apply(this, a);
	      let index = Math.floor(config.random.value() * args[1].length);
				      let noise = args[1][index] !== undefined ? 0.1 * config.random.value() * args[1][index] : 0;
				      args[1][index] = args[1][index] + noise;
		return target;
	      };

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
