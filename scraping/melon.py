import urllib.request

import urllib3
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Melon(object):
    def __init__(self,url,header):
        self.url =url
        self.header = header
    def scrap(self):
        modi1=urllib.request.Request(self.url,headers = self.header)
        htmlcontent1 = urllib.request.urlopen(modi1).read()
        soup = BeautifulSoup(htmlcontent1,'lxml')
        n_title =0
        a = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        for i,j in enumerate(soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})):
            n_title += 1
            print(str(n_title)+"Rank")
            print("title:"+j.find('a').text+"singer"+a[i].find('a').text)


def main():
    Melon('https://www.melon.com/chart/index.htm?dayTime=2021072017',{'User-Agent':'Mozilla/5.0'}).scrap()

if __name__ == '__main__':
    main()