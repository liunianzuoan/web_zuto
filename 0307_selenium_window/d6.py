# 鼠标的操作

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 访问百度
driver.get('http://www.baidu.com')

# 悬浮菜单的定位
setting_ele = driver.find_element_by_xpath("//a[@name='tj_settingicon' and contains(@href,'baidu')]")

ac = ActionChains(driver)

ac.move_to_element(setting_ele).perform()

# 加显示等待 高级搜索可点击
WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,"//a[text()='高级搜索']")))

driver.find_element_by_xpath("//a[text()='高级搜索']").click()
ac.double_click()  # 双击
ac.context_click()  #右击
ac.drag_and_drop()  # 拖拽操作，左键按住某一个元素到另外一个区域，然后释放按键
ac.move_to_element()   # 鼠标悬停


