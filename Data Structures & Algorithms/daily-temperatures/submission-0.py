class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        self.stack = []
        self.resultStack = []
        self.delStack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            print(self.stack)
            while self.stack and temp > self.stack[-1][0]:
                pop = self.stack.pop()
                print(i - pop[1])
                result[pop[1]] = i - pop[1]
            print("result", result)
            pair = temp, i
            self.stack.append(pair)
        return result