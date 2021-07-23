from scraping.models.dataset import Dataset
from scraping.models.service import Service


class View():
    dataset = Dataset()
    service = Service()
    def preprocessing(self, bugs,melon):
        dataset = self.dataset
        service = self.service
        dataset.bugs = service.model(bugs)
        dataset.melon = service.model(melon)
        return dataset
    def modeling(self, bugs, melon):
        this = self.preprocessing(bugs, melon)
        print(f'{(this.bugs)}')
        print(f'{(this.melon).head(2)}')




if __name__ == '__main__':
    view = View()
    view.modeling('bugs.csv','melon.csv')