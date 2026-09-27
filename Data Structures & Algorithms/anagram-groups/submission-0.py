class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        whole = defaultdict(list)
        result = []
        for index1, word1 in enumerate(strs):
            sortWordList = sorted(word1)
            sortWord = "".join(sortWordList)
            whole[sortWord].append(word1)
        for x in whole:
            result.append(whole[x])
        return result