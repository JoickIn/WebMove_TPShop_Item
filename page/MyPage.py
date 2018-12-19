#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
#【我的页面】:
# (0): 导包:
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# (1): 创建我的页面的类。
class MyPage(BaseAction):
    # (2): 我的页面定位登录/注册的特征/元素。
    login_and_sign_up_button = By.XPATH, "//*[@text='登录/注册' and @resource-id='com.tpshop.malls:id/nickname_txtv']"


    # (3): 我的页面登录/注册动作函数。
    def click_login_and_sign_up_button(self):
        self.click(self.login_and_sign_up_button)


#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#