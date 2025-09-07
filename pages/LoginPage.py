from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_ENTER_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGON_FIELD = (By.ID, 'field_email')
    LOGIN_PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    LOGIN_RESET_PASS_LINK = (By.XPATH, '//*[@data-l="t,restore"]')
    LOGIN_REGISTER_BUTTON = (By.CLASS_NAME, 'button-pro __sec mb-3x __wide')
    LOGIN_WITH_VK = (By.CLASS_NAME, 'i ic social-icon __s __vk_id')
    LOGIN_WITH_MAILRU = (By.CLASS_NAME, 'i ic social-icon __s __mailru')
    LOGIN_WITH_YANDEX = (By.CLASS_NAME, 'i ic social-icon __s __yandex')


class LoginPageHelper(BasePage):
    pass
