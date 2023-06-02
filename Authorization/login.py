import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_succes_login(self): #test cases 1
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").send_keys("Admin")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    def test_invalid_usernamedanpassword(self): #test cases 2
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").send_keys("Sherelia")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys("sherelia123")
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    def test_invalid_username(self): #test cases 3
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").send_keys("Sherelia")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    def test_invalid_password(self): #test cases 4
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").send_keys("Admin")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys("sherelia123")
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    def test_empty_usernamedanpassword(self): #test cases 5
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    def test_failed_login(self): #test cases 6
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").send_keys("Admin")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Password']").send_keys("sherelia123")
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    def test_failed_login1(self): #test cases 7
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element(By.CSS_SELECTOR, "[placeholder='Username']").send_keys("Admin")
        driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

if __name__ == '__main__':
    unittest.main()