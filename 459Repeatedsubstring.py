def repeatedsubstr(s):
    N = len(s)

    def pattern(n):
        for i in range(0, N - n, n):
            if s[i : i + n] != s[i + n : i + n * 2]:
                return False
        return True

    for i in range(1, len(s) // 2 + 1):
        if pattern(i):
            return True
    return False


print(repeatedsubstr("abababab"))


#  Solution 2:
def repeatedsubstr(s):
    ds = (s * 2)[1:-1]
    return s in ds
