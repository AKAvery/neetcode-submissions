class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        myHeap = intervals
        heapq.heapify(myHeap)
        result = []
        while myHeap:
            if len(myHeap) > 1:
                first = heapq.heappop(myHeap)
                second = heapq.heappop(myHeap)
                if first[1] < second[0]:
                    result.append(first)
                    heapq.heappush(myHeap, second)
                else:
                    merged = [min(first[0], second[0]), max(first[1], second[1])]
                    heapq.heappush(myHeap, merged)
            else:
                result.append(heapq.heappop(myHeap))
        return result


        