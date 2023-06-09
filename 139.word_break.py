def wordbreak(s, dct):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True
    for i in range(len(s) - 1, -1, -1):
        for w in dct:
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
                break
    return dp[0]


s = "leetcode"
dct = ["leet", "code"]

print(wordbreak(s, dct))
