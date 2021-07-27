import pandas as pd

from titanic.models.dataset import Dataset


class Service(object):
    dataset = Dataset() #Constructor생성. java= Dataset dataset = new Dataset()

    def new_model(self, payload:str)->object:#csv로 들어온 파일을 payload를 통하여 dataframe으로 전환
        this  = self.dataset #생성자
        this.context = './data/'#dataset에 (경로) '../data/'(위치)을 넣어주고.
        this.fname = payload#파일명 dataset에
        return pd.read_csv(this.context+this.fname)#경로에 파일명을 읽어와라?

