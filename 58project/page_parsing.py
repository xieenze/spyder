#coding:utf8
from  bs4 import BeautifulSoup
import requests
import time
import  os
os.environ['PYTHON_EGG_CACHE'] = '/tmp/'
import pymongo

client = pymongo.MongoClient('localhost',27017)#建立mongodb数据库连接
test = client['test']#新建数据库
url_list = test['url_list']#建表
item_info = test['item_info']#建表


#spyder1 将某一页的帖子内的所有网页放入数据库
def get_links_from(channel,pages,who_sells=0):
    #http://sh.58.com/shouji/1/pn2/
    list_view='{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td','t'):
        links = soup.select('tbody > tr > td.t > a')[6:]
        for link in links:
            item_link = link.get('href').split('?')[0]
            if 'jump.zhineng.58.com' in item_link:
            #if item_link.find('jump')>0:
                pass
            else:
                print item_link
                url_list.insert_one({'url': item_link})
            #print item_link
    else :
        pass
    print '=========================================================================================='
    print '=========================================================================================='



# for i in range(90,103):
#     get_links_from('http://sh.58.com/bijiben/',i)

#spyder2 将具体某一页卖东西的帖子内的信息放入数据库
def get_item_info(url):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    no_longer_exist = '404' in soup.find('script',type="text/javascript").get('src').split('/') if soup.find('script',type="text/javascript").get('src')!=None else False
    if no_longer_exist:
        pass
    else:

        title=soup.select(' div.col_sub.mainTitle > h1')[0].text if soup.select(' div.col_sub.mainTitle > h1') else None
        price=soup.select('span.price.c_f50')[0].text if soup.select('span.price.c_f50') else None
        data = soup.select('li.time')[0].text if soup.select('li.time') else None
        area = soup.select('.c_25d a')[1].text if soup.find_all('span', 'c_25d') else None
        item_info.insert_one({'title':title,'price':price,'data':data,'area':area})
        print title,price,data,area


urls=url_list.find()
for url in urls:
    print url
    get_item_info(url['url'])




















