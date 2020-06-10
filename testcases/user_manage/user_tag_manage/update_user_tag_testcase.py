#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: update_user_tag_testcase.py
# @time:2020/6/10 17:29 


import unittest
from utils import common_api
from utils.config_util import cfg
import json
import jsonpath

class UpdateUesrTagTestcase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = cfg.hosts
    def tearDown(self) -> None:
        pass

    def test_update_user_tag(self):
        '''修改公众号已创建的标签''' #单引号
        token = common_api.get_access_token_value()
        res = common_api.update_user_tag_api(token,'100','广东人')
        # print(res.content.decode('utf-8'))
        self.assertEqual(res.json()['errcode'], 0)

if __name__ == '__main__':
    unittest.main()