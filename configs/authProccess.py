import time

import pytest

import configs.authData
from pages.AuthPage import AuthPage


@pytest.fixture
def auth_process(browser):
    a = AuthPage(browser, "https://cabinet.enot.io/login")
    a.open()
    time.sleep(2)
    a.fill_inputs_and_login(configs.authData.email, configs.authData.password)
