import unittest,random.tome,re
from utils.common_function import BaseFunction


class TestCases(BaseFunction):
    def setUp(self) -> None:
        print('start')
#发布预告
    def test_001_release_notice(self):
        try:
            self.find_element('id','iv_one_dialog_close').click()
            self.find_element('id','btn_sign').click()
            self.find_element('id', 'btn_sign').click()
        except:
            pass
        self.find_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[4]/android.view.View')
        