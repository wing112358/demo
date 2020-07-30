import unittest
import sys
from act.case.demo.test_demo import TestDemo
sys.path.append("../..")

smoke_suite = unittest.TestSuite()  # 自定义的TestSuite
smoke_suite.addTests([TestDemo('test_demo_post_normal'), TestDemo('test_demo_get_normal')])

def get_suite(suite_name):    # 获取TestSuite方法
    return globals().get(suite_name)