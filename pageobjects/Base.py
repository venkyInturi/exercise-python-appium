from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver.instance, 30)


    def waitForElementVisibility(self, locator_by) :
        return self.wait.until(EC.visibility_of_element_located(locator_by))
