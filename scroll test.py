import unittest
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


class testScroll(unittest.TestCase):
    driver = webdriver.Chrome()

    def SetUp(self):
        self.driver.get('http://suninjuly.github.io/execute_script.html')


    def testscroll(self):
        self.driver.get('http://suninjuly.github.io/execute_script.html')
        x = self.driver.find_element_by_css_selector('#input_value').text
        y = calc(x)
        self.driver.find_element_by_css_selector('#answer').send_keys(y)
        self.driver.execute_script("window.scrollBy(0, 100);")
        self.driver.find_element_by_css_selector('#robotCheckbox').click()
        self.driver.find_element_by_css_selector('#robotsRule').click()
        self.driver.find_element_by_css_selector('.btn').click()



    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()