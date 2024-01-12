from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class MainPage:
    driver: webdriver = None

    def __init__(self, context):
        self.driver: WebDriver = context.driver

    def is_main_page(self):
        assert "successfully" in self.driver.current_url
