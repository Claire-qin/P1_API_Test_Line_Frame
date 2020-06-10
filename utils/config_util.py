#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: element_data_util.py
# @time:2020/5/8 10:49

import os
import configparser

current_dir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(current_dir, "..", 'config',"config.ini")

class ConfigUtil(object):
    def __init__(self,path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path,encoding='utf-8')

    @property
    def hosts(self):
        url_value = self.cfg.get('default','hosts')
        return url_value

    @property
    def report_path(self):
        report_path_value = self.cfg.get('default', 'report_path')
        return report_path_value

cfg = ConfigUtil()

if __name__=='__main__':
    config = ConfigUtil()
    print(cfg.hosts)
    print(cfg.report_path)
