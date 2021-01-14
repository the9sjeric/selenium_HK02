"""
在尝试了cookie和浏览器复用两种方式进行测试以后，
发现还是浏览器复用方式更加方便快捷，就在测试过程中使用了浏览器复用的方式。
"""

from selenium import webdriver

class BaseRule:
    # 使用浏览器复用的方式初始化dirver。
    def __init__(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"

        self.driver = webdriver.Chrome(options=chrome_args)
        self.driver.implicitly_wait(10)



