import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class test_select(unittest.TestCase):
    driver = webdriver.Chrome()

    def test_sel(self):
        self.driver.get('http://suninjuly.github.io/selects1.html')
        x = self.driver.find_element_by_css_selector('#num1').text
        y = self.driver.find_element_by_css_selector('#num2').text
        char = int(x) + int(y)
        str(char)

        self.driver.find_element_by_css_selector('#dropdown').click()
        select = Select(self.driver.find_element_by_tag_name("select"))
        select.select_by_visible_text((str(char)))
        self.driver.find_element_by_css_selector('.btn').click()

if __name__ == "__main__":
        unittest.main()