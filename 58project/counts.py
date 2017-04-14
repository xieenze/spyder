#coding:utf8
import time
from  page_parsing import url_list


while True:#死循环
    print url_list.find().count()
    time.sleep(5)