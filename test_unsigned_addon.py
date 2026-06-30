import os
import time

from selenium import webdriver

# 1. Fix: Added quotes around path strings
base_dir = os.path.dirname(os.path.abspath(__file__))
addon_path = os.path.join(
    base_dir, 
    "src", 
    "shiftingbrowserfingerprints", 
    "__assets__", 
    "extensions", 
    "audio_ff_unsigned", 
    "web-ext-artifacts", 
    "audio_ff_unsigned_2.xpi"
)

# 2. Fix: Added quotes to the replacement string
clean_path = addon_path.replace("\\", "/")

# Initialise Firefox
driver = webdriver.Firefox()

try:
    # 3. Load the extension temporarily
    addon_id = driver.install_addon(clean_path, temporary=True)
    print(f"Successfully loaded unsigned extension with ID: {addon_id}")

    # Run automation
    driver.get("http://localhost:8080/")

    # 2. Keep the window open for 10 seconds (change this number as needed)
    print("Waiting 10 seconds before closing...")
    time.sleep(10) 

finally:
    # Clean up
    driver.quit()