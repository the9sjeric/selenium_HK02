""""
本页面地址为：https://work.weixin.qq.com/wework_admin/frame#contacts
"""

from page.base import BaseRule

class Add_Dep(BaseRule):

    def add_Dep(self):
        self.driver.find_element_by_css_selector(
            ".qui_dialog_body.ww_dialog_body [class='qui_inputText ww_inputText']").send_keys("shinobu")
        self.driver.find_element_by_css_selector(".js_parent_party_name").click()
        self.driver.find_element_by_css_selector(
            ".qui_dialog_body.ww_dialog_body [id='1688850780039479_anchor']").click()
        self.driver.find_element_by_xpath("//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()

    # def add_Dep_failed(self):
    #     self.driver.find_element_by_css_selector(
    #         ".qui_dialog_body.ww_dialog_body [class='qui_inputText ww_inputText']").send_keys("shibai")
    #     self.driver.find_element_by_css_selector(".js_parent_party_name").click()
    #     self.driver.find_element_by_css_selector(
    #         ".qui_dialog_body.ww_dialog_body [id='1688850780039479_anchor']").click()
    #     self.driver.find_element_by_xpath("//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()
