def disappeared(nums):
    hsh = []
    for n in nums:
        i = abs(n) - 1
        nums[i] = -1 * abs(nums[i])
    for r, i in enumerate(nums):
        if r > 0:
            hsh.append(i + 1)
    return hsh


print(disappeared([4, 3, 2, 7, 8, 2, 3, 1]))
