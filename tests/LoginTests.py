from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_TEXT = 'Введите логин'
EMPTY_PASSWORD_TEXT = 'Введите пароль'


def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_TEXT


def test_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.input_login_field()
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_PASSWORD_TEXT
