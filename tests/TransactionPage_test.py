import time

import configs.authData
from pages.AuthPage import AuthPage
from pages.TransactionPage import TransactionPage



def test_search_input(browser, auth_process):
    tp = TransactionPage(browser, "https://cabinet.enot.io/transactions")
    tp.open()
    tp.fill_search_input_and_find("122")


def test_click_to_transaction_block(browser, auth_process):
    tp = TransactionPage(browser, "https://cabinet.enot.io/transactions")
    tp.open()
    tp.click_to_transaction_block()

    trans_block_title = tp.transaction_block_title()
    transaction_title = tp.transaction_title()

    assert trans_block_title == transaction_title
    print("TEST CASE IS PASSED")


def test_click_to_reps_code(browser, auth_process):
    tp = TransactionPage(browser, "https://cabinet.enot.io/transactions")
    tp.open()
    tp.click_to_transaction_block()
    tp.click_to_resp_code()
    title = tp.get_page_title()
    print(title)

