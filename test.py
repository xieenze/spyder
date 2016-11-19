#coding:utf8
import requests,urllib
from bs4 import BeautifulSoup
#1get code
url='http://jandan.net/pic/page-2301'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
source_code=requests.get(url,headers=header)
plain_text=source_code.text


Soup=BeautifulSoup(plain_text)


download_links = []
foler_path = 'D:\\pachong\\'
for pic_tag in Soup.find_all('img'):
    pic_link = pic_tag.get('src')
    download_links.append(pic_link)
    
for item in download_links:
    try:
        urllib.urlretrieve(item,foler_path+"ch/"+item[-10:])
    except Exception as e:
        print (e)
    print ('done')