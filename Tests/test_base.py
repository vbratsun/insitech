from driver_factory import create_driver
import initial_config


class TestBase:
    def setup_method(self):
        """Настройка теста: создание драйвера и настройка браузера"""
        self.driver = create_driver()  # Создание драйвера
        self.driver.get(initial_config.site_url)  # Переход на сайт

    def teardown_method(self):
        """Очистка после теста: закрытие драйвера"""
        if self.driver:
            self.driver.quit()  # Закрытие браузера

    def get_driver(self):
        """Возвращаем текущий драйвер"""
        return self.driver
