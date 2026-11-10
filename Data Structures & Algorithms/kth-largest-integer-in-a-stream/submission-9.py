import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.index = k
        self.stream = []
        for num in nums:
            if len(self.stream) >= k:
                if num > self.stream[0]:
                    heapq.heappop(self.stream)
                    heapq.heappush(self.stream, num)
            else:  
                heapq.heappush(self.stream, num)


    def add(self, val: int) -> int:
        if len(self.stream) >= self.index:
            if val >= self.stream[0]:
                heapq.heappop(self.stream)
                heapq.heappush(self.stream, val)
        else:
            heapq.heappush(self.stream, val)

        return self.stream[0]
   