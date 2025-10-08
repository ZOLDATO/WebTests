import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_TEXT = 'Введите логин'
EMPTY_PASSWORD_TEXT = 'Введите пароль'

@allure.suite("Проверка формы авторизации")
@allure.title("Проверка появления ошибки при пустой форме авторизации")
def test_empty_login_and_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_TEXT

@allure.suite("Проверка формы авторизации")
@allure.title("Проверка появления ошибки при пустом поле с паролем")
def test_empty_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.input_login_field("test@yandex.ru")
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_PASSWORD_TEXT
