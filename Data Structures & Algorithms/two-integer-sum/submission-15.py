class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        
        for i,v in enumerate(nums):
            ad_target = target - v
            if (ad_target in my_dict):
                if(len(my_dict[ad_target])==1):
                    ad_i = my_dict[ad_target][0]
                elif(len(my_dict[ad_target])>1):
                    ad_i = my_dict[ad_target][1]
                return [ad_i,i]
            if v not in my_dict:
                my_dict[v] = [i]
            else:
                my_dict[v].append(i)     
            

        