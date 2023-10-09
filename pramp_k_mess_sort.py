import heapq


def func(arr, k):
    h, result = [], []
    for val in arr:
        if len(h) > k + 1:
            heapq.heappush(h, val)
        else:
            result.append(heapq.heappop(h, val))
    while h:
        result.append(heapq.heappop(h))
    return result
