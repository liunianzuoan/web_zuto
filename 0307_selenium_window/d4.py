# 鼠标的一些悬浮操作
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

drive = webdriver.Chrome()
# 访问百度
#隐式等待
drive.implicitly_wait(20)
drive.get('http://www.baidu.com')

drive.find_element_by_xpath("//a[@name='tj_settingicon' and contains(@href,'baidu')]").click()
# 加显示等待
WebDriverWait(drive,20).until(EC.element_to_be_clickable((By.XPATH,"//a[text()='高级搜索']")))
drive.find_element_by_xpath("//a[text()='高级搜索']").click()

e = drive.find_element_by_xpath("//select[@name='gpc']")
# print(e)
select = Select(e)
print(select.select_by_value('stf'))
