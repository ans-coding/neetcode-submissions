class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        out = []
        for i,v in enumerate(nums):
            if(v in myDict):
                myDict[v]+=1
            else:
                myDict[v] = 1
        print(myDict)
        dItems = myDict.items()
        sorted_tuples = sorted(dItems,key=lambda x: x[1], reverse = True)
        for i in sorted_tuples:
            out.append(i[0])
        print(out)
        return(out[0:k])

