def isPalindrome(x):
    List=list(num)
    if List[0]=='-' or len(List)<3:
        return False
    if List==List[::-1]:
        return True
    else:
        return False
num = input()
print(isPalindrome(num))
