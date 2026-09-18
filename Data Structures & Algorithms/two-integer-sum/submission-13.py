class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                print("i: "+str(i))
                my_dict[nums[i]] = [i]
            else:
                my_dict[nums[i]].append(i)
        
        for j in range(len(nums)):
            print("j: "+str(j))
            ad_target = target - nums[j]
            print("ad_target: "+str(ad_target))
            if (ad_target in my_dict):
                if(len(my_dict[ad_target])==1):
                    ad_i = my_dict[ad_target][0]
                elif(len(my_dict[ad_target])>1):
                    ad_i = my_dict[ad_target][1]
                print("ad_i: "+str(ad_i))
                if(j<ad_i):
                    return [j,ad_i]
                elif(j>ad_i):
                    return [ad_i,j]
                    
            

        