dict={2:('a','b','c'),
      3:('d','e','f'),
      4:('g','h','i'),
      5:('j','k','l'),
      6:('m','n','o'),
      7:('p','q','r','s'),
      8:('t','u','v'),
      9:('w','x','y','z'),}
def PHONELETTERS(digits):
    digits=digits.replace('1',"")
    digits=digits.replace('0',"")
    if digits=='':
        return []
    ar=[int(i) for i in digits]
    result=[]
    i=1
    temp=dict[ar[0]]
    while i<len(ar):
        for j in dict[ar[i]]:
            for k in range(0,len(temp)):
                result.append(temp[k]+j)
        if result!=[] and i<len(ar)-1:
            temp=result
            result=[]
            i+=1
            continue
        i+=1
    if result==[]:
        return list(temp)
    return result
digits=input()
print(PHONELETTERS(digits))