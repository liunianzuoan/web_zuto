#切换到alert

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
drive = webdriver.Chrome()
# 打开html页面
drive.get(r'D:\PycharmProjects\autoweb\0228_js\d1.html')

alert = drive.switch_to.alert
alert.accept()     # 函数，确定按钮  回到html页面，需要执行accept或者是dismiss函数
alert.dismiss()    #函数，取消按钮
print(alert.text)

# alert的等待
EC.alert_is_present