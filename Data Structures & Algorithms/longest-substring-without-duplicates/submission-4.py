class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        myHash = set()
        longest = 0
        for i in range(len(s)):
            while s[i] in myHash:
                myHash.remove(s[l])
                l += 1
            myHash.add(s[i])
            longest = max(longest, i - l + 1)
        return longest
            