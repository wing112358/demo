import sys
import unittest
import requests
import json

sys.path.append("../..")   # 统一将包的搜索路径提升到项目根目录下

from lib.read_excel import *
from lib.case_log import log_case_info, data_path


class BaseCase(unittest.TestCase):   # 继承unittest.TestCase
    @classmethod
    def setUpClass(cls):
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_list(data_path, cls.__name__)

    def get_case_data(self, case_name):
        return get_test_data(self.data_list, case_name)

    def send_request(self, case_data):
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        args = case_data.get('data')
        headers = case_data.get('headers')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')

        if method.upper() == 'GET':   # GET类型请求
            res = requests.get(url=url, params=json.loads(args))
            log_case_info(case_name, url, json.dumps(json.loads(expect_res), sort_keys=True).encode(("utf-8")),
            json.dumps(res.json(), ensure_ascii=False, sort_keys=True), args)
            self.assertDictEqual(res.json(), json.loads(expect_res))
            print("调用成功且断言成功-GET----" + case_name)

        elif data_type.upper() == 'FORM':   # 表单格式请求
            res = requests.post(url=url, data=json.loads(args), headers=json.loads(headers))
            log_case_info(case_name, url, args, expect_res, res.text)
            self.assertEqual(res.text, expect_res)
            print("调用成功且断言成功-FORM-----"+case_name)
        else:
            res = requests.post(url=url, json=json.loads(args), headers=json.loads(headers))   # JSON格式请求
            log_case_info(case_name, url, json.dumps(json.loads(expect_res), sort_keys=True).encode(("utf-8") ),json.dumps(res.json(), ensure_ascii=False, sort_keys=True),args)
            self.assertDictEqual(res.json(), json.loads(expect_res))
            print("调用成功且断言成功-JSON-----"+case_name)