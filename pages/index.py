from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base import BasePage

class IndexPage(BasePage):

    my_account_locator = (By.XPATH,"//img[@class='mr-5']/..")

    invest_button_locator = (By.XPATH,"//a[contains(@class,'btn-special')]")



    def get_user(self):
        return self.get_visible_element(self.my_account_locator)

    def get_invest_button(self) ->WebElement:
        return self.get_visible_element(self.invest_button_locator)


    def invest_click(self):
        return self.get_invest_button().click()

