class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sNums = sorted(nums)
        numDict = {}
        for i,num in enumerate(nums):
            if num not in numDict:
                numDict[num] = [i]
            else:
                numDict[num].append(i)
        output = []
        p1 = 0
        p2 = len(sNums) - 1
        
        for i, a in enumerate(sNums):
            if i > 0 and a == sNums[i-1]:
                continue
            p1 = i+1
            p2 = len(sNums) - 1
            while(p1<p2):
                if(sNums[i] + sNums[p1] + sNums[p2]<0):
                    p1+=1
                elif(sNums[i] + sNums[p1] + sNums[p2]>0):
                    p2-=1
                elif(sNums[i] + sNums[p1] + sNums[p2]==0):
                    output.append([sNums[i], sNums[p1], sNums[p2]])
                    p1+=1
                    p2-=1
                    while(sNums[p1] == sNums[p1-1] and p1<p2):
                        p1+=1
        return output

                





'''
            for j in range(i+1,len(sNums)):
                if sNums[i] == sNums[j]:
                    continue
                tempVar = 0-sNums[i]-sNums[j]
                if temp
                if(tempVar in numDict):
                    output.append([sNums[i], sNums[j], tempVar])
        return output
'''

                
            

            