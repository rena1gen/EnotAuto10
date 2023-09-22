from selenium.webdriver.common.by import By
class RegistrationPageLocators:


    ALREADY_EXIST_MODAL = (By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div/div/div/p')

    ACCEPT_EMAIL_TEXT = (By.XPATH, '//*[@id="root"]/div/section/div[1]/div/h1')

    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    PASSWORD_REPEAT_INPUT = (By.NAME, 'repeatPassword')

    REG_BTN = (By.CSS_SELECTOR, '[type="submit"]')


