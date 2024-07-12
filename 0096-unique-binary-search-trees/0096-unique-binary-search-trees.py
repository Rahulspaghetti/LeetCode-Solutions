class Solution:
    def numTrees(self, n: int) -> int:
      dp = [0] * (n + 1) # [n => number of combinations]
      dp[0] = 1
      
      for sub in range(1, n + 1):
          combos = 0
          for head in range(1,sub+1):
              lesser = head - 1
              greater = sub - head
              combos += dp[lesser] * dp[greater]
          dp[sub] = combos

      return dp[n]    