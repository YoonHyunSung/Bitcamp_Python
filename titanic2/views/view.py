from titanic2.models.dataset import Dataset
from titanic2.models.service import Service


class View(object):
    dataset = Dataset()
    service = Service()

    def preprocessing(self, train, test) -> object:
        service = self.service
        dataset = self.dataset
        dataset.train = service.model(train)
        dataset.test = service.model(test)
        return dataset
    def modeling(self, train, test):
        this = self.preprocessing(train, test)
        print(f'{(this.train).head(2)}')
        print(f'{(this.test).head(2)}')

if __name__ == '__main__':
    v = View()
    v.modeling('train.csv','test.csv')