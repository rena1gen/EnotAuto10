import configs.payform_link
from Locartors.CreatePayFormPageLocators import CreatePayFormPageLocators as Locator
from pages.BasePage import BasePage
from configs.payform_link import pay_link

class CreatePayFormPage(BasePage):
    def __init__(self, driver, link):
        super().__init__(driver, link)


    def createPayLink_rub(self, name, sum):

        self.element_is_visible(Locator.CREATE_BY_LINK_BTN).click()
        self.element_is_visible(Locator.LINK_CHECKBOX).click()
        self.element_is_visible(Locator.PAYFORM_NAME).send_keys(name)
        self.element_is_visible(Locator.PAYFROM_SUM).send_keys(sum)
        self.element_is_visible(Locator.COPY_LINK_BTN).click()
        link = self.element_is_visible(Locator.LINK)
        link_text = link.get_attribute
        configs.payform_link.pay_link = link_text



