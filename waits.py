import unittest
from selenium import webdriver
import math
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


class testwaits(unittest.TestCase):
    driver = webdriver.Chrome()

    def SetUp(self):
        self.driver.get('http://suninjuly.github.io/math.html')



    def testsome(self):
        self.driver.get('http://suninjuly.github.io/explicit_wait2.html')
        prise = WebDriverWait(self.driver ,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#price'),"100"))
        self.driver.find_element_by_css_selector('#book').click()
        x = self.driver.find_element_by_css_selector('#input_value').text
        y = calc(x)
        self.driver.find_element_by_css_selector('#answer').send_keys(y)
        self.driver.find_element_by_css_selector('#solve').click()
        time.sleep(5)




    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
 unittest.main()