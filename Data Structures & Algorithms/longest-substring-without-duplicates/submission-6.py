
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        substring_dict = {}
        max_substring = 1
        l = 0
        r = 0
        while(r<len(s)):
            if s[r] not in substring_dict:
                substring_dict[s[r]] = 1
                r+=1

            else:
                max_substring = max(max_substring, len(substring_dict))
                while s[r] in substring_dict:
                    del substring_dict[s[l]]
                    l+=1
                substring_dict[s[r]] = 1
                r+=1
                
        max_substring = max(max_substring, len(substring_dict))
        return max_substring
        

            
            