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
#搜索功能
    def test_case1_search(self):
        #点击进入搜索界面
        self.find_element(self.driver,('id','iv_home_search')).click()
        #热门搜索
        self.find_element(self.driver,('name','小易充值')).click()
        #热门搜索关注
        self.find_element(self.driver,('id','iv_user_attention')).click()
        self.find_element(self.driver,('id','iv_user_attention')).click()
        #更多
        self.find_element(self.driver,('id','tv_search_user_more')).click()
        self.is_element_exist(self.driver,('name','用户'))
        #热门搜索进入个人中心
        self.find_element(self.driver, ('name', '小易充值')).click()
        Others_personal_center.fromothers_center(self).click()
        self.find_element(self.driver,('id','iv_common_back')).click()
        #清除搜索结果
        self.find_element(self.driver,('id','iv_search_clean')).click()
        #自定义搜索
        self.find_element(self.driver,('id','et_search_content')).send_keys('30762049')
        self.find_element(self.driver,('id','tv_search_btn')).click()
        self.is_element_exist(self.driver,('id','iv_user_attention'))
        self.find_element(self.driver,('id','iv_search_clean')).click()
        self.find_element(self.driver,('name','30762049')).click()
        self.is_element_exist(self.driver,('id','iv_user_attention'))
        #清除搜索历史
        self.find_element(self.driver,('id','iv_search_clean')).click()
        self.find_element(self.driver,('id','iv_clear_his')).click()
        self.find_element(self.driver,('id','iv_back')).click()
