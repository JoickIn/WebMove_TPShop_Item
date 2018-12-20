#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#
#【base_driver】:
# (0): 导入包。
from appium import webdriver

# (1): 创建函数 driver。
def init_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # tpshop软件的包名
    desired_caps['appPackage'] = 'com.tpshop.malls'
    # tpshop软件的启动名
    desired_caps['appActivity'] = '.SPMainActivity'
    # toast框架
    desired_caps['automationName'] = 'Uiautomator2'
    # desired_caps['noReset'] = True


    # 声明 driver 对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————#