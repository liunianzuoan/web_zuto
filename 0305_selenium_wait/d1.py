from selenium import webdriver
import time

drive=webdriver.Chrome()
drive.get('http://www.baidu.com')
ele = drive.find_element_by_xpath("//input[@id='kw']")

print(ele.tag_name)
print(ele.get_attribute('class'))

# 输入内容
ele.send_keys('selenium')

#点击百度一下
drive.find_element_by_id('su')
time.sleep(3)

ele.clear()  # 清空输入框的内容
ele.send_keys('loadrunner')
time.sleep(2)
drive.quit()