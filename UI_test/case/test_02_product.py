import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from loguru import logger

# 加载对应的路径
from UI_test.common.parse_xlsx import parse_xlsx
from UI_test.common.parse_yaml import parse_yaml
import product
from UI_test.config.config import base_path

product_add_data_path = base_path + parse_yaml("case.path.product.add")
# 加载数据集
data = parse_xlsx(product_add_data_path)


class TestProduct:
    def setup(self):
        self.product = Product()
        self.product.switch_to_main_frame()

    def teardown(self):
        self.product.quit()

    def test_product_list(self):
        assert "货品名称" in self.product.driver.page_source

    @pytest.mark.parametrize("product", data)
    def test_product_add(self, product):
        self.product.add_product(product)
        self.product.go_to_last()
        assert product[1] in self.product.driver.page_source

    def test_product_delete(self):
        time.sleep(2)
        origin_count = self.product.get_total_size()
        self.product.delete_product()
        delete_count = self.product.get_total_size()
        assert origin_count == delete_count + 1
