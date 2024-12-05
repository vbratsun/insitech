import os

# Путь к драйверу
driver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")

# Таймауты
wait_for_element_timeout = 10
wait_until_page_loaded_timeout = 10

# URL сайта
site_url = "https://opm-website.iot-asm-test1.insitech.live"
