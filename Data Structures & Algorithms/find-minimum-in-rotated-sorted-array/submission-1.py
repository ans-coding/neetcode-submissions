class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        ptr1 = 0
        ptr2 = len(nums)-1

        while(ptr1<=ptr2):
            if(nums[ptr1]<nums[ptr2]):
                res = min(res, nums[ptr1])
                break
            mid = (ptr1+ptr2)//2
            res = min(res, nums[mid])
            if(nums[mid]>=nums[ptr1]):
                ptr1=mid+1
            else:
                ptr2 = mid-1
        
        return(res)
            