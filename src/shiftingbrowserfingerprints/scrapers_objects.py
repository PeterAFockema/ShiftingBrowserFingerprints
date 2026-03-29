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
        # Initialize the Chrome driver
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

        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def chrome_driver_canvas_extension_implementation(self):
        file_being_run = os.path.dirname(os.path.abspath(__file__))
        extension_location = str(file_being_run) + "/__assets__/extensions/canvas.crx"
        chrome_options = OptionsChrome()
        chrome_options.add_extension(extension_location)

        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def firefox_driver_implementation(self):
        #Initialise the Firefox driver
        driver = webdriver.Firefox()
        return driver

    def firefox_driver_canvas_extension_implementation(self):
        #Initialise the Firefox driver
        driver = webdriver.Firefox()
        return driver
    
    def firefox_driver_font_extension_implementation(self):
        #Initialise the Firefox driver
        options = OptionsFirefox()
        driver = webdriver.Firefox(options=options)
    
        file_being_run = os.path.dirname(os.path.abspath(__file__))
        extension_location = str(file_being_run) + "/__assets__/extensions/firefox_font.xpi"

        driver.install_addon(extension_location)
        return driver
        
    def firefox_driver_extension_implementation(self, extension_choice: str):
        # Initialise the Firefox driver
        driver = webdriver.Firefox()
        # Check which extensions to install on the driver
        extensions_to_check = ["font", "canvas", "webgl", "screen"]
        extension_location = str(os.path.dirname(os.path.abspath(__file__)))
        if any(ext == extension_choice for ext in extensions_to_check):
            # Combos within an Add On
            if extension_choice == "font":
                extension_location+= "/__assets__/extensions/font_ff/node_modules/font_scrambler_ff-1.0.xpi"
                driver.install_addon(extension_location)
            if extension_choice == "canvas":
                extension_location+= "/__assets__/extensions/canvas_ff/node_modules/canvas_scrambler_ff-1.0.xpi"
                driver.install_addon(extension_location)
            if extension_choice == "webgl":
                extension_location+= "/__assets__/extensions/webgl_ff/node_modules/webgl_scrambler_ff-1.0.xpi"
                driver.install_addon(extension_location)
            if extension_choice == "screen":
                extension_location+= "/__assets__/extensions/screen_ff/node_modules/screen_scrambler_ff-1.0.xpi"
                driver.install_addon(extension_location)
            # Single calls within an Add On
            # The following are for HTMLElement.prototype.'__' HTML elements
            if (extension_choice == "font.offsetHeight") or (extension_choice == "prototype.offsetHeight") or (extension_choice == "offsetHeight"):
                extension_location+= "/__assets__/extensions/font_offsetHeight_ff/node_modules/font_offsetheight_scrambler_ff-1.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "font.offsetWidth") or (extension_choice == "prototype.offsetWidth") or (extension_choice == "offsetWidth"):
                extension_location+= "/__assets__/extensions/font_offsetHeight_ff/node_modules/font_offsetwidth_scrambler_ff-1.0.xpi"
                driver.install_addon(extension_location)
            # The following are for WebGL2RenderingContext.prototype.'__' elements
            if (extension_choice == "webgl.parameter") or (extension_choice == "prototype.parameter") or (extension_choice == "parameter"):
                extension_location+= "/__assets__/extensions/webgl_parameter_ff/node_modules/webgl-parameter-ff-1.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "webgl.buffer") or (extension_choice == "prototype.buffer") or (extension_choice == "buffer"):
                extension_location+= "/__assets__/extensions/webgl_buffer_ff/node_modules/webgl-buffer-ff-1.0.xpi"
                driver.install_addon(extension_location)
            # The following are for CanvasRenderingContext2D.prototype.'__' elements
            if (extension_choice == "canvas.toBlob") or (extension_choice == "prototype.toBlob") or (extension_choice == "toBlob"):
                extension_location+= "/__assets__/extensions/canvas_toBlob_ff/node_modules/canvas_toBlob_ff-1.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "canvas.toDataURL") or (extension_choice == "prototype.toDataURL") or (extension_choice == "toDataURL"):
                extension_location+= "/__assets__/extensions/canvas_toDataURL_ff/node_modules/canvas_toDataURL_ff-1.0.xpi"
                driver.install_addon(extension_location)
            # The following are for Screen.prototype.'__' elements
            if (extension_choice == "screen.availHeight") or (extension_choice == "prototype.availHeight") or (extension_choice == "availHeight"):
                extension_location+= "/__assets__/extensions/screen_availHeight_ff/node_modules/screen_availheight_values_scrambler-1.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "screen.availWidth") or (extension_choice == "prototype.availWidth") or (extension_choice == "availWidth"):
                extension_location+= "/__assets__/extensions/screen_availWidth_ff/node_modules/screen_availwidth_values_scrambler-1.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "screen.colorDepth") or (extension_choice == "prototype.colorDepth") or (extension_choice == "colorDepth"):
                extension_location+= "/__assets__/extensions/screen_colorDepth_ff/node_modules/screen_colordepth_values_scrambler-1.0.xpi"
                driver.install_addon(extension_location)
            if (extension_choice == "screen.devicePixelRatio") or (extension_choice == "prototype.devicePixelRatio") or (extension_choice == "devicePixelRatio"):
                extension_location+= "/__assets__/extensions/screen_devicePixelRatio_ff/node_modules/screen_devicepixelratio_values_scrambler-1.0.xpi"
                driver.install_addon(extension_location)
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
        # Initialize the Chrome driver
        driver = webdriver.Chrome()
        # Navigate to the URL
        driver.get(passed_url)
        # Print the title page
        print(driver.title)
        # Here we close the browser when done
        driver.quit()

    def chrome_driver_implementation_passed_url_mobile(self, passed_url):
        # Initialize the Chrome driver
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
        # Initialize the Chrome driver
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
        # Initialize the Chrome driver
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
        # Initialize the Firefox driver
        driver = webdriver.Firefox()
        driver.set_window_size(667, 375) #Typical screen size for a mobile
        # Navigate to the URL
        driver.get(passed_url)
        # Print the title page
        print(driver.title)
        # Here we close the browser when done
        driver.quit()
    
    def firefox_driver_implementation_passed_url_tablet(self, passed_url):
        # Initialize the Firefox driver
        driver = webdriver.Firefox()
        driver.set_window_size(1024, 768) #Typical screen size for a tablet
        # Navigate to the URL
        driver.get(passed_url)
        # Print the title page
        print(driver.title)
        # Here we close the browser when done
        driver.quit()
    
    def firefox_driver_implementation_passed_url_desktop(self, passed_url):
        # Initialize the Firefox driver
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
        # Initialize the Chrome driver
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
