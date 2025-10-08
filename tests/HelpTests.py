import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.AdvertisementCabinet_Help import AdvertisementCabinetHelper

BASE_URL = 'https://ok.ru/help'


@allure.suite("Проверка страницы помощи")
@allure.title("Проверка перехода на страницу рекламного кабинета")
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scroll_to_item(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelper(browser)
