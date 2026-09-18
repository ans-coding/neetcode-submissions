class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        for i in range(len(s)):
            if(s[i] in s_dic):
                s_dic[s[i]] += 1
            else:
                s_dic[s[i]] = 1
        
        t_dic = {}
        for j in range(len(t)):
            if(t[j] in t_dic):
                t_dic[t[j]] += 1
            else:
                t_dic[t[j]] = 1
        
        return(s_dic == t_dic)