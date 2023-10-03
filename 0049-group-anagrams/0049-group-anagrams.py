class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        mp = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in list(mp.keys()):
                mp[ss].append(s)
            else:
                mp[ss] = [s]
        
        for v in list(mp.values()):
            result.append(v)

        return result