import initial_config
from abc import ABC, abstractmethod

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageBase:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, locator, timeout=initial_config.wait_for_element_timeout):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    @property
    @abstractmethod
    def is_loaded(self):
        pass

    def wait_until_page_loaded(self, timeout=initial_config.wait_until_page_loaded_timeout):
        WebDriverWait(self.driver, timeout).until(lambda driver: self.is_loaded)