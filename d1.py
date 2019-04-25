# import time
# from selenium import webdriver
# from selenium.webdriver.remote.webelement import WebElement
#
# driver = webdriver.Chrome()
# driver.get('http://120.79.176.157:8012/Index/login.html')
#
# phone_ele = driver.find_elements_by_name('phone')
#
# print(phone_ele[0])
#
# pwd_ele = driver.find_elements_by_name('password')
#
#
# pwd_ele[0].send_keys('13825802580')
# pwd_ele.clear()
#
# time.sleep(3)
#
# driver.quit()
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium")
time.sleep(3)
try:
    driver.find_element_by_id("kw").clear()  # 调用clear()方法去清除
    print('test pass: clean successful')
except Exception as e:
    print("Exception found", format(e))
