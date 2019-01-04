#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
#【登录页面 -----> LoginPage.py】:
# (0): 导包。
import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# (1): 创建登录页面的类。
class LoginPage(BaseAction):
    # (2): 定位元素特征。
    # (2.1): 用户名输入框。
    username_input = By.ID, "com.tpshop.malls:id/edit_phone_num"
    # (2.2): 密码输入框。
    password_input = By.ID, "com.tpshop.malls:id/edit_password"
    # (2.3): 登录按钮。
    login_button = By.ID, "com.tpshop.malls:id/btn_login"
    # (2.4): 显示密码的按钮。然后在看下面的代码 (7)
    show_password_button = By.ID, "com.tpshop.malls:id/img_view_pwd"


    # (4): 配置步骤。
    @allure.step("登录页面-输入-用户名")
    # (3): 定位元素的动作函数。
    # (3.1): 输入用户名。
    def input_username(self, text):
        # (5): 配置描述的信息。
        allure.attach("用户名", text)
        self.input(self.username_input, text)

    # (4.1): 配置步骤。
    @allure.step("登录页面-输入-密码")
    # (3.2): 输入密码。
    def input_password(self, text):
        # (5.1): 配置描述的信息。
        allure.attach("密码", text)
        self.input(self.password_input, text)

    # (4.2): 配置步骤。
    @allure.step("登录页面-点击-登录按钮")
    # (3.3): 点击登录按钮。
    def click_login(self):
        self.click(self.login_button)

    # (6): 定义一个方法这个方法是是不是一个登录的按钮。那么这个方法意思就是说如果你的这个按钮是可用的那么就
    #      返回 true 如果是不可用的话就返回 false
    def is_login_button_enabled(self):
        # (6.1): 那么就是说先找到这个按钮的元素,然后在点这个方法。-> .is_enabled()
        # return self.find_element(self.login_button).is_enabled()
        # (6.1.1): 改良版本,用 base 里面公共的方法。
        return self.is_feature_enabled(self.login_button)

        # (6.2): 另外一个写法。那么这个写法的意思就是说,如果系统没给你提供这个is_enabled()的方法那么就自
        #        己去做一个这样的方法,这个方法的意思就是说去获取属性的值。这个方法适用于多个获取属性值的方
        #        式。但是如果系统提供了方法尽量用系统所提供的方法即可。
        # if self.find_element(self.login_button).get_attribute("enabled") == "true":
        #     return True
        # else:
        #     return False


    # (7.1): 配置中文步骤。
    @allure.step("登录页面-点击-显示密码按钮")
    # (7): 对显示按钮进行一个点击的操作。然后在回到 -> scripts 页面里面去调用他看 scripts 里面的 (10.5) 步骤
    def click_show_password_button(self):
        self.click(self.show_password_button)


    # (8): 直接调用之前封装好 get_text() 函数即可,这个函数的意思就是说你给我这个函数一个特征那么我就帮助你返回
    #      文字,所以我们在 scripts 里面去直接调用这个方法就可以了,看 test_login 里面的 (10.6)
    def get_password_text(self):
        return self.get_text(self.password_input)



#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#