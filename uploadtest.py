import unittest
from selenium import webdriver


class testupload(unittest.TestCase):
    driver = webdriver.Chrome()

    def SetUp(self):
        self.driver.get('http://suninjuly.github.io/file_input.html')

    def testupload(self):
        self.driver.get('http://suninjuly.github.io/file_input.html')


    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()