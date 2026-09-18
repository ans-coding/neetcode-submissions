class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in words:
            if i[0] == pref[0]:
                if len(pref) == 1:
                    count+=1
                    continue
                for j in range(1,len(pref)):
                    if i[j] != pref[j]:
                        break
                    if(j==len(pref)-1):
                        count+=1
        return count

