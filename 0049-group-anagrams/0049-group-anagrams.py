class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        final_strs = []

        for word in strs:
            sorted_word = ''.join(sorted(word))
            hashmap[sorted_word].append(word)
        
        for key in hashmap:
            final_strs.append(hashmap[key])
        return final_strs