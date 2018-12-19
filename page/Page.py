#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
#【page页面】:
# (0): 导包
from base.base_action import BaseAction
from page.IndexPage import IndexPage
from page.MyPage import MyPage


# (1): page的类,统一入口。
class Page(BaseAction):
    @property
    def IndexPage(self):
        return IndexPage(self.driver)

    @property
    def MyPage(self):
        return MyPage(self.driver)


#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#