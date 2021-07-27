import csv
import pandas as pd
import matplotlib.pyplot as plt
"""
next() 는 두가지 포맷으로 사용된다
function 구조로 사용되면 header 만 리턴한다
consumer 구조로 사용 되면 data 에서 header를 제거한다

data : [] = list() 는 list 타입의 data 를 list()로 초기화 시키는 것이다.
단, 한 메소드 내에서만 사용하면 로컬에서 초기화 한다. 예제는 다음과 같아.
data :[] = None
def save_highest_temperatures(self):
    data = list()
그러나, 여러 메소드에서 사용하면 필드에서 초기화 한다.


"""
class ChangedTemperaturesOnMyBirthday():
    data : [] = []
    highest_temperatures : [] = list()
    lower_temperatures : [] = list()
    date : [] = list()

    def processing(self):
        self.read_data()
        self.save_data_to_temperature()
        self.save_data_to_temperature1()

    def read_data(self):
        data = csv.reader(open('data/seoul.csv', 'rt', encoding='UTF-8'))
        next(data)
        self.data = data
        # self.data = []
        # self.data.append(data)
    def show_highest_temperature(self):
        return [i[-1] for i in self.data]
    def save_highest_temperature(self):
        [self.highest_temperatures.append(float(row[-1])) for row in self.data if row[-1] !='']

        #for row in data :
         #   if row[-2] !='':
               #self.lower_temperature.append(float(row[-2]))
            #if row[-1] !='':
             #   self.highest_temperature.append(float(row[-1]))
            #date = row[0].split('-')
            #self.date.append(date)

        #self.highest_temperature = highest_temperature
    def visualize_highest_temperature(self):
        plt.plot(self.highest_temperatures, 'r')
        plt.figure(figsize=(10,2))
        plt.show()
    def highest_temperature_my_birthday(self):
        high = [] #최고기온
        low = [] #최저기온
        for i in self.data:
            if i[-1] !='' and i[-2] !='':
                if 1983 <= int(i[0].split('-')[0]):
                    if i[0].split('-')[1]=='02' and i[0].split('-')[2]== '14':
                        high.append(float(i[-1]))
                        low.append(float(i[-2]))
        plt.rc('font', family='malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
        plt.title('내 생일의 기온 변화 그래프')
        plt.plot(high,'hotpink', label='high')
        plt.plot(low, 'skyblue',label='low')
        plt.legend()
        plt.show()
        #[self.highest_temperatures.append(float(i[-1])) for i in self.data if i[-1] !=''
         #if find_month(i[0], )]
if __name__ == '__main__':
    this = ChangedTemperaturesOnMyBirthday()
    this.read_data()
    this.highest_temperature_my_birthday()
    #this.save_highest_temperature()
    #this.visualize_highest_temperature()
    #this.visualize_data()
    #this.extract_date_data()
    #print(this.highest_temperature)

