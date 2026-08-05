class Solution(object):
    def groupAnagrams(self, strs):
        lookup={}
        for i in strs:
            s="".join(sorted(i))
            if s in lookup:
                lookup[s]+=[i]
            else:
                lookup[s]=[i]
        return list(lookup.values())
        