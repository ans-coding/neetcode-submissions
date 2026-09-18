class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [1]
        temp_prod = [1]
        p_holder = 1
        for i in range(0, len(nums)-1):
            p_holder = nums[i] * p_holder
            final.append(p_holder)
        
        p_holder = 1
        for i in reversed(range(1,len(nums))):
            p_holder = nums[i] * p_holder
            final[i-1] = final[i-1]*p_holder


        
        return(final)

        