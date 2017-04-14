#coding:utf8
import requests, urllib,urllib2
from bs4 import BeautifulSoup
import os
import time
import socket


start_url = 'http://sh.58.com/sale.shtml'
url_host = 'http://sh.58.com'
def get_channel_urls(start_url):
    web_data = requests.get(start_url)
    soup = BeautifulSoup(web_data.text,'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        #print link.get('href')
        page_url=url_host+link.get('href')
        print page_url

get_channel_urls(start_url)

channel_list='''
    http://sh.58.com/shouji/
    http://sh.58.com/tongxunyw/
    http://sh.58.com/danche/
    http://sh.58.com/fzixingche/
    http://sh.58.com/diandongche/
    http://sh.58.com/sanlunche/
    http://sh.58.com/peijianzhuangbei/
    http://sh.58.com/diannao/
    http://sh.58.com/bijiben/
    http://sh.58.com/pbdn/
    http://sh.58.com/diannaopeijian/
    http://sh.58.com/zhoubianshebei/
    http://sh.58.com/shuma/
    http://sh.58.com/shumaxiangji/
    http://sh.58.com/mpsanmpsi/
    http://sh.58.com/youxiji/
    http://sh.58.com/jiadian/
    http://sh.58.com/dianshiji/
    http://sh.58.com/ershoukongtiao/
    http://sh.58.com/xiyiji/
    http://sh.58.com/bingxiang/
    http://sh.58.com/binggui/
    http://sh.58.com/chuang/
    http://sh.58.com/ershoujiaju/
    http://sh.58.com/bangongshebei/
    http://sh.58.com/diannaohaocai/
    http://sh.58.com/bangongjiaju/
    http://sh.58.com/ershoushebei/
    http://sh.58.com/yingyou/
    http://sh.58.com/yingeryongpin/
    http://sh.58.com/muyingweiyang/
    http://sh.58.com/muyingtongchuang/
    http://sh.58.com/yunfuyongpin/
    http://sh.58.com/fushi/
    http://sh.58.com/nanzhuang/
    http://sh.58.com/fsxiemao/
    http://sh.58.com/xiangbao/
    http://sh.58.com/meirong/
    http://sh.58.com/yishu/
    http://sh.58.com/shufahuihua/
    http://sh.58.com/zhubaoshipin/
    http://sh.58.com/yuqi/
    http://sh.58.com/tushu/
    http://sh.58.com/tushubook/
    http://sh.58.com/wenti/
    http://sh.58.com/yundongfushi/
    http://sh.58.com/jianshenqixie/
    http://sh.58.com/huju/
    http://sh.58.com/qiulei/
    http://sh.58.com/yueqi/
    http://sh.58.com/chengren/
    http://sh.58.com/nvyongpin/
    http://sh.58.com/qinglvqingqu/
    http://sh.58.com/qingquneiyi/
    http://sh.58.com/chengren/
    http://sh.58.com/xiaoyuan/
    http://sh.58.com/ershouqiugou/
    http://sh.58.com/tiaozao/
'''