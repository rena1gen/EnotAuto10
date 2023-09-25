import time

import configs.authData
from pages.AuthPage import AuthPage
from pages.KassaPage import KassaPage


def test_switch_unswitch_payments_methods(browser, auth_process):
    kp = KassaPage(browser, "https://cabinet.enot.io/shop/dd067645-e4a9-44ec-95da-8494b2c5752d/payment-ways")
    kp.open()
    time.sleep(2)
    kp.payment_method_page_unswitch_and_switch_payments_methods()
    time.sleep(1)