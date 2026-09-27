# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverseAndInverseTree(curr):
            if not curr:
                return
            traverseAndInverseTree(curr.left)
            traverseAndInverseTree(curr.right)
            curr.left, curr.right = curr.right, curr.left
        
        traverseAndInverseTree(root)
        return root