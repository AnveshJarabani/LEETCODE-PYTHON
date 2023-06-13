x = 3
y = 4
x_bin=bin(x)[2:]
y_bin=bin(y)[2:]
max_len=max(len(x_bin),len(y_bin))
x_bin=x_bin.zfill(max_len)
y_bin=y_bin.zfill(max_len)
result=""
carry=0
for i in range(max_len-1,-1,-1):
    r=carry
    r+=1 if x_bin[i]=="1" else 0
    r+=1 if y_bin[i]=="1" else 0
    result= ('1' if r%2==1 else '0')+result
    carry=0 if r<2 else 1
if carry!=0:
    result='1'+result
print(int(result,2))