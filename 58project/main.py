#coding:utf8
from multiprocessing import Pool#调用计算机多核心完成任务
from channel_extract import channel_list
from page_parsing import get_links_from


def get_all_links_from(channel):#遍历所有的信息贴
    for num in range(1,50):
        get_links_from(channel,num)#spyder1 将某一页的购买帖内的所有网页放入数据库


if __name__=='__main__':
    pool = Pool()#创建进程池 可以传参数processes=4
    pool.map(get_all_links_from,channel_list.split())#map可以将第二个集合内的所有参数依次传入第一个函数
    pool.close()  # close后进程池不能在apply任务
    pool.join()

