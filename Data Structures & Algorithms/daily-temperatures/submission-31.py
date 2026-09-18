class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i in reversed(range(0,len(temperatures))):
            print("result "+str(result))
            print("stack "+str(stack))
            while(stack and stack[-1][1]<=temperatures[i]):
                stack.pop()
            stack.append((i,temperatures[i]))
            print("result "+str(result))
            print("stack "+str(stack))
            if(len(stack)>1):
                result[len(temperatures)-i-1]=stack[-2][0] - stack[-1][0]
                print("added to result")
            elif(len(stack)==1):
                result[len(temperatures)-i-1] = 0
                print("added 0 to result")
            
        result = result[::-1]



        return result
        
            
        