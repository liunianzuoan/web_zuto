# 窗口滚动的场景   懒加载   ajax  下面的版权信息可见之后定位

# 通过执行selenium代码来滚动到最下面
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.douban.com/")

e = driver.find_element_by_xpath("//span[@id='icp']")
e.location_once_scrolled_into_view

time.sleep(3)
driver.quit()

