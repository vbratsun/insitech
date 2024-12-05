from home_page_po import HomePage
from test_base import TestBase

class TestMainPage(TestBase):
    """Проверить что главная страница содержит необходимые элементы и они доступны"""
    def test_main_page_layout(self):

        home_page = HomePage(self.get_driver())
        home_page.wait_until_page_loaded()

        self.assert_element_is_displayed_and_enabled(home_page.main_logo, "Главный логотип")
        self.assert_element_is_displayed_and_enabled(home_page.city_location_button, "Кнопка местоположения города")
        self.assert_element_is_displayed_and_enabled(home_page.search_icon, "Иконка поиска")
        self.assert_element_is_displayed_and_enabled(home_page.search_input, "Поле ввода поиска")
        assert home_page.search_input_placeholder == "Найти", "Неверный плейсхолдер в инпуте"
        self.assert_element_is_displayed_and_enabled(home_page.shop_address_button, "Кнопка адреса магазина")
        self.assert_element_is_displayed_and_enabled(home_page.notifications_button, "Кнопка уведомлений")
        self.assert_element_is_displayed_and_enabled(home_page.auth_user_button, "Кнопка войти")
        self.assert_element_is_displayed_and_enabled(home_page.order_button, "Кнопка заказы")
        self.assert_element_is_displayed_and_enabled(home_page.cart_button, "Кнопка корзина")
        self.assert_element_is_displayed_and_enabled(home_page.favourite_button, "Кнопка избранное")
        self.assert_element_is_displayed_and_enabled(home_page.faq_button, "Кнопка FAQ")
        self.assert_element_is_displayed_and_enabled(home_page.console_category_button, "Кнопка консоль")
        self.assert_element_is_displayed_and_enabled(home_page.tablet_category_button, "Кнопка планшет")
        self.assert_element_is_displayed_and_enabled(home_page.smartphone_category_button, "Кнопка смартфон")
        self.assert_element_is_displayed_and_enabled(home_page.watch_category_button, "Кнопка часы")
        self.assert_element_is_displayed_and_enabled(home_page.camera_category_button, "Кнопка камера")
        self.assert_element_is_displayed_and_enabled(home_page.chat_button, "Кнопка чата")


    def assert_element_is_displayed_and_enabled(self, element, element_name):
        assert element.is_displayed(), f"{element_name} не отображается"
        assert element.is_enabled(), f"{element_name} не доступен"
