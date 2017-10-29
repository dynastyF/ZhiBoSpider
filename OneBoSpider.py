# -*- coding:utf-8 -*-

import urllib2
import bs4
from bs4 import BeautifulSoup

if __name__ == '__main__':
    #ID = input("请输入斗鱼主播id:\n")
    ID = 85981
    print ID
    #res = urllib.urlopen("https://www.douyu.com/room/follow");

    #url = "https://www.douyu.com/85981"
    url = "https://www.douyu.com/85981"
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0')
    res = urllib2.urlopen(req)
    #print res.read()


    soup = BeautifulSoup(res,'html.parser',from_encoding = 'utf-8')

    we = soup.find_all('div',id="anchor-info" )
    for w in we:
        #print w.h1.get_text()
        print w
