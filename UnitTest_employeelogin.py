import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class waves_Test8(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_employeelogin(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://wavesfit.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li[2]/a/b').click()
        #time.sleep(0.5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("SamRuth")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("sam1")
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/div/form/p[3]/input').click()
        time.sleep(2)
        try:
            time.sleep(2)
            elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li[1]/a/b')
            assert True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()