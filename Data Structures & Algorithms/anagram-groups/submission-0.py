class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            st = "".join(sorted(s))
            d[st] = d.get(st, []) + [s]

        return list(d.values())