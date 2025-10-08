import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=ru")
    driver = webdriver.Remote(command_executor="http://84.54.30.146:4444", options=options)
    yield driver
    if driver:
        driver.quit()
