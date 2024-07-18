class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
      count = 0
      visited = set()

      def dfs(node):
        for neighbor, n in enumerate(isConnected[node]):
          if n and neighbor not in visited:
            visited.add(neighbor)
            dfs(neighbor)

      for node in range(len(isConnected)):
        if node not in visited:
          visited.add(node)
          dfs(node)
          count += 1
      return count
