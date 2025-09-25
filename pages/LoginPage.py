import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_ENTER_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    LOGIN_RESET_PASS_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    LOGIN_REGISTER_BUTTON = (By.XPATH, '//*[@class="button-pro __sec mb-3x __wide"]')
    LOGIN_WITH_VK = (By.XPATH, '//*[@class="i ic social-icon __s __vk_id"]')
    LOGIN_WITH_MAILRU = (By.XPATH, '//*[@class="i ic social-icon __s __mailru"]')
    LOGIN_WITH_YANDEX = (By.XPATH, '//*[@class="i ic social-icon __s __yandex"]')
    LOGIN_ERROR_TEXT = (By.XPATH, '//*[@class="input-e login_error"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_ENTER_TAB)
        self.find_element(LoginPageLocators.LOGIN_QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_QR_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_RESET_PASS_LINK)
        self.find_element(LoginPageLocators.LOGIN_REGISTER_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_WITH_VK)
        self.find_element(LoginPageLocators.LOGIN_WITH_MAILRU)
        self.find_element(LoginPageLocators.LOGIN_WITH_YANDEX)

    @allure.step("Кликаем на кнопку 'Войти'")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.LOGIN_ERROR_TEXT).text

    @allure.step('Вводим текст в поле логин')
    def input_login_field(self, login):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)