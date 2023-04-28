def threeSum(nums):
    # if nums.count(0)==len(nums) and len(nums)>2:
    #     return [[0,0,0]]
    nums.sort()
    span=len(nums)
    k=0
    j,l=k+1,span-1
    lst=[]
    while (k<span-2):
        if j<l:
            sum=nums[k]+nums[j]+nums[l]
            if sum<0:
                while nums[j]==nums[j+1] and j<l-1:
                    j+=1
                j+=1
            elif sum>0:
                while nums[l]==nums[l-1] and j<l-1:
                    l-=1
                l-=1
            elif sum==0:
                lst.append([nums[k],nums[j],nums[l]])
                print([nums[k],nums[j],nums[l]]," K= ",k)
                while nums[j]==nums[j+1] and j<l-1:
                    j+=1
                j+=1
        else:
            while nums[k]==nums[k+1] and k<span-2:
                k+=1
            k+=1
            j,l=k+1,span-1
    return lst
print(threeSum(list(map(int,input().split(",")))))
