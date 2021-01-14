""""
本页面地址为：https://work.weixin.qq.com/wework_admin/frame#contacts
"""
from page.base import BaseRule
from page.contacts_add_dep import Add_Dep
from time import sleep
# 通讯录页面
class Contacts(BaseRule):

    # 添加部门按钮
    def goto_add_dep(self):
        self.driver.find_element_by_css_selector(".member_colLeft_top_addBtn").click()
        self.driver.find_element_by_css_selector(".js_create_party").click()
        return Add_Dep()

    # 跳转导入页面
    def goto_import_list(self):
        pass

    # 通过搜索的方式验证部门是否添加成功
    def get_dep(self, depname):
        self.driver.find_element_by_xpath('//*[@id="memberSearchInput"]').send_keys(depname)
        sleep(3)

        dep_webelment_list = self.driver.find_elements_by_id("search_party_list")
        dep_list = []
        for i in dep_webelment_list:
            dep_list.append(i.text)

        return dep_list
