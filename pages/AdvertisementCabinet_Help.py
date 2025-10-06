import allure
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class AdvertisementCabinetHelpPageLocators:
    TITLE = (By.XPATH, '//span[text()="Рекламный кабинет"]')


class AdvertisementCabinetHelpHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы Рекламного кабинета'):
            self.attach_screenshot()
            self.find_element(AdvertisementCabinetHelpPageLocators.TITLE)
