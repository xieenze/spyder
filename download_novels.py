# coding:utf8
import requests, urllib,urllib2
from bs4 import BeautifulSoup
import os
import time
import socket
import re
import socket
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


def get_webSource(url):#获取解析之后的网页源码
    try:
        source_code = requests.get(url)
    except Exception as e:
        print '获取页面失败！！！'
        return
    source_code.encoding = 'gb2312'
    plain_text = source_code.text
    Soup = BeautifulSoup(plain_text, 'lxml')
    return Soup

def downloadetxt(rooturl,rootpath):
    socket.setdefaulttimeout(4)  # 4秒内没有打开web页面，就算超时
    #os.makedirs(rootpath)
    Soup=get_webSource(rooturl)
    rootpath = unicode(rootpath)
    text1 = Soup.findAll('div','tpc_content do_not_catch')
    text2=Soup.findAll('div','tpc_content')
    text1 = Soup.findAll('div', 'tpc_content do_not_catch')
    text2 = Soup.findAll('div', 'tpc_content')
    text = text1 if len(text1) > len(text2) else text2#两种页面格式
    if len(text)>0:
        print rooturl, rootpath,'获取成功！！'
        strtext = unicode(text[0].get_text())
    else:
        print rooturl,rootpath,'获取失败！！'
        return
    strlist = []
    strlist = strtext.split(' ')
    print len(strlist)
    file = open(rootpath, 'w')

    for s in strlist:
        try:
            file.write('    ' + s + '\n\n')
        except Exception as e:
            print '下载失败！',rootpath,e
    file.close()

def get_dirpath_nexturls(rooturl,rootpath):  #获取这一页所有帖子的标题和超链接
    Soup = get_webSource(rooturl)
    titles = Soup.select('tbody > tr > td.tal > h3 > a')
    reals = titles[8:]  # 直接过滤前八个  只需要针对第一页
    nexturls=[]  #存放每一个帖子的href
    dirpath=[]   #存放每一个帖子的名字

    #os.mkdir(folder)#先创建根目录
    for real in reals:  # 创建对应的文件夹
        try:
            #fobj = open(folder+unicode(real.get_text())+'.txt', 'w')
            #fobj.close()
            realtitle=unicode(real.get_text()).replace('/','').replace('?','').replace('[','').replace(']','').replace(':','').replace('-','')#去掉题目中的一些符号，防止创建失败
            dirpath.append(rootpath+realtitle+'.txt')
            nexturls.append('http://cl.wm3.lol/' + real.get('href'))
            #print 'success to create dir'
        except Exception as e:
            print 'fail to create dir ',rootpath+unicode(real.get_text()),e
    return nexturls,dirpath

def main():
    pagestartnum=1 #页码数
    pageendnum=8
    rooturls = ['http://cl.wm3.lol/thread0806.php?fid=20&search=&page={}'.format(str(i)) for i in range(pagestartnum, pageendnum, 1)]
   # rooturl1 = 'http://cl.wm3.lol/thread0806.php?fid=20'
    #url='http://cl.wm3.lol/htm_data/20/1704/2335231.html'
    rootpath = 'd:\\downloadtextnew\\'
    os.makedirs(rootpath)
    #downloadetxt(url,rootpath)
    k=pagestartnum-1
    for url in rooturls:
        k=k+1
        folder = rootpath + u'第' + str(k) + u'页' + '\\'
        os.mkdir(folder)  # 中文前加一个u解决创建中文文件夹乱码问题
        nexturls,dirpath=get_dirpath_nexturls(url,folder)
        for i in range(len(nexturls)):
            downloadetxt(nexturls[i],dirpath[i])

main()


