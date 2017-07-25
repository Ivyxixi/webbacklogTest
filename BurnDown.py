#-*- coding:UTF-8  -*-
# @2017.7.19
# @author:FuYuQian
# @content:UI TEST OF BURN DOWN
# @2017.7.24
# @author:FuYuQian
# @content: write log file: myapp.log


from selenium import webdriver
from configLogFormat import *
import time
class BurnDown:
    def __init__(self):
        LogFormat()
        logging.info("the tests of BurnDown starts.")
        try:
            self.driver=webdriver.Chrome()
            self.url="http://127.0.0.1:8000/webbacklog/releaseburndown/"
            self.driver.get(self.url)
            logging.info("load web page successfully.")
        except:
            logging.error("load web page failed.")

    def __del__(self):
        self.driver.quit()
        logging.info("the tests of BurnDown ends.\n")

    #测试H1的title,输出控制台并返回h1.title
    def H1title(self):
        driver=self.driver
        try:
            h1=driver.find_element_by_tag_name("h1")
            print(h1.text)
            logging.info("h1-title run successfully.")
        except:
            logging.error("h1-title run failed.")
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
            logging.info("the link of Home run successfully.")
        except:
            succ=0
            logging.error("the link of Home run failed.")
        mylist[0]=succ

        try:
            print driver.find_element_by_link_text("Release mgmt.").text
            mylist[1]=driver.find_element_by_link_text("Release mgmt.").text
            time.sleep(0.5)

            print driver.find_element_by_xpath("/html/body/div/div[1]/section[1]/ol/li[3]").text
            mylist[2] = driver.find_element_by_xpath("/html/body/div/div[1]/section[1]/ol/li[3]").text
            time.sleep(0.5)
            logging.info('the text of breadcrumb run successfully.')
        except:
            logging.error("the text of breadcrumb run failed.")
        return mylist

    #测试h3的文本和帮助按钮,结果输出并用mylist[0]文本值、mylist[1]帮助按钮是否正常来返回
    def h3(self):
        mylist=["0","0"]
        driver=self.driver
        try:
            print driver.find_element_by_id("panel-title").text
            mylist[0]=driver.find_element_by_id("panel-title").text
            logging.info("the panel-title run successfully.")
        except:
            logging.error("the panel-title run failed.")

        succ=1
        try:
            driver.find_element_by_class_name("help").click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
            logging.info("the button of help run successfully.")
        except:
            succ=0
            logging.error("the button of help run failed.")
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
            logging.info("the text of main-footer run successfully.")
        except:
            succ1=0
            logging.error("the text of main-footer run failed.")
        mylist[0]=succ1

        succ2=1
        try:
            driver.find_element_by_link_text("Nokia").click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
            logging.info("the link of Nokia run successfully.")
        except:
            succ2=0
            logging.error("the link of Nokia run failed.")
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
            logging.info("the dropdown of systemRealse run successfully.")
        except:
            logging.error("the dropdown of systemRealse run failed.")
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
            logging.info("the dropdown of Team run successfully.")
        except:
            logging.error("the dropdown of Team run failed.")
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
            logging.info("the canvas run successfully.")
        except:
            succ=0
            logging.error("the canvas run failed.")
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