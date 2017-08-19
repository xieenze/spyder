#coding:utf8
import requests
from bs4 import BeautifulSoup

url = 'https://2017.icml.cc/Conferences/2017/Schedule?type=Poster'

'''获取所有title的url和title内容'''
def getNextUrl(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    Soup = BeautifulSoup(plain_text, 'lxml')
    titles = Soup.select('div.maincardBody')
    titleLink = Soup.select("div.maincard.narrower.Poster")
    nextUrlList = []
    for link in titleLink:
        # print link.get("id")[9:]
        nextUrlList.append('https://2017.icml.cc/Conferences/2017/Schedule?showEvent=' + link.get("id")[9:])
    titlesList = []
    for title in titles:
        titlesList.append(title.get_text())
    return nextUrlList,titlesList



'''获取每个title对应的摘要'''
def getAbstract(nextUrl):
    source_code = requests.get(nextUrl)
    plain_text = source_code.text
    Soup = BeautifulSoup(plain_text, 'lxml')
    text =  Soup.select('div.abstractContainer')
    #return text[0].get_text()
    return text[0].get_text()

'''
https://2017.icml.cc/Conferences/2017/Schedule?type=Poster
https://2017.icml.cc/Conferences/2017/Schedule?showEvent=606
'''



#links,titles = getNextUrl(url)
#print len(links),len(titles)
'''for link in links:
    print link

for title in titles:
    print title
'''

'''
nextUrl='https://2017.icml.cc/Conferences/2017/Schedule?showEvent=665'
text = getAbstract(nextUrl)
print text
'''


if __name__=="__main__":
    links , titles = getNextUrl(url)
    length = len(links)
    for i in range (0,length):
        print (" 一共%d篇文章，第%d篇下载中" % (length,i+1))
        link = links[i]
        text = getAbstract(link)
        title = titles[i]
        print "link:    "+link
        print "title:   "+title
        print "text:    "+text
        print "==============================="

