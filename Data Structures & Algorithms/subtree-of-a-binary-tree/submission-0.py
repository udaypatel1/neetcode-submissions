from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def sameTree(self, p: TreeNode, q: TreeNode):

        # Both are None, so they are the same
        if not p and not q:
            return True
        
        # One is None, the other isn't, OR values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check left and right subtrees
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        st = deque([root])
        visited = set()

        while st:

            node = st.pop()
            visited.add(node)

            if self.sameTree(node, subRoot):
                return True
            
            if node.left and node.left not in visited:
                st.append(node.left)
            if node.right and node.right not in visited:
                st.append(node.right)
            
        return False


        