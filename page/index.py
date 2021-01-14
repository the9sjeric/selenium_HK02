""""
本页面地址为：https://work.weixin.qq.com/wework_admin/frame#index
"""

from page.base import BaseRule
from page.contacts_page import Contacts

class Index(BaseRule):

    def goto_contacts(self):
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']").click()
        return Contacts()

    def goto_import_list(self):
        pass

    def goto_add_menbers(self):
        pass