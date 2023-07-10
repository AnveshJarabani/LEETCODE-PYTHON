def combinationsum(lst, target):
    result = []

    def dfs(i, cur, sum):
        if sum == target:
            result.append(cur.copy())
            return
        if sum > target or i >= len(lst):
            return
        cur.append(lst[i])
        dfs(i, cur, sum + lst[i])
        cur.pop()
        dfs(i + 1, cur, sum)

    dfs(0, [], 0)
    return result


print(combinationsum([2, 3, 6, 7], 7))
