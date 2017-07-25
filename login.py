#-*- coding:UTF-8 -*-
#@ 2017.7.20
#@ author:FuYuQian
#@ content:UI test for Resource allocation vs P2 contract
#@ 2017.7.24
#@ author:FuYuQian
#@ content: write log file: myapp.log

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
            logging.info("load web page successfully.")
        except:
            logging.error("load web page failed.")


    def __del__(self):
        self.driver.quit()
        logging.info('the tests of login ends.\n')

    #测试登录的logo
    def loginLogo(self):
        driver=self.driver
        try:
            logo =driver.find_element_by_link_text("Webbacklog")
            logo.click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
            logging.info("the link of 'Webbacklog' run successfully.")
        except:
            logging.error("the link of 'Webbacklog' run failed.")
        try:
            t=driver.find_element_by_xpath("/html/body/div/div[1]/a/b").text
            logging.info("the text of 'Sign in to start your session' run successfully.")
        except:
            logging.error("the text of 'Sign in to start your session' run failed.")
        print t
        return t

    #测试登录的输入框login-box-body
    def loginBox(self):
        driver=self.driver
        succ=1
        try:
            driver.find_element_by_class_name("login-box-body")
            logging.info("the 'login-box-body' run successfully.")
        except:
            succ=0
            logging.error("the 'login-box-body' run failed.")
        return succ

    #测试输入提示框login-box-msg
    def loginBoxMsg(self):
        driver=self.driver
        try:
            print driver.find_element_by_class_name("login-box-msg").text
            logging.info("the 'login-box-msg' run successfully.")
        except:
            logging.error("the 'login-box-msg' run failed.")
        return driver.find_element_by_class_name("login-box-msg").text

    #测试email输入
    def emailId(self):
        driver=self.driver
        succ=1
        try:
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/input").clear()
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/input").send_keys("123")
            time.sleep(1)
            logging.info("the input of user-account run successfully.")
        except:
            succ=0
            logging.error("the input of user-account run failed.")
        return succ

    #测试密码输入
    def passwd(self):
        driver=self.driver
        succ=1
        try:
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input").clear()
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input").send_keys("123456")
            time.sleep(1)
            logging.info("the input of user-passwd run successfully.")
        except:
            succ=0
            logging.error("the input of user-passwd run failed.")
        return succ

    #测试邮箱输入的图标
    def Icon_email(self):
        driver=self.driver
        time.sleep(1)
        succ=1
        try:
            #driver.find_element_by_class_name("glyphicon glyphicon-envelope form-control-feedback")
            driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/span")
            logging.info("the icon of user-account run successfully.")
        except:
            succ=0
            logging.error("the icon of user-account run failed.")
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
            logging.info("the icon of user-passwd run successfully.")
        except:
            succ = 0
            logging.error("the icon of user-passwd run failed.")
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
            logging.info("the checkbox of remember me run successfully.")
        except:
            succ=0
            logging.error("the checkbox of remember me run failed.")
        return succ

    #测试登录按钮
    def submit(self):
        driver=self.driver
        time.sleep(1)
        succ=1
        try:
            driver.find_element_by_css_selector('button[type=submit]').click()
            time.sleep(0.5)
            logging.info("the button of submit run successfully.")
        except:
            succ=0
            logging.error("the button of submit run failed.")
        return succ

def myTest():
    myT=login()
    #myT.loginLogo()
    #myT.loginBox()
    #myT.loginBoxMsg(
    #myT.emailId()
    #myT.passwd()
    #myT.Icon_email()
    #myT.Icon_passwd()
    #myT.RememerMe()
    #myT.submit()

if __name__=='__main__':
    myTest()