#我的等级、按钮
    def test_case2_settings1(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        #进入设置界面
        self.find_element(self.driver,('id','mine_settings')).click()
        #关注提醒按钮
        self.find_element(self.driver,('id','notice_follow_event_cb')).click()
        self.find_element(self.driver,('id','notice_follow_event_cb')).click()
        #新私信提醒按钮
        self.find_element(self.driver,('id','notice_chat_event_cb')).click()
        self.find_element(self.driver,('id','notice_chat_event_cb')).click()
        #免打扰按钮
        self.find_element(self.driver,('id','notice_all_cb')).click()
        self.find_element(self.driver,('id','notice_all_cb')).click()
        #我的等级
        self.find_element(self.driver,('id','my_grade')).click()
        self.find_element(self.driver,('name','财富等级')).click()
        self.find_element(self.driver,('name','主播等级')).click()
        self.find_element(self.driver,('id','close_iv')).click()
#多语言功能
    def test_case3_lanuagesetting(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        #进入设置界面
        self.find_element(self.driver,('id','mine_settings')).click()
        #多语言界面
        self.find_element(self.driver,('id','language_setting')).click()
        self.is_element_exist(self.driver,('name','繁体中文'))
        #选择英文
        self.find_element(self.driver,('name','English')).click()
        self.find_element(self.driver,('id','tv_title_fun')).click()
        #判断英文环境
        self.find_element(self.driver,('name','Mine')).click()
        self.find_element(self.driver,('id','mine_settings')).click()
        self.find_element(self.driver,('id','language_setting')).click()
        self.find_element(self.driver,('name','简体中文')).click()
        self.find_element(self.driver,('id','tv_title_fun')).click()
        self.is_element_exist(self.driver,('name','预告'))
#邀请好友的搜索好友、感兴趣的人
    def test_case4_interest_person(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        #进入设置界面
        self.find_element(self.driver,('id','mine_settings')).click()
        #进入邀请好友界面
        self.find_element(self.driver,('id','invite_friend')).click()
        #搜索好友
        self.find_element(self.driver,('id','et_invite_keywords')).click()
        self.find_element(self.driver,('id','et_invite_keywords')).send_keys('小易充值')
        #关注、取消关注
        self.find_element(self.driver,('id','iv_user_attention')).click()
        self.find_element(self.driver,('id','iv_user_attention')).click()
        #进入个人中心
        self.driver.swipe(369,478,369,478,0)
        Others_personal_center.fromothers_center(self).click()
        self.find_element(self.driver,('id','tv_invate_cancel')).click()
        #感兴趣的人
        self.find_element(self.driver,('name','感兴趣的人')).click()
        self.driver.swipe(369,478,369,478,0)
        Others_personal_center.fromothers_center(self).click()
        self.driver.swipe(945,493,945,493,0)
        time.sleep(1)
        self.driver.swipe(945,493,945,493,0)
        #其他分类
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[2]/android.view.View')).click()
        self.find_element(self.driver,('xpath','	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[3]/android.view.View')).click()
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[4]/android.view.View')).click()
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[5]/android.view.View')).click()
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[5]/android.view.View')).click()
        #返回邀请好友
        self.find_element(self.driver,('id','iv_common_back')).click()
#附近的人
    def test_case5_nearby_person(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        #进入设置界面
        self.find_element(self.driver,('id','mine_settings')).click()
        #进入邀请好友界面
        self.find_element(self.driver,('id','invite_friend')).click()
        #附近的人
        self.find_element(self.driver,('name','附近的人')).click()
        self.driver.swipe(369,478,369,478,0)
        Others_personal_center.fromothers_center(self).click()
        self.driver.swipe(945,350,945,350,0)
        time.sleep(1)
        self.driver.swipe(945,350,945,350,0)
        self.find_element(self.driver,('id','iv_common_back')).click()
        self.find_element(self.driver,('id','iv_common_back')).click()
#直播消息
    def test_case6_live_message(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        #进入设置界面
        self.find_element(self.driver,('id','mine_settings')).click()
        #直播消息提醒
        self.find_element(self.driver,('id','notice_push_message_setting_rl')).click()
        #直播消息总开关
        self.find_element(self.driver,('id','location_toggle_tb')).click()
        self.find_element(self.driver,('id','location_toggle_tb')).click()
        #主播消息
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.CheckBox')).click()
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.CheckBox')).click()
        self.find_element(self.driver,('accessibility id','转到上一层级')).click()
#账号管理
    def test_case7_account_manage(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        #进入设置界面
        self.find_element(self.driver,('id','mine_settings')).click()
        #进入账号管理
        self.find_element(self.driver,('id','account_bind_tv')).click()
        #更换手机号
        self.find_element(self.driver,('id','bind_phone_tv')).click()
        #点击发送验证码
        self.find_element(self.driver,('id','time_btn')).click()
        self.is_element_exist(self.driver,('name','秒后重发'))
        self.find_element(self.driver,('id','iv_common_back')).click()
        #绑定微信
        self.find_element(self.driver,('id','bind_weixin_tv')).click()
        self.find_element(self.driver,('id','iv_common_back')).click()
#密码管理
    def test_case8_passwordmanage(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        #进入设置界面
        self.find_element(self.driver,('id','mine_settings')).click()
        #进入密码管理界面
        self.find_element(self.driver,('id','password_manager_setting_rl')).click()
        #修改密码
        self.find_element(self.driver,('id','et_input_old')).send_keys('123456')
        self.find_element(self.driver,('id','et_input_new')).send_keys('12345678')
        self.find_element(self.driver,('id','et_input_agagin')).send_keys('12345678')
        #展示密码
        self.find_element(self.driver,('id','show_password_iv')).click()
        self.find_element(self.driver,('id','show_new_password_iv')).click()
        self.find_element(self.driver,('id','show_confirm_password_iv')).click()
        #修改完成
        self.find_element(self.driver,('id','confirm_btn')).click()
        self.is_element_exist(self.driver, ('name', '设置'))
        #还原密码
        self.find_element(self.driver, ('id', 'password_manager_setting_rl')).click()
        self.find_element(self.driver, ('id', 'et_input_old')).send_keys('12345678')
        self.find_element(self.driver, ('id', 'et_input_new')).send_keys('123456')
        self.find_element(self.driver, ('id', 'et_input_agagin')).send_keys('123456')
        self.find_element(self.driver, ('id', 'confirm_btn')).click()
#清除缓存、检查更新、联系我们、关于、退出登陆
    def test_case9_clean(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        #进入设置界面
        self.find_element(self.driver,('id','mine_settings')).click()
        #清理缓存
        self.find_element(self.driver,('id','item_clean_cached')).click()
        self.is_element_exist(self.driver,('name','KB'))
        #检查更新
        self.find_element(self.driver,('id','manual_check_update_rl')).click()
        #联系我们
        self.driver.swipe(529,1737,529,647,1000)
        self.find_element(self.driver,('id','contact_us_rl')).click()
        self.is_element_exist(self.driver,('name','公会合作'))
        self.find_element(self.driver,('id','close_iv')).click()
        #关于
        self.find_element(self.driver,('id','about_us_rl')).click()
        #版本号
        self.is_element_exist(self.driver,('name','V5.9.0.0612'))
        #关于易直播
        self.find_element(self.driver,('id','tv_about_us')).click()
        self.find_element(self.driver,('accessibility id','转到上一层级')).click()
        #版权说明
        self.find_element(self.driver,('name','版权说明')).click()
        self.find_element(self.driver,('accessibility id','转到上一层级')).click()
        #封号处理准则
        self.find_element(self.driver,('name','封号处理准则')).click()
        self.find_element(self.driver,('id','close_iv')).click()
        self.find_element(self.driver,('id','iv_common_back')).click()
        #退出登陆
        self.find_element(self.driver,('id','logout_btn')).click()
        self.find_element(self.driver,('id','button1')).click()



if __name__ == '__main__':
   discover = unittest.defaultTestLoader.discover(start_dir='.', pattern='unittest*.py')
   runner = unittest.TextTestRunner()
   runner.run(discover)
