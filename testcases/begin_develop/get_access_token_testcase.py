#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: get_access_token_testcase.py
# @time:2020/6/9 18:22

import unittest
from utils import common_api
from utils.config_util import cfg

class GetAccesstokenTestcase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = cfg.hosts
    def tearDown(self) -> None:
        pass

    def test_get_accesstoken(self):
        '''获取token测试''' #单引号
        res = common_api.get_access_token_api('client_credential',
                                 'wxb9013645f9c6f66b',
                                 '8c80367d3fac3cb6d3dc910fe6416436')
        self.assertEqual(res.json()['expires_in'],7200)

    def test_appid_error(self):
        res = common_api.get_access_token_api('client_credential',
                                 'wxb9013645f9c6',
                                 '8c80367d3fac3cb6d3dc910fe6416436')
        self.assertEqual(res.json()['errcode'], 40013)

if __name__ == '__main__':
    unittest.main()