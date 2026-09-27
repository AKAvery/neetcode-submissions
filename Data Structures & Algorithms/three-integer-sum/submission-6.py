class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = 0
        k = len(nums) - 1
        sList = sorted(nums)
        result = []
        print(sList)
        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                print(i, j, k)
                if -sList[i] == sList[j] + sList[k]:
                    if [sList[i], sList[j], sList[k]] not in result:
                        result.append([sList[i], sList[j], sList[k]])
                    j += 1
                elif -sList[i] < sList[j] + sList[k]:
                    k -= 1
                else: 
                    j += 1

        return result