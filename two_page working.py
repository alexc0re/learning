import pytest
from selenium import webdriver
from links import links
from links import links_dev8
import time
from datetime import datetime
import random


class Test_offers():


    @classmethod
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        return self.driver


    def test_pages(self):
        i = 0
        link = links_dev8()
        while i < len(link):
            self.driver.get("http://" + link[i])
            url = self.driver.current_url
            if url.__contains__("sign-up"):
                ##ONE PAGE TEST
                try:
                    try:
                        self.driver.execute_script("window.scrollBy(0, 100);")
                        self.driver.find_element_by_css_selector("#reg-form-btn").click()
                        time.sleep(5)
                        print(link[i] + "one")
                        i += 1
                    except:
                        self.driver.execute_script("window.scrollBy(0, 100);")
                        self.driver.find_element_by_css_selector("#reg-form1-btn").click()
                        time.sleep(5)
                        print(link[i] + "one")
                        i += 1
                except:
                    print("Something wrong with " + link[i])
                    i += 1
                    continue
            else:
                try:
                    try:
                        self.driver.find_element_by_css_selector("#optin-form-first_name").send_keys("test")
                        self.driver.find_element_by_css_selector("#optin-form-email").send_keys(
                            "test_" + datetime.now().strftime("%m.%d.%Y_%H.%M.%S") + "@qa.team")
                        self.driver.find_element_by_css_selector("#optin-form-btn").click()
                        self.driver.find_element_by_css_selector("#reg-form-btn").click()
                        time.sleep(5)
                        print(link[i] + "two")
                        i += 1
                    except:
                        self.driver.find_element_by_xpath('(//*[@id="optin-form-first_name"])[2]').send_keys("test")
                        self.driver.find_element_by_xpath('(//*[@id="optin-form-email"])[2]').send_keys("test_" + datetime.now().strftime("%m.%d.%Y_%H.%M.%S") + "@qa.team")
                        self.driver.find_element_by_xpath('(//*[@id="optin-form-btn"])[2]').click()
                        self.driver.find_element_by_css_selector("#reg-form-btn").click()
                        time.sleep(5)
                        print(link[i] + "two")
                        i += 1

                except:
                    print("Something wrong with " + link[i])
                    i += 1
                    continue
    @classmethod
    def teardown_method(self):
        print("quit browser for test..")
        self.driver.quit()


if __name__ == "__main__":
 pytest.main()
