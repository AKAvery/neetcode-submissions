class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        whole = defaultdict(list)
        result = []
        for word1 in strs:
            sortedWordList = sorted(word1)
            sortedWord = "".join(sortedWordList)
            whole[sortedWord].append(word1)
        for x in whole:
            result.append(whole[x])
        return result