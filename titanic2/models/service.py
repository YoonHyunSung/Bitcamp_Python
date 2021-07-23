import pandas as pd

from titanic2.models.dataset import Dataset


class Service():
    dataset = Dataset()

    def model(self, payload:str)->object:
        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context+this.fname)

def create_train(s:[str])->object:
    return None
def create_label(this)->int:
    return None
def drop_feature(this, *featuire)->object:
    return None
def embarked_nominal(this)->str :
    return this
def fare_oridnal(this)->float:
    return this
def title_nominal(this)->object:
    return this
def gender_norminal(this)->str:
    return this
def age_ordina(this)->int:
    return this
def create_k_fold()->object:
    return None
def accuracy_by_classfier(this)->str:
    return ""