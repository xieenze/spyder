
from bs4 import BeautifulSoup
import requests
import time

url = 'http://cl.oiee.biz/thread0806.php?fid=7&search=&page=4'
urls=['http://cl.oiee.biz/thread0806.php?fid=7&search=&page={}'.format(str(i))for i in range(1,90,1)]
wb_data = requests.get(url)
def gg(url):
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles    = soup.select('h3 > a[target="_blank"]')
    #imgs      = soup.select('img[width="160"]')
    #cates     = soup.select('div.p13n_reasoning_v2')
    for title in titles:
        data={'title':title.get('href')}
        print (data.values())

    '''for title, img, cate in zip(titles, imgs, cates):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'cate': list(cate.stripped_strings),
        }
        print(data)'''

for u in urls:
    gg(u)
