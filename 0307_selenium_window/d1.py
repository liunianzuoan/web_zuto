#浏览器窗口  iframe  和alert窗口的切换
#//a[contains(text(),'lemon.ke.qq.com/')]

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
drive=webdriver.Chrome()
#隐式等待
drive.implicitly_wait(30)
# 访问百度
drive.get('http://baidu.com')
#找到输入框
input_ele = drive.find_element_by_id('kw')
# 发送柠檬班
input_ele.send_keys('柠檬班')
#定位百度一下按钮点击
input_ele.click()

#柠檬班定位
# 这里需要加显示等待
nm = WebDriverWait(drive,20).until\
    (EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'lemon.ke.qq.com/')]")))
# drive.switch_to_window(drive.window_handles[0])
# nm = drive.find_element_by_xpath("//a[contains(text(),'lemon.ke.qq.com/')]")
nm.click()

# 查询有几个window页面
print(drive.window_handles)
print(drive.current_window_handle)
# 切换页面
drive.switch_to_window(drive.window_handles[-1])
# 加等待时间
WebDriverWait(drive,15).until(EC.new_window_is_opened(('CDwindow-20226B45580646F785507B0CC08F8F0E',)))
#  定位华华老师
# 加等待时间
huahua = WebDriverWait(drive,20).until(EC.element_to_be_clickable((By.XPATH,"//h4[text()='华华老师']")))
# huahua =drive.find_element_by_xpath("//h4[text()='华华老师']")
print(huahua.tag_name)
drive.quit()
# 鼠标的操作 双击，悬停，拖拽  按键  直接发生js代码



