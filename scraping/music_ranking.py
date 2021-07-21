import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime
from pandas import DataFrame
class MusicRanking(object):
    #java 에서는 파라미터가 없으면 defalut constructor python에서는 init이없으면
    findall = []
    fname =''
    url = ''
    tag_name=''
    headers ={'User-Agent':'Mozilla/5.0'}
    class_name = []
    artists=[]
    titles=[]
    dict={}
    df = None
    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text
    def output(self):
        soup = BeautifulSoup(self.html, 'lxml')
        info= []
        for name in self.class_name:
            info.append(soup.find_all(name=f'{self.tag_name}', attrs={'class': f'{name}'}))
        for title,artist in zip(*info):
            print('제목 :'+title.find('a').text+'\n가수 : '+artist.find('a').text)


        #for i,j in zip(info):
         #   self.titles.append(i.find('a').text)
          #  self.artists.append(j.find('a').text)

           # for i in info:
            #    print(i.find('a').text)

        #for title,artist in zip(info):
            #print( "Rank" + "title:" + title.find('a').text + "*" + "singer" + artist.find('a').text)

    def insert_dict(self):
        soup = BeautifulSoup(self.html, 'lxml')
        info = []
        for name in self.class_name:
            info.append(soup.find_all(name=f'{self.tag_name}', attrs={'class': f'{name}'}))
        for title, artist in zip(*info):
            self.titles.append(title.find("a").text)
            self.artists.append(artist.find("a").text)
        for i,j in zip(self.artists,self.titles):
            self.dict[i] = j
        #for i in range(0, len(self.tag_name)):
        #    self.dict[self.titles[i]]=self.artists[i]
        #방법 2
      #  for i, j in zip(self.titles, self.artists):
       #     self.dict[i]=j
        #방법 3
        #for i,j in enumerate(self.titles):
         #   self.dict[j] = self.artistis[i]

        #print(dict)
    def dict_to_dataframe(self):
        dict = self.dict
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')

    def df_to_csv(self):
        path = f'./data/{self.fname}.csv'
        self.df.to_csv(path,sep=',', na_rep='NaN')

def print_menu(ls):
    # return '\t'.join(ls)
    t = ''
    for i, j in enumerate(ls):
        t += str(i) + '-' + j + '\t'
    return int(input(t))
def main():
    now = datetime.datetime.now()
    mr = MusicRanking()
    while 1:
        menu = print_menu(['exit','Bugs URL','Melon URL','Output','Bugsinsert_dict',
                           'Meloninsert_dict','Dict To Dataframe','Dataframe to CSV' ])
        if menu ==0:return
        elif menu == 1:
            d = now.strftime('%Y%m%d')
            t = now.strftime('H')
            mr.class_name = ['title', 'artist']
            mr.tag_name = 'p'
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string = f'chartdate={d}&charthour={t}'
            mr.set_html()
        elif menu == 2:
            mr.class_name=['ellipsis rank01','ellipsis rank02']
            mr.tag_name = 'div'
            dt = now.strftime('%Y%m%d%H')
            mr.domain ='https://www.melon.com/chart/index.htm?'
            mr.query_string =f'dayTime={dt}'
            mr.set_html()
        elif menu == 3:
            mr.output()
        elif menu == 4:
            mr.class_name = ['title', 'artist']
            mr.tag_name = 'p'
            mr.insert_dict()
            mr.dict_to_dataframe()
        elif menu == 5:
            mr.class_name = ['ellipsis rank01', 'ellipsis rank02']
            mr.tag_name = 'div'
            mr.insert_dict()
            mr.dict_to_dataframe()
        elif menu == 6:
            mr.fname = input(f'파일명 :')
            mr.df_to_csv()
if __name__ == '__main__':
    main()