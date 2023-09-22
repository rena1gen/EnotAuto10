from selenium.webdriver.common.by import By

class CreatePayFormPageLocators:


    CREATE_BY_LINK_BTN = (By.XPATH, '//*[@id="root"]/div/div/div/div/form/div[1]/div[1]/div/button[3]')
    LINK_CHECKBOX = (By.CLASS_NAME, '_option__checkbox_1z0hv_18')
    PAYFORM_NAME = (By.CLASS_NAME, '_formItem_mksnf_4')
    PAYFROM_SUM = (By.XPATH, '//*[@id="root"]/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input')
    COPY_LINK_BTN = (By.CSS_SELECTOR, '[type="submit"]')
    LINK = (By.NAME, 'successWidgetModal')


