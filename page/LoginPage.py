#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
#【登录页面 -----> LoginPage.py】:
# (0): 导包。
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


    # (3): 定位元素的动作函数。
    # (3.1): 输入用户名。
    def input_username(self, text):
        self.input(self.username_input, text)

    # (3.2): 输入密码。
    def input_password(self, text):
        self.input(self.password_input, text)

    # (3.3): 点击登录按钮。
    def click_login(self):
        self.click(self.login_button)






















#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#