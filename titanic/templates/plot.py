from titanic.models.dataset import Dataset
from titanic.models.service import Service
import matplotlib.pyplot as plt
from  matplotlib import font_manager,rc
import seaborn as sns
rc('font', family=font_manager.FontProperties(fname='C:/Users/bitcamp/anaconda3/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/H2GTRE.ttf').get_name())
"""
titanis's features
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
"""
class Plot(object):
    dataset =Dataset()
    service =Service()
    def __init__(self):
        self.df = self.service.new_model('train.csv')

    def show_plot_survived_dead(self):
        this = self.df
        f, ax = plt.subplots(1,2,figsize=(18, 8))
        series = this['Survived'].value_counts()
        print(type(series))
        print(series)
        series.plot.pie(explode=[0,0.1],autopct='%1.1f',ax=ax[0],shadow=True)
        #this['Survived'].value_counts().plot.pie(explode=[0,0.1], autopct='%1.1f',ax=ax[0],shadow=True)
        ax[0].set_title('0.사망자vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()
    def show_plot_pclass(self):
        this = self.df
        this['생존결과'] = this['Survived'].replace(0,'사망자').replace(1,'생존자')
        this['좌석등급'] = this['Pclass'].replace(1,'1등석').replace(2,'1등석').replace(3,'1등석')
        sns.countplot(data=this, x='좌석등급',hue='생존결과')
        plt.show()
    def show_plot_Embarked(self):
        this = self.df
        this['생존결과'] = this['Survived'].replace(0, '사망자').replace(1, '생존자')
        this['승선항구'] = this['Embarked'].replace('C', '쉘버그').replace('S', '사우스햄튼').replace('Q','퀸즈파크')
        sns.countplot(data=this, x='승선항구', hue='생존결과')
        plt.show()
    def show_plot_sex(self):
        this =self.df
        f, ax = plt.subplots(1, 2,figsize=(18,8))
        male_series = this['Survived'][this['Sex']=='male'].value_counts()
        female_series = this['Survived'][this['Sex']=='female'].value_counts()
        male_series.plot.pie(explode=[0, 0.1], autopct='%1.1f', ax=ax[0], shadow=True)
        female_series.plot.pie(explode=[0, 0.1], autopct='%1.1f', ax=ax[1], shadow=True)
        ax[0].set_title('남성의 생존비율0.사망자vs 1.생존자')
        ax[1].set_title('여성의 생존비율0.사망자vs 1.생존자')

        plt.show()
        #this['생존결과'] = this['Survived'].replace(0, '사망자').replace(1, '생존자')
        #this['승선항구'] = this['Embarked'].replace('male', '남성').replace('female', '여성')
        #sns.countplot(data=this, x='성별', hue='생존결과')
        #plt.show()