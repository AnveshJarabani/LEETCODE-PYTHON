needle=input()
haystack=input()
def needle_index(haystack,needle):
    result=0
    while haystack!="":
        if haystack.startswith(needle):
            return result
        else:
            haystack=haystack[1:]
            result+=1
    return -1
result=needle_index(haystack,needle)
print(result)
    
