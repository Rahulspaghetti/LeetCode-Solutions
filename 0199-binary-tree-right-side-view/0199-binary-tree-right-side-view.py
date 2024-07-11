# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        frontier = [root]
        output = []
        
        while frontier:
            output.append(frontier[-1].val)
            level_count = len(frontier)
            
            for _ in range(level_count):
                node = frontier.pop(0)
                if node.left:
                    frontier.append(node.left)
                if node.right:
                    frontier.append(node.right)
                    
        return output