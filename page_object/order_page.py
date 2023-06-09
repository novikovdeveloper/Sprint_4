import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage:
    inputs = [By.XPATH, "//input[contains(@class, 'Input_Responsible__1jDKN')]"]
    metro_station_input = [By.CLASS_NAME, 'select-search__input']
    metro_station_row = [By.CLASS_NAME, 'select-search__row']
    next_button = [By.XPATH, "//button[contains(text(), 'Далее')]"]
    inputs_second_page = [By.XPATH, "//input[contains(@class, 'Input_Responsible__1jDKN')]"]
    date_picker_selected = [By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]"]
    dropdown_control = [By.CLASS_NAME, 'Dropdown-control']
    dropdown_option = [By.CLASS_NAME, 'Dropdown-option']
    black_checkbox = [By.ID, 'black']
    grey_checkbox = [By.ID, 'grey']
    order_button = [By.XPATH, "//button[contains(text(), 'Заказать') and contains(@class, 'Button_Middle__1CSJM')]"]
    yes_button = [By.XPATH, "//button[contains(text(), 'Да') and contains(@class, 'Button_Middle__1CSJM')]"]
    order_has_been_placed = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ввести имя')
    def set_name(self):
        self.driver.find_elements(*self.inputs)[0].send_keys('Петр')

    @allure.step('Ввести фамилию')
    def set_surname(self):
        self.driver.find_elements(*self.inputs)[1].send_keys('Петров')

    @allure.step('Ввести адрес')
    def set_address(self):
        self.driver.find_elements(*self.inputs)[2].send_keys('Москва, Проспект Андропова, 22')

    @allure.step('Выбрать станцию метро')
    def set_metro_station(self):
        self.driver.find_element(*self.metro_station_input).send_keys('Бульвар Рокоссовского')
        self.driver.find_element(*self.metro_station_row).click()

    @allure.step('Ввести номер телефона')
    def set_phone_number(self):
        self.driver.find_elements(*self.inputs)[3].send_keys('+79009998877')

    @allure.step('Нажать Далее')
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Выбор даты')
    def set_date(self):
        self.driver.find_elements(*self.inputs_second_page)[0].send_keys('11.06.2023')
        self.driver.find_element(*self.date_picker_selected).click()

    @allure.step('Выбрать срок аренды: трое суток')
    def set_rent_period(self):
        self.driver.find_element(*self.dropdown_control).click()
        self.driver.find_elements(*self.dropdown_option)[2].click()

    @allure.step('Выбрать черный цвет')
    def click_black_color(self):
        self.driver.find_element(*self.black_checkbox).click()

    @allure.step('выбрать серый цвет')
    def click_grey_color(self):
        self.driver.find_element(*self.grey_checkbox).click()

    @allure.step('Ввести комментарий')
    def set_comment(self):
        self.driver.find_elements(*self.inputs_second_page)[1].send_keys('Комментарий')

    @allure.step('Нажать Заказать')
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Нажать Да')
    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    @allure.step("Получить текст Заказ оформлен")
    def order_is_processed_text(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.order_has_been_placed)).text

