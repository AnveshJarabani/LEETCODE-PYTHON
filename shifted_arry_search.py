def find(arr, num,offset):
    if len(arr)==1 and arr[0]==num:
      return offset
    span = len(arr)
    l, r = 0, span - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < num:
            l = mid
        elif arr[mid] > num:
            r = mid+offset
        else:
            return arr[mid]
    return -1


def shifted_arr_search(shiftArr, num):
    span = len(shiftArr)
    l, r = 0, span - 1
    while l < r:
        if l == (r - 1):
            offset = r
            break
        mid = (l + r) // 2
        if shiftArr[mid] < shiftArr[r]:
            r = mid
        elif shiftArr[l] < shiftArr[mid]:
            l = mid
    if num >= shiftArr[0] and num <= shiftArr[offset - 1]:
        res = find(shiftArr[:offset], num,0)
    elif num >= shiftArr[offset] and num <= shiftArr[span - 1]:
        res = find(shiftArr[offset:], num,offset)
    return res


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
