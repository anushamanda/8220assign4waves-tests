import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class waves_Test4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_enrolledevents(self):

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
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/nav/div/div[1]/p/a[4]/b').click()
        time.sleep(2)

        try:
            time.sleep(2)
            elem = driver.find_element_by_xpath('//*[@id="enrolled_events"]/div/div/div/p')
            assert True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()