# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        
        def findMaxDepth(curr):
            if curr is None:
                return 0
            
            left = findMaxDepth(curr.left)
            right = findMaxDepth(curr.right)

            depth = max(left, right) + 1
            return depth
        return findMaxDepth(root)