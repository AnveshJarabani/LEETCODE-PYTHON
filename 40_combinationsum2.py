def combinationsum2(lst, target):
    result = []
    lst.sort()

    def dfs(i, cur, sum):
        if sum == target:
            result.append(cur)
            return
        if sum > target:
            return
        for i in range(i, len(lst)):
            dfs(i, cur.append(lst[i]), sum + lst[i])

    dfs(0, [], 0)
    return result


print(combinationsum2([10, 1, 2, 7, 6, 1, 5], 8))
