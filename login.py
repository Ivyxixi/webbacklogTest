#-*- coding:UTF-8 -*-
#@ 2017.7.20
#@ author:FuYuQian
#@ content:UI test for Resource allocation vs P2 contract
# @2017.7.24
# @author:FuYuQian
# @content: write log file: myapp.log

from selenium import webdriver
import time
from configLogFormat import *

class login:
    def __init__(self):
        # 调用logFormat类来设置log输出格式
        LogFormat()
        logging.info('the tests of login starts.')
        try:
            self.driver=webdriver.Chrome()
            self.url="http://127.0.0.1:8000/webbacklog/login/?next=/webbacklog/rscalcvsp2/"
            self.driver.get(self.url)
            logging.info("页面加载正常")
        except:
            logging.error("页面加载失败")


    def __del__(self):
        self.driver.quit()
        logging.info('the tests of login ends.')

    #测试登录的logo
    def loginLogo(self):
        driver=self.driver
        try:
            logo =driver.find_element_by_link_text("Webbacklog")
            logo.click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
            logging.info('Webbacklog的链接正常.')
        except:
            logging.error('Webbacklog的链接错误.')
        try:
            t=driver.find_element_by_xpath("/html/body/div/div[1]/a/b").text
            logging.info('Sign in to start your session文本正常')
        except:
            logging.error('Sign in to start your session文本错误')
        print t
        return t

    #测试登录的输入框login-box-body
    def loginBox(self):
        driver=self.driver
        succ=1
        try:
            driver.find_element_by_class_name("login-box-body")
            logging.info("login-box-body登录的输入框正常")
        except:
            succ=0
            logging.error("login-box-body登录的输入框错误")
        return succ

    #测试输入提示框login-box-msg
    def loginBoxMsg(self):
        driver=self.driver
        try:
            print driver.find_element_by_class_name("login-box-msg").text
            logging.info("login-box-msg输入提示框正常")
        except:
            logging.error("login-box-msg输入提示框错误")
        return driver.find_element_by_class_name("login-box-msg").text

    #测试email输入
    def emailId(self):
        driver=self.driver
        succ=1
        try:
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/input").clear()
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/input").send_keys("123")
            time.sleep(1)
            logging.info("账号输入框正常.")
        except:
            succ=0
            logging.error("账号输入框错误.")
        return succ

    #测试密码输入
    def passwd(self):
        driver=self.driver
        succ=1
        try:
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input").clear()
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input").send_keys("123456")
            time.sleep(1)
            logging.info("密码输入框正常.")
        except:
            succ=0
            logging.error("密码输入框错误.")
        return succ

    #测试邮箱输入的图标
    def Icon_email(self):
        driver=self.driver
        time.sleep(1)
        succ=1
        try:
            #driver.find_element_by_class_name("glyphicon glyphicon-envelope form-control-feedback")
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/span")
            logging.info("账号输入框右侧图标正常")
        except:
            succ=0
            logging.error("账号输入框右侧图标错误")
        print succ
        return succ

    #测试密码输入的图标
    def Icon_passwd(self):
        driver = self.driver
        time.sleep(1)
        succ = 1
        try:
            #driver.find_element_by_class_name("glyphicon glyphicon-lock form-control-feedback")
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/span")
            logging.info("密码输入框右侧图标正常")
        except:
            succ = 0
            logging.error("密码输入框右侧图标错误")
        print succ
        return succ

    #测试remember me的复选框
    def RememerMe(self):
        driver=self.driver
        time.sleep(1)
        succ=1
        try:
            driver.find_element_by_css_selector('input[type=checkbox]').click()
            time.sleep(1)
            logging.info("‘记住我’复选框右侧图标正常")
        except:
            succ=0
            logging.error("‘记住我’复选框右侧图标错误")
        return succ

    #测试登录按钮
    def submit(self):
        driver=self.driver
        time.sleep(1)
        succ=1
        try:
            driver.find_element_by_css_selector('button[type=submit]').click()
            time.sleep(0.5)
            logging.info("登录按键正常.")
        except:
            succ=0
            logging.error("登录按键错误.")
        return succ

def myTest():
    myT=login()
    #myT.loginLogo()
    #myT.loginBox()
    #myT.loginBoxMsg()
    #myT.emailId()
    #myT.passwd()
    #myT.Icon_email()
    #myT.Icon_passwd()
    #myT.RememerMe()
    #myT.submit()

if __name__=='__main__':
    myTest()