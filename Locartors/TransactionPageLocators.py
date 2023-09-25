from selenium.webdriver.common.by import By

class TransactionPageLocators:

    SEARCH_INPUT = (By.CLASS_NAME, '_input_1i8ph_1')
    TRANSACTION_BLOCK = (By.CLASS_NAME, '_serviceName_dmrhq_45')
    RESPONSE_CODE_BTN = (By.TAG_NAME, 'button')
    RESEND_HTTP_BTN = (By.XPATH, '//*[@id="modal-container"]/div/div/div/div/div[2]/div[3]/div[1]/div/button')
    SEE_DETAILS_BTN = (By.XPATH, '//*[@id="modal-container"]/div/div/div/div/div[2]/div[4]/div/div/div[1]/span')

    STATUS_TEXT = (By.CLASS_NAME, '_status_text_7d1ze_1')

    TRANSACTION_TITLE = (By.CLASS_NAME, '_serviceName_ie3ta_47')

    TRANSACTION_BLOCK_TITLE = (By.CLASS_NAME, '_serviceName_dmrhq_45')


    EXPORT_BUTTOM = (By.XPATH, '//*[@id="root"]/div/div/div/div/section[2]/div/div[6]/button[2]')




