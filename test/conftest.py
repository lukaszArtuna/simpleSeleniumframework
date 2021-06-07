import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

from config import base_url
from site_access import site_user, user_password


@pytest.fixture()
def setup(request):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # driver = webdriver.Remote(command_executor='http://xxxxx/wd/hub',
    #                           desired_capabilities=DesiredCapabilities.FIREFOX,
    #                           options=options)
    driver.get(base_url)
    driver.find_element(By.ID, "txtUsername").send_keys(site_user)
    driver.find_element(By.ID, "txtPassword").send_keys(user_password)
    driver.find_element(By.ID, "btnLogin").click()
    driver.implicitly_wait(20)
    driver.maximize_window()
    request.cls.driver = driver
    before_fail = request.session.testsfailed
    yield
    if request.session.testsfailed != before_fail:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()
