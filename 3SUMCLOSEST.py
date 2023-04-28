def threeSumclosest(nums,target):
    nums.sort()
    span=len(nums)
    diff=abs(target-(nums[0]+nums[1]+nums[span-1]))
    result=nums[0]+nums[1]+nums[span-1]
    for i in range(0,span-2):
        j,k=i+1,span-1
        while nums[j]==nums[j+1] and j+1<k:
            j+=1
        if nums[j-1]==nums[j] and (j-1)!=i:
            j-=1
        while nums[k]==nums[k-1] and j+1<k:
            k-=1
        while (j<k):
            temp=(nums[i]+nums[j]+nums[k])
            if temp>target:
                k-=1
            elif temp<target:
                j+=1
            else:
                return temp
            if diff>abs(target-temp):
                diff=abs(target-result)
                result=temp
            if diff==0:
                return result
    return result
nums=list(map(int,input().split(",")))
target=int(input())
print(threeSumclosest(nums,target))