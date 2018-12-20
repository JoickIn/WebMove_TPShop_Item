#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
#【测试脚本登录页面 -> test_login】:
# (0): 导包。
from page.IndexPage import IndexPage
from page.MyPage import MyPage
import time
from base.base_driver import init_driver
from page.Page import Page


# (1): 创建脚本登录页面 test_login 的类。
class TestLogin:
    # (2): 初始化页面。
    def setup(self):
        self.driver = init_driver()
        self.Page = Page(self.driver)


    # (3): 初始化结束页面。
    def teardown(self):
        time.sleep(5)
        self.driver.quit()


    # (4): 这条用例作为测试用。
    # def test_login0(self):
    #     print("test01")


    # (5): 测试用例: longin
    def test_login(self):
        # (5.1): 点击我的。
        self.Page.IndexPage.click_my_button()

        # (5.2): 登录/注册。
        self.Page.MyPage.click_login_and_sign_up_button()

        # (5.3): 登录。
        # (5.3.1): 填写 username
        self.Page.LoginPage.input_username('13800138006')
        # (5.3.2): 填写 password
        self.Page.LoginPage.input_password('123456')
        # (5.3.3): 点击登录按钮
        self.Page.LoginPage.click_login()




















#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#