# ShiftingBrowserFingerprints

<p align="center">
  <img src="./docs/images/fingerprint_logo.png" alt="alt text">
</p>

## About
A package for web scraper code to utilise fingerprint obfuscation techniques against browser fingerprinting software in Firefox when web scraping from a pre-defined page.
Various browser fingerprinting obfuscation techniques that can be called, with any combination, include:
* Audio
* Battery
* Canvas
* ClientRects
* Font
* Screen
* Navigator
* WebGL
* WebRTC

By following this method of stacking techniques, we can increase our coverage against browser 
fingerprinting techniques.

![alt text](./docs/images/fingerprint_obfuscation_concept_explanation.png)

## Example Usage
First install the package:
```
pip install -v git+https://github.com/PeterAFockema/ShiftingBrowserFingerprints
```

We run the following code in Python 3.
Locally generate the API extensions/ Addons that will be utilised for fingerprint obfuscation.
```
from shiftingbrowserfingerprints.generate_xpis import build_all_unsigned_xpi_extensions

build_all_unsigned_xpi_extensions()
```

To scrape from the desired web page, run the following as a Python script:

```
from shiftingbrowserfingerprints.firefox_scrapers import FirefoxScrapers as Scrapers

scrapers = Scrapers()
driver = scrapers.firefox_driver_extension_list_implementation(passed_value)

# Navigate to the user-defined page
url = "<INSERT URL ADDRESS HERE>"

driver.get(url)
```

## Demonstration of Usage
A demonstration of this repository's usage can be observed at:
```
https://github.com/PeterAFockema/BrowserFingerprintUtilisation
```
At BrowserFingerprintUtilisation the method of testing is using the BDD framework, behave [^1],
to test combinations of the browser fingerprinting obfuscation techniques against a test website
that has been developed, and is run locally, that calculates the browser fingerprints of the
visiting user using the open-source version of FingerprintJS [^2][^3].

## References
[^1]: Behave. (2026). *behave 1.4.0.dev0 documentation*, [Source Link](https://behave.readthedocs.io/en/latest/)   
[^2]: Fingerprint. (2026). *Identify Every Visitor*, [Source Link](https://fingerprint.com/try/identify-now)   
[^3]: FingerprintJS. (2026). *fingerprintjs*, [Source Link](https://github.com/fingerprintjs/fingerprintjs)   