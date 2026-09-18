class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def finder(start, end, target):
            if start>end:
                return -1
            middle = (start+end)//2
            
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                return finder(middle+1, end, target)
            elif target < nums[middle]:
                return finder(start, middle-1, target)
            
        
        return finder(0,len(nums)-1,target)
        