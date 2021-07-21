import urllib.request

import urllib3
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Melon(object):
    def __init__(self,url):
        self.url = url
        self.header = {'User-Agent':'Mozilla/5.0'}
    def scrap(self):

        modi1=urllib.request.Request(self.url,headers = self.header)
        htmlcontent1 = urllib.request.urlopen(modi1).read()
        soup = BeautifulSoup(htmlcontent1,'lxml')
        n_title =0
        a = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        b = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        for i,j in zip(a,b):
            n_title += 1
            print(str(n_title)+"Rank"+"title:"+i.find('a').text+"*"+"singer"+j.find('a').text)


def main():
    Melon('https://www.melon.com/chart/index.htm?dayTime=2021071015').scrap()

if __name__ == '__main__':
    main()