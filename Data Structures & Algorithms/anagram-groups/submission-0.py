class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        o_list = []
        ana_dict = {}
        for i,v in enumerate(strs):
            v_sor = "".join(sorted(v))
            if v_sor in ana_dict:
                o_list[ana_dict[v_sor]].append(v)
            else:
                ana_dict[v_sor]=len(o_list)
                o_list.append([v])
        return o_list
