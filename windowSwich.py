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
        self.driver.get('http://suninjuly.github.io/redirect_accept.html')
        self.driver.find_element_by_css_selector('.trollface').click()
        new_window = self.driver.window_handles[1] # 0/1/2/3 - номера окон
        self.driver.switch_to.window(new_window) # переключение между окнами
        time.sleep(4)
        x = self.driver.find_element_by_css_selector('#input_value').text
        y = calc(x)
        self.driver.find_element_by_css_selector('#answer').send_keys(y)
        self.driver.find_element_by_css_selector('.btn').click()
        time.sleep(5)


    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()