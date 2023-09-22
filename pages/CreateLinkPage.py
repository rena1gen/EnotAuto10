from Locartors.PayFormLocators import PayFormLocators as Locator
from pages.BasePage import BasePage


class CreatePayFormPage(BasePage):
    def __init__(self, driver, link):
        super.__init__(driver, link)


    def createPayLink_rub(self, name, sum):
        self.element_is_visible(Locator.PAYFORM_CREATE_INPUT).send_keys(name)
        self.element_is_visible(Locator.PAYFORM_CREATE_INPUT_SUM).send_keys(sum)

