import ast
input=ast.literal_eval(input())
def lenghtoflis(nums):
    hash_list=[1]*len(nums)
    for i in range(len(nums),-1,-1):
        for j in range(i+1,len(nums)):
            if nums[i]<nums[j]:
                hash_list[i]=max(hash_list[i],hash_list[j]+1)
    return max(hash_list)
print(lenghtoflis(input))

        
        
        