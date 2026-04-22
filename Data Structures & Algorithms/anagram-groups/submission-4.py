class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        
        for s in strs:
            key = tuple(sorted(s))
            dictionary[key].append(s)

        return list(dictionary.values())
