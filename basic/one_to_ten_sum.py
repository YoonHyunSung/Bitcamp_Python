#def one_to_ten_sum1():
   #example 1
#    sum = 0
    #function 조건 parametherzone과 앞에 호출이없다(example --.sum..).
 #   for i in range(1, 11):
  #      sum += i
   # print(sum)
def one_to_ten_sum2():
    print(sum(i for i in range(1, 11)))
def one_to_ten_sum3():
    print(sum(range(1, 11)))
#print(sum(return i for i in range(1, 11))) return omission되어있는거임.
if __name__ == '__main__':
    one_to_ten_sum3()


