# wms-web-ui-pytest

#### 项目介绍
该项目是一个web-ui自动化框架的测试项目, 其中测试的项目是一个仓储管理系统, 使用的技术主要是

Selenium,Pytest等核心技术, 主要包括的功能有日志管理, 配置文件管理, 测试用例的数据和用例分离, 自动化测试, 测试报告Allure自动化报告等

该项目可以快速帮助各位同学掌握自动化测试的核心实现

#### 软件架构
| 软件名称             | 软件版本 | 备注说明                           |
| :------------------- | -------- | ---------------------------------- |
| Java环境             | jdk8     | 用于运行演示项目wms                |
| MySQL                | 5.6      | 导入数据库脚本, 部署系统           |
| Tomcat               | tomcat7  | 运行wms项目                        |
| Python               | 3.10.0   | python环境:https://www.python.org/ |
| Selenium             | 4.1.0    | https://www.selenium.dev/zh-cn/    |
| loguru               | 0.5.3    | python日志框架                     |
| openpyxl             | 3.0.9    | excel数据表格读取                  |
| PyYAML               | 6.0      | 读取yaml配置文件                   |
| pytest               | 6.2.5    | 执行python测试用例                 |
| pytest-rerunfailures | 10.2     | 重试执行测试用例                   |
| allure-pytest        | 2.9.45   | 生成html测试报告                   |

#### 模块说明

| 功能模块      | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| base          | 基础组件层  selenium框架原生的api的一个通用的封装            |
| page          | 业务对象层 对于业务系统中的每一个模块页面的封装: 比如登录页面, 商品页面, 部门管理页面 |
| case          | 测试用例层 编写的测试用例, 本项目使用的是pytest测试用例      |
| config        | 基础配置层 包括项目路径的配置 业务数据的配置yaml文件         |
| common        | 通用组件封装, 包括读取yaml配置文件, 读取excel测试用例数据    |
| data          | 测试数据, 存放的是excel格式的测试用例数据                    |
| report        | 生成报告的目录                                               |
| allure-report | 生成可视化html测试报告                                       |
| run.py        | pytest的启动执行文件 存放在项目的根目录                      |
| pytest.ini    | pytest的配置文件                                             |
| png           | 项目错误的截图文件保存路径                                   |
| log           | 项目中的日志存储路径                                         |
| wms           | 显示项目中的sql脚本和运行的项目                              |

#### 安装教程

1. 从官网下载jdk8以上安装, 并且配置好JAVA_HOME
2. 从官网下载mysql5.6以上的数据库进行安装, 如果是MySQL8.0 需要设置时区为东八区 
3. 创建好数据库wmsdemo, 并且导入数据库脚本wmsdemo.sql
4. 修改Tomcat7-WMS\webapps\ROOT\WEB-INF\classes目录下的db.properties文件,修改数据库的用户名和密码
5. 把Tomcat7-WMS最好放到D盘根目录,运行Tomcat7-WMS\bin的启动脚本startup.bat文件
6. 导入项目源码到项目中, 并且建议配置一个虚拟的venv的python环境
7. 在虚拟环境中执行 pip install -r requirements.txt 安装所有的依赖文件
8. 在本地配置并且下载安装allure环境(配置好环境变量)
9. 修改项目中的一些基础配置: config/config.py, config/data.yaml
10. 启动项目运行run.py
11. 在pycham中打开测试报告index.html(注意不要直接在本地打开)

#### 技术要点

1.  selenium web自动化
2.  pytest 测试框架
3.  日志管理框架loguru
4.  PyYAML yaml配置文件的使用和解析
5.  openpyxl excel数据文件的读取
6.  装饰器设计模式的使用
7.  allure测试报告
8.  parameter参数化测试用例数据管理

#### 项目截图

![](wms/image/01_用户登录.gif)

![](wms/image/02_商品添加.gif)

![](wms/image/03_商品删除.gif)

![](wms/image/04_测试报告.png)

![](wms/image/05_测试报告.png)

![](wms/image/06_项目结构.png)

![](wms/image/07_项目代码.png)





#### 联系方式

如果在使用该框架的时候, 有疑问可以联系 qq: 2679743435  加qq请务必备注自动化测试框架项目