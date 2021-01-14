from page.work_weixin_page import Work_WeiXin
from page.contacts_page import Contacts
from time import sleep

class Testcase:

    # 实例化登陆页面和通讯录
    def setup_class(self):
        self.main = Work_WeiXin()
        self.contacts = Contacts()

    # 新增部门并断言新增是否成功
    def test_add_dep(self):
        self.main.login().goto_contacts().goto_add_dep().add_Dep("shinobu")
        sleep(3)
        result = self.contacts.get_dep("shinobu")

        assert "shinobu" in result








    # def test_add_dep_failed(self):
    #     self.main.login().goto_contacts().goto_add_dep().add_Dep()
    #     result = self.contacts.get_dep()
    #
    #     assert "shinobu" not in result

