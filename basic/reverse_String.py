from pprint import pprint
from typing import List

def str_to_list(payload: str) -> []:
    return [i for i in payload if i.isalnum()]
def list_to_str(ls:[])-> str:
    return ''.join(ls)
def reverse_String(s:[str])->[]:
    #return [i for i in s if ]
    left, right =0, len(s) - 1
    while left <right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

if __name__ == '__main__':
    ls = str_to_list(input("Input"))
    print(ls)
    ls2 = list_to_str(ls)
    print(ls2)
    reverse_String(ls)

    #print(reverse_String(ls2))

