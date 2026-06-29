const DEFAULT_SETTINGS = {
    enabled: true,
    audio: true,
};
// Generate a session-based random seed (changes each browser session)
const SESSION_SEED = Math.random().toString(36).substring(2) + Date.now().toString(36);
    
// Initialise settings on install
browser.runtime.onInstalled.addListener(async (details) => {
    if (details.reason === 'install') {
        await browser.storage.local.set({
            settings: DEFAULT_SETTINGS,
            sessionSeed: SESSION_SEED
        });
    }
});
// Ensure settings exist and refresh seed on startup (Clear session storage, verify local config)
browser.runtime.onStartup.addListener(async () => {
    const data = await browser.storage.local.get(['settings', 'sessionSeed']);
    if (!data.settings) {
        await browser.storage.local.set({
            settings: DEFAULT_SETTINGS
        });
    }
    // Set a new unique seed for this browser session
    await browser.storage.local.set({
        sessionSeed: SESSION_SEED
    });
});

// Handle messages from content scripts or popup (Handles service worker wake-ups dynamically)
browser.runtime.onMessage.addListener((message, _sender, sendResponse) => {
    if (message.type === 'getSettings') {
        browser.storage.local.get(['settings', 'sessionSeed'])
            .then((data) => {
                sendResponse({
                    settings: data.settings || DEFAULT_SETTINGS,
                    sessionSeed: data.sessionSeed || SESSION_SEED
                });
            });
        return true; // Keep channel open for async response
    }
    if (message.type === 'updateSettings') {
        browser.storage.local.set({
                settings: message.settings
            })
            .then(() => {
                // Notify all tabs about settings change
                browser.tabs.query({})
                    .then((tabs) => {
                        tabs.forEach((tab) => {
                            browser.tabs.sendMessage(tab.id, {
                                    type: 'settingsUpdated',
                                    settings: message.settings
                                })
                                .catch(() => {
                                    /* Ignore inactive tabs which may not have a content script*/
                                });
                        });
                    });
                sendResponse({
                    success: true
                });
            });
        return true;
    }
    if (message.type === 'resetSettings') {
        browser.storage.local.set({
                settings: DEFAULT_SETTINGS
            })
            .then(() => {
                sendResponse({
                    success: true,
                    settings: DEFAULT_SETTINGS
                });
            });
        return true;
    }
});

// Initialise on first load
(async () => {
    const data = await browser.storage.local.get(['settings', 'sessionSeed']);
    if (!data.settings) {
        await browser.storage.local.set({
            settings: DEFAULT_SETTINGS
        });
    }
    if (!data.sessionSeed) {
        await browser.storage.local.set({
            sessionSeed: SESSION_SEED
        });
    }
})();