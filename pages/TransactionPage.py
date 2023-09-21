from pages.BasePage import BasePage
from pages.FilterModule import FilterModule
from Locartors.TransactioPageLocators import TransactionPageLocators as Locators

class TransactionPage(BasePage, FilterModule):

    def __init__(self, driver, link):
        super().__init__(driver, link)


    def get_block_status_text(self):
        return self.element_is_visible(Locators.CREATE_STATUS).text


