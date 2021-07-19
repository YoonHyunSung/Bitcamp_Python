

class Grade():
    def __init__(self,name):
        self.name = name
        self.scores = []

    def addScores(self,score):
        self.scores.append(score)
    def average(self):
        return sum(self.scores)/len(self.scores)
    @staticmethod
    def main():
        grade = Grade(input('Input Student Name : '))
        for i in ['korea','eng','math']:
            grade.addScores(int(input(f'{i}:')))
        avg = grade.average()
        print(f'{grade.name}{int((grade.average()))}{int(avg)}')


        """if str(grade.average()) >= '90':
            result ='A'
        elif str(grade.average()) >= '80':
            result ='B'
        elif str(grade.average()) >= '70':
            result ='C'
        elif str(grade.average()) >= '60':
            result ='D'
        elif str(grade.average()) >= '50':
            result ='E'
        else:
            result ='F'
        print(f'{grade.addScores()}{result}')"""



Grade.main()
