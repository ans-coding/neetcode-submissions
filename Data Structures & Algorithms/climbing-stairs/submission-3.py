class Solution:
    global memo
    memo = {}
    def climbStairs(self, n: int) -> int:
        
        
        if n<=2:
            memo[n] = n
        elif (n-1) in memo and (n-2) in memo:
            memo[n] = memo[n-1]+memo[n-2]
        if n in memo:
            return memo[n]
        
        
        return self.climbStairs(n-1)+self.climbStairs(n-2)
            
        