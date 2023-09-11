def shifted_arr_search(nums, target):
    span = len(nums)
    l, r = 0, span - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > nums[-1]: # this has to be compared with nums[-1] because we are trying to find pivot only
            l = mid+1
        else:
            r = mid-1
    def bst(l,r,target):
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l=mid+1
        return -1

    #Binary search over the elements on the pivot element's left
    if (answer:= bst(0,l-1,target))!=-1: return answer
    return bst(l,span-1,target)


shiftArr = [1,2]
num = 2
print(shifted_arr_search(shiftArr, num))
"""
Define the pivot index as representing the smallest element in nums.


In a rotated sorted array, the pivot value signifies where the rotation occurs. It partitions the array (of length nnn) into two sorted portions nums[0 ~ pivot - 1] and nums[pivot ~ n - 1].

Approach 1: Find Pivot Index + Binary Search
Intuition
If you are not familiar with binary search, please refer to our explore cards Binary Search Explore Card. We will focus on the usage in this article and not the underlying principles or implementation details.

To pinpoint the pivot value, we can employ a modified binary search algorithm and find the leftmost element that is smaller than or equal to the last element in nums.


After identifying the middle element in the searching space [left ~ right], we compare nums[mid] with nums[-1].

If nums[mid] > nums[-1], it suggests that the pivot value lies on the right of nums[mid]. We will then proceed with the right half of the search space, which is [mid + 1 ~ right].
Otherwise, the pivot value is nums[mid] or it's situated to the left of nums[mid], we continue with the left half of the searching space, which is [left ~ mid - 1].

By determining the pivot value, we set the boundaries for our subsequent binary searches. Once we have the pivot value, we can execute two binary searches on each half of the array to locate the target element.


Note: the typical way to calculate mid is (left + right) / 2. However, a safer way is left + (right - left) / 2. The two equations are equivalent, but the second one is safer because it guarantees no number larger than right is ever stored. In the first equation, if left + right is huge, then it could end up overflowing.

Algorithm
Perform a binary search to locate the pivot element by initializing the boundaries of the searching space as left = 0 and right = n - 1. While left < right:

Let mid = left + (right - left) // 2.
If nums[mid] > nums[n - 1], this suggests that pivot is located to the right of mid, hence we set left = mid + 1. Otherwise, pivot could be either at mid or to the left of mid, in which case we should set right = mid - 1.
Upon completion of the binary search, we have the pivot index denoted as pivot = left.

nums consists of two sorted subarrays, nums[0 ~ left - 1] and nums[left ~ n - 1].

Perform a binary search over nums[0 ~ left - 1] for target. If target is within this subarray, return its index.

Otherwise, perform a binary search over nums[left ~ n - 1] for target. If target is within this subarray, return its index. Otherwise, return -1.

Implementation
"""
