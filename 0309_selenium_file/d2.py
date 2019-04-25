# input标签的上传文件
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('file:///D:/PycharmProjects/autoweb/0226_html/d2.html')
e = driver.find_element_by_xpath("//input[@type='file']")
print(e)
driver.find_element_by_xpath("//input[@type='file']").send_keys(r'D:\Xshell\readme.txt')
#一定要等待

time.sleep(3)
driver.quit()

