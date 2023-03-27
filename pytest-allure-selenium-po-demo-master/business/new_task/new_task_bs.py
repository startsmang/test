# coding=utf-8
from base.base import *
from base.base import BasePage
from .new_task_page import NewTaskPage as CLP
from common.get_images_path import *
#
class NewTaskBusiness(BasePage):
#

# class NewTaskBusiness():
#
#     def __init__(self,driver):
#         self.driver1 = BasePage(driver)
#         self.driver2 = BasePage(driver)
#         self.driver.input_text(CLP.commodity_search, text=text['project_name'], doc='输入工程名称：%s'%text['project_name'])
#



    """进入工程概览"""
    def enter_search_risk(self,text):

        self.input_text(CLP.commodity_search, text=text['project_name'], doc='输入工程名称：%s'%text['project_name'])
        self.click_element(CLP.enter_search_risk,doc='点击输入搜索')

        self.click_element(CLP.Select_search_risk,doc='点击进入工程')



        """进入任务管理列表"""
    def risk_identification_risk(self,text):
        self.click_element(CLP.menu_expansion, doc='展开菜单')
        self.click_element(CLP.risk_management, doc='点击风险管理')
        self.click_element(CLP.risk_identification, doc='点击风险辨识')





    def Add_task_risk(self,text): #新增工程任务
        self.click_element(CLP.task_management, doc='点击任务管理')
        self.click_element(CLP.new_task, doc='点击新增任务')
        self.input_text(CLP.enter_task_name, text='%s_%s'%(text['task_name'],text['num']), doc='%s_%s'%(text['task_name'],text['num']))#输入任务名称
        self.click_element(CLP.risk_unit, doc='点击风险单元输入框')
        self.click_element(CLP.risk_unit_list, doc='选择风险单元')
        self.click_element(CLP.risk_Evaluation_type, doc='点击评估类型输入框')
        self.click_element(CLP.risk_type_list, doc='选择评估类型')
        self.click_element(CLP.risk_Evaluation_method, doc='点击评估方法输入框')
        self.click_element(CLP.risk_method_list, doc='选择评估方法')
        self.input_text(CLP.risk_closing_date, text=str(text['risk_date']), doc='输入截止时间%s'%(text['risk_date']) )  # 输入截止时间
        self.click_element(CLP.risk_closing_date_cancel, doc='点击其他位置取消选择框')
        self.click_element(CLP.risk_Evaluation_criteria, doc='点击选择评价准则输入框')
        self.click_element(CLP.risk_criteria_list, doc='选择评价准则')
        self.click_element(CLP.risk_riskBtn_blueBtn, doc='选择确定提交')


    def Add_Engineering_data(self,text):#新增工程资料
        self.click_element(CLP.new_Engineering_data, doc='列表进入新增工程资料')
        self.click_element(CLP.add_Engineering_data_, doc='点击新增工程资料')
        self.input_text(CLP.Data_name, text='%s_%s'%(text['name'],text['num']), doc='输入工程资料名称%s_%s'%(text['name'],text['num']))
        self.input_text(CLP.Engineering_data_des, text='%s_%s'%(text['data_des'],text['num']), doc='输入工程资料描述%s_%s'%(text['data_des'],text['num']))
        for index,file in enumerate(get_images_list(3)):#随机添加3张工程资料图片
            #self.input_text(CLP.Upload_data_map, text=file, doc='第{}次添加工程资料图片'.format(index+1))
            self.upload_file_notInput(CLP.Upload_data_map, file=file,doc='第{}次'.format(index+1))
            time.sleep(1)

        self.click_element(CLP.Engineering_data_Submit, doc='点击确定')




    def Task_assignment(self,text):#任务指派专家
        self.click_element(CLP.Back_button_Engineering_data, doc='返回到工程任务列表')
        self.click_element(CLP.Invite_experts_interface, doc='点击进入邀请专家界面')
        self.click_element(CLP.add_personnel, doc='点击新增')
        self.input_text(CLP.Search_People, text=text['name'], doc='输入邀请的人员%s'%text['name'])
        self.click_element(CLP.Search_button, doc='点击搜索按钮')
        self.click_element(CLP.Select_All, doc='点击全选')
        self.click_element(CLP.Confirm_invitation, doc='点击确认邀请')




    def Task_send_task(self, text):  # 发送任务专家
        self.click_element(CLP.close_Invite_experts, doc='关闭邀请界面')
        self.click_element(CLP.send_task, doc='点击发送任务给专家')




