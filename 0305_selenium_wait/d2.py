import time
from selenium import webdriver

# 设置等待的时间
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
drive = webdriver.Chrome()

drive.implicitly_wait(20)  # 隐式等待
drive.get('http://www.baidu.com')

drive.find_element_by_id('kw')


# 显示等待  不能点击  出现了但是不能使用

wait = WebDriverWait(drive,20)
e = wait.until(EC.element_to_be_clickable(By.ID,'kw'))
print(e)

