#-*- coding:UTF-8  -*-
# @2017,7,19
# @author:fuYuQian
# @content:UI TEST OF BURN DOWN
# @log file: myapp.log

from selenium import webdriver
from configLogFormat import *
import time
class BurnDown:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.url="http://127.0.0.1:8000/webbacklog/releaseburndown/"
        self.driver.get(self.url)
        LogFormat()
        logging.info("the tests of BurnDown starts.")

    def __del__(self):
        self.driver.quit()
        logging.info("the tests of BurnDown ends.")

    #测试H1的title,输出控制台并返回h1.title
    def H1title(self):
        driver=self.driver
        try:
            h1=driver.find_element_by_tag_name("h1")
            print(h1.text)
            logging.info("h1-title正常")
        except:
            logging.error("h1-title错误")
        return h1.text

    # 测试右边栏的提示,输出控制台并通过mylist[]返回，便于测试
    def ol(self):
        driver=self.driver
        mylist=[[0] for i in range (3)]
        succ=1
        try:
            driver.find_element_by_link_text("Home").click()
            driver.back()
            time.sleep(0.5)
            logging.info("Home正常")
        except:
            succ=0
            logging.error("Home错误")
        mylist[0]=succ

        try:
            print driver.find_element_by_link_text("Release mgmt.").text
            mylist[1]=driver.find_element_by_link_text("Release mgmt.").text
            time.sleep(0.5)

            print driver.find_element_by_xpath("/html/body/div/div[1]/section[1]/ol/li[3]").text
            mylist[2] = driver.find_element_by_xpath("/html/body/div/div[1]/section[1]/ol/li[3]").text
            time.sleep(0.5)
            logging.info('右边栏文本正常')
        except:
            logging.error("右边栏文本错误")
        return mylist

    #测试h3的文本和帮助按钮,结果输出并用mylist[0]文本值、mylist[1]帮助按钮是否正常来返回
    def h3(self):
        mylist=["0","0"]
        driver=self.driver
        try:
            print driver.find_element_by_id("panel-title").text
            mylist[0]=driver.find_element_by_id("panel-title").text
            logging.info("panel-title正常")
        except:
            logging.error("panel-title错误")

        succ=1
        try:
            driver.find_element_by_class_name("help").click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
            logging.info("help按键正常")
        except:
            succ=0
            logging.error("help按键错误")
        mylist[1]=succ
        return mylist


    #测试footer的文本显示和“nokia"的链接,并返回测试结果
    def footer(self):
        driver=self.driver
        driver.get(self.url)
        time.sleep(1)
        mylist=[0,0]
        succ1=1
        try:
            print driver.find_element_by_class_name("main-footer").text
            mylist[0]=driver.find_element_by_class_name("main-footer").text
            logging.info("main-footer文本正常")
        except:
            succ1=0
            logging.error("main-footer文本错误")
        mylist[0]=succ1

        succ2=1
        try:
            driver.find_element_by_link_text("Nokia").click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
            logging.info("Nokia链接正常")
        except:
            succ2=0
            logging.error("Nokia链接错误")
        mylist[1]=succ2
        return mylist

    #测试systemRelease的下拉框,并返回各个下拉框的值
    def systemRealse(self):
        driver=self.driver
        try:
            mylist=[[0] for i in range(14)]
            driver.find_element_by_id("systemRelease").click()
            time.sleep(1)
            s=1
            while s<=14:
                xpath="/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[1]/div[1]/ul/li["+str(s)+"]/a"
                name=driver.find_element_by_xpath(xpath).text
                print name
                mylist[s-1]=name
                s=s+1
            logging.info("systemRealse下拉框正常")
        except:
            logging.error("systemRealse下拉框错误")
        return mylist

   #测试Team的下拉框,并返回各个下拉框的值
    def Team(self):
        driver=self.driver
        time.sleep(1)
        try:
            mylist=[[0] for i in range(3)]
            driver.find_element_by_id("systemRdCmt").click()
            time.sleep(1)
            s=1
            while s<=3:
                xpath="/html/body/div/div[1]/section[2]/div/section/div/div[2]/div[1]/div[2]/ul/li["+str(s)+"]/a"
                name=driver.find_element_by_xpath(xpath).text
                print name
                mylist[s-1]=name
                s=s+1
            logging.info("Team下拉框正常")
        except:
            logging.error("Team下拉框错误")
        return mylist

        # 测试Team的下拉框,并返回各个下拉框的值

    #测试画布是否存在，存在的haul返回值1
    def canvas(self):
        driver = self.driver
        time.sleep(1)
        succ=1
        try:
            driver.find_element_by_tag_name("canvas")
            time.sleep(0.5)
            logging.info("canvas画布正常")
        except:
            succ=0
            logging.error("canvas画布错误")
        return succ


def myTest():
    myT=BurnDown()
    #myT.H1title()
    #myT.ol()
    #myT.h3()
    #myT.footer()
    #myT.systemRealse()
    #myT.Team()
    #myT.canvas()

if __name__ == '__main__':
    myTest()