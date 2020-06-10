#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: get_user_tag_testcase.py
# @time:2020/6/10 17:28

import unittest
import json
import jsonpath
from utils import common_api
from utils.config_util import cfg

class GetUesrTagTestcase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = cfg.hosts
    def tearDown(self) -> None:
        pass

    def test_get_user_tag(self):
        '''获取公众号已创建的标签''' #单引号
        token = common_api.get_access_token_value()
        res = common_api.get_uesr_tag_api(token)
        res_01 = res.content.decode('utf-8')
        json_data = json.loads(res_01)  # josn对象
        value = jsonpath.jsonpath(json_data, '$.tags[0].id')
        self.assertEqual(value[0],2)

if __name__ == '__main__':
    unittest.main()