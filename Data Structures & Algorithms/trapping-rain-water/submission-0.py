class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        left_max = 0
        right_max = 0

        total_w = 0

        while(left<=right):
            if height[left]<=height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    total_w += left_max - height[left] 
                left+=1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_w += right_max - height[right] 
                right-=1
        return total_w
        '''
        temp_max = 0
        pre_max = []
        suf_max = []
        total_w = 0

        for i in range(len(height)):
            if(height(temp_max) < height(i) and temp_max!=0):
                temp_max = i
                pre_max.append(i)
            elif(height(temp_max) < height(i)):
                temp_max = i
                suf_max.append(i)
                pre_max.append(i)
        '''
            
                

                

            
            