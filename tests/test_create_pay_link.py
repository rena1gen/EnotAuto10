import time

import configs.authData
from pages.AuthPage import AuthPage
from pages.CreateLinkPage import CreatePayFormPage


def test_1(browser):

    a = AuthPage(browser, 'https://cabinet.enot.io/shop/dd067645-e4a9-44ec-95da-8494b2c5752d/widgets')
    cpp = CreatePayFormPage(browser, 'https://cabinet.enot.io/shop/dd067645-e4a9-44ec-95da-8494b2c5752d/widgets')
    a.open()
    time.sleep(3)
    a.fill_inputs_and_login(configs.authData.email, configs.authData.password)
    time.sleep(3)
    cpp.open()
    time.sleep(5)
    cpp.createPayLink_rub("тестовый платеж", 100)
    time.sleep(5)

