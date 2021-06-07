from config import base_url
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        url = base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def wait_element_visible(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print("ELEMENT NOT FOUND WITHIN GIVEN TIME!")
            self.driver.quit()
