from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_span=len(words[0])
        len_substr=word_span*len(words)
        words_map={i:words.count(i) for i in set(words)}
        if len_substr>len(s):
            return []
        i,res=0,[]
        while i<(len(s)-len_substr)+1:
            cur_str=s[i:i+len_substr]
            p,str_lst=0,[]
            while p<len(cur_str):
                str_lst.append(cur_str[p:p+word_span])
                p+=word_span
            # for word in words: 
            #     if word in str_lst:
            #         str_lst.remove(word)
            #     else:
            #         break
            sub_map={i:str_lst.count(i) for i in set(str_lst)}
            if sub_map==words_map:
                res.append(i)
            i+=1
        return res

print(Solution().findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))