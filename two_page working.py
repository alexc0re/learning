import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import random
from links import links

class testwaits(unittest.TestCase):
    driver = webdriver.Firefox()
    def SetUp(self):
        self.driver.get('http://suninjuly.github.io/math.html')


    def testsome(self):
        self.driver.implicitly_wait(20)
        i = 0
        link = links()
        print(link)
        while i < len(link):
            self.driver.get(link[i])
            self.driver.find_element_by_css_selector("#optin-form-first_name").send_keys("test")
            self.driver.find_element_by_css_selector("#optin-form-email").send_keys("test_" + datetime.now().strftime("%m.%d.%Y_%H.%M.%S") + "@qa.team")
            self.driver.find_element_by_css_selector("#optin-form-btn").click()
            self.driver.find_element_by_css_selector("#reg-form-last_name").send_keys("test")
            self.driver.find_element_by_css_selector("#reg-form-phone_number").send_keys("19212345{}".format(random.randint(10, 99)))
            self.driver.find_element_by_css_selector("#reg-form-btn").click()
            self.driver.find_element_by_css_selector(".timer")

            print(str(i) + str(link[i]) + '_TEST PASS')

            i += 1


    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
 unittest.main()