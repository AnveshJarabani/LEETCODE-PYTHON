#     # if nums.count(0)==len(nums) and len(nums)>2:
#     #     return [[0,0,0]]
#     nums.sort()
#     span = len(nums)
#     k = 0
#     j, l = k + 1, span - 1
#     lst = []
#     while k < span - 2:
#         if j < l:
#             sum = nums[k] + nums[j] + nums[l]
#             if sum < 0:
#                 while nums[j] == nums[j + 1] and j < l - 1:
#                     j += 1
#                 j += 1
#             elif sum > 0:
#                 while nums[l] == nums[l - 1] and j < l - 1:
#                     l -= 1
#                 l -= 1
#             elif sum == 0:
#                 lst.append([nums[k], nums[j], nums[l]])
#                 print([nums[k], nums[j], nums[l]], " K= ", k)
#                 while nums[j] == nums[j + 1] and j < l - 1:
#                     j += 1
#                 j += 1
#         else:
#             while nums[k] == nums[k + 1] and k < span - 2:
#                 k += 1
#             k += 1
#             j, l = k + 1, span - 1
#     return lst


def threeSum(nums):
    if len(nums) == 3 and sum(nums) == 0:
        return [nums]
    nums.sort()
    i, j, k = 0, 1, len(nums) - 1
    result = []
    while i < len(nums) - 3:
        target_sum = -nums[i]
        while j < k:
            if nums[j] + nums[k] > target_sum:
                k -= 1
            elif nums[j] + nums[k] < target_sum:
                j += 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                while nums[j] == nums[j - 1] and j < k:
                    j += 1
        i += 1
        while nums[i] == nums[i - 1] and i < len(nums) - 2:
            i += 1
        j = i + 1
        k = len(nums) - 1
    return result


print(threeSum(list(map(int, input().split(",")))))
