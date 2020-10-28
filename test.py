import unittest
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


class testMath(unittest.TestCase):
    driver = webdriver.Chrome()

    def SetUp(self):
        self.driver.get('http://suninjuly.github.io/math.html')



    def testsom(self):
        self.driver.get('http://suninjuly.github.io/get_attribute.html')
        time.sleep(3)
        x_element = self.driver.find_element_by_css_selector('#treasure')
        x = x_element.get_attribute('valuex')
        y = calc(x)
        self.driver.find_element_by_css_selector('#answer').send_keys(y)
        self.driver.find_element_by_css_selector('#robotCheckbox').click()
        self.driver.find_element_by_css_selector('#robotsRule').click()
        self.driver.find_element_by_css_selector('.btn').click()


    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()