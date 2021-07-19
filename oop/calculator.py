class Calculator():#상속

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1+self.num2

    def subtract(self):
        return self.num1 - self.num2

    def mutiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    @staticmethod
    def main():
        while 1:
            num1 = int(input('first number: '))
            num2 = int(input('second number: '))
            calc = Calculator(num1, num2)
            menu = input('0-Exit 1-add 2-subtract 3-multiple 4-divide\n')
            if menu == '0':
                return
            elif menu == '1':
                print(f'{calc.num1}+{calc.num2}={calc.add()}')
                break
            elif menu == '2':
                print(f'{calc.num1}-{calc.num2}={calc.subtract()}')
                break
            elif menu == '3':
                print(f'{calc.num1}*{calc.num2}={calc.mutiple()}')
                break
            elif menu == '4':
                print(f'{calc.num1}/{calc.num2}={calc.divide()}')
                break

            else:
                print('fail')
                break




Calculator.main()
