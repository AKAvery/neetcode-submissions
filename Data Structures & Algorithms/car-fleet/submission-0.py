class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        result = []
        myList = []
        pairs = []
        for i, pos in enumerate(position):
            pair = pos, speed[i]
            print(pair)
            pairs.append(pair)
        sortedList = sorted(pairs, reverse=True)
        for pair in sortedList:
            myList.append((target - pair[0]) / pair[1])
        for var in myList:
            if stack and var <= stack[-1]:
                continue
            else:
                #print("we're in else")
                stack.append(var)
        return len(stack)