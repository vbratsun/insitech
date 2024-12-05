from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import initial_config

def create_driver():
    service = Service(initial_config.driver_path)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    return driver