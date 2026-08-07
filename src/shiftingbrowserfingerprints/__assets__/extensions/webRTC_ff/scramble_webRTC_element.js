(function() {
	'use strict';

	const settingsForPage = {
		enabled: true,
		webrtc: true
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
