class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        sP = s.replace(" ", "")
        right = len(sP) - 1
        while left < right:
            while sP[left].isalnum() == False:
                left += 1
                if left > len(sP) - 1:
                    left = len(sP) - 1
                    break
            while sP[right].isalnum() == False:
                right -= 1
                if right < 0:
                    right = 0
                    break            
            if sP[left].lower() != sP[right].lower() and sP[left].isalnum() and sP[right].isalnum():
                return False
            left += 1
            right -=1
        return True