from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    driver: webdriver = None

    def __init__(self, context):
        self.driver: WebDriver = context.driver

    def go_to_login_page(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'submit').click()

    def is_error_message_present(self):
        error_banner = self.driver.find_element(By.ID, 'error')
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of(error_banner))
        assert 'Your username is invalid!' == error_banner.text
