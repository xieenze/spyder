#coding:utf8
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
'''
半自动模拟登陆任何网站
为爬虫爬取那些需要登陆的网站做准备
参考知乎这位老哥的代码
https://zhuanlan.zhihu.com/p/28587931
一套代码解决所有网站登陆问题
'''

'''pre：下载并配置chromeDriver'''
wd = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
#设置登陆界面的url，拿同济教务处做测试
loginUrl = 'http://4m3.tongji.edu.cn/eams/login.action'
wd.get(loginUrl) #进入登陆界面

time.sleep(45)#设定45秒睡眠，期间进行手动登陆。
cookies = wd.get_cookies()#获得当前浏览器的Cookies
req = requests.Session()
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value'])
req.headers.clear()

#登陆后的url
test = req.get('http://4m3.tongji.edu.cn/eams/home!index.action') #测试是否已经成功登陆
plain_text = test.text
Soup = BeautifulSoup(plain_text, 'lxml')
print Soup#打印登陆后界面的html

#剩下的就是分析网页了
