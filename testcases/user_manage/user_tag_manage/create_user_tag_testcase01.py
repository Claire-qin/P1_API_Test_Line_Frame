#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: create_user_tag.py
# @time:2020/6/9 20:46 

import unittest
from utils import common_api
from utils.config_util import cfg


class CreateUsertagTestcase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = cfg.hosts
    def tearDown(self) -> None:
        pass   # 可调用删除标签

    def test_create_user_tag(self):
        token = common_api.get_access_token_value()
        res = common_api.create_user_tag_api(token,'newdream110')
        self.assertEqual(res.json()['tag']['name'],'newdream110')

if __name__ == '__main__':
    unittest.main()