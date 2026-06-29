// Fingerprint Defender - Content Script
// Injects protection into page context BEFORE any page scripts run
(function() {
    'use strict';
    // Default settings
    const defaultSettings = {
        enabled: true,
        webgl: true
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
              
                return function() { h = Math.sin(h) * 10000; return h - Math.floor(h); };
              }
            

              function(target) {
                    let proto = target.prototype ? target.prototype : target.__proto__;
                    proto.getParameter = new Proxy(proto.getParameter, {
                        apply(target, self, args) {
=                            if (args[0] === 3415) return 0;
                            else if (args[0] === 3414) return 24;
                            else if (args[0] === 36348) return 30;
                            else if (args[0] === 7936) return "WebKit";
                            else if (args[0] === 37445) return "Google Inc.";
                            else if (args[0] === 7937) return "WebKit WebGL";
                            else if (args[0] === 3379) return config.random.number([14, 15]);
                            else if (args[0] === 36347) return config.random.number([12, 13]);
                            else if (args[0] === 34076) return config.random.number([14, 15]);
                            else if (args[0] === 34024) return config.random.number([14, 15]);
                            else if (args[0] === 3386) return config.random.int([13, 14, 15]);
                            else if (args[0] === 3413) return config.random.number([1, 2, 3, 4]);
                            else if (args[0] === 3412) return config.random.number([1, 2, 3, 4]);
                            else if (args[0] === 3411) return config.random.number([1, 2, 3, 4]);
                            else if (args[0] === 3410) return config.random.number([1, 2, 3, 4]);
                            else if (args[0] === 34047) return config.random.number([1, 2, 3, 4]);
                            else if (args[0] === 34930) return config.random.number([1, 2, 3, 4]);
                            else if (args[0] === 34921) return config.random.number([1, 2, 3, 4]);
                            else if (args[0] === 35660) return config.random.number([1, 2, 3, 4]);
                            else if (args[0] === 35661) return config.random.number([4, 5, 6, 7, 8]);
                            else if (args[0] === 36349) return config.random.number([10, 11, 12, 13]);
                            else if (args[0] === 33902) return config.random.float([0, 10, 11, 12, 13]);
                            else if (args[0] === 33901) return config.random.float([0, 10, 11, 12, 13]);
                            else if (args[0] === 37446) return config.random.item(["Graphics", "HD Graphics", "Intel(R) HD Graphics"]);
                            else if (args[0] === 7938) return config.random.item(["WebGL 1.0", "WebGL 1.0 (OpenGL)", "WebGL 1.0 (OpenGL Chromium)"]);
                            else if (args[0] === 35724) return config.random.item(["WebGL", "WebGL GLSL", "WebGL GLSL ES", "WebGL GLSL ES (OpenGL Chromium"]);
                            return Reflect.apply(target, self, args);
                        }
                    });
                }

              // For WebGL obfuscation we want to add noise to the WebGL canvas rendering
              if (settings.webgl) {
                // WebGL fingerprint noise is added via canvas noise which affects WebGL too
                // No static spoofing is implemented and we instead will let the real GPU info 
                // through, as it otherwise makes the browser fingerprint more unique.



                
              }

            })();
                `;
        const script = document.createElement('script');
        script.textContent = code;
        const parent = document.documentElement || document.head || document.body; // We want to inject to documentElement and run this before the page scripts
        parent.insertBefore(script, parent.firstChild);
        script.remove();
    };
    injectProtection(defaultSettings); // Now inject with default settings immediately (sync)
    
    if (typeof browser !== 'undefined') {
        browser.runtime.sendMessage({
                type: 'getSettings' // Get settings from background
            })
            .then(response => {
                // The settings are loaded and already injected with defaults
                // For new setting s the user would need to refresh
            })
            .catch(() => {});
    }
})();