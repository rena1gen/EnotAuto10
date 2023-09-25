import time

import configs.sensData
from pages.CreateWithdrawModule import CreateWithdrawPage


def test_withdraw_smoke_test(browser, auth_process):
    wp = CreateWithdrawPage(browser, "https://cabinet.enot.io/payments")
    wp.open()
    wp.withdraw_process_to_card(configs.sensData.card_num, "160", "возврат денежный средств")
    time.sleep(2)


def test_withdraw_by_other_methods(browser, auth_process):
    wp = CreateWithdrawPage(browser, "https://cabinet.enot.io/payments")
    wp.open()
    wp.withdraw_by_other_methods()
    time.sleep(2)

