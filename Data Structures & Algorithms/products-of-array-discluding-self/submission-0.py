class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i, x in enumerate(nums):
            product = 1
            for j, y in enumerate(nums):
                if i != j:
                    product *= y
            result.append(product)
            product = 1
        return result