class Solution(object):
    def letterCombinations(self, digits):
        digits_map = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res=[]
        if len(digits) ==0:
            return res
            
        self.dfs(digits, 0, digits_map, '', res)
        return res
    
    def dfs(self, nums, index, digits_map, path, res):
        if index >=len(nums):
            res.append(path)
            return
        string1 =digits_map[nums[index]]
        for i in string1:
            self.dfs(nums, index+1, digits_map, path + i, res)