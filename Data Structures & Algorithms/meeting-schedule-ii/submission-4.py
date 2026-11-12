"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        intervals.sort(key=lambda i: i.start)
        startList = [i.start for i in intervals]
        intervals.sort(key=lambda i: i.end)
        endList = [i.end for i in intervals]
        print(startList, endList)
        maxRooms = 0
        currRooms = 0
        s, e = 0, 0
        while s < len(intervals) and e < len(intervals):
            if startList[s] < endList[e]:
                s += 1
                currRooms += 1
            else:
                e += 1
                if currRooms > maxRooms:
                    maxRooms = currRooms
                currRooms -= 1
        maxRooms = max(currRooms, maxRooms)
        return maxRooms
        
                
