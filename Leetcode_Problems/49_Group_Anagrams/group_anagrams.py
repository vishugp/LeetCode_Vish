class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {strs[0]:[strs[0]]}
        sorted_grp_keys = {}
        print(sorted(strs[0]))
        sorted_grp_keys["".join(sorted(strs[0]))] =  strs[0]
        check = 0
        for s in strs[1:]:
            try:
                groups[sorted_grp_keys["".join(sorted(s))]].append(s)
            except:
                groups[s]=[s]
                sorted_grp_keys["".join(sorted(s))] = s


        return list(groups.values())
    
a = Solution()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
