from selenium import webdriver
import unittest
import time

class testAssert(unittest.TestCase):

    # Ваш код, который заполняет обязательные поля
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_assert1(self):
        driver = self.driver
        link = "http://suninjuly.github.io/registration1.html"
        self.driver.get(link)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//label[contains(text(),'First name*')]/..").is_displayed()
        namefield = self.driver.find_element_by_css_selector('.first_block > div:nth-child(1) input')
        namefield.send_keys('Test')
        self.driver.find_element_by_xpath("//label[contains(text(),'Last name*')]/..").is_displayed()
        surnamefield = self.driver.find_element_by_css_selector('.first_block > div:nth-child(2) > input')
        surnamefield.send_keys('Test')
        self.driver.find_element_by_xpath("//label[contains(text(),'Email*')]/..").is_displayed()
        emailfield = self.driver.find_element_by_css_selector('.first_block > div:nth-child(3) input')
        emailfield.send_keys("test@qa.team")

        # Отправляем заполненную форму
        button = self.driver.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(4)
        welcome_text_elt = self.driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
