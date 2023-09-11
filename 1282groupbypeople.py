class Solution:
    def groupThePeople(self, gs: List[int]) -> List[List[int]]:
        res_map={}
        for i,val in enumerate(gs):
            if val in res_map:
                if len(res_map[val][-1])<val:
                    res_map[val][-1].append(i)
                else:
                    res_map[val].append([i])
            else:
                res_map[val]=[[i]]
        result=[]
        for lst in res_map.values():
            result.extend(lst)
        return result

"""
Key to solving this problem is 
[3,3,3,3,3,1,3]
1. gs[i]=val(size of group)
can group indexes to the length of value.
use same values to group.
so basically, group on the groups with same values. but with indexes.
keep pooling indexes into a cur_list until len(cur_list)==val.
o(n) approach:
iterate through each value once.
if it's a seen value, add it to the list of the key.
if not seen, add a new key with value and the index into the list.
if the len of internal list is equal to key, then add a new list.
how to keep track length - 
Key:([[vals..]],cur_len)
so if cur_len==key, change cur_len to 0 and add new list inside.
"""