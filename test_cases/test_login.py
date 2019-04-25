import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login import LoginPage
from pages.index import IndexPage
from ddt import ddt,data
from data import login_data
import pytest

@pytest.mark.all
#@ddt
class TestLogin():

    @classmethod
    def setUpClass(cls):
        # url = 'http://120.78.128.25:8765/Index/login.html'
        # cls.driver = webdriver.Chrome()
        # cls.driver.get(url)
        # cls.login_page = LoginPage(cls.driver)
        # cls.index_page = IndexPage(cls.driver)
        pass

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    # def tearDown(self):
    #     # 删除输入框的没有加在这里  ?  登录成功的没法清空  所以需要放在异常案例断言之后
    #
    #     self.login_page.clear_phone()
    #     self.login_page.clear_pwd()


    @pytest.mark.usefixtures('init_driver')
    @pytest.mark.login
    @pytest.mark.smoke
    @pytest.mark.parametrize("data",login_data.user_incorrect)
    #@data(*login_data.user_incorrect)
    def test_login_1_failed(self,data,init_driver):
        driver,login_page = init_driver
        login_page.submit_userinfo(data['phone'],data['password'])
        assert login_page.alert_info().text == data['expected']
        #self.assertTrue(self.login_page.alert_info().text == data['expected'])
        login_page.clear_phone()
        login_page.clear_pwd()


    #@data(*login_data.user_unauthorized)
    @pytest.mark.parametrize('data',login_data.user_unauthorized)
    @pytest.mark.smoke
    @pytest.mark.usefixtures('init_driver')
    def test_login_1_unauthorized(self,data,init_driver):
        driver, login_page = init_driver
        login_page.submit_userinfo(data['phone'],data['password'])
        #self.assertTrue(self.login_page.unauthorized().text == data['expected'])
        assert (login_page.unauthorized().text == data['expected'])
        login_page.clear_phone()
        login_page.clear_pwd()

    @pytest.mark.smoke
    @pytest.mark.usefixtures('my_set_class')
    @pytest.mark.login_success
    def test_login_2_success(self,my_set_class):
        driver,login_page,index_page = my_set_class
        login_page.submit_userinfo('18684720553','python')
        #断言
        # 账户的元素
        user_ele = index_page.get_user()
        assert ('小蜜蜂' in user_ele.text)
        #self.assertTrue('小蜜蜂' in user_ele.text)


if __name__ == '__main__':
    unittest.main()


