#coding:utf-8
from bs4 import BeautifulSoup
import requests,urllib
import time

#url = 'http://cl.oiee.biz/thread0806.php?fid=7&search=&page=4'
urls=['http://photo.hupu.com/nba/feature?p={}&o=1'.format(str(i))for i in range(1,3,1)]
#wb_data = requests.get(url)
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Cookie':'pgv_pvi=7853641728; fts=1476085314; _ga=GA1.2.1112240921.1477045215; rpdid=kmiqlokqoodopmmwpsiww; buvid3=43235FB7-FBCD-4BA8-B68C-CA30C7685A9330819infoc; pgv_si=s8973609984; purl_token=bilibili_1479459456; sid=am7gca4m; CNZZDATA2724999=cnzz_eid%3D592149708-1476085314-%26ntime%3D1479460337'
}

def gg(url):
    wb_data = requests.get(url)#请求网站数据
    soup = BeautifulSoup(wb_data.text,'lxml')#网页转成源码
    titles    = soup.select('h3 > a[target="_blank"]')
    wangzhi = []
    i=0
    #imgs      = soup.select('img[width="160"]')
    #cates     = soup.select('div.p13n_reasoning_v2')
    for title in titles:
        #data={'title':title.get('href')}
        wangzhi.append('http://cl.oiee.biz/'+title.get('href'))
        download_links = []
        foler_path = 'D:\\pachong\\'
        for wz in wangzhi:
            print(wz)
            source_code = requests.get(wz)
            soup = BeautifulSoup(source_code.text, 'lxml')
            #print (soup.find_all('input[type="image"]'))
            for pic in soup.find_all('input'):
                p_link=pic.get('src')
                download_links.append(p_link)
            for item in download_links:
                try:
                    urllib.urlretrieve(item, foler_path + item[-20:-10]+'.jpg')
                    i=i+1
                except Exception as e:
                    print (e)
                print ('done'+str(i))
        time.sleep(4)
    '''for title, img, cate in zip(titles, imgs, cates):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'cate': list(cate.stripped_strings),
        }
        print(data)'''
def ggg(url):
    wb_data = requests.get(url)  # 请求网站数据
    soup = BeautifulSoup(wb_data.text, 'lxml')  # 网页转成源码
    titles = soup.select('dl > dt > a')#获取有关title的标签内的内容
    wangzhi = []
    download_links = []
    foler_path = 'D:\\pachong\\'
    for title in titles:
        wangzhi.append('http://photo.hupu.com' + title.get('href'))#获取title的url

    for wz in wangzhi:
        #print(wz)
        source_code = requests.get(wz)
        soup = BeautifulSoup(source_code.text, 'lxml')
        # print (soup.find_all('input[type="image"]'))
        for pic in soup.find_all('img["id="bigpicpic"]'):
            p_link = pic.get('src')
            download_links.append(p_link)
            print (download_links)
        for item in download_links:
            try:
                urllib.urlretrieve(item, foler_path + item[-20:-12] + '.jpg')
                i = i + 1
            except Exception as e:
                print (e)
            print ('done' + str(i))
    time.sleep(4)



for u in urls:
    ggg(u)
