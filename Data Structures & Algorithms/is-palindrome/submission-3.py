class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_space = ""
        for char in s:
            if(char.isalnum()):
                no_space = no_space + char
        for i in range(len(no_space)//2):
            if(no_space[i]!=no_space[len(no_space)-i-1]):
                if(no_space[i].isalpha() and no_space[len(no_space)-i-1].isalpha() and no_space[i].lower()==no_space[len(no_space)-i-1].lower()):
                    continue

                return False
        return True


        