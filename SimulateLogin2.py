#coding:utf8


import time
from selenium import webdriver
'''
参考：
http://cuiqingcai.com/2599.html
http://blog.csdn.net/ylbf_dev/article/details/51482250
'''

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
#设置登陆界面的url，拿同济教务处做测试
loginUrl = 'http://4m3.tongji.edu.cn/eams/login.action'

#设置弹窗大小
driver.set_window_size(1000, 760)
driver.get(loginUrl) #进入登陆界面

time.sleep(20)#设定45秒睡眠，期间进行手动登陆。

#获取登陆后当前url
current_url = driver.current_url
#获取当前浏览器的Cookies
cookies = driver.get_cookies()
#获取网页源代码
page_source = driver.page_source

#通过selector定位元素
elem = driver.find_element_by_css_selector('div.modulebody')
#获取元素的文本内容
text = elem.text
elem = driver.find_element_by_css_selector('a.p_1')
#获取元素的属性值
href = elem.get_attribute('href')

