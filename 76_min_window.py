class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=='': return ''
        l,r=0,1
        lst=[i for i in t]
        t_map={i:lst.count(i) for i in set(lst)} 
        t_span=len(t_map)
        h_map={i:0 for i in t_map}
        check_span=0
        while r<len(s):
            if s[l] in h_map:
                h_map[s[l]]+=1
                if h_map[s[l]]>=t_map[s[l]]:
                    check_span+=1
            if check_span>=t_span:
                result=s[l:r+1]
            if r<len(s): r+=1
            else: l-=1
        return result
            
print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))