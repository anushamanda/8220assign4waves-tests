import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class waves_Test5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_alreadyenrolled(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("https://wavesfit.herokuapp.com/")
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li[2]/a/b').click()
        #time.sleep(0.5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("MathewRodgers")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("mathew1")
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/div/div/div/div[2]/div/form/p[3]/input').click()
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/nav/div/div[1]/p/a[3]/b').click()
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="listings"]/div/div/div[2]/table/tbody/tr[3]/td[3]/a').click()
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/table/tbody/tr/td[6]/button').click()
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="inquiryModal"]/div/div/div[2]/form/button').click()
        try:
            time.sleep(2)
            elem = driver.find_element_by_xpath('//*[@id="listings"]/div/div/div[1]')
            assert True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()