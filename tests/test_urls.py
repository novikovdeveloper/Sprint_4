import allure
from page_object.base_page import BasePage


class TestURLs:

    @allure.title('Проверка: При нажатии на логотип "Самокат", то произойдет переход на главную страницу "Самокат"')
    def test_scooter_logo(self, driver):
        base_page = BasePage(driver)
        base_page.click_on_upper_order_button()
        base_page.click_on_scooter_logo()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка: При нажатии на лого "Яндекс", в новом окне откроется главная страница "Dzen"')
    def test_ya_dzen_logo(self, driver):
        base_page = BasePage(driver)
        base_page.click_on_yandex_logo()
        second_window = driver.window_handles[1]
        driver.switch_to.window(second_window)
        base_page.wait_for_loading_dzen_page()
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

