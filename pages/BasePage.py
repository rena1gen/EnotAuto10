from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import configs.authData
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver, link):
        self.driver = driver
        self.link = link

    def open(self):
        self.driver.get(self.link)

    def get_page_title(self):
        title = self.driver.title
        return title

    def get_current_url(self):
        return self.driver.current_url

    def get_screenshot(self, file_name):
        self.driver.get_screenshot_as_file(file_name)

    def element_is_visible(self, locator):
        return WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))

    def get_text(self, element):
        return element.text


    # def get_auth(self):
    #
    #    self.driver.find_element(By.CLASS_NAME, "_floatingInput_1jqa2_68").send_keys(configs.authData.email)
    #    self.driver.find_element(By.CSS_SELECTOR, "[type='password']").send_keys(configs.authData.password)
    #    self.driver.find_element(By.CLASS_NAME, "_group_iwcsa_23").click()



