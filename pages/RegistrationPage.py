import time

from pages.BasePage import BasePage
from Locartors.RegistrationPageLocators import RegistrationPageLocators as Locators

class RegistrationPage(BasePage):

    def __init__(self, driver, link):
        super().__init__(driver, link)


    def smoke_test_reg_process(self, email, password1, password2):

        self.element_is_visible(Locators.EMAIL_INPUT).send_keys(email)
        time.sleep(1)
        self.element_is_visible(Locators.PASSWORD_INPUT).send_keys(password1)
        time.sleep(1)
        self.element_is_visible(Locators.PASSWORD_REPEAT_INPUT).send_keys(password2)
        self.element_is_visible(Locators.REG_BTN).click()
        time.sleep(5)


    def get_already_exist_text(self):
        time.sleep(2)
        return self.element_is_visible(Locators.ALREADY_EXIST_MODAL).text


    def get_email_incorrect_format_msg(self):
        return self.element_is_visible(Locators.EMAIL_INCORRECT_FORMAT_MSG).text

    def get_accept_email_text(self):
        return self.element_is_visible(Locators.ACCEPT_EMAIL_TEXT).text


    def go_to_login_page(self):
        self.element_is_visible(Locators.LOGIN_BTN).click()




