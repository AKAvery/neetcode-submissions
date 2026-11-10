class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        myHeap = []
        answer = []
        for point in points:
            distance = math.sqrt(point[0]*point[0] + point[1]*point[1])
            heapq.heappush(myHeap, (distance, point[0], point[1]))
        print(myHeap)
        for i in range(k):
            answer.append(heapq.heappop(myHeap)[1:])
        return answer