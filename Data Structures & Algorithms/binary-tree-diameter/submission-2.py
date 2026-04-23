# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        # define state
        def dfs(node):
            nonlocal diameter
            
            # 1. base case
            if not node:
                return 0

            # 2. recursive case
            left = dfs(node.left)
            right = dfs(node.right)

            # update
            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        
        # 3. call dfs on root
        dfs(root)

        return diameter

            