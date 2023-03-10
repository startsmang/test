import requests,pytest
from 自学.tools.get_phone import get_phone

@pytest.mark.parametrize('data',get_phone())
def test_login(self,data):
    data = get_phone()
    print(data)



if __name__ == '__main__':
    pytest.main(['--vs'])