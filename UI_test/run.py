import os
import time

import pytest

if __name__ == '__main__':
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    path = "./report/" + now + "/"
    pytest.main(["--alluredir=" + path])
    # 调用系统命令 生成测试报告到指定目录
    os.system("allure generate " + path + " -o allure-report/html/" + now)
