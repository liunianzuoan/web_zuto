# 窗口滚动的场景   懒加载   ajax  下面的版权信息可见之后定位

# 通过执行js代码来滚动到最下面
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.douban.com/")
js_code = "window.scrollTo(0,document.body.scrollHeight)"

driver.execute_script(js_code)

time.sleep(4)
driver.quit()

