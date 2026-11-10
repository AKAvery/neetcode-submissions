class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        myHeap = []
        for num in nums:
            if len(myHeap) >= k:
                if myHeap[0] < num:
                    heapq.heappop(myHeap)
                    heapq.heappush(myHeap, num)
            else:
                heapq.heappush(myHeap, num)
        return myHeap[0]