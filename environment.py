from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def before_all(context):
    context.service_obj = Service()
    context.chrome_options = webdriver.ChromeOptions()
    context.chrome_options.add_argument('--start-maximized')
    context.driver = webdriver.Chrome(service=context.service_obj, options=context.chrome_options)


def after_all(context):
    context.driver.close()
