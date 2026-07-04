class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        anagrams = defaultdict(list)
        
        for s in strs:
            key = tuple(sorted(s))
            anagrams[key].append(s)
        
        return list(anagrams.values())