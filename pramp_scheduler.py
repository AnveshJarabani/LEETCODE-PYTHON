def meeting_planner(slotsA, slotsB, dur):
    p1, p2 = 0, 0
    spanA, spanB = len(slotsA) - 1, len(slotsB) - 1
    while p1 < spanA and p2 < spanB:
        if (
            abs(slotsA[p1][1] - slotsB[p2][0]) >= dur
            and abs(slotsB[p2][1] - slotsA[p1][0]) >= dur
        ):
            max_start = max(slotsA[p1][0], slotsB[p2][0])
            print(slotsA[p1][0], slotsB[p2][0])
            return [max_start, max_start + dur]
        elif slotsA[p1][1] > slotsB[p2][1]:
            p2 += 1
        else:
            p1 += 1
    return []


slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8
print(meeting_planner(slotsA, slotsB, dur))
"""
Time Planner
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return an empty array.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

Implement an efficient solution and analyze its time and space complexities.

Examples:

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: [] # since there is no common slot whose duration is 12
"""
