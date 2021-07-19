'''
국어kor 영어eng 수학math 를입력받아서
평균점수를 통해 A~F 학점을 출력하시오
'''


class Grade():
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math
    def average(self):
        return self.total()/3
    @staticmethod
    def main():
        kor = int(input('국어점수 : '))
        eng = int(input('영어점수 : '))
        math = int(input('수학점수 : '))
        grade = Grade(kor, eng, math)
        print(int(grade.average()))

        if str(grade.average()) >= '90':
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
        print(f'{result}')



Grade.main()
