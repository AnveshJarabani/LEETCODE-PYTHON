class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        hash_map={i:0 for i in arr}
        for i in arr:
            hash_map[i]+=1
        occur_list=[val for _,val in hash_map.items()]
        return list(set(occur_list))==occur_list
print(Solution().uniqueOccurrences([1,2,2,1,1,3]))