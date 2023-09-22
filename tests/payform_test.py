import time

import configs.sensData
import configs.payform_link
from pages.CreateLinkPage import CreatePayFormPage
from pages.PayformPage import PayformPage


def test_pay_by_card_test(browser):
    p = PayformPage(browser, configs.payform_link.pay_link)
    p.open()
    time.sleep(3)
    p.pay_by_card(configs.sensData.card_num, configs.sensData.expire_date, configs.sensData.cvv)
    time.sleep(3)
    title_payment = p.get_pay_method_title()
    assert title_payment == "Оплата картой"
    time.sleep(5)


def test_pm_usd(browser):
    p = PayformPage(browser, configs.payform_link.pay_link)
    p.open()
    time.sleep(5)
    p.pay_by_PM_USD()
    title = p.get_pay_method_title()
    assert title == "Perfect Money"
    time.sleep(5)
    print("Заголовок соотвествует")


def test_pm_eur(browser):
    p = PayformPage(browser, configs.payform_link.pay_link)
    p.open()
    p.pay_by_PM_EUR()
    time.sleep(4)
    title = p.get_pay_method_title()
    assert title == "Perfect Money"
    print("Заголовок соотвествует")

def test_pay_by_yoomoney(browser):
    p = PayformPage(browser, configs.payform_link.pay_link)
    p.open()
    p.pay_by_YOOMONEY()
    title = p.get_pay_method_title()
    assert title == "ЮMoney"
    print("Заголовок соотвествует")

def test_pay_by_crypto(browser):
    p = PayformPage(browser, configs.payform_link.pay_link)
    p.open()
    time.sleep(2)
    p.pay_by_crypto()

def test_click_to_payment_details(browser):
    p = PayformPage(browser, configs.payform_link.pay_link)
    p.open()
    p.click_to_payment_detais()
    payment_title = p.get_payment_details_title()
    assert payment_title == "Детали платежа"
    print("Заголовок соотвествует")


def test_switch_lang_test(browser):
    p = PayformPage(browser, configs.payform_link.pay_link)
    p.open()
    time.sleep(5)
    p.switch_lang_to_eng()
    time.sleep(5)
    title = p.get_pay_method_title()
    assert title == "Payment by card"
    print("Заголовок соотвествует")

def test_check_rate_process(browser):
    p = PayformPage(browser, configs.payform_link.pay_link)
    p.open()
    time.sleep(5)
    p.check_rate_process()













