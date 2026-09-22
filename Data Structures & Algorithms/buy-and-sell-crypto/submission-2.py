class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while(r<len(prices)):
            print("l: "+str(l)+" "+str(prices[l]))
            print("r: "+str(r)+" "+str(prices[r]))
            print
            print(max_profit)
            if prices[l] > prices[r]:
                l+=1
            elif prices[l]<prices[r]:
                max_profit = max(max_profit, prices[r]-prices[l])
                r+=1
            else:
                r+=1
            
        
        return max_profit

