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
        # (5.3.4): 判断关键字: 登录成功。基本判断,断言。
        # 解答: 如果登录成功等于 True 那么断言为 True 否则断言为 False 那么这个可以写为一行代码。看新的判断断言。
        # if self.Page.LoginPage.is_toast_keyword("登录成功") == True:
        #     assert True
        # else:
        #     assert False
        #
        #
        # (5.3.4): 新的断言
        # 解答: 那么这个意思就是说本身自己如果是正确的有这个关键字那么就直接断言为 True 如果没有那么直接也断言
        #       为 Fasle。一个巧妙的处理手段。意思就是说直接断言返回的这个
        #       self.Page.LoginPage.is_toast_keyword("登录成功")值即可。然后还有一个奇怪的写法。看这个奇怪
        #       的写法。
        assert self.Page.LoginPage.is_toast_keyword("登录成功")
        #
        #
        # (5.3.4): 奇怪的写法。
        # 解答: 那么就是说如果我希望关键字判断正确的时候给我返回 Fasle 的话那么,直接取反即可。但是一般不这么写。
        # assert not self.Page.LoginPage.is_toast_keyword("登录成功")






















#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#