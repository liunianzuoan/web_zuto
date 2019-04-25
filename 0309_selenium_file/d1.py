#点击事件的上传文件操作

import win32gui

import time
import win32con
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('file:///D:/PycharmProjects/autoweb/0226_html/d2.html')
driver.find_element_by_xpath("//input[@type='file']").click()
#一定要等待
time.sleep(3)

dialog = win32gui.FindWindow("#32770","打开")  #一级窗口
print(dialog)
#找到窗口
ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None) #二级窗口
print(ComboBoxEx32)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)   #三级窗口
print(ComboBox)
Edit = win32gui.FindWindowEx(ComboBox,0,'Edit',None)   #四级窗口
print(Edit)
button = win32gui.FindWindowEx(dialog,0,"Button",'打开（&O）') #打开按钮
print(button)
print('ok')
time.sleep(2)
#操作
win32gui.SendMessage(Edit,win32con.WM_SETTEXT,None,r'D:\Xshell\readme.txt')
time.sleep(2)
#发生文件路径
win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)
time.sleep(2)
driver.quit()