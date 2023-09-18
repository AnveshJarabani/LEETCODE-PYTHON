def find_array_quadruplet(arr, s):
  if not arr: return []
  arr.sort()
  span=len(arr)
  l,r=0,span-1
  while l<r:
    target=s-(arr[l]+arr[r])
    if target<0:
      r-=1
      continue
    sub_arr=arr[l+1:r]
    print(sub_arr)
    s_l,s_r=0,len(sub_arr)-1
    while s_l<s_r:
      cur_sum=sub_arr[s_l]+sub_arr[s_r]
      if cur_sum<target:
        s_l+=1
      elif cur_sum>target:
        s_r-=1
      else:
        return [arr[l],sub_arr[s_l],sub_arr[s_r],arr[r]]
    l+=1
  return []
      
#  arr = [2, 7, 4, 0, 9, 5, 1, 3]
 # s = 20
arr=[4,4,4,4]
s=16
print(find_array_quadruplet(arr,s))
"""
Array Quadruplet
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

Example:

input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
"""