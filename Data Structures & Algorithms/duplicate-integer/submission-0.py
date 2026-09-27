class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arrayOne = []
        for x in nums:
            if x in arrayOne:
                return True
            arrayOne.append(x)
        return False