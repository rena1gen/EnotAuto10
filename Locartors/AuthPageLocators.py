from selenium.webdriver.common.by import By
import selenium


class AuthPageLocators:

    EMAIL_INPUT = (By.CLASS_NAME, "_floatingInput_1jqa2_68")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[type='password']")
    AUTH_BUTTON = (By.CLASS_NAME, "_group_iwcsa_23")

    ERROR_AUTH = (By.CLASS_NAME, "_error_qz7jq_1")

    ERROR_EMAIL = (By.XPATH, "//*[@id='root']/div/section/div[1]/div/form/div[1]/div[2]/p")

    CHAT_BUTTON = (By.ID, "uw-main-button")

    CHAT_MODAL_TITLE = (By.XPATH, '//*[@id="usedesk-messenger"]/div/div[1]/div/div[1]/div/p')

    CHAT_MESSAGE_INPUT = (By.NAME, "message")

    CHAT_MESSAGE_SEND_BTN = (By.ID, "uw-message-submit-button")

    MESSAGE_CONTENT = (By.CLASS_NAME, "sc-fEXmlR KSlBc uw__chat-message__text")

    REG_BTN = (By.CLASS_NAME, "_link_181sc_61")



