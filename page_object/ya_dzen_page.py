import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DzenPage:
    showcase_button = [By.XPATH, "//div[contains(text(), 'Mozilla Firefox больше не поддерживает поиск Яндекса')]"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки страницы Дзэн')
    def wait_for_loading_dzen_page(self):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.showcase_button))