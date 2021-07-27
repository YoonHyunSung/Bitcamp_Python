import pandas as pd
import matplotlib.pyplot as plt
class Test():
    data : [] =[]
    def read_data(self):
        data = pd.read_csv('data/seoul.csv')
        self.data =data
        print(data)

if __name__ == '__main__':
    test = Test()
    test.read_data()
