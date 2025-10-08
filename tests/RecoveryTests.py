import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper

BASE_URL = 'https://ok.ru/'
LOGIN_TEXT = 'email'
PASSWORD_TEXT = '1'


@allure.suite("Проверка восстановления профиля")
@allure.title("Проверка перехода к восстановлению профиля после нескольких неудачных попыток входа")
def test_goto_recovery_page_after_many_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.input_login_field(LOGIN_TEXT)

    for _ in range(3):
        LoginPage.input_password_field(PASSWORD_TEXT)
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPageHelper(browser)
