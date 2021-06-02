import unittest
from utils.common_function import BaseFunction
class Others_personal_center(BaseFunction):
    def setUp(self):
        self.init_driver()
    def fromothers_center(self):
        return self.driver.find_element_by_id('iv_go_back')