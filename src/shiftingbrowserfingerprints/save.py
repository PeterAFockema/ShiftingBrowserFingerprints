from selenium import webdriver

def save_page(page:str, save_to_page:str):
    with open(save_to_page, "w", encoding='utf-8') as f:
        f.write(page)

def get_and_save_page(driver, page_source:str, save_to_page:str):
    driver_types = [webdriver.Chrome(), webdriver.Firefox()]
    if driver not in driver_types:
        raise ValueError("Invalid driver type. Expected one of: %s" % driver_types)
    
    driver.get(page_source)
    with open(save_to_page, "w", encoding='utf-8') as f:
        f.write(driver.page_source)