""""
本页面地址为：https://work.weixin.qq.com/wework_admin/frame#index
"""

from page.base import BaseRule
from page.contacts_page import Contacts

# 企业微信登陆后的主页面
class Index(BaseRule):

    # 跳转通讯录页面
    def goto_contacts(self):
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']").click()
        return Contacts()

    # 跳转导入页面
    def goto_import_list(self):
        pass

    # 跳转添加员工页面
    def goto_add_menbers(self):
        pass