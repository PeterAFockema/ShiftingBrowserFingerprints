(function() {
	'use strict';

	const settingsForPage = {
		enabled: true,
		navigator: true
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

  // settings.navigator obfuscation - Static spoofing DISABLED
  if (settings.navigator) {
    // Here we follow the method demonstrated and discussed by Fingerprint Defender,
    // where we disable the static spoofing as spoofing UA/ platform creates unique
    // fingerprints, instead of blending in- as navigator values are typically common.
    // By letting real navigator values through to match other users with the same browser
    // and we only the hide plugins list as a privacy measure we don't create a unique fingerprint.
    Object.defineProperty(navigator, 'plugins', {get:()=>[]});
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
