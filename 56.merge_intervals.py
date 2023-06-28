def merge(intervals):
    intervals.sort()
    result=[intervals[0]]
    for indx in range(1,len(intervals)):
        if result[-1][1]>=intervals[indx][0]:
            temp=result[-1]+intervals[indx]
            result[-1]=[min(temp),max(temp)]
        else:
            result.append(intervals[indx])
    return result
intervals=[[1,4],[0,0]]
print(merge(intervals))