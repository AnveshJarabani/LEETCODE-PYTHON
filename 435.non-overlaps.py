def overlaps(intervals):
    count = 0
    intervals.sort()
    previous_end = intervals[0][0]
    for i, j in intervals[1:]:
        if previous_end <= i:
            previous_end = j
        else:
            previous_end = min(j, previous_end)
            count += 1
    return count


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(overlaps(intervals))
