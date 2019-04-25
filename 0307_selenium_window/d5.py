# 输入键盘的操作

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
drive = webdriver.Chrome()

# 访问百度
drive.get('http://www.baidu.com')

e = drive.find_element_by_id('kw')
e.send_keys('柠檬班',Keys.ENTER)



