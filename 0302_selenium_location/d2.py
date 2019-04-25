import time
from selenium import webdriver
import time

drive=webdriver.Chrome()
drive.get('http://www.baidu.com')

# 刷新
drive.refresh()

# 全屏
drive.maximize_window()
time.sleep(2)
#调整大小

drive.set_window_size(1000,800)

drive.get('http://www.douban.com')

# 后退
drive.back()

#前进
drive.forward()

# url
print(drive.current_url)

#标题
print(drive.title)
# 关闭标签
drive.close()
time.sleep(3)
# 退出浏览器
drive.quit()

