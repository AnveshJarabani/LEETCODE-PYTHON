class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_set=[]
        max_substr=0
        for i in s:
            if i not in temp_set:
                temp_set.append(i)
                max_substr=max(max_substr,len(temp_set))
            else:
                temp_set=temp_set[temp_set.index(i)+1:]
                temp_set.append(i)
        return max_substr
    
print(Solution().lengthOfLongestSubstring('aabaab!bb'))