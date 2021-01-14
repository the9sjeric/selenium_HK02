"""
本页面地址为https://work.weixin.qq.com/
"""
from page.base import BaseRule
from page.index import Index

class Work_WeiXin(BaseRule):

    def login(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        return Index()

    def register(self):
        pass

    def download(self):
        pass