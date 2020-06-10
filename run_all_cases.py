#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: run_all_cases.py
# @time:2020/6/9 11:12


# 接口线性框架一定要把
import time,os
import unittest
import HTMLTestRunner   # 第一种  不好看的报告
from utils.config_util import cfg
from utils import HTMLTestReportCN

# 加载测试集合
def get_testsuite():
        discover = unittest.defaultTestLoader.discover(start_dir='./testcases',
                                                       pattern='*_testcase.py',
                                                       top_level_dir='./testcases')
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)
        return all_suite
# 执行方式一：HTMLTestRunner
# now_time = time.strftime('%Y-%m-%d %H-%M-%S') #不覆盖：按日期生成
# html_report = os.path.join(cfg.report_path,'result_%s.html'%now_time)
# file = open(html_report,'wb') #html文件必须以二进制方式写入，wb
# html_runner = HTMLTestRunner.HTMLTestRunner(stream=file,
#                                             title='API测试',
#                                             description='测试描述')
# html_runner.run(get_testsuite())

# 执行方式二：HTMLTestReportCN执行测试用例
report_dir = HTMLTestReportCN.ReportDirectory(cfg.report_path+'/') # 自定义测试报告目录
report_dir.create_dir("API_TEST")# 创建目录
dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path') #报告的目录
report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')

fp = open(report_path, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                         title="API_TEST",
                                         description="Newdream_p1",
                                         tester='qch')
runner.run(get_testsuite())
fp.close()