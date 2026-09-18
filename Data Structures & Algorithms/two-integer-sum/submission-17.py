class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        
        for i,v in enumerate(nums):
            ad_target = target - v
            if (ad_target in my_dict):
                return [my_dict[ad_target],i]
            my_dict[v] = i
            

        