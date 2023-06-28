def merge(intervals,newInterval):
    intervals.append(newInterval)
    intervals.sort()
    result=[intervals[0]]
    for indx in range(1,len(intervals)):
        if result[-1][1]>=intervals[indx][0]:
            temp=result[-1]+intervals[indx]
            result[-1]=[min(temp),max(temp)]
        else:
            result.append(intervals[indx])
    return result
intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval=[4,8]
print(merge(intervals,newInterval))