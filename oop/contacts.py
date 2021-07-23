'''name phone email address
'''


class Contacts(object):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
def to_string(self):
    print(f'{self.name},{self.phone},{self.email}.{ self.address}')


def set_contacts() -> object:
    return Contacts(input('name'), input('phone'), input('email'), input('address'))


def get_contacts(ls):
    for i in ls:
        Contacts.to_string(i)



def del_contact(ls,name):
    for i,j in enumerate(ls):#i=index j=element
        if name == j.name:
            del ls[i]
        else :
            break

def menu(ls) -> int:
    t=''
    for i,j in enumerate(ls):
        t +=str(i)+'-'+j+'\t'
    return int(input(t))
# return '\t'.join(ls)

def main():
    ls = []
    while 1:
        menu = menu(['exit','set_contacts','get_contacts','del_contact'])
        if menu == 1:
            t = set_contacts()
            ls.append(t)
        elif menu == 2:
            get_contacts(ls)
        elif menu == 3:
            name = input('삭제할이름')
            del_contact(ls,name)
        else:
            break

if __name__ == '__main__':
    main()