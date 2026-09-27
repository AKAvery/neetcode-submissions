class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for index1, x in enumerate(nums):
            for index2, y in enumerate(nums):
                if (x + y == target) and index1 != index2:
                    result.append(index1)
                    result.append(index2)
                    print(result)
                    return result
