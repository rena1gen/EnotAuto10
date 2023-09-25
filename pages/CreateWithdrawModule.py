import time

from pages.BasePage import BasePage
from Locartors.CreateWidthdrawModuleLocator import CreateWithdrawModuleLocators as Locator


class CreateWithdrawPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)


    def withdraw_process_to_card(self, cardNum, sum, comment):
        self.element_is_visible(Locator.CREATE_WITHDRAW_BTN).click()
        self.element_is_visible(Locator.CARD_INPUT).send_keys(cardNum)
        time.sleep(2)
        self.element_is_visible(Locator.CONTINUE_CP_PROCCESS_BTN).click()
        self.element_is_visible(Locator.SUM_INPUT).send_keys(sum)
        time.sleep(2)
        self. element_is_visible(Locator.COMMENT_INPUT).send_keys(comment)
        time.sleep(2)
        self.element_is_visible(Locator.WITHDRAW_BTN).click()

    def withdraw_by_other_methods(self):
        self.element_is_visible(Locator.CREATE_WITHDRAW_BTN).click()
        btn_elements = self.elements_are_visible(Locator.OTHER_WITHDRAW_METHODS)

        for btn in btn_elements:
            btn.click()
            time.sleep(1)



