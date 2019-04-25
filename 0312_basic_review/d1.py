"""
1.为什么做ui自动化？  你对web自动化测试的理解？ ui自动化比手动测试好吗？
简历里面：使用了selenium做了web自动化测试实现了什么样的效果，为什么使用selenium
2.html   标签，属性，text，和下属标签
3.Form表单和后台接口的交互，action，method
4.js和dom对象  网页的对象，浏览器概念，树状结构
    获取元素，元素定位，
    改变元素的值-->  开启一个服务，
    事件，alert  onload，onclick
5.selenium的原理，
    service,subprocess,wendriver.exe
    client -->urlib3 -->访问服务  类似于request访问接口
    __init__.py 文件的作用？？？   -->可以简化调用包内部的调用过程。  单例模式？？？
6.八大元素定位  id,name,tag_name,link_text,partial_link_text,xpath,class_name,css_selector
都是调用的是find_element 函数   但是写了很多的函数是为了方便阅读和调用
7.等待  必不可少  页面发生变化的时候，一定要等待，页面加载，点击完以后，交互操作基本都会发生页面变化
    元素找不到一般都是缺少等待
8.简单的交互操作  select 点击option   或者是Select类
9.鼠标操作  ActionChains   链式调用，返回的是对象自己本身，核心思想是列表[]
10.键盘操作  send_keys()
11.窗口滚动
12.脚本怎么操作  js  要等待  更新数据需要用到js来更新，python只能获取html属性的数据，不能更改
13.文件上传  pypiwin32
14.窗口切换  窗口，frame，alert  dismiss  accept
python的动态属性
"""

