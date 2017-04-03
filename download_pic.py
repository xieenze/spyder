# coding:utf8
import requests, urllib
from bs4 import BeautifulSoup
import os
import time


#url = 'http://cl.wm3.lol/htm_data/8/1704/2335131.html'
#path='d:/pachong111/'
rootpath='D:\\download\\'#x下载到本地的地址
rooturl='http://cl.wm3.lol/thread0806.php?fid=8'#网址
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

def download_pic(url,path):#下载某一个帖子中图片

    source_code = requests.get(url)
    plain_text = source_code.text
    Soup = BeautifulSoup(plain_text, 'lxml')
    download_links = []
    foler_path=path
    images = Soup.find_all('input')

    for pic_tag in Soup.find_all('input'):
        if pic_tag.get('src') != None:
            pic_link = pic_tag.get('src')
            #print pic_link
            download_links.append(pic_link)
    i=1
    #print '下载新帖子了,帖子名字是： '+str(path)+'  帖子的链接是 '+str(url)
    print path,url
    for item in download_links:
        try:
            urllib.urlretrieve(item, foler_path + item[-6:])
            print ('下载第 '+str(i)+' 张图成功！ 图片是'+item)
            i=i+1
        except Exception as e:
            print '下载第 '+str(i)+' 张图失败！ 图片是 '+item


def getnexturls(rooturl):#获取这一页所有帖子的url
    source_code = requests.get(rooturl)
    source_code.encoding = 'gb2312'
    plain_text = source_code.text
    Soup = BeautifulSoup(plain_text, 'lxml')
    titles = Soup.select('tbody > tr > td.tal > h3 > a')
    errors = Soup.select('td.tal > h3 > a > b > font')
    # print len(errors)
    # for e in errors:
    #      print e.get_text()
    # reals= list(set(titles)^set(errors)) #titles集合删除errors集合
    reals = titles[8:]  # 直接过滤前八个

    # for i in titles:
    #     if i not in errors:
    #         reals.append(i)
    folder = rootpath
    nexturls=[]
    for real in reals:  # 创建对应的文件夹
        nexturls.append('http://cl.wm3.lol/'+real.get('href'))
    return nexturls

def createdir(rooturl,rootpath):
    source_code = requests.get(rooturl)
    source_code.encoding = 'gb2312'
    plain_text = source_code.text
    Soup = BeautifulSoup(plain_text, 'lxml')
    titles = Soup.select('tbody > tr > td.tal > h3 > a')
    errors = Soup.select('td.tal > h3 > a > b > font')
    # print len(errors)
    # for e in errors:
    #      print e.get_text()
    # reals= list(set(titles)^set(errors)) #titles集合删除errors集合
    reals = titles[8:]  # 直接过滤前八个
    '''#ajaxtable > tbody:nth-child(2) > tr:nth-child(11) > td.tal > h3 > a > b > font
    #ajaxtable > tbody:nth-child(2) > tr:nth-child(13) > td.tal > h3 > a
    '''
    dirpath=[]
    # for i in titles:
    #     if i not in errors:
    #         reals.append(i)
    folder = rootpath
    for real in reals:  # 创建对应的文件夹
        try:
            os.mkdir(folder+real.get_text())
            dirpath.append(folder+real.get_text()+'\\')
            #print 'success to create dir'
        except Exception as e:
            print 'fail to create dir '
    return dirpath


nexturls = getnexturls(rooturl)
dirpath = createdir(rooturl,rootpath)#nexturls和dirpath 长度一致

for i in range(len(nexturls)):
    #print nexturls[i],dirpath[i][12:-6],len(nexturls)
    download_pic(nexturls[i],dirpath[i])
    #time.sleep(1)


#createdir(rooturl,rootpath)
#download_pic(url,path)
# os.makedirs('d:/pachong/pachong')
# os.mkdir('d:/pachong111')
# folders=['d:/pachong/pachong{}'.format(str(i)) for i in range(0,10,1)]批量创建文件夹
# for folder in folders:
#     os.mkdir(folder)

