import ast
nums=ast.literal_eval(input())
target=ast.literal_eval(input())
def searchInsert(nums,target):
    L,R=0,len(nums)-1
    while L<=R:
        mid=(L+R)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            L=mid+1
        else:
            R=mid-1
    return L
    # counter=0
    # for i in nums:
    #     if i==target:
    #         return counter
    #     elif i>target:
    #         return counter
    #     counter+=1
    # return counter
result=searchInsert(nums,target)
print(result)