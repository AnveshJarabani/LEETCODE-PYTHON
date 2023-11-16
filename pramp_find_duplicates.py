def find_duplicates(a1, a2):
  p1,p2=0,0
  res=[]
  while p1<len(a1) and p2<len(a2):
    if a1[p1]<a2[p2]:
      p1+=1
    elif a1[p1]>a2[p2]:
      p2+=1
    else:
      res.append(a1[p1])
      p1+=1
      
  return res  
arr1 = [1, 2, 3, 5, 6, 7, 10]
arr2 = [3, 6]

len(arr1) = m
len(arr2) = n
m >> n

for num in smaller_arr:
  if binary_search(num, larger_arr):
    res.append(num)
              
return res

O(mlog(n))

print(find_duplicates(arr1,arr2))
  
"""
arr1 = [1, 2, 3, 5, 6, 7, 10]  len(arr1) = 7
                          p1 = 6
arr2 = [3, 6, 7, 8, 10]        len(arr2) = 5
                    p2 = 2
len(a1)!=len(a2)
find all common elements in ascending order. 
case 1 - M ≈ N -
case 2 - M >> N 
assumption - uniques. 
p1,p2=0,0
res=[]
while p1<len(a1) and p2<len(a2):
  if a1[p1]<a2[p2]:
    p1+=1
  elif a1[p1]>a2[p2]:
    p2+=1
  else:
    res.append(a1[p1])
return res
[1,50]
[1,2,4,5.......50]
time case 1(m+n)
time case 1 - o(m)
space - o(n)
"""
