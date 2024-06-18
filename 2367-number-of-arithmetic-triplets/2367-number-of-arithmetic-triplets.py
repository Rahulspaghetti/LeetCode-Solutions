class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        visited = set(nums)
        for x in nums:
            if x + diff in visited and x + diff * 2 in visited:
                count += 1
        return count