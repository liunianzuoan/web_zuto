import unittest
import time
import pytest
from selenium import webdriver
from pages.base import BasePage
from pages.login import LoginPage
from data import login_data
from pages.index import IndexPage
from pages.invest import InvestPage

class TestInvest():

    @classmethod
    def setUpClass(cls):
        pass
        # url = 'http://120.78.128.25:8765/Index/login.html'
        # cls.driver = webdriver.Chrome()
        # cls.driver.get(url)
        # cls.login_page = LoginPage(cls.driver)
        # cls.index_page =IndexPage(cls.driver)
        # cls.invest_page = InvestPage(cls.driver)

    def setUp(self):
        pass
        # url = 'http://120.78.128.25:8765/Index/login.html'
        # self.driver = webdriver.Chrome()
        # self.driver.get(url)
        # self.login_page = LoginPage(self.driver)
        # self.login_page.submit_userinfo(login_data.user_correct['phone'], login_data.user_correct['password'])
        # self.index_page = IndexPage(self.driver)
        # self.invest_page = InvestPage(self.driver)

    def tearDown(self):
        pass
        # self.driver.quit()

    @pytest.mark.smoke
    @pytest.mark.usefixtures('invest_set_class')
    def test_invest_1_success(self,invest_set_class):
        # 点击首页的投标按钮
        driver, login_page, index_page, invest_page= invest_set_class
        index_page.invest_click()

        # 投资页面输入投资金额
        amount = invest_page.invest_input.get_attribute("data-amount")
        invest_page.invest_money(100)
        invest_page.click_invest_submit()

        # 断言

        #self.assertTrue('投标成功！' == self.invest_page.invest_result_text())
        assert ('投标成功！' == invest_page.invest_result_text())
        invest_page.look_active_click()
        #self.assertTrue(self.invest_page.invest_success_amount.text ==str(float(amount) - 100)+'元')
        assert (invest_page.invest_success_amount.text ==str(float(amount) - 100)+'元')

    @pytest.mark.smoke
    @pytest.mark.usefixtures('invest_set_class')
    def test_invest_2_failed(self,invest_set_class):
        driver, login_page, index_page, invest_page= invest_set_class
        invest_page.click()
        index_page.invest_click()

        invest_page.invest_money(1)
        #self.assertTrue('请输入10的整数倍' ==self.invest_page.submit_text())
        assert ('请输入10的整数倍' ==invest_page.submit_text())

    @pytest.mark.smoke
    @pytest.mark.usefixtures('invest_set_class')
    def test_invest_3_failed(self,invest_set_class):
        driver, login_page, index_page, invest_page = invest_set_class
        invest_page.click()
        index_page.invest_click()

        invest_page.invest_money(10)
        invest_page.click_invest_submit()

        #self.assertTrue("投标金额必须为100的倍数" == self.invest_page.invest_incorrect_text())
        assert ("投标金额必须为100的倍数" == invest_page.invest_incorrect_text())

if __name__ == '__main__':
    unittest.main()