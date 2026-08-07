(function() {
	'use strict';

	const settingsForPage = {
		enabled: true,
		audio: true,
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
  function randFloat(min, max, s) {
    const r = seededRandom(sessionSeed + s);
    return min + r() * (max - min);
  }

  // audio obfuscation
  if (settings.audio && typeof AudioContext !== 'undefined') {
    const OrigAudio = AudioContext;
    const OrigOfflineAudio = typeof OfflineAudioContext !== 'undefined' ? OfflineAudioContext : null;
    const audioNoise = randFloat(-0.0001, 0.0001, 'audioNoise');

    function patchAudioContext(ctx) {
      const origAnalyser = ctx.createAnalyser.bind(ctx); // Here we patch createAnalyser
      ctx.createAnalyser = function() {
	const an = origAnalyser();
	const origFloat = an.getFloatFrequencyData.bind(an);
	const origByte = an.getByteFrequencyData.bind(an);
	const origFloatTime = an.getFloatTimeDomainData.bind(an);
	const origByteTime = an.getByteTimeDomainData.bind(an);
	an.getFloatFrequencyData = function(arr) {
	  origFloat(arr);
	  for (let i = 0; i < arr.length; i++) arr[i] += randFloat(-0.1, 0.1, 'af' + i);
	};
	an.getByteFrequencyData = function(arr) {
	  origByte(arr);
	  for (let i = 0; i < arr.length; i++) arr[i] = Math.max(0, Math.min(255, arr[i] + randInt(-1, 1, 'ab' + i)));
	};
	an.getFloatTimeDomainData = function(arr) {
	  origFloatTime(arr);
	  for (let i = 0; i < arr.length; i++) arr[i] += randFloat(-0.0001, 0.0001, 'aft' + i);
	};
	an.getByteTimeDomainData = function(arr) {
	  origByteTime(arr);
	  for (let i = 0; i < arr.length; i++) arr[i] = Math.max(0, Math.min(255, arr[i] + randInt(-1, 1, 'abt' + i)));
	};
	return an;
      };

      const origOscillator = ctx.createOscillator.bind(ctx); // Here we patch createOscillator
      ctx.createOscillator = function() {
	const osc = origOscillator();
	const origFreq = Object.getOwnPropertyDescriptor(osc.frequency, 'value');
	if (origFreq) {
	  Object.defineProperty(osc.frequency, 'value', {
	    get: origFreq.get,
	    set: function(v) { origFreq.set.call(this, v + audioNoise); }
	  });
	}
	return osc;
      };

      const origCompressor = ctx.createDynamicsCompressor.bind(ctx); // Here we patch createDynamicsCompressor
      ctx.createDynamicsCompressor = function() {
	const comp = origCompressor();

	const origReduction = Object.getOwnPropertyDescriptor(comp, 'reduction');
	if (origReduction && origReduction.get) {
	  Object.defineProperty(comp, 'reduction', {
	    // Add noise to the reduction value
	    get: function() { return origReduction.get.call(this) + audioNoise; }
	  });
	}
	return comp;
      };

      const origCreateBuffer = ctx.createBuffer.bind(ctx); // Here we patch getChannelData for rendered buffers
      ctx.createBuffer = function(...args) {
	const buffer = origCreateBuffer(...args);
	const origGetChannelData = buffer.getChannelData.bind(buffer);
	buffer.getChannelData = function(channel) {
	  const data = origGetChannelData(channel);
	  for (let i = 0; i < data.length; i += 100) {
	    data[i] += audioNoise;
	  }
	  return data;
	};
	return buffer;
      };
      return ctx;
    }
    window.AudioContext = function(...a) {
      return patchAudioContext(new OrigAudio(...a));
    };
    Object.setPrototypeOf(window.AudioContext, OrigAudio);
    window.AudioContext.prototype = OrigAudio.prototype;

    if (OrigOfflineAudio) {
    // We also want to patch OfflineAudioContext which is used for fingerprinting
      window.OfflineAudioContext = function(...a) {
	const ctx = new OrigOfflineAudio(...a);
	patchAudioContext(ctx);
	const origStartRendering = ctx.startRendering.bind(ctx); // patch renderedBuffer
	ctx.startRendering = function() {
	  return origStartRendering().then(function(buffer) {
	    const origGetChannelData = buffer.getChannelData.bind(buffer);
	    buffer.getChannelData = function(channel) {
	      const data = origGetChannelData(channel);
	      for (let i = 0; i < data.length; i += 100) {
		data[i] += audioNoise;
	      }
	      return data;
	    };
	    return buffer;
	  });
	};
	return ctx;
      };
      Object.setPrototypeOf(window.OfflineAudioContext, OrigOfflineAudio);
      window.OfflineAudioContext.prototype = OrigOfflineAudio.prototype;
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
