'''이름 나이 주소를 입력받아서 자기 소개하는 프로그램을 작성하시오
출력은 안녕하세요, 제이름은 TOM이고 나이는 28세이고, 서울에 거주합니다. 로됩니다
이때 여러사람이 전부 입력 받아서 전체가 일괄 출력되는 시스템이어야 합니다.'''
class Person(object):
    def __init__(self,name,age,adress):
        self.name = name
        self.age = age
        self.adress = adress
    def to_String(self):
        print(f'안녕하세요, 제이름은 {self.name}이고 나이는 {self.age}이고, {self.adress}에 거주합니다. 로됩니다')



def main():
    persons = []
    while 1:
        menu = input('0- 1- 2-')
        if menu =='0':
            return
        elif menu =='1':
            persons.append(Person(input('이름'),input('나이'),input('주소')))
        elif menu =='2':
            for i in persons:
                i.to_String()

if __name__ == '__main__':
    main()























class Person(object):
    def __init__(self,name,age,adress):
        self.name = name
        self.age = age
        self.adress = adress

    def to_String(self):
            print(f' 안녕하세요, 제이름은 {self.name} 나이는 {self.age}세이고, {self.adress}에 거주합니다.')

def main():
    persons = []
    while 1:
        menu = input('0-Exit 1-생성 2-목록')
        if menu=='0': return
        elif menu=='1': persons.append(Person(input(f'이름'),input(f'나이'),input(f'주소')))
        elif menu =='2':
            for i in persons:
                i.to_String()


if __name__ == '__main__':
    main()