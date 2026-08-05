class Solution(object):
    def groupAnagrams(self, strs):
        lookup={}
        for i in strs:
            s="".join(sorted(i))
            if s not in lookup:
                lookup[s]=[]
            lookup[s].append(i)
        return list(lookup.values())
        