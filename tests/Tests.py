import unittest
from pageobjects.CodePathHomePage import CodePathHome
from webdriver.Webdriver import Driver


class CodePathTests(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def test_ChapterFundamentals(self):
        codePathHome = CodePathHome(self.driver)
        codePathHome.clickChapterFundamentals()

    def test_UserInteractions(self):
            codePathHome = CodePathHome(self.driver)
            codePathHome.clickChapterUserInteractions()


    def tearDown(self):
        self.driver.instance.quit()
