import unittest
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


class testalert(unittest.TestCase):
    driver = webdriver.Chrome()

    def SetUp(self):
        self.driver.get('http://suninjuly.github.io/math.html')



    def testsome(self):
        self.driver.get('http://suninjuly.github.io/alert_accept.html')
        self.driver.find_element_by_css_selector('.btn').click()
        confirm = self.driver.switch_to.alert
        confirm.accept()
        x = self.driver.find_element_by_css_selector('#input_value').text
        y = calc(x)
        self.driver.find_element_by_css_selector('#answer').send_keys(y)
        self.driver.find_element_by_css_selector('.btn').click()
        time.sleep(5)


    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()