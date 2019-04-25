# iframe  窗口切换

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

drive = webdriver.Chrome()
# 隐式等待
drive.implicitly_wait(30)
#打开课堂派登录页面
drive.get('https://www.ketangpai.com/User/login.html')
# 加显式等待
WebDriverWait(drive,20).until(EC.element_to_be_clickable((By.XPATH,"//a[text()='微信登录']")))
#定位微信登录元素
drive.find_element_by_xpath("//a[text()='微信登录']").click()

# 找到iframe元素
ele = drive.find_element_by_tag_name('iframe')
#切换iframe
drive.switch_to.frame(ele)
# 加等待时间
# WebDriverWait(drive,15).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME,'iframe')))
WebDriverWait(drive,15).until(EC.element_to_be_clickable((By.XPATH,"//div[text()='微信登录']")))
wx = drive.find_element_by_xpath("//div[text()='微信登录']")
print(wx.text)

# 回到默认页面
drive.switch_to.default_content()

#回到上一级的iframe页面
# drive.switch_to.parent_frame()
