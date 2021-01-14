from page.work_weixin_page import Work_WeiXin
from page.contacts_page import Contacts


class Testcase:

    def setup_class(self):
        self.main = Work_WeiXin()
        self.contacts = Contacts()

    def test_add_dep(self):
        self.main.login().goto_contacts().goto_add_dep().add_Dep()
        result = self.contacts.get_dep()

        assert "shinobu" in result

    # def test_add_dep_failed(self):
    #     self.main.login()
    #     result = self.main.goto_list().goto_add_dep().add_Dep().get_dep()
    #
    #     assert "shinobu" not in result
