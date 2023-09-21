from selenium.webdriver.common.by import By


class FilterModule:

    def __init__(self, driver):
        self.driver = driver

    b_create_status = '_tagName_3eklf_38'
    f_create_status = 'class="_label_1z0hv_35"'
    f_paid_status = '//*[@id="root"]/div/div/div/div/section[2]/div/div[1]/div/ul/li[3]/div/span'
    f_error_status = '//*[@id="root"]/div/div/div/div/section[2]/div/div[1]/div/ul/li[4]/div/div'
    f_expired_status = '//*[@id="root"]/div/div/div/div/section[2]/div/div[1]/div/ul/li[5]/div/div'
    def click_to_status_block(self):
        self.driver.find_element(By.CLASS_NAME, '_selectWrapper_5gw9h_22').click()

    def get_f_create_status_text(self):
        return self.driver.find_element(By.CLASS_NAME, self.f_create_status).text

    def click_to_create_status(self):
        self.click_to_status_block()
        self.driver.find_element(By.CLASS_NAME, self.f_create_status).click()
        self.click_apply_button()

    def click_apply_button(self):
        self.driver.find_element(By.XPATH,
                                 '//*[@id="root"]/div/div/div/div/section[2]/div/div[6]/button[1]/div').click()

    def click_to_paid_status(self):
        self.click_to_status_block()
        self.driver.find_element(By.XPATH, self.f_paid_status).click()
        self.click_apply_button()

    def click_to_error_status(self):
        self.click_to_status_block()
        self.driver.find_element(By.XPATH, self.f_error_status).click()
        self.click_apply_button()

    def click_to_expired_status(self):
        self.click_to_status_block()
        self.driver.find_element(By.XPATH, self.f_expired_status).click()
        self.click_apply_button()




