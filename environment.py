import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def before_all(context):
    context.service_obj = Service()
    context.chrome_options = webdriver.ChromeOptions()
    context.chrome_options.add_argument('--start-maximized')
    context.driver = webdriver.Chrome(service=context.service_obj, options=context.chrome_options)


def after_all(context):
    context.driver.close()


def after_step(context, step):
    if step.status == "failed":
        # Create the screenshots directory if it doesn't exist
        screenshots_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # Capture the screenshot
        screenshot_name = os.path.join(screenshots_dir, step.name + datetime.now().strftime(" %m-%d-%Y %H:%M:%S") +
                                       ".PNG")
        context.driver.get_screenshot_as_file(screenshot_name)
