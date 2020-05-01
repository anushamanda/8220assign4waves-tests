import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class waves_Test9(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addevent(self):

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
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/nav/div/div[1]/p/a[3]/b').click()
        elem = driver.find_element_by_xpath('//*[@id="listings"]/div/div/div[2]/table/tbody/tr[1]/td[3]/a/span').click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_event_name")
        elem.send_keys("Weight lifting")
        elem = driver.find_element_by_id("id_trainer_name")
        elem.send_keys("sri vidya")
        elem = driver.find_element_by_id("id_branch")
        elem.send_keys("72nd st omaha, NE waves branch1")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("power lifting is a great muscle building session")
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()

        try:
            time.sleep(2)
            elem = driver.find_element_by_xpath('//*[@id="listings"]/div/div/div[1]/h2')
            assert True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()