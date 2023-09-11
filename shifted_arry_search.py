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
1,2,3,4,5 -> 3,4,5,1,2
          
input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left
shiftAarr.index(num) o(n) o(1)
1. offset of a [sorted distinct array] & [it's shifted by x positions]

1,2,3,4,5

9 12 1 2 4 5 6 7 8
l 9, r 8, mid 


[9, 10, 12, 17, 2, 4, 5] - > 
1. find the offset.
2. use l,r at the offset point and offset-1
3. continue with log(n) soution like a sorted arry. ->
k=4
l,r=4-4,3-4
while 

1,r 
output: 3 # since it’s the index of 2 in arr
"""
