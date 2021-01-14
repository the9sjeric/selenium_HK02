from time import sleep
from selenium import webdriver
# from selenium.webdriver.remote.webdriver import WebDriver

class BaseRule:

    def __init__(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"

        self.driver = webdriver.Chrome(options=chrome_args)
        self.driver.implicitly_wait(10)



