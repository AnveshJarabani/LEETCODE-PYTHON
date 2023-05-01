def maxprofit(lst):
    l,r,maxP=0,1,0
    while r<len(lst):
        if lst[l]<lst[r]:
            cur=lst[r]-lst[l]
            maxP=max(maxP,cur)
        else:
            l=r
        r+=1
    return maxP
import ast
print(maxprofit(ast.literal_eval(input())))

#   profit=0
#         for i in range(0,len(lst)-1):
#             cur_profit=max(lst[i+1:])-min(lst[0:i+1])
#             if cur_profit>profit:
#                 profit=cur_profit
#         return profit