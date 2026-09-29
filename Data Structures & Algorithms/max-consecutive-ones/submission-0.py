class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        temp_max = 0
        curr = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                curr+=1
            else:
                curr = 0
            temp_max = max(temp_max, curr)
        return temp_max

            

            