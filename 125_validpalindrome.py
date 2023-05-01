def palindrome(s):
    lst=[i for i in s.lower() if i.isalpha()]
    if len(lst)==1:
        return False
    elif len(lst)%2!=0:
        return lst[:len(lst)//2]==lst[(len(lst)//2)+1:][-1::-1]
    else:
        return lst[:len(lst)//2]==lst[len(lst)//2:][-1::-1]
print(palindrome(input()))
