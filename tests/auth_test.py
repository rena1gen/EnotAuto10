import time

from pages.AuthPage import AuthPage


def test_open(browser):
    a = AuthPage(browser, "https://cabinet.enot.io")
    a.open()
    time.sleep(3)
    title = a.get_page_title()
    assert title == "Авторизация"
    print("PASSED")


def test_smoke_test_auth(browser):
    a = AuthPage(browser, "https://cabinet.enot.io")
    a.open()
    time.sleep(3)
    a.fill_inputs_and_login("vmbesh-test@mail.ru", "Easy777!")
    time.sleep(3)
    title = a.get_page_title()
    assert title == "Главная"

def test_negative_auth(browser):
    a = AuthPage(browser, "https://cabinet.enot.io")
    a.open()
    time.sleep(3)
    a.fill_inputs_and_login("vmbesh-test@mail.ru", "Eas777!")
    time.sleep(3)
    assert a.get_error_auth_text() == "Неверный логин или пароль"

def test_negative_email(browser):
    a = AuthPage(browser, "https://cabinet.enot.io")
    a.open()
    time.sleep(3)
    a.fill_inputs_and_login("vmbesh-testail.ru", "Eas777!")
    time.sleep(3)
    assert a.get_email_format_error() == "Неверный формат почты"


def test_click_to_reg_button(browser):
    a = AuthPage(browser, "https://cabinet.enot.io")
    a.open()
    time.sleep(3)
    a.click_to_reg_button()
    time.sleep(2)
    title = a.get_page_title()
    assert title == "Регистрация"
    print("TEST CASE IS PASSED")

def test_send_message_to_support_chat(browser):
    a = AuthPage(browser, "https://cabinet.enot.io")
    a.open()
    time.sleep(10)
    a.click_to_chat_button()
    time.sleep(2)
    assert a.get_chat_modal_title() == "Служба поддержки"
    print("Тест прошел")
    time.sleep(2)
    a.send_message_to_chat("тестовое сообщение")
    time.sleep(4)
    assert a.get_message_text() == "тестовое сообшение"









