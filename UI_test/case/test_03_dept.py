import pytest

# 加载对应的路径
from UI_test.common.parse_xlsx import parse_xlsx
from UI_test.common.parse_yaml import parse_yaml
from UI_test.page.department import Department
from UI_test.config.config import base_path

dept_add_data_path = base_path + parse_yaml("case.path.dept.add")
# 加载数据集
data = parse_xlsx(dept_add_data_path)


# 测试用例执行错误的截图
def wrapper_error(fun):
    def inner(self, *args, **kwargs):
        try:
            fun(self, *args, **kwargs)
        except AssertionError as e:
            self.dept.save_screenshot(doc="测试用例执行失败")
            raise

    return inner


class TestDept:
    def setup(self):
        self.dept = Department()
        self.dept.switch_to_main_frame()

    def teardown(self):
        self.dept.quit()

    def test_dept_list(self):
        assert "部门名称" in self.dept.driver.page_source

    @pytest.mark.parametrize("dept", data)
    def test_dept_add(self, dept):
        self.dept.add_dept(dept)
        self.dept.go_to_last()
        assert dept[1] in self.dept.driver.page_source

    @wrapper_error
    def test_dept_delete(self):
        origin_count = self.dept.get_total_size()
        self.dept.delete_dept()
        delete_count = self.dept.get_total_size()
        assert origin_count == delete_count + 1
