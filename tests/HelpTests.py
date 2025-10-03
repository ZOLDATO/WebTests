import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.AdvertisementCabinet_Help import AdvertisementCabinetHelpHelper

BASE_URL = 'https://ok.ru/help'


@allure.suite("Проверка страницы помощи")
@allure.title("Проверка перехода на страницу рекламного кабинета")
def test_help_test(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scroll_to_item(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)
