import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pLen = len(piles)
        if(h<pLen):
            return -1
        piles.sort()
        
        start = 1
        end = piles[-1]
        mid = (start+end)//2
        while(start<end):
            mid = (start+end)//2
            mid_test = self.possible_k_test(mid, piles)
            if(mid_test<=h):
                end = mid
            else:
                start = mid+1

        
        while(self.possible_k_test(mid, piles) > h):
            mid+=1
        return mid


    def possible_k_test(self, k: int, piles: List[int]) -> int:
        output_h = 0
        for pile in piles:
            output_h+= math.ceil(pile/k)
        return output_h


        
        


            
