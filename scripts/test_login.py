#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
#【测试脚本登录页面 -> test_login】:
# (0): 导包。
import time
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.Page import Page
import pytest


# (1): 创建脚本登录页面 test_login 的类。
class TestLogin:
    # (2): 初始化页面。
    def setup(self):
        self.driver = init_driver()
        self.Page = Page(self.driver)


    # (3): 初始化结束页面。
    def teardown(self):
        self.driver.quit()


    # (4): 这条用例作为测试用。
    # def test_login0(self):
    #     print("test01")


    # (6): 配置参数化。在这个函数头上直接写即可。然后直接调用方法即可。看(6.1)
    # @pytest.mark.parametrize("args", analyze_file("test_login_data.yml", "test_login"))
    # (5): 测试用例: longin/(6.1): 加入形参 args 看(6.2)
    # def test_login(self, args):
        # (6.2): 准备数据。看(6.3)
        # username = args['username']
        # password = args['password']
        # info = args['info']


        # (5.1): 点击我的。
        # self.Page.IndexPage.click_my_button()

        # (5.2): 登录/注册。
        # self.Page.MyPage.click_login_and_sign_up_button()

        # (5.3): 登录。
        # (5.3.1): 填写 username
        # self.Page.LoginPage.input_username('13800138006')
        # (6.4): 将字符串改为对应的数据变量。
        # self.Page.LoginPage.input_username(username)
        # (5.3.2): 填写 password
        # self.Page.LoginPage.input_password('123456')
        # (6.4): 将字符串改为对应的数据变量。
        # self.Page.LoginPage.input_password(password)
        # (5.3.3): 点击登录按钮
        # self.Page.LoginPage.click_login()
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
        # assert self.Page.LoginPage.is_toast_keyword("登录成功")
        # (6.4): 将字符串改为对应的数据变量。
        # assert self.Page.LoginPage.is_toast_keyword(info)
        #
        #
        # (5.3.4): 奇怪的写法。
        # 解答: 那么就是说如果我希望关键字判断正确的时候给我返回 Fasle 的话那么,直接取反即可。但是一般不这么写。
        # assert not self.Page.LoginPage.is_toast_keyword("登录成功")




    # (7): 第 2 套脚本设计 -> 只输入用户民或者密码。
    # (7.1): 定义第 2 套函数。
    # @pytest.mark.parametrize("args", analyze_file("test_login_data.yml", "test_login_miss_part"))
    # def test_login_miss_part(self, args):
        # (7.2): 准备数据。
        # username = args['username']
        # password = args['password']

        # (7.3): 点击我的。
        # self.Page.IndexPage.click_my_button()

        # (7.4): 登录/注册。
        # self.Page.MyPage.click_login_and_sign_up_button()

        # (7.5): 输入用户名。
        # self.Page.LoginPage.input_username(username)

        # (7.6): 输入密码。
        # self.Page.LoginPage.input_password(password)

        # (8): 如果数据在设计的时候没有不输入的 key 那么就使用下面的全部的写法。或者直接用上面的 (7) 系列也是可以的。
        # if "username" in args:
            # (8.1): 登录输入用户名。
            # self.Page.LoginPage.input_username(args['username'])

        # if "password" in args:
            # (8.2): 登录输入密码。
            # self.Page.LoginPage.input_password(args['password'])


        # (9): 断言,如果登录按钮可以点击,那么不通过,如果登录按钮不可以点击,那么就通过。
        # if self.Page.LoginPage.is_login_button_enabled() == True:
        #     assert False
        # else:
        #     assert True




    # (10): 测试显示密码。
    def test_show_password(self):
        # (10.7): 准备数据。
        input_password = "111111"


        # (10.1): 点击我的。
        self.Page.IndexPage.click_my_button()


        # (10.2): 点击 [登录/注册] 按钮。
        self.Page.MyPage.click_login_and_sign_up_button()


        # (10.3): 登录页面-输入密码。
        # self.Page.LoginPage.input_password("111111")
        #
        # (10.3.1): ||||||升级的版本: 把原来的数据替换为变量。
        self.Page.LoginPage.input_password(input_password)


        # (10.4): 密码是不是没有显示(说白了在没点击显示按钮的时候密码是不是黑点的状态)。如果输入的密码前提是在没点这个显
        #         示按钮之前就显示了密码的本体,那么就是说这个时候说明软件是有 bug 的。那么我们要做一个判断。 那么就是说
        #         这个断言为 False 之后那么就是说后面的代码就不会去执行了。
        # 解答: 那么就是说当这个 if 的条件如果是为真的时候,那么这个断言False他就会报错了,那么也就是说后面 else 里面的代
        #       码是不会去执行的,那么如果说这个 if 判断条件他为 false 那么也不会进入到这个条件里面来而是直接就执行 else
        #       里面的条件了。
        if self.Page.LoginPage.get_password_text() == input_password:
            assert False, "备注: password上的文字在没按显示按钮(默认的密码是黑点)的时候就显示了密码的实体,说明软件有 Bug。"
        else:
            # (10.5): 点击显示密码的按钮(就是那个小眼睛的按钮)。
            self.Page.LoginPage.click_show_password_button()

            # (10.6): 断言: 密码框里面的文字是不是和之前输入的一致,如果是和之前输入的文字是一致的那么就没有 bug。那么我们要
            #          封装到 base 里面一个函数,看 base 里面的 get_text() 这个封装好的函数,由于这个函数已经被封装好了, 那
            #          么就是说我们在 LoginPage 里面直接去使用这个函数即可。 看 LoginPage 里面的 (8) 然后那么就是说他得到
            #          的就是这 111111 那么我就要用这个函数去进行一个断言看看是不是 111111 那么由于这个几个 1 是重复的我们
            #          可以放到一个变量里面去。看 (10.7)。
            # assert "111111" == self.Page.LoginPage.get_password_text()
            #
            # (10.6.1): ||||||升级的版本: 把原来的数据替换为变量。
            assert input_password == self.Page.LoginPage.get_password_text()


























#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#