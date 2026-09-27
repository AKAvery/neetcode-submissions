class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        myHash = set()
        longest = 0
        found = False
        while r < len(s):
            if s[r] in myHash:
                l += (s[l:r].find(s[r])) + 1   
            else: 
                myHash.add(s[r])   
            curr = s[l : r + 1]
            longest = max(len(curr), longest)
            r += 1
            found = False
        return longest