import pytest
class Test_Api:
    # 基础用法
    @pytest.mark.parametrize('args',['shengqi','qi','qi'])
    def test_api(self,args):
        print(args)
    @pytest.mark.parametrize('name,age',[['shengqi',18],['qi',18],['qi',20]])
    def Tets_api1(self,name,age):
            print(name,age)
        # 解包用法
if __name__ == '__main__':
    pytest.main(['-vs','Test_api.py'])