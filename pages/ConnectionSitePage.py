from pages.BasePage import BasePage
from Locartors.ConnectionSitePageLocators import ConnectionSitePageLocators as Locators


class SiteConnectionPage(BasePage):


    def __init__(self, driver, link):
        super().__init__(driver, link)


    def fill_site_connection_inputs(self, sitename, domain_name, desc):

        self.element_is_visible(Locators.SITE_NAME_INPUT).send_keys(sitename)
        self.element_is_visible(Locators.SITE_ADRESS_INPUT).send_keys(domain_name)
        self.element_is_visible(Locators.SITE_DESC_INPUT).send_keys(desc)
        self.element_is_visible(Locators.SITE_CONNECTION_BTN).click()
