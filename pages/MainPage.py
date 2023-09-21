from pages.BasePage import BasePage
from Locartors.MainPageLocators import MainPageLocators as Locator

class MainPage(BasePage):

    def __init__(self, driver, link):
        super().__init__(driver, link)


    def click_to_analytics_btn(self):
        self.element_is_visible(Locator.ANALYTICS_BTN).click()

    def click_to_active_kassa(self):
        self.element_is_visible(Locator.ACTIVE_KASSA).click()

    def click_to_disabled_kassa(self):
        self.element_is_visible(Locator.DISABLED_KASSA).click()

    def click_to_blocked_kassa(self):
        self.element_is_visible(Locator.BLOCKED_KASSA).click()

    def click_to_connect_site_btn(self):
        self.element_is_visible(Locator.CONNECT_SITE_BTN).click()

    def click_to_go_to_kassa_btn(self):
        self.element_is_visible(Locator.GO_TO_KASSA_BTN).click()

    def click_to_balance_btn(self):
        self.element_is_visible(Locator.BALANCE_BTN).click()

    def get_balance(self):
        b = self.element_is_visible(Locator.BALANCE_BTN)
        b_text = b.text
        return b_text

    def get_available_balance(self):
        self.click_to_balance_btn()
        b = self.element_is_visible(Locator.AVAILABLE_BALANCE_INFO)
        b_t = b.text
        return b_t

    def get_freeze_balance(self):
        self.click_to_balance_btn()
        b = self.element_is_visible(Locator.FREEZE_BALANCE_INFO)
        b_t = b.text
        return b_t

    def click_to_acc_icon(self):
        self.element_is_visible(Locator.ACC_ICON_BTN).click()

    def click_to_acc_exit_btn(self):
        self.click_to_acc_icon()
        self.element_is_visible(Locator.EXIT_ACC_BTN).click()

    def click_to_acc_settings_btn(self):
        self.click_to_acc_icon()
        self.element_is_visible(Locator.ACC_SETTINGS_BTN).click()

    def click_to_doc_btn(self):
        self.click_to_acc_icon()
        self.element_is_visible(Locator.DOC_BTN)


    def click_to_create_payment_btn(self):

        self.element_is_visible(Locator.BALANCE_BTN).click()
        self.element_is_visible(Locator.CREATE_PAYMENT_BTN).click()

    def create_payment_modal_title(self):
        payment_modal_title = self.element_is_visible(Locator.PAYMENT_MODAL_TITLE)
        payment_modal_title_text = payment_modal_title.text
        return payment_modal_title_text

    def get_common_balance(self):
        common_balance = self.element_is_visible(Locator.COMMON_BALANCE_INFO)
        common_balance_text = common_balance.text
        return common_balance_text






