class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqs = {}
        for char in s:
            freqs[char] = freqs.get(char, 0) + 1
        for char in t:
            freqs[char] = freqs.get(char, 0) - 1
        for count in freqs.values():
            if count != 0:
                return False
        return True