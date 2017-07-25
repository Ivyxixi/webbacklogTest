#-*- coding:utf-8  -*-
#@ 2017/7/24
#@ author:FuYuQian
#@ content: config log format use the logging.basicConfig so that it can be used repeatedly.
#@ usage:LogFormat()

import logging

class LogFormat:
    def __init__(self):
        self.basicConfig()

    # 设置logging file的输出等级为INFO及以上，并设置格式等
    def basicConfig(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='myapp.log',
                            filemode='w')

    def __del__(self):
        pass
