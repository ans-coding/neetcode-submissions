class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        
        for i,v in enumerate(nums):
            ad_target = target - v
            if (ad_target in my_dict):
                ad_i = my_dict[ad_target]
                return [ad_i,i]
            if v not in my_dict:
                my_dict[v] = i
            

        