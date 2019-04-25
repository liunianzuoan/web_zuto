from selenium import webdriver
# 打开谷歌浏览器
driver = webdriver.Chrome()
# 打开百度首页
driver.get('http://www.baidu.com')
print(type(driver),driver)

# 元素定位

ele = driver.find_element_by_id('kw')
print(ele)
print(ele.get_attribute('class'))

# 其他定位方式
driver.find_element_by_name('wd')
driver.find_element_by_class_name('s_ipt')
driver.find_element_by_tag_name('input')
driver.find_element_by_partial_link_text('新')
driver.find_element_by_link_text('新闻')
driver.find_element_by_css_selector('input'['name'=='kw'])
driver.find_elements_by_name('wd')  # 返回的是列表[]
