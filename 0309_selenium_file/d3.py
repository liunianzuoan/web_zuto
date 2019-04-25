# python是不能浏览器的属性的  只能通过js去改变  所以需要发生js代码
import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.12306.cn/index/')

def find_element(locator)->WebElement:
    """locator定位器"""
    date_ele = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located(locator))
    if not isinstance(date_ele , WebElement):
        raise Exception
    return date_ele

date_ele = find_element((By.ID,'train_date'))
print(date_ele)

js_code = "arguments[0].readOnly=false"
#执行js代码
driver.execute_script(js_code,date_ele)
time.sleep(3)

js_code = "arguments[0].value='2019-03-14'"
driver.execute_script(js_code,date_ele)

time.sleep(4)
driver.quit()

