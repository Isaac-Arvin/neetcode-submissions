# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def diameter_search(curr):
            if curr is None:
                return 0
            
            left = diameter_search(curr.left)
            right = diameter_search(curr.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)
        
        diameter_search(root)
        return self.diameter