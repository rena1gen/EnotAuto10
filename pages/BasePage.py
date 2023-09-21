from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, link):
        self.driver = driver
        self.link = link

    def open(self):
        self.driver.get(self.link)

    def get_page_title(self):
        title = self.driver.title
        return title

    def get_screenshot(self, file_name):
        self.driver.get_screenshot_as_file(file_name)

    def element_is_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))


