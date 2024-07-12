# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        if root:
          queue.append((root, 1))

          while queue:  
            node, height = queue.popleft()

            if not node.left and not node.right:
                return height

            if node.left:
                queue.append((node.left, height + 1))
            if node.right:
                queue.append((node.right, height + 1))

        return 0