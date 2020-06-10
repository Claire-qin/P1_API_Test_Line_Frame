#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: get_user_fans_list_testcse.py
# @time:2020/6/10 17:30 


import unittest
import json
import jsonpath
from utils import common_api
from utils.config_util import cfg

class GetUesrFansListTestcase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = cfg.hosts
    def tearDown(self) -> None:
        pass

    def test_get_user_fans_list(self):
        '''获取标签下粉丝列表''' #单引号
        token = common_api.get_access_token_value()
        res = common_api.get_user_fans_list_api(token,100)
        self.assertEqual(res.json()['count'], 2)

if __name__ == '__main__':
    unittest.main()