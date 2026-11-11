class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        coolDown = deque()
        counts = {}
        time = 0
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        myHeap = [-counts[task] for task in counts]
        heapq.heapify(myHeap)

        while coolDown or myHeap:
            time += 1
            if myHeap:
                freq = heapq.heappop(myHeap) + 1
                if freq != 0:
                    coolDown.append((freq ,time + n))
            if coolDown:
                if coolDown[0][1] == time:
                    heapq.heappush(myHeap, coolDown.popleft()[0])

        return time