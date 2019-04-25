import time


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import logging

logging.basicConfig(filename='test.log')
logger = logging.getLogger()

class BasePage:

    def __init__(self,driver:Chrome):
        self.driver = driver

    def get_visible_element(self,locator,eqc=20):
        try:
            return WebDriverWait(self.driver, eqc).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            #logger
            logger.error('no this element:{}'.format(e))
            self.driver.save_screenshot("{}.jpg".format(time.time()))


