# -*- coding:UTF-8 -*-
# @2017.7.21
# @author:FuYuQian
# content: practise of logging


from selenium import webdriver
import logging
from logging.handlers import RotatingFileHandler
import time

#1、日志级别
#   日志一共分成5个等级，从低到高分别是：DEBUG INFO WARNING ERROR CRITICAL。
#   DEBUG：   详细的信息,通常只出现在诊断问题上
#   INFO：    确认一切按预期运行
#   WARNING： 一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
#   ERROR：   更严重的问题,软件没能执行一些功能
#   CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行
#   这5个等级，分别对应5种打日志的方法： debug 、info 、warning 、error 、critical。
#   默认的是WARNING，当在WARNING或之上时才被跟踪。
#2、日志输出
#   两种方式记录跟踪，一种输出控制台，另一种记录到文件（日志文件）


class mylogging:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "http:\\www.baidu.com"
        self.driver.get(self.url)

    def __del__(self):
        self.driver.quit()

    #result:  logging将日志打印到屏幕，日志级别为WARNING；
    #日志级别：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
    def test1(self):
        logging.debug('debug message')
        logging.info('info message')
        logging.warning('warn message')

    #利用basicConfig()函数来输出
    #result: 按照指定的格式输出
    #   +Fri, 21 Jul 2017 14:00:34 loggingPractise.py[line:33] DEBUG debug message
    #   +Fri, 21 Jul 2017 14:00:34 loggingPractise.py[line:34] INFO info message
    #   +Fri, 21 Jul 2017 14:00:34 loggingPractise.py[line:35] WARNING warn message
    #notes:
    #logging.basicConfig函数各参数:
    #   filename: 指定日志文件名
    #   filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
    #   format:   指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
    #   %(levelno)s:   打印日志级别的数值
    #   %(levelname)s: 打印日志级别名称
    #   %(pathname)s:  打印当前执行程序的路径，其实就是sys.argv[0]
    #   %(filename)s:  打印当前执行程序名
    #   %(funcName)s:  打印日志的当前函数
    #   %(lineno)d:    打印日志的当前行号
    #   %(asctime)s:   打印日志的时间
    #   %(thread)d:    打印线程ID
    #   %(threadName)s:打印线程名称
    #   %(process)d:   打印进程ID
    #   %(message)s:   打印日志信息
    #   datefmt:       指定时间格式，同time.strftime()
    #   level:         设置日志级别，默认为logging.WARNING
    #   stream:        指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
    def test2basicConfig(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='myapp.log',
                            filemode='w')
        logging.debug('debug message')
        logging.info('info message')
        logging.warning('warn message')

    #将日志同时输出到文件和屏幕
    def test3Handler(self):

        #以下为将文件写入日志文件中
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='myapp.log',
                            filemode='w')

        #以下为将文件输出到控制台
        #定义一个streamHandler,将Info级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对应文件
        console=logging.StreamHandler()
        #定义能输出的最高类型为INFO
        console.setLevel(logging.INFO)
        formatter=logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        #将logger添加到handler里面
        logging.getLogger('').addHandler(console)

        logging.debug('debug message')
        logging.info('info message')
        logging.warning('warn message')

    # 日志回滚
    # 定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
    # logging的几种回滚方式：
    #   logging.StreamHandler: 日志输出到流，可以是sys.stderr、sys.stdout或者文件
    #   logging.FileHandler: 日志输出到文件日志回滚方式，实际使用时用RotatingFileHandler和TimedRotatingFileHandler
    #   logging.handlers.BaseRotatingHandler
    #   logging.handlers.RotatingFileHandler
    #   logging.handlers.TimedRotatingFileHandler
    #   logging.handlers.SocketHandler: 远程输出日志到TCP/IP sockets
    #   logging.handlers.DatagramHandler:  远程输出日志到UDP sockets
    #   logging.handlers.SMTPHandler:  远程输出日志到邮件地址
    #   logging.handlers.SysLogHandler: 日志输出到syslog
    #   logging.handlers.NTEventLogHandler: 远程输出日志到Windows NT/2000/XP的事件日志
    #   logging.handlers.MemoryHandler: 日志输出到内存中的制定buffer
    #   logging.handlers.HTTPHandler: 通过"GET"或"POST"远程输出到HTTP服务器
    #   注：StreamHandler和FileHandler是常用的日志处理方式，所以直接包含在logging模块中，而其他方式则包含在logging.handlers模块中

    def test4Rotate(self):
        Rthandler = RotatingFileHandler('myapp.log', maxBytes=10 * 1024 * 1024, backupCount=5)
        Rthandler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        Rthandler.setFormatter(formatter)
        #logging有一个日志处理的主对象，其它处理方式都是通过addHandler添加进去的
        logging.getLogger('').addHandler(Rthandler)

    #有多个模块需要输出日志时，日志的输出顺序就是模块的执行顺序








def myTest():
    myT = mylogging()
    #myT.test1()
    #myT.test2basicConfig()
    #myT.test3Handler()
    myT.test4Rotate()


if __name__ == '__main__':
    myTest()