def foursum(nums, target):
    ct = 1
    i = 0
    while True:
        if nums[i] == nums[i + 1]:
            ct += 1
            if ct > 4:
                nums.pop(i + 1)
            else:
                i += 1
        else:
            ct = 1
            i += 1
        if i == (len(nums) - 1):
            break
    result = []
    HT = {}
    unq = list(set(nums))
    for i in list(set(nums)):
        HT[i] = nums.count(i)
    HT = dict(sorted(HT.items(), key=lambda x: x[1], reverse=True))
    for i in dict(list(HT.items())[:-3]):
        if HT[i] == 4:
            if i * 4 == target:
                result.append([i, i, i, i])
            if (len(HT) - list(HT.keys()).index(i)) > 3:
                ind = list(HT.keys()).index(i)
                for j in dict(list(HT.items())[ind:]):
                    if HT[j] > 2:
                        if (i * 3 + j) == target:
                            result.append([i, i, i, j])
                        if (i + j) * 2 == target:
                            result.append([i, i, j, j])
                        if (i + 3 * j) == target:
                            result.append([i, j, j, j])
                    if HT[j] == 2:
                        if (i + j) * 2 == target:
                            result.append([i, i, j, j])
                        if (i * 3 + j) == target:
                            result.append([i, i, i, j])
                    if HT[j] == 1:
                        if (i * 3 + j) == target:
                            result.append([i, i, i, j])
            if (len(HT) - list(HT.keys()).index(i)) > 3:
                ind = list(HT.keys()).index(i)
                for j in dict(list(HT.items())[ind:]):
                    if HT[j] >= 2:
                        if (i + j) * 2 == target:
                            result.append([i, i, j, j])
                    else:
                        inj = list(HT.keys()).index(j)
                        for k in dict(list(HT.items())[inj:]):
                            if (i * 2 + j + k) == result:
                                result.append([i, i, j, k])

            if HT[i] == 1:
                return result


nums = list(map(int, input().split(",")))
target = int(input())
print(foursum(nums, target))


#  if HT[i]>=3:
#                 ind=list(HT.keys()).index(i)
#                 for j in dict(list(HT.items())[ind:]):
#                     if (i*3+j)==target:
#                         result.append([i,i,i,j])
#             if HT[i]>=2:
#                 ind=list(HT.keys()).index(i)
#                 for j in dict(list(HT.items())[ind:]):
#                     if HT[j]>=2:
#                         if (i+j)*2==result:
#                             result.append([i,i,j,j])
#                     else:
#                         inj=list(HT.keys()).index(j)
#                         for k in dict(list(HT.items())[inj:]):
#                             if (i*2+j+k)==result:
#                                 result.append([i,i,j,k])
