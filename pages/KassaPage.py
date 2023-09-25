import time

from selenium.common.exceptions import NoSuchFrameException
from pages.BasePage import BasePage
from Locartors.KassaPageLocators import KassaPageLocators as Locators


class KassaPage(BasePage):

    def __init__(self, driver, link):
        super().__init__(driver, link)


    def payment_method_page_unswitch_and_switch_payments_methods(self):
        switches = self.elements_are_visible(Locators.SWITCH_BTN)

        for btn in switches:
            time.sleep(1)
            btn.click()

        self.element_is_visible(Locators.SAVE_CHANGES_BTN).click()

    def commission_block_is_visible(self):
        try:
            self.element_is_visible(Locators.COMMISSION_BLOCK_1)

        except NoSuchFrameException:
            return False

        return True




