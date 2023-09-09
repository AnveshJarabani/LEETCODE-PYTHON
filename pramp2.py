def get_shortest_unique_substring(arr, str):
  arr_map={i:1 for i in arr}
  sub_map={}
  have,want=len(arr),0
  min_l=float('inf')
  l=0
  for r in range(len(str)):
    char=str[r]
    sub_map[char]=1+sub_map.get(char,0)
    if char in arr_map and arr_map[char]==sub_map[char]:
      want+=1
    while have==want:
      if r-l+1<min_l:
        sub_str=[l,r]
        min_l=r-l+1
      sub_map[str[l]]-=1
      l+=1
      if char in arr_map and arr_map[char]>sub_map[char]:
        have-=1
  return str[sub_str[0]:sub_str[1]+1] if min_l != float('inf') else ''
  
arr = ['x','y','z']
str = "xyyzyzyx"
print(get_shortest_unique_substring(arr,str))

