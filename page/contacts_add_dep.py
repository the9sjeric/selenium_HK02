""""
本页面地址为：https://work.weixin.qq.com/wework_admin/frame#contacts
"""

from page.base import BaseRule
from time import sleep
class Add_Dep(BaseRule):

    # 新增部门 depname
    def add_Dep(self, depname):
        self.driver.find_element_by_css_selector(
            ".qui_dialog_body.ww_dialog_body [class='qui_inputText ww_inputText']").send_keys(depname)
        self.driver.find_element_by_css_selector(".js_parent_party_name").click()
        self.driver.find_element_by_css_selector(
            ".qui_dialog_body.ww_dialog_body [id='1688850780039479_anchor']").click()
        self.driver.find_element_by_xpath("//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()
        sleep(3)








    # def add_Dep_failed(self):
    #     self.driver.find_element_by_css_selector(
    #         ".qui_dialog_body.ww_dialog_body [class='qui_inputText ww_inputText']").send_keys("shibai")
    #     self.driver.find_element_by_css_selector(".js_parent_party_name").click()
    #     self.driver.find_element_by_css_selector(
    #         ".qui_dialog_body.ww_dialog_body [id='1688850780039479_anchor']").click()
    #     self.driver.find_element_by_xpath("//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()
