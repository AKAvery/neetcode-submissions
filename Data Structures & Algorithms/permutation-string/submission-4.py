class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window = len(s1)
        notIt = False
        for i in range(len(s2) - window + 1):
            myList = {}
            chunk = s2[i : i + window]
            for char in s1:
                myList[char] = myList[char] + 1 if char in myList else 1
            for j in chunk:
                if j in myList:
                    myList[j] -= 1
                else:
                    break
            for j in myList:
                if myList[j] != 0:
                    notIt = True
            if notIt == False:
                return True
            notIt = False
        return False
        