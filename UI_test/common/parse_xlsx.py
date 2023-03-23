from openpyxl import load_workbook

from UI_test.config.config import base_path


def parse_xlsx(filename, sheet_name="Sheet1"):
    """
    解析读取excel表格中的全部数据, 返回的数据是一个元组
    :param filename:读取的文件路径
    :param sheet_name: 读取的具体的页签
    :return: 元组, 具体的业务数据
    """
    excel = load_workbook(filename)
    data = []
    for value in excel[sheet_name].values:
        if value[0] > 1:
            data.append(value[1:])
    excel.close()
    return data


if __name__ == '__main__':
    data = parse_xlsx(base_path + "data\商品新增测试用例.xlsx")
    print(data)
