from collections import Counter
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    counter_map=Counter(s)
    for i in range(2,len(s)):
        sub_str=s[0:i]
        counter_map[''.join(sorted(sub_str))]+=1
        for j in range(1,len(s)):
            if i+j<=len(s):
                counter_map[''.join(sorted(s[j:j+i]))]+=1
    result=0
    for val in counter_map.values():
        result+=val*(val-1)//2
    return result

print(sherlockAndAnagrams('aacbbc'))