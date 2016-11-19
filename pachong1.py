# coding:utf8
import requests, urllib
from bs4 import BeautifulSoup

# 1get code
url = 'http://cl.oiee.biz/htm_data/16/1611/2136695.html'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Cookie':'__cfduid=d5e339ebc72b3c1713f769fa0786e73a11479364908; 227c9_lastfid=0; 227c9_lastvisit=0%091479389433%09%2Fread.php%3Ftid%3D2142197%26page%3D2; __utmt=1; CNZZDATA950900=cnzz_eid%3D762292266-1479363741-%26ntime%3D1479389942; __utma=198696189.297603167.1479364909.1479388253.1479393607.6; __utmb=198696189.4.10.1479393607; __utmc=198696189; __utmz=198696189.1479364909.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
}
source_code = requests.get(url,headers=header)
plain_text = source_code.text
Soup = BeautifulSoup(plain_text,'lxml')
download_links = []
foler_path = 'D:\\pachong1\\'
for pic_tag in Soup.find_all('input'):
    pic_link = pic_tag.get('src')
    print pic_link.get_text()
    download_links.append(pic_link)


for item in download_links:
    try:
        urllib.urlretrieve(item, foler_path+ item[-20:-10]+'.jpg')
    except Exception as e:
        print (e)
    print ('done')