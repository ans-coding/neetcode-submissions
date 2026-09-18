class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hasher = {}
        for element in nums:
            if(element in hasher):
                hasher[element] += 1
            else:
                hasher[element] = 1
        sorted_nums = sorted(hasher)
        counter = 0
        max_count = 0
        for index in range(0,len(sorted_nums)-1):
            print(sorted_nums[index]+1)
            print(sorted_nums[index+1])
            if(sorted_nums[index]+1 == sorted_nums[index+1]):
                print("increment")
                counter+=1;
            else:
                print(counter)
                print(max_count)
                max_count = max(max_count,counter+1)
                counter = 0
        max_count = max(max_count,counter+1)
        return(max_count)


