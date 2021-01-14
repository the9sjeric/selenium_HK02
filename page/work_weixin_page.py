"""
本页面地址为https://work.weixin.qq.com/
"""
from page.base import BaseRule
from page.index import Index

# 企业微信登陆页面
class Work_WeiXin(BaseRule):

    # 登录按钮
    def login(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        return Index()
    # 注册按钮
    def register(self):
        pass
    # 下载按钮
    def download(self):
        pass