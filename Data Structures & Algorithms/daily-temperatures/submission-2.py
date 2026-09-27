class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                pop = stack.pop()
                result[pop[1]] = i - pop[1]
            pair = temp , i
            stack.append(pair)
        return result