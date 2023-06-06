import allure
from page_object.order_page import OrderPage
from page_object.base_page import BasePage



class TestOrder:

    @allure.title('Проверка: оформление заказа с черным самокатом')
    def test_first_order_case(self, driver):
        base_page = BasePage(driver)
        base_page.click_on_upper_order_button()
        order_page = OrderPage(driver)
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
    def test_second_order_case(self, driver):
        base_page = BasePage(driver)
        base_page.click_on_down_order_button()
        order_page = OrderPage(driver)
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
