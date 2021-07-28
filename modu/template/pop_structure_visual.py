import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as tk
import pandas as pd
import os

class Population(object):
    data : [] = list()

    def read_data(self):
      #data =pd.da('./data/202106_202106_연령별인구현황_월간.csv')
      #data_read=pd.read_csv(data,header=1,thousands=',')
      data = csv.reader(open('./data/202106_202106_연령별인구현황_월간.csv','rt',encoding='UTF-8'))
      print(data)
      #self.data = data_read
    def pop_per_dong(self,dong:str)-> []:
        arr=[]
        [arr.append(j) for i in self.data if dong in i[0] for j in i[3:]]
        return arr

    def show_plot(self,arr:[]):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()
    def find_similar_area(self):
        data =self.data
        home = np.array([])
        name = input('동:')
        #[np.append(home, np.array([i])) for i in data if name in i[0] for j in i[3:]]
        print(data)
        for i in data:
            if data[''] == '':
                print(name)
                home = np.array(i[3:],dtype=int)
        plt.rc('font',family='Malgun Gothic')
        plt.title(name+'지역 인구 구조')
        plt.plot(home)
        plt.show()


        #[home.append(i) for i in data if name in i[0] for j in i[3:]]
        #for i in data:
            #if name in i[0]:
                #for j in i[3:]:
                    #home.append(j)

        print(home)

if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    pop.data
    #pop.pop_per_dong('역삼1동')
    #pop.find_similar_area()