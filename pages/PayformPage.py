import time

from pages.BasePage import BasePage
from Locartors.PayFormLocators import PayFormLocators as Locator

class PayformPage(BasePage):

    def __init__(self, driver, link):
        super().__init__(driver, link)



    def get_pay_method_title(self):
        return self.element_is_visible(Locator.PAYS_METHODS_TITLE).text

    def check_rate_process(self):

        self.element_is_visible(Locator.RATE_BTN).click()
        arr = self.elements_are_visible(Locator.RATE_STARS)
        for element in arr:
            time.sleep(0.5)
            element.click()

        comment_arr = self.elements_are_visible(Locator.RATE_COMMENT)
        for element in comment_arr:
            time.sleep(1)
            element.click()

        self.element_is_visible(Locator.SEND_COMNET_INPUT).send_keys("Все круто!")
        time.sleep(5)
        self.element_is_visible(Locator.SEND_RATE_BTN).click()





    def switch_lang_to_eng(self):
        self.element_is_visible(Locator.SWITCH_LANG_BTN).click()
        self.element_is_visible(Locator.ENG_BTN).click()

    def get_payment_details_title(self):
        return self.element_is_visible(Locator.PAYMENT_DETAILS_CONTENT).text



    def click_to_payment_detais(self):
        self.element_is_visible(Locator.PAYMENT_DETAILS_BTN).click()

    def pay_by_card(self, card_num, expire, cvv):
        self.element_is_visible(Locator.CARD_NUM_INPUT).send_keys(card_num)
        self.element_is_visible(Locator.CARD_EXP_INPUT).send_keys(expire)
        time.sleep(5)
        self.element_is_visible(Locator.CARD_CVV_INPUT).send_keys(cvv)
        time.sleep(5)
        self.element_is_visible(Locator.PAY_BTN).click()

    def pay_by_PM_USD(self):
        self.element_is_visible(Locator.PM_BTN).click()
        self.element_is_visible(Locator.USD_PAY_BTN).click()
        self.element_is_visible(Locator.PAY_BTN).click()

    def pay_by_PM_EUR(self):
        self.element_is_visible(Locator.PM_BTN).click()
        self.element_is_visible(Locator.EUR_PAY_BTN).click()
        self.element_is_visible(Locator.PAY_BTN).click()

    def pay_by_YOOMONEY(self):
        self.element_is_visible(Locator.YOOMONEY_BTN).click()
        self.element_is_visible(Locator.YOO_MONEY_PAY_BTN).click()


    def pay_by_crypto(self):
        for elements in Locator.CRYPTO_ARR:
            self.element_is_visible(elements).click()
            time.sleep(1)





















