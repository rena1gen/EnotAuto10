from selenium.webdriver.common.by import By
class PayFormLocators:




    #ПРОЦЕСС ОЦЕНКИ ПЕЙФОРМЫ
    RATE_BTN = (By.CLASS_NAME, '_buttonWrapper_12jlg_130')
    RATE_TITLE = (By.CLASS_NAME, '_title_1c25v_143')
    RATE_STARS = (By.CLASS_NAME, 'css-ykqdxu')

    SEND_COMNET_INPUT = (By.ID, 'outlined-textarea')

    SEND_RATE_BTN = (By.CLASS_NAME, '_button_1c25v_278')

    RATE_COMMENT = (By.CSS_SELECTOR, '[role="button"]')


    SWITCH_LANG_BTN = (By.XPATH, '//*[@id="root"]/div/div/footer/div/div/div/div/button')
    ENG_BTN = (By.CLASS_NAME, 'dropdown__item')

    PAYMENT_DETAILS_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/button')
    PAYMENT_DETAILS_CONTENT = (By.CLASS_NAME, '_headerTitle_b1rsw_137')

    #Оплата картой
    PAYS_METHODS_TITLE = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/div[1]/div[1]/h2')
    CARD_NUM_INPUT = (By.ID, "cardNumber")
    CARD_EXP_INPUT = (By.ID, "cardExpire")
    CARD_CVV_INPUT = (By.ID, 'cardCvv')
    PAY_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/button')

    #PERFECT MONEY

    PM_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div/div/button[2]')
    USD_PAY_BTN = (By.CSS_SELECTOR, "[value='USD']")
    EUR_PAY_BTN = (By.CSS_SELECTOR, "[value='EUR']")


    #YOOMONEY

    YOOMONEY_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div/div/button[3]')
    YOO_MONEY_PAY_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/div[1]/form/button')

    #CRYPTOPAY

    CRYPTO_ARR = []
    BTC_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div/div/button[4]')
    ETH_BTN = (By.XPATH, ' //*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div/div/button[5]')
    TRC20_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div/div/button[6]')
    ERC20_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div/div/button[7]')
    LTC_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div/div/button[8]')
    TON_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div/div/button[9]')
    TRX_BTN = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[1]/div[2]/div/div/div/button[10]')

    CRYPTO_ARR.append(BTC_BTN)
    CRYPTO_ARR.append(ETH_BTN)
    CRYPTO_ARR.append(TRC20_BTN)
    CRYPTO_ARR.append(ERC20_BTN)
    CRYPTO_ARR.append(LTC_BTN)
    CRYPTO_ARR.append(TON_BTN)
    CRYPTO_ARR.append(TRX_BTN)











