import unittest
from appium import webdriver
from utils.common_function import BaseFunction
import pymysql
import warnings
import time,random
from po.common_parameter import Others_personal_center
class TestCaseTest1(BaseFunction):
    def setUp(self):
        self.init_driver()
        warnings.simplefilter('ignore', ResourceWarning)
#红人榜和任性榜
    def test_case1_rank(self):
        #进入发现页
        self.find_element(self.driver,('id','tab_discovery')).click()
        #红人榜
        self.find_element(self.driver,('id','cb_interval_month')).click()
        self.find_element(self.driver,('id','cb_interval_year')).click()
        self.find_element(self.driver,('id','cb_interval_total')).click()
        #任性榜
        self.find_element(self.driver,('id','cb_assets_rank_send')).click()
        self.find_element(self.driver,('id','cb_interval_month')).click()
        self.find_element(self.driver,('id','cb_interval_year')).click()
        self.find_element(self.driver,('id','cb_interval_week')).click()
        #进入个人中心
        self.find_element(self.driver,('id','riv_ranking_first_avatar')).click()
        Others_personal_center.fromothers_center(self).click()


if __name__ == '__main__':
   discover = unittest.defaultTestLoader.discover(start_dir='.', pattern='unittest*.py')
   runner = unittest.TextTestRunner()
   runner.run(discover)
