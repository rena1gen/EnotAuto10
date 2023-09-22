import time

from pages.RegistrationPage import RegistrationPage


def test_smoke_testing_exist_user_registration(browser):

    reg = RegistrationPage(browser, 'https://cabinet.enot.io/registration')
    reg.open()
    time.sleep(2)
    reg.smoke_test_reg_process('SUSUS@mail.ru', '1213pppaS!', '1213pppaS!')
    time.sleep(2)
    exist_title = reg.get_already_exist_text()
    time.sleep(1)
    assert exist_title == "Пользователь уже существует"
    print("Тест кейс пройден")


def test_new_user_registration(browser):
    reg = RegistrationPage(browser, 'https://cabinet.enot.io/registration')
    reg.open()
    time.sleep(2)
    reg.smoke_test_reg_process('adninadni10@mail.ru', '1213pppaS!', '1213pppaS!')
    time.sleep(5)
    page_title = reg.get_accept_email_text()
    assert page_title == "Подтвердите email"
    print("Тест кейс пройден")




