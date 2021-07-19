'''이름 나이 주소를 입력받아서 자기 소개하는 프로그램을 작성하시오
출력은 안녕하세요, 제이름은 TOM이고 나이는 28세이고, 서울에 거주합니다. 로됩니다
이때 여러사람이 전부 입력 받아서 전체가 일괄 출력되는 시스템이어야 합니다.'''
class Person(object):
    def __init__(self):
        #self.age = age
        #self.adress = adress
        #self.name = name
        self.peoples = []
    def addPerson(self,person):
        return self.peoples.append(person)

    def to_String(self,param):
        print(f' 안녕하세요, 제이름은 {param.name} 나이는 {param.age}세이고, {param.address}에 거주합니다.')
    @staticmethod
    def main():
        person = Person()
        
        #person = Person(input('이름'),input('나이'),input('주소'))
        #print(person.age,person.name,person.adress)
        for i in ['이름','나이','주소']:
            person.addPerson((input(f'{i} :')))
        for i in [person.peoples]:





Person.main()