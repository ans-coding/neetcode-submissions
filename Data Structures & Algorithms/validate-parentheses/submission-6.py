class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        stack = []
        paren_Dict = {"{":"}","(":")","[":"]"}
        for i in range(0,len(s)):
            print(stack)
            print(s[i])
            if(s[i] == "{" or s[i] == "(" or s[i] == "["):
                stack.append(s[i])
            elif(len(stack)>0 and paren_Dict[stack[-1]] == s[i]):
                stack.pop()
                continue
            else:
                return False
        if(len(stack)):
            return False
        return True