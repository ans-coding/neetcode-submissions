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
            temp_prod.append(p_holder)

        
        for i in range(0,len(nums)):
            final[i] = final[i]*temp_prod[len(nums)-i-1]
        
        return(final)

        