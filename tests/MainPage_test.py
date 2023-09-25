import time

import configs.authData
from pages.AuthPage import AuthPage
from pages.MainPage import MainPage


def test_click_to_analys_btn(browser, auth_process):
    mp = MainPage(browser, "https:///cabinet.enot.io/main")
    mp.open()
    time.sleep(3)
    mp.click_to_analytics_btn()
    time.sleep(2)
    title = mp.get_page_title()
    assert title == "Аналитика"
    print("Тест кейс пройден")


def test_click_to_active_kassa(browser):
    mp = MainPage(browser, "https:///cabinet.enot.io/main")
    mp.open()
    time.sleep(3)
    mp.click_to_active_kassa()
    time.sleep(3)
    title = mp.get_page_title()
    assert title == "Способ оплаты"

def test_click_to_blocked_kassa(browser, auth_process):
    mp = MainPage(browser, "https:///cabinet.enot.io/main")
    mp.open()
    time.sleep(3)
    mp.click_to_blocked_kassa()
    time.sleep(3)
    title = mp.get_page_title()
    assert title == "Касса заблокирована"
    print("Test is passed")

def test_click_to_disabled_kassa(browser):
    mp = MainPage(browser, "https:///cabinet.enot.io/main")
    mp.open()
    time.sleep(3)
    mp.click_to_disabled_kassa()
    time.sleep(3)
    title = mp.get_page_title()
    assert title == "Касса отклонена"

def test_connect_site_btn(browser):
    mp = MainPage(browser, "https:///cabinet.enot.io/main")
    mp.open()
    time.sleep(3)
    mp.click_to_connect_site_btn()
    time.sleep(3)
    title = mp.get_page_title()
    assert title == "Подключите свой сайт"

def test_click_go_to_kassa_btn(browser, auth_process):
    mp = MainPage(browser, "https:///cabinet.enot.io/main")
    mp.click_to_go_to_kassa_btn()
    time.sleep(3)
    title = mp.get_page_title()
    assert title == "Кассы"

def test_click_to_acc_exit_btn(browser, auth_process):
    mp = MainPage(browser, "https:///cabinet.enot.io/main")
    mp.open()
    time.sleep(2)
    mp.click_to_acc_exit_btn()
    time.sleep(3)
    title = mp.get_page_title()
    assert title == "Авторизация"

#тест кейс проверки соответсвия баланса [баланс = "замороженные средства + доступные средств]

def test_balance_is_correct(browser, auth_process):
    mp = MainPage(browser, "https:///cabinet.enot.io/main")
    time.sleep(3)
    balance = float(mp.get_balance()[:-1]) # удаляем символ рубля
    time.sleep(1)
    freeze_balance = float(mp.get_freeze_balance()[:-1])
    time.sleep(1)
    available_balance = float(mp.get_available_balance()[:-1])

    assert available_balance + freeze_balance == round(balance, 1)
    print("Баланс соотвествует")

def test_create_payment_btn(browser, auth_process):
    mp = MainPage(browser, "https:///cabinet.enot.io/main")
    mp.open()
    time.sleep(2)
    mp.click_to_create_payment_btn()
    time.sleep(1)
    title = mp.create_payment_modal_title()
    time.sleep(1)
    assert title == "Создать выплату"


def test_common_balance_correspondence_and_balance_button(browser, auth_process):
    mp = MainPage(browser, "https:///cabinet.enot.io/main")
    time.sleep(4)
    common_balance = float(mp.get_common_balance()[:-1])
    time.sleep(1)
    balance_btn = float(mp.get_balance()[:-1])

    assert balance_btn == common_balance
    time.sleep(3)
    mp.get_screenshot("balance_screen")
    print("Значения балансов соответствует")



    






