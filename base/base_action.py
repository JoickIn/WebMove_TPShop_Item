#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
#【公共动作特征页面】:
# (0): 导入包。
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# (1): 创建 BaseAction 类。
class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
        by = feature[0]
        value = feature[1]
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10, poll=1):
        by = feature[0]
        value = feature[1]
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def get_text(self, feature):
        return self.find_element(feature).text

    # (2): 判断弹出框的关键字。
    # (2.1): 首先要传入一个 text 的形参文字,然后根据这个文字去判断有没有对应文字的提示,如果有返回 True 如果没有
    #        返回 False
    def is_toast_keyword(self, text):
        # (2.3): 在外侧加一给 try。然后在看(2.4)
        try:
            # (2.2): 那么这个写法就是由脚本页面传递过来的关键字,然后去进行一个判断,并且我们要加一个括号将这个括号里面的
            #        数据给扩起来,扩起来的原因就是由于这个find_element里面的参数就传递一个,而这个相当于是两个参数了,第
            #        一个参数给了featur那么第2个参数就给了timeout了但是我需要将他两个变为一个参数传递给feature 那么就
            #        得他他们两个参数给用括号的方式给扩起来然后就变为一个参数了。所以要加一个括号的方式。然后在看(2.3)
            self.find_element((By.XPATH, "//*[contains(@text, '%s')]" % text))
            # (2.4): 如果有这个你从 test_login(5.3.4) 传递过来的字。那么返回 True 否者返回看(2.5)
            return True
        except Exception:
            # (2.5): 如果没有的话返回 False
            return False








#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#