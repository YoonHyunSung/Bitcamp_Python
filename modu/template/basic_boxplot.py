import matplotlib.pyplot as plt
import random

from modu.template import ChangedTemperaturesOnMyBirthday
from modu.template.basic_hist import highest_temperature

def sorted_random_arr()-> []:
    arr = []
    [arr.append(random.randint(1, 1000)) for i in range(13)]
    return arr

def show_boxplot(arr:[]):
    plt.boxplot(arr)
    plt.show()

def show_boxplot_month(month:str):
    plt.boxplot(highest_temperature(month))
    plt.show()
def show_boxplot_all_month():
    birth = ChangedTemperaturesOnMyBirthday()
    birth.read_data()
    data = birth.data

    #monthls =[]
    #month1 = []
    month = [[],[],[],[],[],[],[],[],[],[],[],[]]
    #for row in data:
      #  if row[-1] !='':
     #       month[int(row[0].split('-')[1])-1].append(float(row[-1]))
    #print(len(month))
    #print(month)
    #[[month1[int(row[0].split('-')[1]) - 1].append(float(row[-1])) for row in data if row[-1] != ''] for i in range(12)]
    #month = []
    [[month[int(row[0].split('-')[1])-1].append(float(row[-1])) for row in data if row[-1] !=''] for i in range(12)]
    #print(month[4])
    #print(len(month))
    return month

def show_boxplot_per_date(month : str):
    birth = ChangedTemperaturesOnMyBirthday()
    birth.read_data()
    data = birth.data
    day =[]
    [day.append([]) for i in range(31)]
    [day[int(i[0].split('-')[2])-1].append(float(i[-1])) for i in data if i[-1] !='' if i[0].split('-')[1]==month]
    plt.style.use('ggplot')
    plt.figure(figsize=(10,5),dpi=300)
    plt.boxplot(day, showfliers=False)
    plt.show()

if __name__ == '__main__':
    #highest_temperature_boxplot(arr=highest_temperature(month='08'))
    #show_boxplot_all_month()
    #show_boxplot(show_boxplot_all_month())
    show_boxplot_per_date('08')