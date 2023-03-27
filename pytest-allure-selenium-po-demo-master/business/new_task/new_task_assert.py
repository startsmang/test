# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from common.logger import Logger
from base.base import BasePage
from selenium.webdriver.support import expected_conditions as EC
from .new_task_page import NewTaskPage as CLP

class NewTaskAssert:

    def __init__(self, driver):
        self.driver =BasePage(driver)


    def add_commodity_assert(self, expect_text):
        return self.driver.assert_text(CLP.assert_search_risk, expect_text, doc="进入工程界面断言" + expect_text)

    def risk_identification_assert(self, expect_text):#进入任务管理断言
        return self.driver.assert_text(
            CLP.task_management,expect_text, doc="任务管理界面断言" + expect_text)

    def Add_task_risk_assert(self, expect_text):#新建任务断言
        return self.driver.assert_text(
            CLP.Add_task_risk_assert, expect_text, doc="新建任务后断言" + expect_text)


    def Add_Engineering_data_assert(self, expect_text):#新建工程资料断言
        return self.driver.assert_text(
            CLP.Add_Engineering_assert, expect_text, doc="新建任务后断言" + expect_text)



    def Task_assignment_assert(self,expect_text):
        return self.driver.assert_text(
            CLP.Expert_list_status, expect_text, doc="邀请专家后断言 专家状态" + expect_text)



    def Task_send_task_assert(self,expect_text):#发送任务断开

        return self.driver.assert_text(
            CLP.Task_send_assert, expect_text, doc="发送任务断言" + expect_text)


