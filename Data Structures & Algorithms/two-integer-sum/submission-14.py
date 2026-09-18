class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        
        for j in range(len(nums)):
            ad_target = target - nums[j]
            if (ad_target in my_dict):
                if(len(my_dict[ad_target])==1):
                    ad_i = my_dict[ad_target][0]
                elif(len(my_dict[ad_target])>1):
                    ad_i = my_dict[ad_target][1]
                if(j<ad_i):
                    return [j,ad_i]
                elif(j>ad_i):
                    return [ad_i,j]
            
            if nums[j] not in my_dict:
                my_dict[nums[j]] = [j]
            else:
                my_dict[nums[j]].append(j)     
            

        