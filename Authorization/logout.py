import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_succes_logout(self): #test cases 1
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").send_keys("Admin")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name").click()
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > header:nth-child(2) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)").click()
        

if __name__ == '__main__':
    unittest.main()