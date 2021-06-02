import unittest

class Testcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.uid = 1
        print('开始测试')
    @classmethod
    def tearDownClass(cls):
        print('测试结束')
    def setUp(cls):
        print('开始执行用例')
    def tearDown(cls):
        print('用例执行结束')
   # def __init__(self):
       # self.cid = 1
    def test_case1_run(cls):
        print('第一条用例')
        print(cls.uid)
    def test_case2_drink(cls):
        cls.test_case1_run()
        print('第二条用例')
if __name__ == '__main__':
   discover = unittest.defaultTestLoader.discover(start_dir='.', pattern='unittest*.py')
   runner = unittest.TextTestRunner()
   runner.run(discover)