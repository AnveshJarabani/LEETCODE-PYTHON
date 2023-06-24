def arrange_coins(n):
    rows = 0
    steps = 0
    while steps < n:
        rows += 1
        steps += rows
    return rows if steps == n else rows - 1


print(arrange_coins(5))


def binary_coin_search(n):
    l, r = 1, n
    res = 0
    while l <= r:
        mid = (l + r) // 2
        coins = (mid / 2) * (mid + 1)
        if coins > n:
            r = mid - 1
        else:
            l = mid + 1
            res = max(mid, res)
    return res
