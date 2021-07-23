import pandas as pd

from scraping.models.dataset import Dataset


class Service(object):
    dataset = Dataset()
    def model(self, payload):
        dataset = self.dataset
        dataset.context = '../data/'
        dataset.fname = payload
        return pd.read_csv(dataset.context+dataset.fname)
