#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# @Time    : 2022/11/30 20:42
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : 5.1定位.py
# @Software: PyCharm
#-------------------------------------------------------------------------------




'''

xpath基本定位语法
表达式      说明
/          绝对定位，从根节点选取
//         相对定位，从匹配选择的当前节点选择文档中的节点，而不考虑他们的位置
.          选取当前节点
..         选取父节点
@          选取属性，@class='xxx' @id='xxx'，属性放在中括号[]中
*          通配符。匹配所有 //*
@*         通配符。匹配所有属性  //*[@*='xxx']
/html/body/div[1]/div[2]/div[5]/div[1]/div/form/span[1]/input
//*[@id="kw"]

文本、模糊、逻辑定位
1，文本定位：使用text()元素的text内容，如：//input[text()='登录']
2，模糊定位：使用contains包含函数 如：//input[contains(text()='登录')]，//input[contains(@class,"s_ipt")]
3,使用逻辑运算符 and or 如：//input[@name='phone' and @id = 'xxx']


  语法 //*[@属性=属性值] 例如：//input[@id="kw"]
 1) 利用元素属性来顶我 标签的基础属性、自定义属性都可以
 2) 通过层级与属性结合  从父亲->爷爷->祖先元素 + 属性值
 3）使用逻辑运算符  且 and  或 or
 4）函数定位/包含关系
    text() 例子：//div[@id="s-top-left"]//a[text()='地图']
    contains //span[contains(text(),"坠湖公交司")]  //span[contains(@class,"quickdelete-wrap")]
 5）轴定位
   1.parent:: 上层父节点，爸爸 只找一个 例子 //input[@id='kw' and @name='wd']/parent::span
   2.child：：下层所有子节点 儿子们
   3.ancestor：：上面的所有节点 祖先(爸爸、爷爷 ...)
   4.following-sibling：： 同层下节点，就是弟弟妹妹
   5.preceding-sibling：：同层上阶段，就是哥哥姐姐


1.通过界面text值定位
//div[text()="工程列表"]

2. 通过标签属性定位
//*[@placeholder='请输入工程名称关键字搜索']


3、descendant
# 选取当前节点的所有后代元素（子、孙等）
风险管理-风险辨识-任务管理-指定专家-新增
//div[text()="评估专家"]/../descendant::*[@class="btn"]
//div[text()="评估专家"]/..//*[@class="btn"]
#//*[@id="app"]/div/div[3]/section/div/div[6]/div/div[2]/div/div[1]/div[2]


风险管理-风险辨识-任务管理
//*[@class="tsbRow"]//*[@class="hyh_btn lg line mlr_12"][2]


4 倒数索引取值

//tbody/tr[last()-2] 倒数第三
//tbody/tr[last()] 倒数第一




'''


