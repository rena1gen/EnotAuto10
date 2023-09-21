import time

import configs.authData
from pages.AuthPage import AuthPage
from pages.TransactionPage import TransactionPage
from pages.FilterModule import FilterModule


def test_filter_transaction(browser):
    tp = TransactionPage(browser, "https://cabinet.enot.io/transactions")
    a = AuthPage(browser, "https://cabinet.enot.io/transactions")
    f = FilterModule(browser)
    a.open()
    time.sleep(3)
    a.fill_inputs_and_login(configs.authData.email, configs.authData.password)
    time.sleep(3)
    tp.open()
    time.sleep(3)
    f.click_to_create_status()
    f.click_to_paid_status()
    f.click_to_error_status()
    f.click_to_expired_status()

def test_create_status_check(browser):
    fp = FilterModule(browser)
    tp = TransactionPage(browser, "https://cabinet.enot.io/transactions")
    a = AuthPage(browser,  "https://cabinet.enot.io/transactions")
    a.open()
    time.sleep(4)
    a.fill_inputs_and_login(configs.authData.email, configs.authData.password)
    time.sleep(4)
    tp.open()
    time.sleep(4)
    fp.click_to_create_status()
    time.sleep(1)
    title = fp.get_f_create_status_text()
    block_title = tp.get_block_status_text()
    assert title == block_title
    print("Статусы совпадают")

