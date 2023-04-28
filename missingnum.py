import ast
class solution:
    def missingnum(self,nums):
       return [i for i in range(0,len(nums)+1) if i not in nums][0]
   
nums=ast.literal_eval(input())
print(solution().missingnum(nums=nums))