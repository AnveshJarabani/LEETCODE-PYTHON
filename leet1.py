temp=dict(
I = 1,
V = 5,
X = 10,
L = 50,
C = 100,
D = 500,
M = 1000)
class Solution:
    s=input().replace("\"","")
    def roman(self,s:str) -> int:
        output=0
        i=0
        while i < len(s):
            x=temp[s[i]]
            if i!=len(s)-1:
                if ((s[i+1]=='V' or s[i+1]=='X') and (s[i]=='I'))| \
                    ((s[i+1]=='L' or s[i+1]=='C') and (s[i]=='X'))| \
                    ((s[i+1]=='D' or s[i+1]=='M') and (s[i]=='C')):
                    x=temp[s[i+1]]-temp[s[i]]
                    i+=1
            output=output+x
            i+=1
        return output
    print(roman(input().replace("\"","")))
