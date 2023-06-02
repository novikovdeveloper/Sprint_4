import allure
from selenium import webdriver
from page_object.main_page import MainPage
from page_object.order_page import OrderPage


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Проверка: оформление заказа с черным самокатом')
    def test_first_order_case(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_on_upper_order_button()
        order_page = OrderPage(self.driver)
        order_page.set_name()
        order_page.set_surname()
        order_page.set_address()
        order_page.set_metro_station()
        order_page.set_phone_number()
        order_page.click_next_button()
        order_page.set_date()
        order_page.set_rent_period()
        order_page.click_black_color()
        order_page.set_comment()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_is_processed_text().startswith('Заказ оформлен')

    @allure.title('Проверка: оформление заказа с серым самокатом и нижней кнопкой "Заказать"')
    def test_second_order_case(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_on_down_order_button()
        order_page = OrderPage(self.driver)
        order_page.set_name()
        order_page.set_surname()
        order_page.set_address()
        order_page.set_metro_station()
        order_page.set_phone_number()
        order_page.click_next_button()
        order_page.set_date()
        order_page.set_rent_period()
        order_page.click_grey_color()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_is_processed_text().startswith('Заказ оформлен')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()