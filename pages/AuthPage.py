from pages.BasePage import BasePage
from Locartors.AuthPageLocators import AuthPageLocators as Locator


class AuthPage(BasePage):

    def __init__(self, driver, link):
        super().__init__(driver, link)

    # LOCATORS

    def fill_inputs_and_login(self, email, password):

        self.element_is_visible(Locator.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(Locator.PASSWORD_INPUT).send_keys(password)
        self.element_is_visible(Locator.AUTH_BUTTON).click()

    def click_to_reg_button(self):
        self.element_is_visible(Locator.REG_BTN).click()

    def get_error_auth_text(self):
        e = self.element_is_visible(Locator.ERROR_AUTH)
        return e.text

    def get_email_format_error(self):
        em = self.element_is_visible(Locator.ERROR_EMAIL)
        return em.text

    def click_to_chat_button(self):
        self.element_is_visible(Locator.CHAT_BUTTON).click()


    def get_chat_modal_title(self):
        title = self.element_is_visible(Locator.CHAT_MODAL_TITLE)
        return title.text

    def send_message_to_chat(self, message):
        message = self.element_is_visible(Locator.CHAT_MESSAGE_INPUT).send_keys(message)
        self.element_is_visible(Locator.CHAT_MESSAGE_SEND_BTN).click()


    def get_message_text(self):

        return self.element_is_visible(Locator.MESSAGE_CONTENT).text





