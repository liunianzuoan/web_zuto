from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base import BasePage

class InvestPage(BasePage):

    invest_input_locator = (By.XPATH,"//input[contains(@class,'invest-unit-investinput')]")

    invest_submit_locator = (By.XPATH,"//button[contains(@class,'height_style')]")

    invest_popup_locator = (By.XPATH,"//div[contains(@class,'layui-layer-content')]//div[contains(@class,'capital_font1')]")
    invest_incorrect_locator = (By.XPATH,"//div[@class='text-center']")

    invest_success_active_locator = (By.XPATH,"//div[@class='layui-layer-content']//div[@class='capital_ts']//div[@class='capital_btn']//button[text()='查看并激活']")

    invest_success_amount_locator = (By.XPATH,"//li[@class='color_sub']")

    invest_project_locator = (By.XPATH,"//div[text()='投资项目']")

    click_index_locator = (By.XPATH,"//a[text()='首页']")

    @property
    def invest_input(self)->WebElement:
        return self.get_visible_element(self.invest_input_locator)

    def invest_money(self,value):
        return self.invest_input.send_keys(value)

    @property
    def invest_submit(self)->WebElement:
        return self.get_visible_element(self.invest_submit_locator)

    def click_invest_submit(self):
        return self.invest_submit.click()

    def submit_text(self):
        return self.invest_submit.text

    def invest_popup(self)->WebElement:
        return self.get_visible_element(self.invest_popup_locator)

    def invest_result_text(self):
        return self.invest_popup().text


    def invest_incorrect_number(self)->WebElement:
        return self.get_visible_element(self.invest_incorrect_locator)

    def invest_incorrect_text(self):
        return self.invest_incorrect_number().text

    def look_success_active(self)->WebElement:  #查看并激活按钮定位
        return self.get_visible_element(self.invest_success_active_locator)

    def look_active_click(self):   # 点击查看并激活按钮
        return self.look_success_active().click()

    @property
    def invest_success_amount(self)->WebElement:
        return self.get_visible_element(self.invest_success_amount_locator)

    def invest_project(self)->WebElement:  # 投资项目定位
        return self.get_visible_element(self.invest_project_locator)

    def invest_project_click(self):
        return self.invest_project().click()  # 点击投资项目

    def click_index(self)->WebElement: # 首页按钮定位
        return self.get_visible_element(self.click_index_locator)

    def click(self):  #点击首页
        return self.click_index().click()



