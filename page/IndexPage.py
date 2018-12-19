#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
#【首页 -> IndexPage】:
# (0): 导包
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# (1): 首页类名。
class IndexPage(BaseAction):
    # (2): 首页我的按钮的特征(定位元素) 解答: 那么就是说我要点击【我的】这个按钮,如果名字换了的话那么就不能定位他了
    #      所以我们要用更精确的方式去进行一个定位。中间连接一个并且,这样使用逻辑运算符会更加的精确。
    my_button = By.XPATH, "//*[@text='我的' and @resource-id='com.tpshop.malls:id/tab_txtv']"

    # (3): 首页我的按钮的动作(函数)
    def click_my_button(self):
        self.click(self.my_button)


#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#