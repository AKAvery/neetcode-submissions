class TimeMap:

    def __init__(self):
        self.myDict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
       
        self.myDict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        myDictVals = self.myDict[key]
        l, r = 0, len(myDictVals) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            print(len(myDictVals))
            if len(myDictVals) == 1:
                if myDictVals[0][1] <= timestamp:
                    return myDictVals[0][0]
                else:
                    return ""
            else:
                if myDictVals[mid][1] > timestamp:
                    r = mid - 1
                else:
                    i = mid
                    while i < len(myDictVals) - 1 and myDictVals[i + 1][1] <= timestamp:
                        i += 1
                    return myDictVals[i][0]
        return ""

