import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    first_question = [By.ID, 'accordion__heading-0']
    second_question = [By.ID, 'accordion__heading-1']
    third_question = [By.ID, 'accordion__heading-2']
    fourth_question = [By.ID, 'accordion__heading-3']
    fifth_question = [By.ID, 'accordion__heading-4']
    sixth_question = [By.ID, 'accordion__heading-5']
    seventh_question = [By.ID, 'accordion__heading-6']
    eighth_question = [By.ID, 'accordion__heading-7']

    first_answer = [By.ID, 'accordion__panel-0']
    second_answer = [By.ID, 'accordion__panel-1']
    third_answer = [By.ID, 'accordion__panel-2']
    fourth_answer = [By.ID, 'accordion__panel-3']
    fifth_answer = [By.ID, 'accordion__panel-4']
    sixth_answer = [By.ID, 'accordion__panel-5']
    seventh_answer = [By.ID, 'accordion__panel-6']
    eighth_answer = [By.ID, 'accordion__panel-7']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на первый вопрос (со скроллом о последнего, чтобы они прогрузились)')
    def click_on_first_question(self):
        last_element = self.driver.find_element(*self.eighth_question)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_element)
        question = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.first_question))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()

    @allure.step('Нажать на второй вопрос')
    def click_on_second_question(self):
        last_element = self.driver.find_element(*self.eighth_question)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_element)
        question = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.second_question))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()

    @allure.step('Нажать на третий вопрос')
    def click_on_third_question(self):
        last_element = self.driver.find_element(*self.eighth_question)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_element)
        question = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.third_question))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()

    @allure.step('Нажать на четвертый вопрос')
    def click_fourth_question(self):
        last_element = self.driver.find_element(*self.eighth_question)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_element)
        question = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.fourth_question))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()

    @allure.step('Нажать на пятый вопрос')
    def click_fifth_question(self):
        last_element = self.driver.find_element(*self.eighth_question)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_element)
        question = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.fifth_question))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()

    @allure.step('Нажать на шестой вопрос')
    def click_sixth_question(self):
        last_element = self.driver.find_element(*self.eighth_question)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_element)
        question = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.sixth_question))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()

    @allure.step('Нажать на седьмой вопрос')
    def click_seventh_question(self):
        last_element = self.driver.find_element(*self.eighth_question)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_element)
        question = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.seventh_question))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()

    @allure.step('Нажать на восьмой вопрос')
    def click_eighth_question(self):
        last_element = self.driver.find_element(*self.eighth_question)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_element)
        question = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.eighth_question))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()



    @allure.step('Вернуть текст первого ответа')
    def get_first_answer_text(self):
        return WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.first_answer)).text

    @allure.step('Вернуть текст второго ответа')
    def get_second_answer_text(self):
        return WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.second_answer)).text

    @allure.step('Вернуть текст третьего ответа')
    def get_third_answer_text(self):
        return WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.third_answer)).text

    @allure.step('Вернуть текст четвертого ответа')
    def get_fourth_answer_text(self):
        return WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.fourth_answer)).text

    @allure.step('Вернуть текст пятого ответа')
    def get_fifth_answer_text(self):
        return WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.fifth_answer)).text

    @allure.step('Вернуть текст шестого ответа')
    def get_sixth_answer_text(self):
        return WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.sixth_answer)).text

    @allure.step('Вернуть текст седьмого элемента')
    def get_seventh_answer_text(self):
        return WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.seventh_answer)).text

    @allure.step('Вернуть текст восьмого элемента')
    def get_eighth_answer_text(self):
        return WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.eighth_answer)).text


