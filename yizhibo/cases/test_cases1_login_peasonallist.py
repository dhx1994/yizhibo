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
#登录账号
    def test_case1_login(self):
        # 切换密码登录
        self.find_element(self.driver, ('id', 'tv_loginStyle')).click()
        # 输入手机号
        self.find_element(self.driver, ('id', 'et_registerPhone')).send_keys('13957869385')
        # 输入密码
        self.find_element(self.driver, ('id', 'et_password')).send_keys('123456')
        # 点击登录
        self.find_element(self.driver, ('id', 'btn_login')).click()
        # 判断登录
        self.is_element_exist(self.driver, ('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[3]/android.view.View'))
#发布预告
    def test_case2_notice(self):
        # 首页签到
        try:
            self.find_element(self.driver, ('id', 'btn_sign')).click()
            self.find_element(self.driver, ('id', 'btn_sign')).click()
        except:
            pass
        # 进入预告页
        self.find_element(self.driver, ('xpath',
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[4]/android.view.View')).click()
        # 进入发布预告页
        self.find_element(self.driver, ('id', 'discover_notice_submit_btn')).click()
        # 添加预告标题
        self.find_element(self.driver, ('id', 'et_title')).send_keys("啦啦啦德玛西亚")
        # 选择预告时间
        self.driver.swipe(389, 744, 389, 600, 1000)
        # 选择图片
        self.find_element(self.driver, ('id', 'iv_cover')).click()
        self.find_element(self.driver, ('xpath',
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[2]/android.widget.TextView')).click()
        self.find_element(self.driver, ('xpath',
                                                 '//android.widget.ListView[@content-desc="本地相册"]/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.TextView[1]')).click()
        self.find_element(self.driver, ('xpath',
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout')).click()
        self.find_element(self.driver, ('accessibility id', '确定')).click()
        self.find_element(self.driver, ('accessibility id', '确定')).click()
        # 发布预告
        self.find_element(self.driver, ('id', 'tv_title_fun')).click()
        self.is_element_exist(self.driver, ('id', 'discover_notice_submit_btn'))
# 我的界面》个人信息测试
    def test_case3_person_information(self):
        # 进入我的界面
        self.find_element(self.driver, ('id', 'tab_message')).click()
        # 判断昵称存在
        self.is_element_exist(self.driver, ('id', 'mine_name'))
        # 判断成长等级存在
        self.is_element_exist(self.driver, ('id', 'user_level_tv'))
        # 判断用户年龄存在
        self.is_element_exist(self.driver, ('id', 'user_gender_tv'))
        # 判断财富等级存在
        self.is_element_exist(self.driver, ('id', 'user_vip_level_iv'))
        # 判断主播等级存在
        self.is_element_exist(self.driver, ('id', 'user_anchor_level_iv'))
        # 判断认证存在
        self.is_element_exist(self.driver, ('id', 'official_cert_level_name'))
        # 判断头像存在
        self.is_element_exist(self.driver, ('id', 'my_user_photo'))
        # 判断认证标志存在
        self.is_element_exist(self.driver, ('id', 'icon_vip'))
        # 判断粉丝存在
        self.is_element_exist(self.driver, ('id', 'mine_fans'))
        # 判断关注存在
        self.is_element_exist(self.driver, ('id', 'mine_attention'))
        print('个人信息正常')
#我的详情界面
    def test_case4_details_information(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        # 进入个人中心
        self.find_element(self.driver,('id', 'my_user_photo')).click()
        # 判断昵称存在
        self.is_element_exist(self.driver, ('id', 'tv_pannel_username'))
        # 判断成长等级存在
        self.is_element_exist(self.driver, ('id', 'user_level_new_tv'))
        # 判断用户年龄存在
        self.is_element_exist(self.driver, ('id', 'user_gender_new_tv'))
        # 判断财富等级存在
        self.is_element_exist(self.driver, ('id', 'user_vip_level_new_iv'))
        # 判断主播等级存在
        self.is_element_exist(self.driver, ('id', 'user_anchor_level_new_iv'))
        # 判断认证存在
        self.is_element_exist(self.driver, ('id', 'official_cert_level_name_two'))
        #判断星座存在
        self.is_element_exist(self.driver,('id','user_constellation_new_tv'))
        # 判断头像存在
        self.is_element_exist(self.driver, ('id', 'iv_user_photo'))
        #判断id存在
        self.is_element_exist(self.driver,('name','31415411'))
        # 判断定位存在
        self.is_element_exist(self.driver, ('id', 'tv_user_location'))
        # 判断粉丝存在
        self.is_element_exist(self.driver, ('id', 'tv_user_fans_count'))
        # 判断关注存在
        self.is_element_exist(self.driver, ('id', 'tv_user_follow_count'))
        # 判断工会存在
        self.is_element_exist(self.driver, ('id', 'tv_user_union_name1'))
        #左滑操作
        self.driver.swipe(921,1249,174,1249,1000)
        self.is_element_exist(self.driver,('name', '游戏'))
        print('详情信息正常')
#个人信息编辑测试
    def test_case5_edit_information(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        # 进入个人中心
        self.find_element(self.driver,('id', 'my_user_photo')).click()
        #进入个人信息编辑界面
        self.find_element(self.driver, ('id', 'iv_user_data_edit')).click()
        '''#更换头像
        self.find_element(self.driver,('id','user_info_portrait_iv')).click()
        #拍照上传
        self.find_element(self.driver,('id','bs_list_title')).click()
        self.find_element(self.driver,('name','选择本地图片'))
        self.driver.swipe(533,1981,533,1981,1000)
        self.find_element(self.driver,('accessibility id','确定')).click()
        self.find_element(self.driver,('accessibility id','确定')).click()
        #self.find_element(self.driver,('id','top_frame')).click()
        #self.find_element(self.driver,('id','head_select_right')).click()
        #self.find_element(self.driver,('id','head_select_right')).click()'''
        #修改定位位置
        self.find_element(self.driver,('id','ui_locate_et')).click()
        #self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[5]/android.widget.RelativeLayout')).click()
        #self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[8]/android.widget.RelativeLayout')).click()
        x = random.randint(1000,1800)
        y = random.randint(1000, 1600)

        self.driver.swipe(150,x,150,x,duration=0)
        self.driver.swipe(128,y,128,y,duration=0)
        #点击保存
        self.find_element(self.driver,('id','btn_location_save')).click()
        #修改昵称
        self.find_element(self.driver,('id','user_info_nickname_et')).clear()
        #随机昵称
        nickname_depot = ['烽火流云','烽火三国','暮雪纷呈','江南烟雨']
        nickname = nickname_depot[random.randint(0,3)]
        self.find_element(self.driver,('id','user_info_nickname_et')).send_keys(nickname)
        #修改性别

        self.find_element(self.driver,('id','text1')).click()
        sex_depot = ('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]',
                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]')
        self.find_element(self.driver,('xpath',sex_depot[random.randint(0,1)])).click()
        #修改出生日期
        self.find_element(self.driver,('id','birthday_et')).click()
        x = random.randint(217,858)
        y = random.randint(1211,1443)
        self.driver.swipe(x,y,x,y,0)
        self.find_element(self.driver,('id','button1')).click()
        #修改地区
        self.find_element(self.driver,('id','ui_location_et')).click()
        z = random.randint(800,1900)
        self.driver.swipe(490,z,490,z,0)
        #兴趣标签
        self.find_element(self.driver,('id','interest_et')).click()
        interest = random.randint(2, len(self.driver.find_elements_by_class_name("android.widget.TextView")))
        #print(self.driver.find_elements_by_class_name("android.widget.TextView"))
        interest_name = self.driver.find_elements_by_class_name("android.widget.TextView")[interest].text

        self.driver.find_elements_by_class_name("android.widget.TextView")[interest].click()
        self.find_element(self.driver,('id','menu_complete')).click()
        self.assertIn(interest_name,self.driver.find_element_by_id('interest_et').text)
        #取消兴趣标签
        self.find_element(self.driver,('id','interest_et')).click()
        self.driver.find_element_by_name(interest_name).click()
        print('true')
        #点击完成
        self.find_element(self.driver,('id','menu_complete')).click()
        self.assertNotEquals(interest_name,self.driver.find_element_by_id('interest_et').text)
        #点击完成
        self.find_element(self.driver,('id','tv_user_info_finish')).click()
#粉丝列表、关注列表
    def test_case6_fan_follow(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        # 进入个人中心
        self.find_element(self.driver,('id', 'my_user_photo')).click()
        #点击进入粉丝列表
        self.find_element(self.driver,('id','tv_user_fans_count')).click()
        #判断是否进入粉丝列表
        self.is_element_exist(self.driver,('name','粉丝'))
        #点击进入个人中心,然后返回
        a = random.randint(100,800)
        b = random.randint(300,2100)
        self.driver.swipe(a,b,a,b,0)
        self.is_element_exist(self.driver,('id','tv_room_state'))
        Others_personal_center.fromothers_center(self).click()
        #关注、取消关注
        self.driver.swipe(945,350,945,350,0)
        time.sleep(2)
        self.driver.swipe(945, 350, 945, 350, 0)
        #返回个人中心
        self.find_element(self.driver,('id','iv_common_back')).click()
        #进入关注列表
        self.find_element(self.driver,('id','tv_user_follow_count')).click()
        self.is_element_exist(self.driver,('name','关注'))
        self.driver.swipe(a,b,a,b,0)
        self.is_element_exist(self.driver,('id','tv_room_state'))
        Others_personal_center.fromothers_center(self).click()
        #关注、取消关注
        self.driver.swipe(945,350,945,350,0)
        time.sleep(2)
        self.driver.swipe(945, 350, 945, 350, 0)
        #返回个人中心
        self.find_element(self.driver,('id','iv_common_back')).click()
#视频列表
    def test_case7_videolist(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        # 进入个人中心
        self.find_element(self.driver,('id', 'my_user_photo')).click()
        #判断视频数量是否存在
        self.is_element_exist(self.driver,('id','tv_video_count'))
        #判断视频长度元素是否存在
        self.is_element_exist(self.driver,('id','tv_video_duration'))
        #判断视频观看数量元素是否存在
        self.is_element_exist(self.driver,('id','tv_video_count'))
        #判断视频标题元素是否存在
        self.is_element_exist(self.driver,('id','tv_video_title'))
        #判断视频时间是否存在
        self.is_element_exist(self.driver,('id','tv_video_time'))
        #判断视频权限是否存在
        self.is_element_exist(self.driver,('name','私密'))
        #权限修改测试
        self.find_element(self.driver,('id','tv_video_state')).click()
        #私密转公开
        self.find_element(self.driver,('id','bs_list_title')).click()
            #判断公开
        self.is_element_exist(self.driver,('name','公开'))
        #公开转付费
        self.find_element(self.driver,('id','tv_video_state')).click()
        self.find_element(self.driver,('name','设为付费观看')).click()
            #设置付费价格
        self.find_element(self.driver,('id','et_pay')).send_keys('1')
        self.find_element(self.driver,('id','add_option_tv')).click()
        self.is_element_exist(self.driver,('name','付费'))
        #付费转公开
        self.find_element(self.driver,('id','tv_video_state')).click()
        self.find_element(self.driver,('name','设为公开')).click()
        self.is_element_exist(self.driver,('name','公开'))
        #公开转私密
        self.find_element(self.driver,('id','tv_video_state')).click()
        self.find_element(self.driver,('name','设为私密')).click()
        self.is_element_exist(self.driver,('name','私密'))
            #私密转公开
        self.find_element(self.driver,('id','tv_video_state')).click()
        self.find_element(self.driver,('id','bs_list_title')).click()
            #公开转付费
        self.find_element(self.driver,('id','tv_video_state')).click()
        self.find_element(self.driver,('name','设为付费观看')).click()
        self.find_element(self.driver,('id','et_pay')).send_keys('1')
        self.find_element(self.driver,('id','add_option_tv')).click()
        #付费转私密
        self.find_element(self.driver,('id','tv_video_state')).click()
        self.find_element(self.driver,('name','设为私密')).click()
        self.is_element_exist(self.driver,('name','私密'))
        #回放视频更多
        self.find_element(self.driver,('id','iv_video_operation')).click()
        self.find_element(self.driver,('name','封面变更')).click()
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[2]/android.widget.TextView')).click()
        self.find_element(self.driver,('name','相机')).click()
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout')).click()
        self.find_element(self.driver,('accessibility id','确定')).click()
        self.find_element(self.driver,('accessibility id','确定')).click()
        #删除回放测试
        self.find_element(self.driver,('id','iv_video_operation')).click()
        self.find_element(self.driver,('name','删除')).click()
        self.find_element(self.driver,('id','button1')).click()
        #取消测试
        self.find_element(self.driver,('id','iv_video_operation')).click()
        self.find_element(self.driver,('name','取消')).click()
#个人形象视频上传
    def test_case8_imagedisplay(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        # 进入个人中心
        self.find_element(self.driver,('id', 'my_user_photo')).click()
        #进入播放页
        self.find_element(self.driver,('id','tv_image_name')).click()
        self.driver.swipe(474,1671,504,671,1000)
        #添加个人形象视频
        self.find_element(self.driver,('id','iv_user_image_add')).click()
        self.find_element(self.driver,('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView[1]')).click()
        self.find_element(self.driver,('id','button_complete')).click()
        self.is_element_exist(self.driver,('id','iv_image_thumb'))
#贡献榜及礼物界面
    def test_case9_rank_gift(self):
        #进入我的界面
        self.find_element(self.driver,('id','tab_message')).click()
        # 进入个人中心
        self.find_element(self.driver,('id', 'my_user_photo')).click()
        #查看礼物面板
        self.find_element(self.driver,('id','tv_gift_name')).click()
        #查看排行榜
        self.find_element(self.driver,('id','iv_right')).click()
        self.find_element(self.driver,('id','tab_week')).click()
        self.find_element(self.driver,('id','tab_year')).click()
        self.find_element(self.driver,('id','tv_title_fun')).click()
        self.find_element(self.driver,('id','iv_common_back')).click()
        self.find_element(self.driver, ('id', 'iv_common_back')).click()
if __name__ == '__main__':
   discover = unittest.defaultTestLoader.discover(start_dir='.', pattern='unittest*.py')
   runner = unittest.TextTestRunner()
   runner.run(discover)
