import allure
from selenium import webdriver
from page_object.ya_dzen_page import DzenPage
from page_object.main_page import MainPage


class TestURLs:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')

    @allure.title('Проверка: При нажатии на логотип "Самокат", то произойдет переход на главную страницу "Самокат"')
    def test_scooter_logo(self):
        main_page = MainPage(self.driver)
        main_page.click_on_upper_order_button()
        main_page.click_on_scooter_logo()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка: При нажатии на лого "Яндекс", в новом окне откроется главная страница "Dzen"')
    def test_ya_dzen_logo(self):
        main_page = MainPage(self.driver)
        main_page.click_on_yandex_logo()
        second_window = self.driver.window_handles[1]
        self.driver.switch_to.window(second_window)
        dzen_page = DzenPage(self.driver)
        dzen_page.wait_for_loading_dzen_page()
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()