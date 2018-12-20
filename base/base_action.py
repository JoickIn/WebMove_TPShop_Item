#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
#【公共动作特征页面】:
# (0): 导入包。
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# (1): 创建 BaseAction 类。
class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10.0, poll=1.0):
        by = feature[0]
        value = feature[1]
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10.0, poll=1.0):
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
        # (2.3): 在外侧加一给 try。然后在看 (2.4)。
        try:
            # (2.2): 那么这个写法就是由脚本页面传递过来的关键字,然后去进行一个判断,并且我们要加一个括号将这个括号里面的
            #        数据给扩起来,扩起来的原因就是由于这个find_element 里面的参数就传递一个,而这个相当于是两个参数了,第
            #        一个参数给了featur那么第2 个参数就给了timeout 了但是我需要将他两个变为一个参数传递给feature 那么就
            #        得他他们两个参数给用括号的方式给扩起来然后就变为一个参数了。 所以要加一个括号的方式。 然后在看  (2.3)。
            #        |||||更新(1): 加一个参数为 timeout=5 那么这个意思就是说等待 5 秒时间,那么就是说
            #                      我们每一次没找到的话就节省了 5 秒的时间。然后看更新(2)
            #        |||||更新(2): 加这个参数的意思就是说间隔几秒去找一次,那么这个参数我不想改为 1 我
            #                      改为 0.5 那么就会报错了,因为find_element里面封装的 poll=1是int的
            #                      类型然后我在这个里面传递的是浮点类型,所以就报错了, 如果强转的话也是
            #                      不行的。那么就是说类型要保证是一致的。那么就是说我们可以将这个这个这
            #                      个 find_element 函数里面的 poll  的值给包装一层 float 然后我在传递
            #                      这个 0.5 就不会有错了,同时我们看到的一个规律就是int可以自动转换为这个
            #                      这个 float 而 float 不能自动转换为 int 那么就是说你int比如说6那么转换
            #                      为小数就是6.0的,那么就是最好就是将find_element里面的都转换为float 类型
            #                      就行了,我们在使用的时候可以写小数的方式了,同时小数包含了整数。最好都写成这
            #                      个 float 这样你写不管是整数还是小数都没有问题。那么这个就是改 toast 的方法。
            self.find_element((By.XPATH, "//*[contains(@text, '%s')]" % text), timeout=5, poll=0.5)
            # (2.4): 如果有这个你从 test_login(5.3.4) 传递过来的字。那么返回 True 否者返回看 (2.5)。
            return True
        except Exception:
            # (2.5): 如果没有的话返回 False
            return False








#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#