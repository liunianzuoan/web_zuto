# 课堂派元素定位

# 课堂派首页链接元素
from selenium import webdriver
drive = webdriver.Chrome()
drive.get('https://www.ketangpai.com/')
ele = drive.find_element_by_xpath("//a[text()='首页']")
print(ele.get_attribute('class'))

# 课堂派登录按钮元素
drive.find_element_by_xpath("//a[@class='login']")

# 进入课堂派
drive.find_element_by_xpath("//span[text()='进入课堂派']")

#免费注册按钮链接
drive.find_element_by_xpath("//a[@class='reg-btn']")

# 节省超40%的教育时间
drive.find_element_by_xpath("//h3[text()='节省超40%教学时间']")

#p标签的内容

drive.find_element_by_xpath("//div[@class='word']/p")

# 批量给分的元素
drive.find_element_by_xpath("//div[@style='display: block;']")

#ppt授课
drive.find_element_by_xpath("//h3[text()='颠覆乏味的PPT授课，与课堂互动无缝融合']")

# 定位悬浮的解决方案下面的申请机构版

#1.先定位到元素解决方案
drive.find_element_by_xpath("//a[@target='_blank' and text()='解决方案']")
#2.再定位元素申请机构版
drive.find_element_by_xpath("//a[ text()='申请机构版']")

# 提供站内查重定位 段落的值
drive.find_element_by_xpath("//div[@class='word']/p[text()='提供站内查重']")
drive.find_element_by_xpath("//div[@class='word']/p[text()='快速给出最大相似度']")
drive.find_element_by_xpath("//div[@class='word']/p[text()='轻松过滤搭便车行为。']")
#提供站内查重定位
drive.find_element_by_xpath("//h3[text()='作业查重杜绝抄袭']")

#会员标签
drive.find_element_by_xpath("//a[@target='_blank' and text()='会员']")

#帮助中心
drive.find_element_by_xpath("//a[text()='帮助中心']")

#移动端
drive.find_element_by_xpath("//a[text()='移动端']")