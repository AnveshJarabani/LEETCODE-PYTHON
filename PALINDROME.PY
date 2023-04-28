def isPalindrome(num) -> bool:
    List=list(str(num))
    if List[0]=='-':
        return False
    ln=len(List)
    if len(List) % 2==0:
        return List[:ln//2]==List[ln//2:][::-1]
    else:
        return List[:ln//2]==List[ln//2+1:][::-1]
x=input()
print(isPalindrome(x))