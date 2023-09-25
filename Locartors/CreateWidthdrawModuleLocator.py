from selenium.webdriver.common.by import By

class CreateWithdrawModuleLocators:


    CARD_INPUT = (By.ID, 'cardNumber')
    CONTINUE_CP_PROCCESS_BTN = (By.XPATH, '//*[@id="modal-container"]/div/div/div/div/div[2]/div/div/div[2]/div[1]/form/button')
    SUM_INPUT = (By.ID, 'filled-basic')
    COMISSION_CHECKBOX = (By.XPATH, '//*[@id="modal-container"]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[3]/div/div')
    COMMENT_INPUT = (By.CSS_SELECTOR, '[maxlength = "30"]')
    WITHDRAW_BTN = (By.XPATH, '//*[@id="modal-container"]/div/div/div/div/div[2]/div/div/div/div[2]/form/div[2]/button')
    CREATE_WITHDRAW_BTN = (By.CLASS_NAME, '_group_iwcsa_23')

    OTHER_WITHDRAW_METHODS = (By.CLASS_NAME, '_item_138h6_1')

    RETURN_BACK_BTN = (By.XPATH, '//*[@id="modal-container"]/div/div/div/div/div[2]/div/div/div/div[1]/div[1]/div/button')