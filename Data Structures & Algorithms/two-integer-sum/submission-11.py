class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                print("i: "+str(i))
                my_dict[nums[i]] = 1
            else:
                my_dict[nums[i]] += 1
        
        for j in range(len(nums)):
            print("j: "+str(j))
            ad_target = target - nums[j]
            print("ad_target: "+str(ad_target))
            if (ad_target in my_dict):
                ad_i = nums.index(ad_target)
                print("ad_i: "+str(ad_i))
                if(j<ad_i):
                    return [j,ad_i]
                elif(j>ad_i):
                    return [ad_i,j]
                    
            

        