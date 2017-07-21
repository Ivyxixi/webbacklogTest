#coding=utf-8
#2017/7/18
#author:Sunxia
#task:Release Milestones & Resource Allocation To Release

from selenium import webdriver
import time
import logging

class Selenium_Resource_Allocation_To_Release:

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.fh = logging.FileHandler(r"./log.txt")
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)

        self.driver = webdriver.Chrome()
        self.url="http://127.0.0.1:8000/webbacklog/"
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(1)
        self.driver.find_element_by_link_text("Resource mgmt.").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Resource allocation to releases").click()
        time.sleep(1)

    # 返回页面title
    def Find_title_Resource_Allocation_To_Release(self):
        try:
            return self.driver.find_element_by_tag_name("h1").text, self.driver.find_element_by_tag_name("h2").text, self.driver.find_element_by_tag_name("h3").text
        except:
            self.logger.exception("The 'Find_title_Resource_Allocation_To_Release' method Exception Logged")

    # 验证Release mgmt和Release Milestonss文字是否显示
    def Find_link_Test(self):
        try:
            text1 = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[1]/ol/li[2]").text
            text2 = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[1]/ol/li[3]").text
            return text1, text2
        except:
            self.logger.exception("The 'Find_link_Test' method Exception Logged")

    #点击Home文字链接
    def Click_Home(self):
        string = ""
        try:
            time.sleep(1)
            self.driver.find_element_by_link_text("Home").click();
            time.sleep(1)
            self.driver.back()
            string = "Success"
            self.logger.info("The 'Click_Home' method running Successfully")
        except:
            string = "Error :Element in method 'Click_Home' Not Founded"
            self.logger.exception("The 'Click_Home' method Exception Logged")
        return string

    #点击问号按钮并关闭
    def Click_question_Button(self):
        string = ""
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[1]/div[1]/div/div[1]/i").click();
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='resourceModal']/div/div/div/div/div[1]/button").click()
            time.sleep(1)
            string = "Success"
            self.logger.info("The 'Click_question_Button' method running Successfully")
        except:
            string = "Error :Element in method 'Click_question_Button' Not Founded"
            self.logger.exception("The 'Click_question_Button' method Exception Logged")
        return string

    #测试第一个图形按钮
    def Click_First_Button(self):
        time.sleep(1)
        string = ""
        try:
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='n4']").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[2]/div[1]/div[1]/div[1]/ul/li[2]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='n4']").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[2]/div[1]/div[1]/div[1]/ul/li[3]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='n4']").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[2]/div[1]/div[1]/div[1]/ul/li[4]/a").click()
            time.sleep(1)
            string = "Success"
            self.logger.info("The 'Click_First_Button' method running Successfully")
        except:
            string = "Error :Element in method 'Click_First_Button' Not Founded"
            self.logger.exception("The 'Click_First_Button' method Exception Logged")
        return string

    #测试第二个图形按钮
    def Click_Second_Button(self):
        time.sleep(1)
        string = ""
        try:
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='n5']").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[2]/div[1]/div[1]/div[2]/ul/li[2]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='n5']").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[2]/div[1]/div[1]/div[2]/ul/li[5]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='n5']").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[2]/div[1]/div[1]/div[2]/ul/li[14]/a").click()
            time.sleep(1)
            string = "Success"
            self.logger.info("The 'Click_Second_Button' method running Successfully")
        except:
            string = "Error :Element in method 'Click_Second_Button' Not Founded"
            self.logger.exception("The 'Click_Second_Button' method Exception Logged")
        return string


    #测试第三个图形按钮
    def Click_Third_Button(self):
        time.sleep(1)
        string = ""
        try:
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='systemRelease']").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[2]/div[1]/div[1]/div[3]/ul/li[2]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='systemRelease']").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[2]/div[1]/div[1]/div[3]/ul/li[5]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='systemRelease']").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[2]/div[1]/div[1]/div[3]/ul/li[35]/a").click()
            time.sleep(1)
            string = "Success"
            self.logger.info("The 'Click_Third_Button' method running Successfully")
        except:
            string = "Error :Element in method 'Click_Third_Button' Not Founded"
            self.logger.exception("The 'Click_Third_Button' method Exception Logged")
        return string

    #测试第四个图形按钮
    def Click_Fourth_Button(self):
        time.sleep(2)
        string = ""
        try:
            time.sleep(0.5)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[2]/div[1]/div[1]/div[4]/button").click()
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[2]/div[1]/div[1]/div[4]/div/ul/li[1]/a").click()
            time.sleep(1)
            string = "Success"
            self.logger.info("The 'Click_Fourth_Button' method running Successfully")
        except:
            string = "Error :Element in method 'Click_Fourth_Button' Not Founded"
            self.logger.exception("The 'Click_Fourth_Button' method Exception Logged")
        return string

    #Pipeline Info时间选择测试
    def Date_Select(self):
        time.sleep(2)
        string = ""
        try:
            self.driver.find_element_by_xpath("//*[@id='from']").click()
            self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[1]").click()
            self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[1]/option[3]").click()
            self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[2]").click()
            self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[2]/option[1]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='to']").click()
            self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[1]").click()
            self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[1]/option[3]").click()
            self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[2]").click()
            self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/div/select[2]/option[2]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/section[2]/div/section/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/input[3]").click()
            time.sleep(1)
            string = "Success"
            self.logger.info("The 'Date_Select' method running Successfully")
        except:
            string = "Error :Element in method 'Date_Select' Not Founded"
            self.logger.exception("The 'Date_Select' method Exception Logged")
        return string

    #验证搜索功能
    def Search_Send_Keys(self):
        time.sleep(1)
        str = ""
        try:
            head = self.driver.find_element_by_xpath("//*[@id='DataTables_Table_0_filter']/label")
            head.find_element_by_tag_name("input").send_keys("capacity")
            time.sleep(1)
            head.find_element_by_tag_name("input").clear()
            head.find_element_by_tag_name("input").send_keys(" ")
            str = "Success"
            self.logger.info("The 'Search_Send_Keys' method running Successfully")
        except:
            str  = "Error :Element in method 'Search_Send_Keys' Not Founded"
            self.logger.exception("The 'Search_Send_Keys' method Exception Logged")
        return str

    #选择显示多少条信息
    def Select_Show_Num(self):
        string = ""
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@id='DataTables_Table_0_length']/label/select").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='DataTables_Table_0_length']/label/select/option[2]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='DataTables_Table_0_length']/label/select/option[3]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='DataTables_Table_0_length']/label/select/option[4]").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id='DataTables_Table_0_length']/label/select").click()
            string = "Success"
            self.logger.info("The 'Select_Show_Num' method running Successfully")
        except:
            string = "Error :Element in method 'Select_Show_Num' Not Founded"
            self.logger.exception("The 'Select_Show_Num' method Exception Logged")
        return string

    #检查表格完整性
    def Verify_Table_Integrity(self):
        try:
            table = []
            time.sleep(3)
            table_loc = self.driver.find_element_by_xpath("//*[@id='DataTables_Table_0']/tbody")
            rows = len(table_loc.find_elements_by_tag_name("tr"))
            columns = len(table_loc.find_element_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr[1]").find_elements_by_tag_name("td"))
            for row in range(1,rows+1):
                table_row = []
                for column in range(1, columns+1):
                    xpath = "//*[@id='DataTables_Table_0']/tbody/tr[" + str(row) + "]/td[" + str(column) +"]"
                    table_row.append(self.driver.find_element_by_xpath(xpath).text)
                table.append(table_row)
            return table
        except:
            self.logger.exception("The 'Verify_Table_Integrity' method Exception Logged")

    #判断图表是否加载
    def Canvas_is_Showed(self):
        time.sleep(1)
        str = ""
        try:
            self.driver.find_element_by_xpath("//*[@id='charts']/div[1]/canvas").click()
            str = "Success"
            self.logger.info("The 'Canvas_is_Showed' method running Successfully")
        except:
            str = "Error :Element in method 'Canvas_is_Showed' Not Founded"
            self.logger.exception("The 'Canvas_is_Showed' method Exception Logged")
        return str

    #图下方文字点击
    def Under_Canvas_Click(self):
        time.sleep(3)
        str = ""
        try:
            head = self.driver.find_element_by_xpath("//*[@id='j-legend']/ul")
            all_li = head.find_elements_by_tag_name("li")
            for i in all_li:
                i.find_element_by_class_name("name").click()
            str = "Success"
            self.logger.info("The 'Under_Canvas_Click' method running Successfully")
        except:
            str = "Error :Element in method 'Under_Canvas_Click' Not Founded"
            self.logger.exception("The 'Under_Canvas_Click' method Exception Logged")
        return str

    #表格页面切换
    def Table_Page_Change(self):
        time.sleep(1)
        string= ""
        try:
            head = self.driver.find_element_by_xpath("//*[@id='DataTables_Table_0_paginate']/ul")
            all_li = head.find_elements_by_tag_name("li")
            li_num = len(all_li)
            #验证数字按钮
            for i in range(2,li_num):
                xpath = "//*[@id='DataTables_Table_0_paginate']/ul/li[" + str(i) + "]/a"
                self.driver.find_element_by_xpath(xpath).click()
                time.sleep(0.5)
            #验证Previous按钮
            for i in range(li_num-2):
                xpath = "//*[@id='DataTables_Table_0_paginate']/ul/li[" + str(1) + "]/a"
                self.driver.find_element_by_xpath(xpath).click()
                time.sleep(0.5)
            #验证Next按钮
            for i in range(li_num-2):
                xpath = "//*[@id='DataTables_Table_0_paginate']/ul/li[" + str(li_num) + "]/a"
                self.driver.find_element_by_xpath(xpath).click()
                time.sleep(0.5)
            #返回第一个页面
            self.driver.find_element_by_xpath("//*[@id='DataTables_Table_0_paginate']/ul/li[2]/a").click()
            string = "Success"
            self.logger.info("The 'Table_Page_Change' method running Successfully")
        except:
            string = "Error :Element in method 'Table_Page_Change' Not Founded"
            self.logger.exception("The 'Table_Page_Change' method Exception Logged")
        return string

