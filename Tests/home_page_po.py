from selenium.webdriver.common.by import By
from page_base import PageBase

class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)  # Инициализация родительского конструктора

    @property
    def main_logo(self):
        return self.wait_for_element(By.CSS_SELECTOR, "#main_logo")

    @property
    def city_location_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, "#open_city_modal_btn")

    @property
    def search_icon(self):
        return self.wait_for_element(By.CSS_SELECTOR, '[data-testid="SearchIcon"]')

    @property
    def search_input(self):
        return self.wait_for_element(By.CSS_SELECTOR, 'div > input')

    @property
    def search_input_placeholder(self):
        return self.search_input.get_attribute("placeholder")

    @property
    def shop_address_button (self):
        return self.wait_for_element(By.CSS_SELECTOR, '#shop_address_map_btn')

    @property
    def notifications_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, '#notifications_btn')

    @property
    def auth_user_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, '#auth_user_modal_btn')

    @property
    def order_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, '#go_to_order_page_btn')

    @property
    def cart_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, '#go_to_cart_page_btn')

    @property
    def favourite_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, '#go_to_favourite_page_btn')

    @property
    def console_category_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, '#device_type_5')

    @property
    def tablet_category_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, '#device_type_1')

    @property
    def smartphone_category_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, '#device_type_2')

    @property
    def watch_category_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, '#device_type_3')

    @property
    def camera_category_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, '#device_type_4')

    @property
    def chat_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, "#chat_btn")

    @property
    def faq_button(self):
        return self.wait_for_element(By.CSS_SELECTOR, "#faq_btn")

    @property
    def is_loaded(self):
        return self.main_logo.is_displayed() and self.faq_button.is_displayed()

