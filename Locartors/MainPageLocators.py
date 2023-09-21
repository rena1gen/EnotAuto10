from selenium.webdriver.common.by import By

class MainPageLocators:

    ANALYTICS_BTN = (By.XPATH, '//*[@id="root"]/div/div/section[1]/div[1]/button/div/div/a')

    ACTIVE_KASSA = (By.XPATH, '//*[@id="root"]/div/div/section[2]/div[2]/a[1]/div')

    BLOCKED_KASSA = (By.XPATH, '//*[@id="root"]/div/div/section[2]/div[2]/a[4]')

    DISABLED_KASSA = (By.XPATH, '//*[@id="root"]/div/div/section[2]/div[2]/a[6]')

    CONNECT_SITE_BTN = (By.XPATH, '//*[@id="root"]/div/div/section[2]/div[2]/a[35]')

    GO_TO_KASSA_BTN = (By.XPATH, '//*[@id="root"]/div/div/section[2]/div[1]/button/div')

    BALANCE_BTN = (By.XPATH, '//*[@id="root"]/div/header/div/div/div[1]/div[3]/nav/ul/div[1]/div/button')

    AVAILABLE_BALANCE_INFO = (By.XPATH, '//*[@id="root"]/div/header/div/div/div[1]/div[3]/nav/ul/div[1]/div/div/div/div/div/div/div[1]/span')

    FREEZE_BALANCE_INFO = (By.XPATH, '//*[@id="root"]/div/header/div/div/div[1]/div[3]/nav/ul/div[1]/div/div/div/div/div/div/div[3]/span')

    ACC_ICON_BTN = (By.XPATH, '//*[@id="root"]/div/header/div/div/div[1]/div[3]/nav/ul/div[2]/div/button')
    EXIT_ACC_BTN = (By.XPATH, '//*[@id="root"]/div/header/div/div/div[1]/div[3]/nav/ul/div[2]/div/div/div/button/p')
    ACC_SETTINGS_BTN = (By.XPATH, '//*[@id="root"]/div/header/div/div/div[1]/div[3]/nav/ul/div[2]/div/div/div/a[1]')
    DOC_BTN = (By.XPATH, '//*[@id="root"]/div/header/div/div/div[1]/div[3]/nav/ul/div[2]/div/div/div/a[2]')
    CREATE_PAYMENT_BTN = (By.XPATH, '//*[@id="root"]/div/header/div/div/div[1]/div[3]/nav/ul/div[1]/div/div/div/div/button')
    PAYMENT_MODAL_TITLE = (By.XPATH, '//*[@id="modal-container"]/div/div/div/div/div[2]/div/div/div[1]/div[1]/span')
    COMMON_BALANCE_INFO = (By.XPATH, '//*[@id="root"]/div/header/div/div/div[2]/div/div/span[1]')