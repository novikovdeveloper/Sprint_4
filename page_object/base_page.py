import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    yandex_button = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    scooter_button = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    order_button = [By.CLASS_NAME, 'Button_Button__ra12g']
    kill_cookie = [By.ID, 'rcc-confirm-button']
    showcase_button = [By.XPATH, "//div[contains(text(), 'Mozilla Firefox больше не поддерживает поиск Яндекса')]"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на логотип Яндекс')
    def click_on_yandex_logo(self):
        self.driver.find_element(*self.yandex_button).click()

    @allure.step('Нажать на логотип Самокат')
    def click_on_scooter_logo(self):
        self.driver.find_element(*self.scooter_button).click()

    @allure.step('Нажать на кнопку Заказать вверху страницы')
    def click_on_upper_order_button(self):
        self.driver.find_element(*self.kill_cookie).click()
        self.driver.find_elements(*self.order_button)[0].click()

    @allure.step('Нажать на кнопку Заказать внизу страницы (без kill_cookie тест упадет)')
    def click_on_down_order_button(self):
        self.driver.find_element(*self.kill_cookie).click()
        self.driver.find_elements(*self.order_button)[2].click()

    @allure.step('Ожидание загрузки страницы Дзэн')
    def wait_for_loading_dzen_page(self):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.showcase_button))

    @allure.step('Принять куки')
    def accept_cookie(self):
        self.driver.find_element(*self.kill_cookie).click()

