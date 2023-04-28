def longestCommonPrefix(strs):
    if len(strs)==1:
        return strs[0]
    strs_nums=[]
    for i in range(0,len(strs)):
        strs_nums.append(len(strs[i]))
    min_str=strs[strs_nums.index(min(strs_nums))]
    x=list(min_str)
    if len(x)==0:
        return ""
    output=""
    i=0
    for letter in x:
        for p,each_word in enumerate(strs):
            if letter==each_word[i]:
                if p==len(strs)-1:
                    output=output+letter
            else:
                return output
        i+=1
    return output

print(longestCommonPrefix(input().split(",")))
        