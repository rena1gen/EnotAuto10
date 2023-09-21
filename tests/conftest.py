import selenium
from selenium.webdriver import Chrome
import pytest


@pytest.fixture()
def browser():
    driver = selenium.webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
