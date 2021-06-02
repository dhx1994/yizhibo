from selenium.webdriver.support.wait import WebDriverWait      # 这里是导入动态查找需要的第三方包
from appium import webdriver
import pymysql.cursors
import unittest

class BaseFunction(unittest.TestCase):
    def init_driver(self):
        # 打开被测的app
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 打开什么平台的app，固定的 > 启动安卓平台
        desired_caps['platformVersion'] = '10'  # 安卓系统的版本号：adb shell getprop ro.build.version.
        desired_caps['deviceName'] = 'PCT-AL10'  # 手机/模拟器的型号：adb shell getprop ro.product.model
        desired_caps['appPackage'] = 'com.ccvideo'  # app的名字：adb shell dumpsys activity activities | findstr mResumedActivity"：andriod 8.0
        #desired_caps['automationName']= 'uiautomator2',
        desired_caps['appActivity'] = 'com.yizhibo.video.activity_new.SplashActivity'  # app的启动页名字：adb shell dumpsys activity | findstr "mFocusedActivity" dumpsys activity | findstr "mFocusedActivity"
        desired_caps['unicodeKeyboard'] = True  # 为了支持中文
        desired_caps['resetKeyboard'] = True  # 设置成appium自带的键盘
        desired_caps['noReset'] = True
        # 解锁手机并且去打开app
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    """
        查找单个元素
            参数：locator=("id", "123")
            类型：w
            ID = "id"
            XPATH = "xpath"
            LINK_TEXT = "link text"
            PARTIAL_LINK_TEXT = "partial link text"
            NAME = "name"
            TAG_NAME = "tag name"
            CLASS_NAME = "class name"
            CSS_SELECTOR = "css selector"
    """
    def is_element_exist(self,driver, element):
        try:
            WebDriverWait(driver, 10).until(lambda s: s.find_element(*element))  # 实现元素的动态定位
            return True
        except:
            return False
    def find_element(self,driver, element):
        return WebDriverWait(driver, 10).until(lambda s: s.find_element(*element))