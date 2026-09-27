class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        result = []

        for string in strs:
            wordList = sorted(string)
            word = "".join(wordList)
            myDict[word].append(string)
        for x in myDict:
            result.append(myDict[x])
        return result