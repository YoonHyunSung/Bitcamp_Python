from pprint import pprint


def str_to_list(payload: str) -> []:
    return [char.lower() for char in payload if char.isalnum()]
#    strs = []
   # for char in payload:
    #    if char.isalnum():
   #         strs.append(char.lower())
#  print(strs)
def isPalindrome(ls:[]) -> bool:
    while len(ls) > 1:
       if ls.pop(0) !=ls.pop():
           return False
    return True

if __name__ == '__main__':
    ls =str_to_list("A man , a plan , a canal: pnama")
    pprint(ls)
    pprint(isPalindrome(ls))
