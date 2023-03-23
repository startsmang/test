import yaml

from UI_test.config.config import base_path


def parse_yaml(key, filename=base_path+"config/data.yaml"):
    """
    根据对应的key读取对应的value
    :param key: 多个单词使用.号分割
    :param filename: 默认读取路径
    :return: 值
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        keys = key.split(".")
        for k in keys:
            data = data[k]
        return data


if __name__ == '__main__':
    value = parse_yaml("wms.url.dept.delete")
    print(value)
