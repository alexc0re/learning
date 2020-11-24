import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import random




class OfferTest(unittest.TestCase):
    driver = webdriver.Firefox()

    @classmethod  # Позволяет делать несколько тестов в классе
    def setUpClass(cls):
        cls.driver.get("http://bitcoinsera.dev8.leaddist.team?ip=89.105.202.69")
        cls.driver.implicitly_wait(5)
        cls.driver.find_element_by_css_selector('.col-md-12').is_displayed()
        cls.driver.execute_script("window.scrollBy(0, 100);")

    def test_02_ipDetect(self):  # Проверка определения Ip адреса
        phone = self.driver.find_element_by_css_selector('#reg-form1-phone_number')
        numb = phone.get_attribute('placeholder')
        assert numb == '6 12345678'

    def test_01_widget(self):  # BTC виджет
        self.driver.find_element_by_css_selector('#btc-widget').is_displayed()

    def test_03_registration(self):
        namefield = self.driver.find_element_by_css_selector('#reg-form1-first_name')
        surnamefield = self.driver.find_element_by_css_selector('#reg-form1-last_name')
        emailfield = self.driver.find_element_by_css_selector('#reg-form1-email')
        phonefield = self.driver.find_element_by_css_selector('#reg-form1-phone_number')
        # fill fields
        namefield.send_keys('Test')
        surnamefield.send_keys('Test')
        emailfield.send_keys("test_" + datetime.now().strftime("%m.%d.%Y_%H.%M.%S") + "@qa.team")
        phonefield.send_keys("02000000{}".format(random.randint(10, 99)))
        btn = self.driver.find_element_by_css_selector('#reg-form1-btn')
        self.driver.execute_script("window.scrollBy(0, 100);")
        btn.click()
        phoneerror = self.driver.find_element_by_css_selector('p.help-block:nth-child(2)')
        if phoneerror.is_displayed():
            try:
                phonefield.click()
                phonefield.send_keys(Keys.COMMAND + "a")
                phonefield.send_keys(Keys.BACKSPACE)
                phonefield.send_keys("02000001{}".format(random.randint(10, 99)))
            finally:
                self.driver.find_element_by_css_selector('#reg-form1-btn').click()


    def test_04_regcomp(self):
     btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-wrapper > a:nth-child(1)'))).click()
     btn.click()


    def test_05_broker(self):
        brokermsg = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.buttons > button:nth-child(1)')))
        self.driver.execute_script("window.scrollBy(0, 100);")
        brokermsg.click()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":

    unittest.main()
