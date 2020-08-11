import sys
import unittest
import requests
import os  # 增加了一个os，需要用来组装路径
from lib.read_excel import *    #导入读excel的方法
sys.path.append("../..")      # 提升2级到项目根目录下


from lib.case_log import *

from act.case.basecase import *

class TestDemo(BaseCase):

    @classmethod
    def setUpClass(cls) : #整个测试类只执行一次
        cls.data_list = excel_to_list(os.path.join(data_path,"test_demo_data.xlsx"), "TestDemo")


    def test_demo_post_normal(self):
        case_data =self.get_case_data("test_demo_post_normal")
        self.send_request(case_data)

    def test_demo_get_normal(self):
        case_data = self.get_case_data("test_demo_get_normal")
        self.send_request(case_data)



if __name__ == '__main__':
        unittest.main(verbosity=2)
