#scrapers_objects.py

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from bs4 import BeautifulSoup as soup
import os

class Scrapers(object):
    '''
    A class for web scrapers.
    '''

    def __init__(self):
        print("The Scrapers class initialised...")

    def chrome_driver_implementation(self):
        # Initialise the Chrome driver
        driver = webdriver.Chrome()
        # Navigate to the URL
        driver.get('https://google.com')
        # Print the title page
        print(driver.title)
        # Here we close the browser when done
        driver.quit()
    
    def chrome_driver_extension_implementation(self):
        # cwd = os.getcwd()
        # print("cwd: ", cwd)
        file_being_run = os.path.dirname(os.path.abspath(__file__))
        # print("file being run: ", file_being_run)
        extension_location = str(file_being_run) + "/__assets__/extensions/hello_world.crx"
        # print("extension location: ", extension_location)
        chrome_options = OptionsChrome()
        chrome_options.add_extension(extension_location)

        # Initialise the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def chrome_driver_canvas_extension_implementation(self):
        file_being_run = os.path.dirname(os.path.abspath(__file__))
        extension_location = str(file_being_run) + "/__assets__/extensions/canvas.crx"
        chrome_options = OptionsChrome()
        chrome_options.add_extension(extension_location)

        # Initialise the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def firefox_driver_implementation(self):
        #Initialise the Firefox driver
        driver = webdriver.Firefox()
        return driver

    def firefox_driver_canvas_extension_implementation(self):
        #Initialise the Firefox driver
        options = OptionsFirefox()
        driver = webdriver.Firefox(options=options)
    
        file_being_run = os.path.dirname(os.path.abspath(__file__))
        extension_location = str(file_being_run) + "/__assets__/extensions/canvas_ff/web-ext-artifacts/canvas_scrambler_ff-2.0.xpi"

        driver.install_addon(extension_location)

        return driver
    
    def firefox_driver_font_extension_implementation(self):
        #Initialise the Firefox driver
        options = OptionsFirefox()
        driver = webdriver.Firefox(options=options)
    
        file_being_run = os.path.dirname(os.path.abspath(__file__))
        extension_location = str(file_being_run) + "/__assets__/extensions/firefox_font.xpi"

        driver.install_addon(extension_location)
        return driver
        
    def firefox_driver_extension_string_implementation(self, extension_choice: str):
        # Initialise Firefox Options
        options = OptionsFirefox()

        # Set the specific preference
        # Setting this to True disables the "Manage Exceptions" button in the Privacy & Security menu
        options.set_preference("pref.privacy.disable_button.tracking_protection_exceptions", True)

        # NOTE: An Optional-> Disable the actual tracking protection feature as well
        # (Can be paired with the above to ensure a locked-down, consistent state)
        options.set_preference("privacy.trackingprotection.enabled", False)

        # Disable 'Known Fingerprinters' protection
        options.set_preference("privacy.trackingprotection.fingerprinting.enabled", False)

        # For Private Browsing mode specifically (if applicable)
        options.set_preference("privacy.trackingprotection.pbmode.enabled", False)

        # Disable 'Suspected Fingerprinters' protection (General)
        options.set_preference("privacy.fingerprintingProtection", False)

        # Ensure the global Enhanced Tracking Protection (ETP) isn't overriding this
        # ETP 'Strict' mode often enables suspected fingerprinters by default
        options.set_preference("privacy.trackingprotection.enabled", False)

        # Disable 'Cryptominers' protection
        options.set_preference("privacy.trackingprotection.cryptomining.enabled", False)

        # Disable all cookies
        options.set_preference("network.cookie.cookieBehavior", 2)

        # NOTE: An Optional-> Ensure they are also disabled in Private Browsing mode
        # options.set_preference("network.cookie.cookieBehavior.pbmode", 2)
        
        # Launch the Firefox driver
        # driver = webdriver.Firefox() # NOTE: Vanilla driver-> intend to split this out as a separate option at a later date
        driver = webdriver.Firefox(options=options)
        
        # # Check which extensions to install on the driver
        # extensions_to_check = ["font", "canvas", "webgl", "screen",
        #                        "audio", "battery", "clientRects", "navigator",
        # "font.offsetHeight", "prototype.offsetHeight", "offsetHeight",
        # "font.offsetWidth", "prototype.offsetWidth", "offsetWidth",
        # "webgl.parameter", "prototype.parameter", "parameter",
        # "webgl.buffer", "prototype.buffer", "buffer",
        # "canvas.getImageData", "prototype.getImageData", "getImageData",
        # "canvas.toBlob", "prototype.toBlob", "toBlob",
        # "canvas.toDataURL", "prototype.toDataURL", "toDataURL",
        # "screen.availHeight", "prototype.availHeight", "availHeight",
        # "screen.availWidth", "prototype.availWidth", "availWidth",
        # "screen.colorDepth", "prototype.colorDepth", "colorDepth",
        # "screen.height", "height", "screen.width", "width",
        # "screen.devicePixelRatio", "prototype.devicePixelRatio", "devicePixelRatio",
        # "timezone"]

        # Check which extensions to install on the driver
        extensions_to_check = ["audio", "battery", "font", "canvas", "clientRects", "navigator", "screen", "webgl",
                                "webGL", "webrtc", "webRTC", "timezone",
        "font.offsetHeight", "prototype.offsetHeight", "offsetHeight",
        "font.offsetWidth", "prototype.offsetWidth", "offsetWidth",
        "webgl.parameter", "prototype.parameter", "parameter",
        "webgl.buffer", "prototype.buffer", "buffer",
        "canvas.toBlob", "prototype.toBlob", "toBlob",
        "canvas.toDataURL", "prototype.toDataURL", "toDataURL",
        "screen.availHeight", "prototype.availHeight", "availHeight",
        "screen.availWidth", "prototype.availWidth", "availWidth",
        "screen.colorDepth", "prototype.colorDepth", "colorDepth",
        "screen.devicePixelRatio", "prototype.devicePixelRatio", "devicePixelRatio"]

        extension_location = str(os.path.dirname(os.path.abspath(__file__)))
        if any(ext == extension_choice for ext in extensions_to_check):
            # Combos within an Add On
            if extension_choice == "audio":
                extension_location+= "/__assets__/extensions/audio_ff/web-ext-artifacts/audio_scrambler_ff-1.0.xpi"
                driver.install_addon(extension_location)
            if extension_choice == "battery":
                extension_location+= "/__assets__/extensions/battery_ff/web-ext-artifacts/battery_scrambler_ff-1.0.xpi"
                driver.install_addon(extension_location)
            if extension_choice == "clientRects":
                extension_location+= "/__assets__/extensions/clientRects_ff/web-ext-artifacts/clientRects_scrambler_ff-2.0.xpi"
                driver.install_addon(extension_location)
            if extension_choice == "font":
                extension_location+= "/__assets__/extensions/font_ff/web-ext-artifacts/font_scrambler_ff-3.0.xpi"
                driver.install_addon(extension_location)
            if extension_choice == "canvas":
                extension_location+= "/__assets__/extensions/canvas_ff/web-ext-artifacts/canvas_scrambler_ff-3.0.xpi"
                driver.install_addon(extension_location)
            if extension_choice == "webgl":
                extension_location+= "/__assets__/extensions/webgl_ff/web-ext-artifacts/webgl_scrambler_ff-4.0.xpi"
                driver.install_addon(extension_location)
            if extension_choice.lower() == "webrtc":
                extension_location+= "/__assets__/extensions/webRTC_ff/web-ext-artifacts/webrtc_scrambler_ff-2.0.xpi"
                driver.install_addon(extension_location)
            if extension_choice == "screen":
                extension_location+= "/__assets__/extensions/screen_ff/web-ext-artifacts/screen_scrambler_ff-3.0.xpi"
                driver.install_addon(extension_location)
            if extension_choice == "navigator":
                extension_location+= "/__assets__/extensions/navigator_ff/web-ext-artifacts/navigator_scrambler_ff-1.0.xpi"
                driver.install_addon(extension_location)
            # Single calls within an Add On
            # The following are for HTMLElement.prototype.'__' HTML elements
            if (extension_choice == "font.offsetHeight") or (extension_choice == "prototype.offsetHeight") or (extension_choice == "offsetHeight"):
                extension_location+= "/__assets__/extensions/font_offsetHeight_ff/web-ext-artifacts/font_offsetheight_scrambler_ff-1.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "font.offsetWidth") or (extension_choice == "prototype.offsetWidth") or (extension_choice == "offsetWidth"):
                extension_location+= "/__assets__/extensions/font_offsetWidth_ff/web-ext-artifacts/font_offsetwidth_scrambler_ff-2.0.xpi"
                driver.install_addon(extension_location)
            # The following are for WebGL2RenderingContext.prototype.'__' elements
            if (extension_choice == "webgl.parameter") or (extension_choice == "prototype.parameter") or (extension_choice == "parameter"):
                extension_location+= "/__assets__/extensions/webgl_parameter_ff/web-ext-artifacts/webgl-parameter-ff-2.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "webgl.buffer") or (extension_choice == "prototype.buffer") or (extension_choice == "buffer"):
                extension_location+= "/__assets__/extensions/webgl_buffer_ff/web-ext-artifacts/webgl-buffer-ff-2.0.xpi"
                driver.install_addon(extension_location)
            # The following are for CanvasRenderingContext2D.prototype.'__' elements
            if (extension_choice == "canvas.getImageData") or (extension_choice == "prototype.getImageData") or (extension_choice == "getImageData"):
                extension_location+= "/__assets__/extensions/canvas_getImageData_ff/web-ext-artifacts/getImageData_scrambler_ff-2.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "canvas.toBlob") or (extension_choice == "prototype.toBlob") or (extension_choice == "toBlob"):
                extension_location+= "/__assets__/extensions/canvas_toBlob_ff/web-ext-artifacts/toBlob_scrambler_ff-3.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "canvas.toDataURL") or (extension_choice == "prototype.toDataURL") or (extension_choice == "toDataURL"):
                extension_location+= "/__assets__/extensions/canvas_toDataURL_ff/web-ext-artifacts/canvas_toDataURL_ff-1.0.xpi"
                driver.install_addon(extension_location)
            # The following are for Screen.prototype.'__' elements
            if (extension_choice == "screen.availHeight") or (extension_choice == "prototype.availHeight") or (extension_choice == "availHeight"):
                extension_location+= "/__assets__/extensions/screen_availHeight_ff/web-ext-artifacts/screen_height_values_scrambler_ff-3.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "screen.availWidth") or (extension_choice == "prototype.availWidth") or (extension_choice == "availWidth"):
                extension_location+= "/__assets__/extensions/screen_availWidth_ff/web-ext-artifacts/screen_width_values_scrambler_ff-2.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "screen.colorDepth") or (extension_choice == "prototype.colorDepth") or (extension_choice == "colorDepth"):
                extension_location+= "/__assets__/extensions/screen_colorDepth_ff/web-ext-artifacts/colordepth_values_scramble_ff-3.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "screen.devicePixelRatio") or (extension_choice == "prototype.devicePixelRatio") or (extension_choice == "devicePixelRatio"):
                extension_location+= "/__assets__/extensions/screen_devicePixelRatio_ff/web-ext-artifacts/devicepixelratio_scrambler_ff-2.0.xpi"
            if (extension_choice == "screen.height") or (extension_choice == "height"):
                extension_location+= "/__assets__/extensions/screen_height_ff/web-ext-artifacts/screen_height_only_values_scrambler_ff-3.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "screen.width") or (extension_choice == "width"):
                extension_location+= "/__assets__/extensions/screen_width_ff/web-ext-artifacts/screen_width_only_values_scrambler_ff-2.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "timezone"):
                extension_location+= "/__assets__/extensions/timezone_ff/web-ext-artifacts/timezone_scrambler_ff-1.0.xpi"
                driver.install_addon(extension_location)
        return driver

    def firefox_driver_extension_list_implementation(self, extension_choices: list):
        # Initialise Firefox Options
        options = OptionsFirefox()

        # Set the specific preference
        # Setting this to True disables the "Manage Exceptions" button in the Privacy & Security menu
        options.set_preference("pref.privacy.disable_button.tracking_protection_exceptions", True)

        # NOTE: An Optional-> Disable the actual tracking protection feature as well
        # (Can be paired with the above to ensure a locked-down, consistent state)
        options.set_preference("privacy.trackingprotection.enabled", False)

        # Disable 'Known Fingerprinters' protection
        options.set_preference("privacy.trackingprotection.fingerprinting.enabled", False)

        # For Private Browsing mode specifically (if applicable)
        options.set_preference("privacy.trackingprotection.pbmode.enabled", False)

        # Disable 'Suspected Fingerprinters' protection (General)
        options.set_preference("privacy.fingerprintingProtection", False)

        # Ensure the global Enhanced Tracking Protection (ETP) isn't overriding this
        # ETP 'Strict' mode often enables suspected fingerprinters by default
        options.set_preference("privacy.trackingprotection.enabled", False)

        # Disable 'Cryptominers' protection
        options.set_preference("privacy.trackingprotection.cryptomining.enabled", False)

        # Disable all cookies
        options.set_preference("network.cookie.cookieBehavior", 2)

        # NOTE: An Optional-> Ensure they are also disabled in Private Browsing mode
        # options.set_preference("network.cookie.cookieBehavior.pbmode", 2)
        
        # Launch the Firefox driver
        # driver = webdriver.Firefox() # NOTE: Vanilla driver-> intend to split this out as a separate option at a later date
        driver = webdriver.Firefox(options=options)

        # Check which extensions to install on the driver
        extensions_to_check = ["font", "canvas", "webgl", "screen",
        "font.offsetHeight", "prototype.offsetHeight", "offsetHeight",
        "font.offsetWidth", "prototype.offsetWidth", "offsetWidth",
        "webgl.parameter", "prototype.parameter", "parameter",
        "webgl.buffer", "prototype.buffer", "buffer",
        "canvas.toBlob", "prototype.toBlob", "toBlob",
        "canvas.toDataURL", "prototype.toDataURL", "toDataURL",
        "screen.availHeight", "prototype.availHeight", "availHeight",
        "screen.availWidth", "prototype.availWidth", "availWidth",
        "screen.colorDepth", "prototype.colorDepth", "colorDepth",
        "screen.devicePixelRatio", "prototype.devicePixelRatio", "devicePixelRatio"]

        extension_location = str(os.path.dirname(os.path.abspath(__file__)))
        for extension_choice in extension_choices:
            if any(ext == extension_choice for ext in extensions_to_check):
                # Combos within an Add On
                if extension_choice == "audio":
                    extension_location+= "/__assets__/extensions/audio_ff/web-ext-artifacts/audio_scrambler_ff-1.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "battery":
                    extension_location+= "/__assets__/extensions/battery_ff/web-ext-artifacts/battery_scrambler_ff-1.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "clientRects":
                    extension_location+= "/__assets__/extensions/clientRects_ff/web-ext-artifacts/clientRects_scrambler_ff-2.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "font":
                    extension_location+= "/__assets__/extensions/font_ff/web-ext-artifacts/font_scrambler_ff-3.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "canvas":
                    extension_location+= "/__assets__/extensions/canvas_ff/web-ext-artifacts/canvas_scrambler_ff-3.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "webgl":
                    extension_location+= "/__assets__/extensions/webgl_ff/web-ext-artifacts/webgl_scrambler_ff-4.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "webrtc") or (extension_choice == "webRTC"):
                    extension_location+= "/__assets__/extensions/webRTC_ff/web-ext-artifacts/webrtc_scrambler_ff-2.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "screen":
                    extension_location+= "/__assets__/extensions/screen_ff/web-ext-artifacts/screen_scrambler_ff-3.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "navigator":
                    extension_location+= "/__assets__/extensions/navigator_ff/web-ext-artifacts/navigator_scrambler_ff-1.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                # Single calls within an Add On
                # The following are for HTMLElement.prototype.'__' HTML elements
                if (extension_choice == "font.offsetHeight") or (extension_choice == "prototype.offsetHeight") or (extension_choice == "offsetHeight"):
                    extension_location+= "/__assets__/extensions/font_offsetHeight_ff/web-ext-artifacts/font_offsetheight_scrambler_ff-1.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "font.offsetWidth") or (extension_choice == "prototype.offsetWidth") or (extension_choice == "offsetWidth"):
                    extension_location+= "/__assets__/extensions/font_offsetHeight_ff/web-ext-artifacts/font_offsetwidth_scrambler_ff-2.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                # The following are for WebGL2RenderingContext.prototype.'__' elements
                if (extension_choice == "webgl.parameter") or (extension_choice == "prototype.parameter") or (extension_choice == "parameter"):
                    extension_location+= "/__assets__/extensions/webgl_parameter_ff/web-ext-artifacts/webgl-parameter-ff-2.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "webgl.buffer") or (extension_choice == "prototype.buffer") or (extension_choice == "buffer"):
                    extension_location+= "/__assets__/extensions/webgl_buffer_ff/web-ext-artifacts/webgl-buffer-ff-2.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                # The following are for CanvasRenderingContext2D.prototype.'__' elements
                if (extension_choice == "canvas.getImageData") or (extension_choice == "prototype.getImageData") or (extension_choice == "getImageData"):
                    extension_location+= "/__assets__/extensions/canvas_getImageData_ff/web-ext-artifacts/getImageData_scrambler_ff-2.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "canvas.toBlob") or (extension_choice == "prototype.toBlob") or (extension_choice == "toBlob"):
                    extension_location+= "/__assets__/extensions/canvas_toBlob_ff/web-ext-artifacts/toBlob_scrambler_ff-3.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "canvas.toDataURL") or (extension_choice == "prototype.toDataURL") or (extension_choice == "toDataURL"):
                    extension_location+= "/__assets__/extensions/canvas_toDataURL_ff/web-ext-artifacts/canvas_toDataURL_ff-1.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                # The following are for Screen.prototype.'__' elements
                if (extension_choice == "screen.availHeight") or (extension_choice == "prototype.availHeight") or (extension_choice == "availHeight"):
                    extension_location+= "/__assets__/extensions/screen_availHeight_ff/web-ext-artifacts/screen_height_values_scrambler_ff-3.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "screen.availWidth") or (extension_choice == "prototype.availWidth") or (extension_choice == "availWidth"):
                    extension_location+= "/__assets__/extensions/screen_availWidth_ff/web-ext-artifacts/screen_width_values_scrambler_ff-2.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "screen.colorDepth") or (extension_choice == "prototype.colorDepth") or (extension_choice == "colorDepth"):
                    extension_location+= "/__assets__/extensions/screen_colorDepth_ff/web-ext-artifacts/colordepth_values_scramble_ff-3.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "screen.devicePixelRatio") or (extension_choice == "prototype.devicePixelRatio") or (extension_choice == "devicePixelRatio"):
                    extension_location+= "/__assets__/extensions/screen_devicePixelRatio_ff/web-ext-artifacts/devicepixelratio_scrambler_ff-2.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "screen.height") or (extension_choice == "height"):
                    extension_location+= "/__assets__/extensions/screen_height_ff/web-ext-artifacts/screen_height_only_values_scrambler_ff-3.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "screen.width") or (extension_choice == "width"):
                    extension_location+= "/__assets__/extensions/screen_width_ff/web-ext-artifacts/screen_width_only_values_scrambler_ff-2.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "timezone"):
                    extension_location+= "/__assets__/extensions/timezone_ff/web-ext-artifacts/timezone_scrambler_ff-1.0.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
        return driver
    
    def firefox_driver_webgl_extension_implementation(self):
        #Initialise the Firefox driver
        options = OptionsFirefox()
        driver = webdriver.Firefox(options=options)
    
        file_being_run = os.path.dirname(os.path.abspath(__file__))
        extension_location = str(file_being_run) + "/__assets__/extensions/firefox_webgl.xpi"

        driver.install_addon(extension_location)
        return driver

    def chrome_driver_implementation_passed_url(self, passed_url):
        # Initialise the Chrome driver
        driver = webdriver.Chrome()
        # Navigate to the URL
        driver.get(passed_url)
        # Print the title page
        print(driver.title)
        # Here we close the browser when done
        driver.quit()

    def chrome_driver_implementation_passed_url_mobile(self, passed_url):
        # Initialise the Chrome driver
        driver = webdriver.Chrome()
        driver.set_window_size(375, 667) #, 375) #Typical screen size for a mobile
        driver.set_window_position(200, 200) # Move the window to position x/y
        # Navigate to the URL
        driver.get(passed_url)
        # Print the title page
        print(driver.title)
        time.sleep(5)
        print(soup(driver.page_source))
        # Here we close the browser when done
        driver.quit()
    
    def chrome_driver_implementation_passed_url_tablet(self, passed_url):
        # Initialise the Chrome driver
        driver = webdriver.Chrome()
        driver.set_window_size(1024, 768) #Typical screen size for a tablet
        # Navigate to the URL
        driver.get(passed_url)
        # Print the title page
        print(driver.title)
        print(driver.page_source)
        # Here we close the browser when done
        driver.quit()
    
    def chrome_driver_implementation_passed_url_desktop(self, passed_url):
        # Initialise the Chrome driver
        driver = webdriver.Chrome()
        driver.set_window_size(1080, 1920) #Typical screen size for a desktop
        # Navigate to the URL
        driver.get(passed_url)
        # Print the title page
        print(driver.title)
        # Here we close the browser when done
        driver.quit()

    def firefox_driver_implementation_passed_url(self, passed_url):
        #Initialise the Firefox driver
        driver = webdriver.Firefox()
        #Navigate to the URL
        driver.get(passed_url)
        #Print the title page
        print(driver.title)
        #Here we close the browser when done
        driver.quit()
    
    def firefox_driver_implementation_passed_url_mobile(self, passed_url):
        # Initialise the Firefox driver
        driver = webdriver.Firefox()
        driver.set_window_size(667, 375) #Typical screen size for a mobile
        # Navigate to the URL
        driver.get(passed_url)
        # Print the title page
        print(driver.title)
        # Here we close the browser when done
        driver.quit()
    
    def firefox_driver_implementation_passed_url_tablet(self, passed_url):
        # Initialise the Firefox driver
        driver = webdriver.Firefox()
        driver.set_window_size(1024, 768) #Typical screen size for a tablet
        # Navigate to the URL
        driver.get(passed_url)
        # Print the title page
        print(driver.title)
        # Here we close the browser when done
        driver.quit()
    
    def firefox_driver_implementation_passed_url_desktop(self, passed_url):
        # Initialise the Firefox driver
        driver = webdriver.Firefox()
        driver.set_window_size(1080, 1920) #Typical screen size for a desktop
        # Navigate to the URL
        driver.get(passed_url)
        # Print the title page
        print(driver.title)
        # Here we close the browser when done
        driver.quit()

    def chrome_options(self):
        options = OptionsChrome()
        options.headless = True #Enable headless mode
        options.add_argument("--window-size=1920, 1920") #Defined window browser size
        return options   

    def chrome_driver_implementation_passed_url_and_options(self, passed_url, options):
        # Initialise the Chrome driver
        driver = webdriver.Chrome(options=options)
        # Navigate to the URL
        driver.get(passed_url)
        # Print the title page
        print(driver.title)
        # Here we close the browser when done
        driver.quit()

    def firefox_options(self):
        options = OptionsFirefox()
        options.headless = True #Enable headless mode
        options.add_argument("--window-size=1920, 1920") #Defined window browser size
        return options 

    def firefox_driver_implementation_passed_url_and_options(self, passed_url, options):
        #Initialise the Firefox driver
        driver = webdriver.Firefox(options=options)
        #Navigate to the URL
        driver.get(passed_url)
        #Print the title page
        print(driver.title)
        #Here we close the browser when done
        driver.quit()
