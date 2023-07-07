def canPartition(nums):
    if sum(nums) % 2!=0:
        return False
    target=sum(nums)//2
    dp=set()
    dp.add(0)
    for i in range(len(nums)-1):
        nextdp=set()
        for t in dp:
            if t+nums[i]==target:
                return True
            nextdp.add(t)
            nextdp.add(t+nums[i])
        dp=nextdp
    return True if target in dp else False
print(canPartition([1,5,11,5]))