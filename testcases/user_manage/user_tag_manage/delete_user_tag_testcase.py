#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: delete_user_tag_testcase.py
# @time:2020/6/10 17:29

import unittest
import json
import jsonpath
from utils import common_api
from utils.config_util import cfg

class DeleteUesrTagTestcase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = cfg.hosts
    def tearDown(self) -> None:
        pass

    def test_delete_user_tag(self):
        '''删除公众号已创建的标签''' #单引号
        token = common_api.get_access_token_value()
        res = common_api.delete_user_tag_api(token,194)
        self.assertEqual(res.json()['errcode'], 0)

if __name__ == '__main__':
    unittest.main()