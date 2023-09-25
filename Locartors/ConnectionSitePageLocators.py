from selenium.webdriver.common.by import By

class ConnectionSitePageLocators:

    SITE_NAME_INPUT = (By.NAME, 'siteName')
    SITE_ADRESS_INPUT = (By.NAME, 'domain')
    SITE_CONNECT_CHECKBOX = (By.CLASS_NAME, '_optionPeriodIcon_mki7m_1')

    SITE_DESC_INPUT = (By.CLASS_NAME, '_floatingTextarea_11ubp_14')

    SITE_CONNECTION_BTN = (By.CSS_SELECTOR, '[type="submit"]')

    REQRUITMENTS_BTN = (By.CLASS_NAME, '_linkWithLine_jfzvr_46')

    HTTP_BTN = ()
