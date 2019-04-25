import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):

    # 用户phone元素定位器
    phone_input_locator = (By.NAME,"phone")

    # 密码定位器
    pwd_input_locator = (By.NAME,"password")

    # 没有授权的定位器
    unauthorized_locator = (By.XPATH,"//div[@class='layui-layer-content']")

    # alert 信息的定位器
    alert_locator = (By.XPATH,"//div[@class='form-error-info']")

    # 等待，所有页面的行为，-->继承，basepage
    url = 'http://120.78.128.25:8765/Index/login.html'

    def get(self):
        self.driver.get(self.url)


    def submit_userinfo(self, phone, pwd):
        # 定位输入框   get_user_input()
        phone_ele = self.driver.find_element_by_name('phone')
        pwd_ele = self.driver.find_element_by_name('password')

        # 提交信息

        phone_ele.send_keys(phone)
        pwd_ele.send_keys(pwd)
        phone_ele.submit()

        time.sleep(2)

    def alert_info(self):
        return self.get_visible_element(self.alert_locator)

    def unauthorized(self):
        """弹框错误的信息，然后消失的，未注册成功的账户登录或者是注册过的账户使用错误的密码登录"""
        return self.get_visible_element(self.unauthorized_locator)

    def get_phone_element(self)->WebElement:
        return self.get_visible_element(self.phone_input_locator)

    def get_pwd_element(self)->WebElement:
        return self.get_visible_element(self.pwd_input_locator)

    def clear_phone(self):
        return self.get_phone_element().clear()

    def clear_pwd(self):
        return self.get_pwd_element().clear()

    def click(self):
        pass

