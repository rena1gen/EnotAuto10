import time

from pages.BasePage import BasePage

from Locartors.TransactionPageLocators import TransactionPageLocators as Locator


class TransactionPage(BasePage):

    def __init__(self, driver, link):
        super().__init__(driver, link)


    def fill_search_input_and_find(self, req):
        self.element_is_visible(Locator.SEARCH_INPUT).send_keys(req)
        time.sleep(2)


    def transaction_block_title(self):
        return self.element_is_visible(Locator.TRANSACTION_BLOCK_TITLE).text



    def transaction_title(self):
        return self.element_is_visible(Locator.TRANSACTION_BLOCK).text



    def click_to_transaction_block(self):
        self.element_is_visible(Locator.TRANSACTION_BLOCK).click()
        time.sleep(2)


    def click_export_button_and_send_report(self, email):
        pass

    def click_to_resp_code(self):
        self.element_is_visible(Locator.TRANSACTION_BLOCK).click()
        time.sleep(3)
        btn = self.element_is_visible(Locator.RESPONSE_CODE_BTN).click()
        btn.click()



