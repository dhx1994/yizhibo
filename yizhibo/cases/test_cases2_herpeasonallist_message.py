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
#他人中心信息判断
    def test_case1_herdetails_information(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        # 进入个人中心
        self.find_element(self.driver,('id', 'my_user_photo')).click()
        #进入关注列表
        self.find_element(self.driver,('id','tv_user_follow_count')).click()
        #进入他人个人中心
        self.find_element(self.driver,('name','测试主播')).click()
        #修改备注名
        self.find_element(self.driver,('id','tv_pannel_nickname')).click()
        self.find_element(self.driver,('id','remark_remarks_et')).send_keys('颜值主播')
        self.find_element(self.driver,('id','menu_commit')).click()
        self.is_element_exist(self.driver,('name','颜值主播'))
        self.find_element(self.driver,('id','tv_pannel_nickname')).click()
        self.find_element(self.driver,('id','remark_remarks_et')).send_keys('测试主播')
        self.find_element(self.driver,('id','menu_commit')).click()
        #判断认证标志存在
        self.is_element_exist(self.driver,('id','iv_pannel_guanv'))
        #判断昵称存在
        self.is_element_exist(self.driver,('id','tv_pannel_nickname'))
        # 判断成长等级存在
        self.is_element_exist(self.driver, ('id', 'user_level_new_tv'))
        # 判断用户年龄存在
        self.is_element_exist(self.driver, ('id', 'user_gender_new_tv'))
        # 判断财富等级存在
        self.is_element_exist(self.driver, ('id', 'user_vip_level_new_iv'))
        # 判断主播等级存在
        self.is_element_exist(self.driver, ('id', 'user_anchor_level_new_iv'))
        # 判断认证存在
        self.is_element_exist(self.driver, ('name', '女神'))
        #判断星座存在
        self.is_element_exist(self.driver,('id','user_constellation_new_tv'))
        # 判断头像存在
        self.is_element_exist(self.driver, ('id', 'iv_user_photo'))
        # 判断定位存在
        self.is_element_exist(self.driver, ('id', 'tv_user_location'))
        # 判断粉丝存在
        self.is_element_exist(self.driver, ('id', 'tv_user_fans_count'))
        # 判断关注存在
        self.is_element_exist(self.driver, ('id', 'tv_user_follow_count'))
        # 判断空房间
        self.is_element_exist(self.driver, ('id', 'tv_room_state'))
        #判断id存在
        self.is_element_exist(self.driver,('id','tv_user_ID'))
        # 判断工会存在
        self.is_element_exist(self.driver, ('id', 'tv_user_union_name1'))
        #左滑操作
        self.driver.swipe(921,1249,174,1249,1000)
        self.is_element_exist(self.driver,('name', '运动'))
        self.driver.swipe(174,1249,921,1249,1000)
#他人中心关注、粉丝列表
    def test_case2_herfan_follow(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        # 进入个人中心
        self.find_element(self.driver,('id', 'my_user_photo')).click()
        #进入关注列表
        self.find_element(self.driver,('id','tv_user_follow_count')).click()
        #进入他人个人中心
        self.find_element(self.driver,('name','测试主播')).click()
        # 点击进入粉丝列表
        self.find_element(self.driver, ('id', 'tv_user_fans_count')).click()
        # 判断是否进入粉丝列表
        self.is_element_exist(self.driver, ('name', '粉丝'))
        # 点击进入个人中心,然后返回
        a = random.randint(100, 800)
        b = random.randint(300, 2100)
        self.driver.swipe(a, b, a, b, 0)
        self.is_element_exist(self.driver, ('id', 'tv_room_state'))
        Others_personal_center.fromothers_center(self).click()
        # 关注、取消关注
        self.driver.swipe(945, 350, 945, 350, 0)
        time.sleep(2)
        self.driver.swipe(945, 350, 945, 350, 0)
        # 返回个人中心
        self.find_element(self.driver, ('id', 'iv_common_back')).click()
        # 进入关注列表
        self.find_element(self.driver, ('id', 'tv_user_follow_count')).click()
        self.is_element_exist(self.driver, ('name', '关注'))
        c = random.randint(300,600)
        self.driver.swipe(a, c, a, c, 0)
        self.is_element_exist(self.driver, ('id', 'tv_room_state'))
        Others_personal_center.fromothers_center(self).click()
        # 关注、取消关注
        self.driver.swipe(945, 350, 945, 350, 0)
        time.sleep(2)
        self.driver.swipe(945, 350, 945, 350, 0)
        # 返回个人中心
        self.find_element(self.driver, ('id', 'iv_common_back')).click()
    def test_case3_rank(self):
        # 进入我的界面
        self.find_element(self.driver, ('id', 'tab_message')).click()
        # 进入个人中心
        self.find_element(self.driver, ('id', 'my_user_photo')).click()
        # 进入关注列表
        self.find_element(self.driver, ('id', 'tv_user_follow_count')).click()
        # 进入他人个人中心
        self.find_element(self.driver, ('name', '测试主播')).click()
        #查看排行榜
        self.find_element(self.driver,('id','iv_list1')).click()
        #进入他人中心
        self.driver.swipe(369,485,369,485,0)
        #返回排行榜
        self.find_element(self.driver,('id','iv_go_back')).click()
        self.is_element_exist(self.driver,('id','spikeCheck'))
        self.find_element(self.driver,('id','tab_week')).click()
        self.find_element(self.driver,('id','tab_year')).click()
        self.find_element(self.driver,('id','tv_title_fun')).click()
        #返回个人中心
        self.find_element(self.driver,('id','iv_common_back')).click()
        self.find_element(self.driver,('id','iv_common_back')).click()
#个人形象视频观看、关注、私信按钮
    def test_case4_herimage_display(self):
        # 进入我的界面
        self.find_element(self.driver, ('id', 'tab_message')).click()
        # 进入个人中心
        self.find_element(self.driver, ('id', 'my_user_photo')).click()
        # 进入关注列表
        self.find_element(self.driver, ('id', 'tv_user_follow_count')).click()
        # 进入他人个人中心
        self.find_element(self.driver, ('name', '测试主播')).click()
        #进入个人形象页
        self.find_element(self.driver,('id','tv_image_name')).click()
        #上滑操作
        self.driver.swipe(514,1605,514,496,1000)
        a = int(self.find_element(self.driver,('id','image_watch_count')).text) + 1
        #查看个人形象视频
        self.find_element(self.driver,('id','iv_image_thumb')).click()
        time.sleep(5)
        #判断视频播放是否+1
        self.assertEqual(int(self.find_element(self.driver,('id','image_watch_count')).text),a,msg=None)
        #进入礼物界面
        self.find_element(self.driver,('id','tv_gift_name')).click()
        #关注、取消关注
        self.find_element(self.driver,('id','follow_text')).click()
        self.find_element(self.driver,('id','follow_text')).click()
        #点击进入私信聊天界面
        self.find_element(self.driver,('name','私信')).click()
        self.find_element(self.driver,('id','iv_common_back')).click()
#礼物面板赠送礼物
    def test_case5_gift_pannel(self):
        # 进入我的界面
        self.find_element(self.driver, ('id', 'tab_message')).click()
        # 进入个人中心
        self.find_element(self.driver, ('id', 'my_user_photo')).click()
        # 进入关注列表
        self.find_element(self.driver, ('id', 'tv_user_follow_count')).click()
        # 进入他人个人中心
        self.find_element(self.driver, ('name', '测试主播')).click()
        #进入礼物面板
        self.find_element(self.driver,('id','iv_send_gift')).click()
        #点击选中礼物
        self.driver.swipe(131,1945,131,1945,0)
        #赠送礼物
        self.find_element(self.driver,('id','send_gift_btn')).click()
        self.find_element(self.driver,('id','tv_burst_send_text')).click()
#好友列表
    def test_case6_goodfriend(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        #判断消息气泡存在
        self.is_element_exist(self.driver,('id','unread_message'))
        #进入消息列表
        self.find_element(self.driver,('id','mine_message')).click()
        #进入好友界面
        self.find_element(self.driver,('id','iv_title_friends')).click()
        #进入聊天页
        self.find_element(self.driver,('name','仰望星空')).click()
        #退出聊天页
        self.find_element(self.driver,('id','iv_common_back')).click()
        #进入他人个人中心
        self.driver.swipe(128,343,128,343,0)
        #退出他人个人中心
        Others_personal_center.fromothers_center(self).click()
        #退出好友列表
        self.find_element(self.driver,('id','iv_common_back')).click()
#消息页发消息测试
    def test_case7_message(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        #进入消息列表
        self.find_element(self.driver,('id','mine_message')).click()
        #进入好友界面
        self.find_element(self.driver,('id','iv_title_friends')).click()
        #进入聊天页
        self.find_element(self.driver,('name','仰望星空')).click()
        #点击右上角进入个人中心
        self.find_element(self.driver,('id','iv_title_fun')).click()
        #返回聊天页
        Others_personal_center.fromothers_center(self).click()
        #点击发送文字
        self.find_element(self.driver,('id','et_chat_message_content')).send_keys('测试文字')
        self.find_element(self.driver,('id','bt_chat_msg_send')).click()
        #点击发送图片
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]')).click()
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView[1]')).click()
        self.find_element(self.driver,('id','tv_send')).click()
        #点击转账
        self.find_element(self.driver, ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]')).click()
        #输入转账金额
        self.find_element(self.driver,('id','edit_transfer_account')).send_keys('1')
        self.find_element(self.driver,('id','btn_submit')).click()
        #发送文字受限
        self.find_element(self.driver,('id','iv_common_back')).click()
        #进入好友界面
        #self.find_element(self.driver,('id','iv_title_friends')).click()
        self.find_element(self.driver,('name','蓝色海洋')).click()
        self.is_element_exist(self.driver,('id','open_im'))
#消息界面礼物面板测试
    def test_case8_giftpannel(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        #进入消息列表
        self.find_element(self.driver,('id','mine_message')).click()
        #进入聊天页
        self.find_element(self.driver,('name','仰望星空')).click()
        #打开礼物面板
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]')).click()
        #点击礼物么么哒
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.GridView/android.widget.RelativeLayout[5]/android.widget.LinearLayout/android.widget.ImageView')).click()
        #赠送礼物
        self.find_element(self.driver,('id','send_gift_btn')).click()
        self.find_element(self.driver,('id','tv_burst_send_text')).click()
#其他消息测试
    def test_case9_others(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        #进入消息列表
        self.find_element(self.driver,('id','mine_message')).click()
        #在线客服
        self.find_element(self.driver,('name','在线客服')).click()
        self.find_element(self.driver,('id','input_et')).send_keys('测试')
        self.find_element(self.driver,('id','send_text_btn')).click()
        self.find_element(self.driver,('id','back_iv')).click()
        #新朋友
        self.find_element(self.driver,('name','新朋友')).click()
        # 点击进入个人中心,然后返回
        a = random.randint(100, 800)
        b = random.randint(300, 2100)
        self.driver.swipe(a, b, a, b, 0)
        self.is_element_exist(self.driver, ('id', 'tv_room_state'))
        self.find_element(self.driver, ('id', 'iv_go_back')).click()
        # 关注、取消关注
        self.driver.swipe(945, 350, 945, 350, 0)
        time.sleep(2)
        self.driver.swipe(945, 350, 945, 350, 0)
        #退出新朋友
        self.find_element(self.driver,('id','iv_common_back')).click()
        #调到未读消息处
        self.find_element(self.driver,('id','iv_title_msg')).click()
        #未读消息标为已读测试
        self.find_element(self.driver,('id','iv_title_clear')).click()
        self.find_element(self.driver,('id','tv_confirm')).click()
        #退出消息页
        self.find_element(self.driver,('id','iv_common_back')).click()
if __name__ == '__main__':
   discover = unittest.defaultTestLoader.discover(start_dir='.', pattern='unittest*.py')
   runner = unittest.TextTestRunner()
   runner.run(discover)
