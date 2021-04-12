from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy

from pageobjects.Base import Base


class CodePathHome(Base):


    chapterFundametals = (MobileBy.XPATH, "//*[@text='Chapter 1: App Fundamentals']")
    chapterUserInteractions = (MobileBy.XPATH, "//*[@text='Chapter 4: User Interactions']")

    def __init__(self, driver):
        super().__init__(driver)

    def clickChapterFundamentals(self):
        self.waitForElementVisibility(CodePathHome.chapterFundametals).click()

    def clickChapterUserInteractions(self):
        self.waitForElementVisibility(CodePathHome.chapterUserInteractions).click()