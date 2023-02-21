import pytest
import requests

from Api_test.common.yaml_util import YamlUtil




def test_data_01():
    value= YamlUtil().read_extract_yaml("token")
    print(value)


if __name__ == '__main__':
    pytest.main(['-vs'])