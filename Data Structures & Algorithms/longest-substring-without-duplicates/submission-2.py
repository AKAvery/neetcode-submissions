class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        myHash = set()
        longest = 0
        found = False
        while r < len(s):
            if s[r] in myHash:
                found = True
            print(found)
            if found == True:
                l += (s[l:r].find(s[r])) + 1
                print("l: ", l)
            else: 
                myHash.add(s[r])
                print("myHash after add: ", myHash)
            print("l before curr calc: ", l)
            curr = s[l : r + 1]

            longest = max(len(curr), longest)
            print(curr, longest)

            r += 1
            found = False
        return longest