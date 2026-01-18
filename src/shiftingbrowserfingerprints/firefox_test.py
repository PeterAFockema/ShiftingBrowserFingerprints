from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

import os
import time

# Setup Firefox without extension
def setup_firefox_without_extension():
    driver = webdriver.Firefox()
    return driver

# Setup Firefox with Canvas extension
def setup_firefox_with_canvas_extension():
    options = Options()
    # options.add_extension("path/to/extension.xpi")  # Add your extension
    driver = webdriver.Firefox(options=options)
    
    file_being_run = os.path.dirname(os.path.abspath(__file__))
    extension_location = str(file_being_run) + "/__assets__/extensions/firefox_canvas2.xpi"

    driver.install_addon(extension_location)
    
    return driver

# Setup Firefox with Font extension
def setup_firefox_with_font_extension():
    options = Options()
    driver = webdriver.Firefox(options=options)
    
    file_being_run = os.path.dirname(os.path.abspath(__file__))
    extension_location = str(file_being_run) + "/__assets__/extensions/firefox_font.xpi"

    driver.install_addon(extension_location)
    
    return driver

# Setup Firefox with WebGL extension
def setup_firefox_with_webgl_extension():
    options = Options()
    driver = webdriver.Firefox(options=options)
    
    file_being_run = os.path.dirname(os.path.abspath(__file__))
    extension_location = str(file_being_run) + "/__assets__/extensions/firefox_webgl.xpi"

    driver.install_addon(extension_location)
    
    return driver

#Example usage without extension
print("About to declare driver...")
driver = setup_firefox_without_extension()
print("About to get page...")
driver.get("http://127.0.0.1:8080")
time.sleep(10)
print("About to quit...")
driver.quit()

# Example usage
print("About to declare driver for Canvas extension...")
driver = setup_firefox_with_canvas_extension()
print("About to get page...")
driver.get("http://127.0.0.1:8080")
time.sleep(10)
print("About to quit...")
driver.quit()

# Example usage
print("About to declare driver for Font extension...")
driver = setup_firefox_with_font_extension()
print("About to get page...")
driver.get("http://127.0.0.1:8080")
time.sleep(10)
print("About to quit...")
driver.quit()

# Example usage
print("About to declare driver for WebGL extension...")
driver = setup_firefox_with_webgl_extension()
print("About to get page...")
driver.get("http://127.0.0.1:8080")
time.sleep(10)
print("About to quit...")
driver.quit()