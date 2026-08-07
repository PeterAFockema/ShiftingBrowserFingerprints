#scrapers_objects.py

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as OptionsFirefox
import os

class FirefoxScrapers(object):
    '''
    A class for web scrapers.
    '''

    def __init__(self):
        print("The Scrapers class initialised...")

    def firefox_driver_implementation(self):
        #Initialise the Firefox driver
        driver = webdriver.Firefox()
        return driver
        
    def firefox_driver_extension_string_implementation(self, extension_choice: str):
        # Initialise Firefox Options
        options = OptionsFirefox()

        # Bypass standard domain blocks
        options.set_preference("extensions.webextensions.restrictedDomains", "")

        # Allow unsigned/temporary extensions to run in secure contexts
        options.set_preference("extensions.experiments.enabled", True)
        options.set_preference("xpinstall.signatures.required", False)

        # Bypass insecure certificate warnings
        options.accept_insecure_certs = True
        # Launch the Firefox driver
        # driver = webdriver.Firefox() # NOTE: Vanilla driver-> intend to split this out as a separate option at a later date
        driver = webdriver.Firefox(options=options)

        # Define the base asset directory using path objects
        base_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(base_dir, "__assets__", "extensions")

        extension_paths = {
        "audio": "aud_ff/web-ext-artifacts/aud_ff.xpi",
        "battery": "bat_ff/web-ext-artifacts/bat_ff.xpi",
        "canvas": "can_ff/web-ext-artifacts/can_ff.xpi",
        "clientRects": "clientRects_ff/web-ext-artifacts/clientrects_ff.xpi",
        "font": "font_ff/web-ext-artifacts/font_ff.xpi",
        "navigator": "nav_ff/web-ext-artifacts/nav_ff.xpi",
        "screen": "scre_ff/web-ext-artifacts/scre_ff.xpi",
        "webgl": "webgl_ff/web-ext-artifacts/webgl_ff.xpi",
        "webGL": "webgl_ff/web-ext-artifacts/webgl_ff.xpi",
        "webrtc": "webRTC_ff/web-ext-artifacts/webrtc_ff.xpi",
        "webRTC": "webRTC_ff/web-ext-artifacts/webrtc_ff.xpi",
        "timezone": "timez_ff/web-ext-artifacts/timez_ff.xpi",
        "font.offsetHeight": "font_offHei_ff/web-ext-artifacts/font_offhei_ff.xpi",
        "prototype.offsetHeight": "font_offHei_ff/web-ext-artifacts/font_offhei_ff.xpi",
        "offsetHeight": "font_offHei_ff/web-ext-artifacts/font_offhei_ff.xpi",
        "font.offsetWidth": "font_offWid_ff/web-ext-artifacts/font_offwid_ff.xpi",
        "prototype.offsetWidth": "font_offWid_ff/web-ext-artifacts/font_offwid_ff.xpi",
        "offsetWidth": "font_offWid_ff/web-ext-artifacts/font_offwid_ff.xpi",
        "webgl.parameter": "webgl_param_ff/web-ext-artifacts/webgl_param_ff.xpi",
        "prototype.parameter": "webgl_param_ff/web-ext-artifacts/webgl_param_ff.xpi",
        "parameter": "webgl_param_ff/web-ext-artifacts/webgl_param_ff.xpi",
        "webgl.buffer": "webgl_buf_ff/web-ext-artifacts/webgl_buf_ff.xpi",
        "prototype.buffer": "webgl_buf_ff/web-ext-artifacts/webgl_buf_ff.xpi",
        "buffer": "webgl_buf_ff/web-ext-artifacts/webgl_buf_ff.xpi",
        "canvas.toBlob": "canv_toBl_ff/web-ext-artifacts/canv_tobl_ff.xpi",
        "prototype.toBlob": "canv_toBl_ff/web-ext-artifacts/canv_tobl_ff.xpi",
        "toBlob": "canv_toBl_ff/web-ext-artifacts/canv_tobl_ff.xpi",
        "canvas.getImageData": "canv_getImDat_ff/web-ext-artifacts/canv_getimdat_ff.xpi",
        "prototype.getImageData": "canv_getImDat_ff/web-ext-artifacts/canv_getimdat_ff.xpi",
        "getImageData": "canv_getImDat_ff/web-ext-artifacts/canv_getimdat_ff.xpi",
        "canvas.toDataURL": "canv_toDatURL_ff/web-ext-artifacts/canv_todaturl_ff.xpi",
        "prototype.toDataURL": "canv_toDatURL_ff/web-ext-artifacts/canv_todaturl_ff.xpi",
        "toDataURL": "canv_toDatURL_ff/web-ext-artifacts/canv_todaturl_ff.xpi",
        "screen.height": "scre_hei_ff/web-ext-artifacts/scre_hei_ff.xpi",
        "height": "scre_hei_ff/web-ext-artifacts/scre_hei_ff.xpi",
        "screen.width": "scre_wid_ff/web-ext-artifacts/scre_wid_ff.xpi",
        "width": "scre_wid_ff/web-ext-artifacts/scre_wid_ff.xpi",
        "screen.availHeight": "scre_avaHei_ff/web-ext-artifacts/scre_avahei_ff.xpi",
        "prototype.availHeight": "scre_avaHei_ff/web-ext-artifacts/scre_avahei_ff.xpi",
        "availHeight": "scre_avaHei_ff/web-ext-artifacts/scre_avahei_ff.xpi",
        "screen.availWidth": "scre_avaWid_ff/web-ext-artifacts/scre_avawid_ff.xpi",
        "prototype.availWidth": "scre_avaWid_ff/web-ext-artifacts/scre_avawid_ff.xpi",
        "availWidth": "scre_avaWid_ff/web-ext-artifacts/scre_avawid_ff.xpi",
        "screen.colorDepth": "scre_colDep_ff/web-ext-artifacts/scre_coldep_ff.xpi",
        "prototype.colorDepth": "scre_colDep_ff/web-ext-artifacts/scre_coldep_ff.xpi",
        "colorDepth": "scre_colDep_ff/web-ext-artifacts/scre_coldep_ff.xpi",
        "screen.devicePixelRatio": "scre_devPixRat_ff/web-ext-artifacts/scre_devpixrat_ff.xpi",
        "prototype.devicePixelRatio": "scre_devPixRat_ff/web-ext-artifacts/scre_devpixrat_ff.xpi",
        "devicePixelRatio": "scre_devPixRat_ff/web-ext-artifacts/scre_devpixrat_ff.xpi"
        }

        choice_lower = extension_choice.lower()
        # Install the extension as necessary
        for key, sub_path in extension_paths.items():
            if key == choice_lower:
                full_extension_path = os.path.join(assets_dir, sub_path)
                
                # Install the extension onto the active driver instance
                if os.path.exists(full_extension_path):
                    driver.install_addon(full_extension_path, temporary=True)
                else:
                    raise FileNotFoundError(f"Extension file missing: {full_extension_path}")
                break
        
        return driver

    def firefox_driver_extension_list_implementation(self, extension_choices: list):
        # Initialise Firefox Options
        options = OptionsFirefox()

        # Bypass standard domain blocks
        options.set_preference("extensions.webextensions.restrictedDomains", "")

        # Allow unsigned/temporary extensions to run in secure contexts
        options.set_preference("extensions.experiments.enabled", True)
        options.set_preference("xpinstall.signatures.required", False)

        # Bypass insecure certificate warnings
        options.accept_insecure_certs = True
        
        # Launch the Firefox driver
        # driver = webdriver.Firefox() # NOTE: Vanilla driver-> intend to split this out as a separate option at a later date
        driver = webdriver.Firefox(options=options)

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
        for extension_choice in extension_choices:
            if any(ext == extension_choice for ext in extensions_to_check):
                # Combos within an Add On
                if extension_choice == "audio":
                    extension_location+= "/__assets__/extensions/aud_ff/web-ext-artifacts/aud_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "battery":
                    extension_location+= "/__assets__/extensions/batt_ff/web-ext-artifacts/batt_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "clientRects":
                    extension_location+= "/__assets__/extensions/clientRects_ff/web-ext-artifacts/clientrects_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "font":
                    extension_location+= "/__assets__/extensions/font_ff/web-ext-artifacts/font_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "canvas":
                    extension_location+= "/__assets__/extensions/canv_ff/web-ext-artifacts/canv_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "webgl":
                    extension_location+= "/__assets__/extensions/webgl_ff/web-ext-artifacts/webgl_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "webrtc") or (extension_choice == "webRTC"):
                    extension_location+= "/__assets__/extensions/webRTC_ff/web-ext-artifacts/webrtc_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "screen":
                    extension_location+= "/__assets__/extensions/scre_ff/web-ext-artifacts/scre_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if extension_choice == "navigator":
                    extension_location+= "/__assets__/extensions/nav_ff/web-ext-artifacts/nav_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                # Single calls within an Add On
                # The following are for HTMLElement.prototype.'__' HTML elements
                if (extension_choice == "font.offsetHeight") or (extension_choice == "prototype.offsetHeight") or (extension_choice == "offsetHeight"):
                    extension_location+= "/__assets__/extensions/font_offHei_ff/web-ext-artifacts/font_offhei_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "font.offsetWidth") or (extension_choice == "prototype.offsetWidth") or (extension_choice == "offsetWidth"):
                    extension_location+= "/__assets__/extensions/font_offWid_ff/web-ext-artifacts/font_offwid_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                # The following are for WebGL2RenderingContext.prototype.'__' elements
                if (extension_choice == "webgl.parameter") or (extension_choice == "prototype.parameter") or (extension_choice == "parameter"):
                    extension_location+= "/__assets__/extensions/webgl_param_ff/web-ext-artifacts/webgl_param_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "webgl.buffer") or (extension_choice == "prototype.buffer") or (extension_choice == "buffer"):
                    extension_location+= "/__assets__/extensions/webgl_buf_ff/web-ext-artifacts/webgl_buf_ff.xpi"
                    driver.install_addon(extension_location)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                # The following are for CanvasRenderingContext2D.prototype.'__' elements
                if (extension_choice == "canvas.getImageData") or (extension_choice == "prototype.getImageData") or (extension_choice == "getImageData"):
                    extension_location+= "/__assets__/extensions/canv_getImDat_ff/web-ext-artifacts/canv_getimdat_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "canvas.toBlob") or (extension_choice == "prototype.toBlob") or (extension_choice == "toBlob"):
                    extension_location+= "/__assets__/extensions/canv_toBl_ff/web-ext-artifacts/canv_tobl_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "canvas.toDataURL") or (extension_choice == "prototype.toDataURL") or (extension_choice == "toDataURL"):
                    extension_location+= "/__assets__/extensions/canv_toDatURL_ff/web-ext-artifacts/canv_todaturl_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                # The following are for Screen.prototype.'__' elements
                if (extension_choice == "screen.availHeight") or (extension_choice == "prototype.availHeight") or (extension_choice == "availHeight"):
                    extension_location+= "/__assets__/extensions/scre_avaHei_ff/web-ext-artifacts/scre_avahei_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "screen.availWidth") or (extension_choice == "prototype.availWidth") or (extension_choice == "availWidth"):
                    extension_location+= "/__assets__/extensions/scre_avaWid_ff/web-ext-artifacts/scre_avawid_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "screen.colorDepth") or (extension_choice == "prototype.colorDepth") or (extension_choice == "colorDepth"):
                    extension_location+= "/__assets__/extensions/scre_colDep_ff/web-ext-artifacts/scre_coldep_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "screen.devicePixelRatio") or (extension_choice == "prototype.devicePixelRatio") or (extension_choice == "devicePixelRatio"):
                    extension_location+= "/__assets__/extensions/scre_devPixRat_ff/web-ext-artifacts/scre_devpixrat_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "screen.height") or (extension_choice == "height"):
                    extension_location+= "/__assets__/extensions/scre_hei_ff/web-ext-artifacts/scre_hei_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "screen.width") or (extension_choice == "width"):
                    extension_location+= "/__assets__/extensions/scre_wid_ff/web-ext-artifacts/scre_wid_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
                if (extension_choice == "timezone"):
                    extension_location+= "/__assets__/extensions/timez_ff/web-ext-artifacts/timez_ff.xpi"
                    driver.install_addon(extension_location, temporary=True)
                    extension_location = str(os.path.dirname(os.path.abspath(__file__)))
        return driver

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

    def firefox_driver_implementation_passed_url_and_options(self, passed_url, options):
        #Initialise the Firefox driver
        driver = webdriver.Firefox(options=options)
        #Navigate to the URL
        driver.get(passed_url)
        #Print the title page
        print(driver.title)
        #Here we close the browser when done
        driver.quit()
