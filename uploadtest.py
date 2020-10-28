import unittest
from selenium import webdriver
import os
import time

class testupload(unittest.TestCase):
    driver = webdriver.Chrome()

    def SetUp(self):
        self.driver.get('http://suninjuly.github.io/file_input.html')

    def testupload(self):
        self.driver.get('http://suninjuly.github.io/file_input.html')
        self.driver.find_element_by_css_selector('input.form-control:nth-child(2)').send_keys("Huillo")
        self.driver.find_element_by_css_selector('input.form-control:nth-child(4)').send_keys("Zalupovich")
        self.driver.find_element_by_css_selector('input.form-control:nth-child(6)').send_keys("ZalupovichHuillo@gmail.com")
        current_dir = os.path.abspath(
            os.path.dirname('/Users/alexcore/Desktop/NEMSHYLOV.txt'))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, 'NEMSHYLOV.txt')  # добавляем к этому пути имя файла
        self.driver.find_element_by_css_selector('#file').send_keys(file_path)
        self.driver.find_element_by_css_selector('.btn').click


    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()