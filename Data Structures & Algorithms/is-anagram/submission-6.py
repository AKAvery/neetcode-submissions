class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        for char in s:
            freqs[char] = freqs.get(char, 0) + 1
        for char in t:
            freqs[char] = freqs.get(char, 0) - 1
        for freq in freqs:
            if freqs[freq] != 0:
                return False
        return True