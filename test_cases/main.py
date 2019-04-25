import pytest

if __name__ == '__main__':
    pytest.main(['-m login','--result-log=../report/test.log',
                 '--junit-xml=../report/test.xml',
                 '--html=../report/test.html',
                 '--alluredir=../allure',
                 '--capture=no'])

