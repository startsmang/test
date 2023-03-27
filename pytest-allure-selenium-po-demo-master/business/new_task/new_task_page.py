# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class NewTaskPage:


    """------------------工程列表------------------------"""

    commodity_search = ("xpath", "//*[@placeholder='请输入工程名称关键字搜索']")#输入框
    #//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div/input
    enter_search_risk = (By.XPATH, "//*[@placeholder='请输入工程名称关键字搜索']/../following-sibling::button")#搜索
    #//*[@placeholder='请输入工程名称关键字搜索']/..//parent::*/button
    # //*[@placeholder='请输入工程名称关键字搜索']/../../button

    #Select_search_risk = (By.XPATH,  "//span[text()='查看']")  # 选择工程

    Select_search_risk = (By.XPATH,  "//*[@placeholder='请输入工程名称关键字搜索']/../../following-sibling::div/descendant::*[@class='titleTxt']")  # 选择工程
    #//*[@id="app"]/div/div[2]/div/div[3]/div[3]/div/div[1]/div[2]
    #//div[text()='工程列表']/../descendant::*[@class='titleTxt']


    assert_search_risk= (By.XPATH,  '//*[@class="numBox"]')  # 断言进入工程

    """------------------进入风险待办，新增任务------------------------"""
    menu_expansion=(By.ID,'hamburger-container')#展开菜单

    risk_management=(By.XPATH,  "//span[text()='风险管理']")  # 风险管理
    risk_identification=(By.XPATH,  "//span[text()='风险辨识']")  # 风险辨识
    #task_management=(By.XPATH,  '//*[@class="tsbRow"]/div[2]/button[2]')  # 任务管理
    task_management = (By.XPATH, '//*[@class="tsbRow"]//*[@class="hyh_btn lg line mlr_12"][2]')  # 任务管理
    #//div[text()="风险单元"]/../../..//*[@class="hyh_btn lg line mlr_12"][2]
    # //*[@class="tsbRow"]//*[@class="hyh_btn lg line mlr_12"][2]

    new_task=(By.XPATH,  '//span[text()="新增"]')#新增任务
    enter_task_name=(By.XPATH,  "//*[@placeholder='请输入任务名称']")#输入任务名称
    risk_unit = (By.XPATH, "//*[@placeholder='请选择风险单元']")  # 风险单元输入框
    risk_unit_list=(By.XPATH,  "//*[@x-placement='bottom-start']/div/div/ul/li")#选择风险单元数据

    risk_Evaluation_type=(By.XPATH, "//*[@placeholder='请选择任务类型']")#评估方法输入框 请选择评估方法
    risk_type_list = (By.XPATH, "//*[@x-placement='bottom-start']/div/div/ul/li")  # 选择评估方法
    risk_Evaluation_method = (By.XPATH, "//*[@placeholder='请选择评估方法']")  # 评估方法输入框 请选择评估方法
    risk_method_list = (By.XPATH, "//*[@x-placement='bottom-start']/div/div/ul/li")  # 选择评估方法
    risk_closing_date=(By.XPATH,"//*[@placeholder='选择日期']")#截止日期

    risk_closing_date_cancel=(By.XPATH,"//div[text()='评价准则']")#取消选择框截止日期
    risk_Evaluation_criteria=(By.XPATH,"//*[@placeholder='请选择评价准则']")#评价准则输入框

    risk_criteria_list =(By.XPATH, "//*[@x-placement='bottom-start']/div/div/ul/li")


    risk_riskBtn_blueBtn =(By.XPATH,'//*[@class="hyh_btn lg primary mlr_12"][1]')#确定

    Add_task_risk_assert = (By.XPATH, '//tbody/tr/td/div/span')  # 断言发任务后的 任务名称状态



    """------------------进入风险待办，新增工程资料------------------------"""
    new_Engineering_data=(By.XPATH,'//tbody/tr/*[last()]/div/div/div')#列表进入工程资料界面
    add_Engineering_data_=(By.XPATH,'//*[@class="addBox"]')#工程资料界面，点击新增

    Data_name= (By.XPATH, "//*[@placeholder='请输入工程名称']")#输入资料名称标题
    Engineering_data_des=(By.XPATH, "//*[@placeholder='请输入内容']")#输入工程资料描述
    Upload_data_map=(By.XPATH,"//*[@class='updatainput']")#上传工程资料图
    Engineering_data_Submit=(By.XPATH,'//*[@class="mainPage"]/*[@class="el-dialog__wrapper riskDialog"]/div/*[@class="el-dialog__footer"]/span/div[2]')#确定提交

    Add_Engineering_assert= (By.XPATH, '//*[@class="cardBox"]/div[2]/div')  # 断言新增工程资料的标题



    """------------------任务指派专家------------------------"""
    Back_button_Engineering_data=(By.XPATH,'//*[@class="mainPage"]/div[2]/button')#返回 任务列表
    Invite_experts_interface=(By.XPATH,'//tbody/tr/*[last()]/div/div/div[2]')#进入邀请专家界面
    #add_personnel=(By.XPATH,'//*[@class="tableTitRow"]/div[2]')#新增人员
    add_personnel = (By.XPATH, "//div[text()='评估专家']/following-sibling::div")  # 新增人员
    Search_People = (By.XPATH, "//*[@placeholder='请输入内容']")  # 搜索人员输入框

    Search_button = (By.XPATH, "//*[@placeholder='请输入内容']/following-sibling::div")  # 搜索按钮

    Select_All= (By.XPATH, "//*[@placeholder='请输入内容']/parent::*/parent::*/div[2]//table/thead//span")  # 全选
    Confirm_invitation=(By.XPATH,"//*[@placeholder='请输入内容']/parent::*/parent::*/following-sibling::div//button") #确认邀请

    Expert_list_status=(By.XPATH,'//div[text()="评估专家"]/parent::*/parent::*/descendant::*[@class="el-table__row"]/td[3]/div/span') #断言 邀请专家状态待发送状态

    Task_send_assert= (By.XPATH, '//*[@class="el-table__header-wrapper"]/following-sibling::div//tbody//td[4]//span') #断言发送任务 断言


    #//*[@class="app-main"]/div

    #
    # def personnel_02(self,n):
    #     personnel_02 = (By.XPATH, '/html/body/div[%s]/div/div[2]/div[1]/input'%n)#输入搜索专家姓名
    #     return personnel_02
    # def search_task_name(self, n):
    #     search_task_name=(By.XPATH,"/html/body/div[%s]/div/div[2]/div[1]/div/button/span"%n)#搜索
    #     return search_task_name
    # def personnel_01(self,n):
    #     personnel_01=(By.XPATH,'/html/body/div[%s]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[1]/div/label/span/span'%n)#选择的人员
    #     return personnel_01
    # def experts_interface_Submit(self,n):
    #     experts_interface_Submit=(By.XPATH,'/html/body/div[%s]/div/div[3]/span/div[2]'%n)#确定提交
    #     return experts_interface_Submit


    close_Invite_experts=(By.XPATH,'//*[@class="mainPage"]/*[@class="el-dialog__wrapper mapDialog"]//i')#关闭邀请界面


    """------------------发送任务------------------------"""
    send_task=(By.XPATH,'//tbody/tr/*[last()]/div/div/div[3]')

