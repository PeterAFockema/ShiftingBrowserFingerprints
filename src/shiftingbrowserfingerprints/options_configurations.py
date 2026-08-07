#options_configurations.py

from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox

class OptionsConfigurations(object):
    '''
    A class for Options configurations for Chrome and Firefox.
    '''

    def __init__(self):
        print("The OptionsConfigurations class initialised...")

    def chrome_options(self):
        options = OptionsChrome()
        options.headless = True #Enable headless mode
        options.add_argument("--window-size=1920, 1920") #Defined window browser size
        return options  
    
    def firefox_options(self):
        options = OptionsFirefox()
        options.headless = True #Enable headless mode
        options.add_argument("--window-size=1920, 1920") #Defined window browser size
        return options 