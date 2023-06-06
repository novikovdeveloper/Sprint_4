import allure
from page_object.main_page import MainPage
from page_object.base_page import BasePage


class TestAccordionElements:

    @allure.title('Проверка: первый вопрос')
    def test_first_question(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_first_question()
        assert main_page.get_first_answer_text() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка: Второй вопрос')
    def test_second_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_on_second_question()
        assert main_page.get_second_answer_text() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка: третий вопрос')
    def test_third_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_on_third_question()
        assert main_page.get_third_answer_text() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка: четвертый вопрос')
    def test_fourth_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_fourth_question()
        assert main_page.get_fourth_answer_text() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка: пятый вопрос')
    def test_fifth_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_fifth_question()
        assert main_page.get_fifth_answer_text() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Проверка: шестой вопрос')
    def test_sixth_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_sixth_question()
        assert main_page.get_sixth_answer_text() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка: седьмой вопрос')
    def test_seventh_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_seventh_question()
        assert main_page.get_seventh_answer_text() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка: восьмой вопрос')
    def test_eighth_question(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        base_page.accept_cookie()
        main_page.click_eighth_question()
        assert main_page.get_eighth_answer_text() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

