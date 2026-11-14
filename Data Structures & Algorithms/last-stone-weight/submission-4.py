import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneMaxHeap = [-s for s in stones]
        heapq.heapify(stoneMaxHeap)
        while len(stoneMaxHeap) > 1:
            x, y = heapq.heappop(stoneMaxHeap), heapq.heappop(stoneMaxHeap)       
            if x != y:
                z = abs(y - x)
                z = -z
                heapq.heappush(stoneMaxHeap, z)
        if stoneMaxHeap:
            return -stoneMaxHeap[0]
        return 0