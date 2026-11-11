"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        myHeap = [(i.start, i.end) for i in intervals]
        heapq.heapify(myHeap)
        prev = heapq.heappop(myHeap)
        while myHeap:
            curr = heapq.heappop(myHeap)
            if prev[1] > curr[0]:
                return False
            prev = curr
        return True
