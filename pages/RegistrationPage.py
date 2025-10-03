import allure
import random
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    PHONE_FIELD = (By.XPATH, '//*[@id="field_phone"]')
    COUTRY_LIST = (By.XPATH, '//*[@id="country"]')
    NEXT_BUTTON = (By.XPATH, '//*[@data-l="t,submit"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@data-l="t,support"]')
    COUNTRY_ITEM = (By.CLASS_NAME, 'country-select_i')


class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.COUTRY_LIST)
            self.find_element(RegistrationPageLocators.NEXT_BUTTON)
            self.find_element(RegistrationPageLocators.SUPPORT_BUTTON)

    @allure.step('Кликаем по кнопке "Восстановить профиль" и выбираем страну/регион')
    def select_random_country(self):
        self.find_element(RegistrationPageLocators.COUTRY_LIST).click()
        self.attach_screenshot()  # скрин выпадающего списка
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        country_random_element = random.choice(country_items)
        country_code = country_random_element.find_element(By.CLASS_NAME, "country-select_code").text
        country_random_element.click()
        self.attach_screenshot()  # скрин после выбора рандомной страны
        return country_code

    def get_phone_field_value(self):
        return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('value')
