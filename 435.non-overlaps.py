def overlaps(intervals):
    count=0
    intervals.sort()
    for indx in range(len(intervals)):
        if intervals[indx][0]<=intervals[indx+1][0] and \
        intervals[indx][1]<=intervals[indx+1][1]:
            count+=1
    return count


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(overlaps(intervals))
