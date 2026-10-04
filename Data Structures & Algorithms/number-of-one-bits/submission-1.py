class Solution:
    def hammingWeight(self, n: int) -> int:
        count_1 = 0
        while n > 0:
            n = n & (n-1)
            count_1+=1
        return count_1