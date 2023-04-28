def twoSum(nums,target):
    temp=nums.copy()
    temp.sort()
    x=0
    y=len(nums)-1
    while x < len(nums):
        while y >0:
            i=temp[x]
            m=temp[y]
            if target<i+m:
                y-=1
            elif target>i+m:
                x+=1
            else:
                return [nums.index(i),nums.index(m)]
print('ENTER list')
nums=list(map(int,input().split(",")))
print('Enter target')
target=int(input())
print(twoSum(nums,target))  