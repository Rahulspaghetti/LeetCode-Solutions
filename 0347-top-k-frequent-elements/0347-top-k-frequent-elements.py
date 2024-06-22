class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict()
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        for num, freq in hashmap.items():
            frequency[freq].append(num)
            
        final_result = []
        for i in range(len(frequency)-1, 0, -1):
            final_result.extend(frequency[i])
            if len(final_result) == k:
                return final_result