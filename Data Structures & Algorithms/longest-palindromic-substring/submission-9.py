class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s) == 1):
            return s[0]
        elif(len(s) == 2):
            if(s[0]==s[1]):
                return s
            else:
                return s[0]

        output = ""
        for i in range(len(s)):
            odd = self.expand(s,i,i)
            even = self.expand(s,i,i+1)
            if len(odd) > len(output):
                output = odd
            if len(even) > len(output):
                output = even
        return(output)
    
    def expand(self, s, ptr1, ptr2):
        while(ptr1>=0 and ptr2<len(s) and s[ptr1] == s[ptr2]):
                ptr1-=1
                ptr2+=1
        
        return(s[ptr1+1:ptr2])
            
