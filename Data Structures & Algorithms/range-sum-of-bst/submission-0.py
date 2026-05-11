from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:
            return -1

        q = deque([root])

        visited = set()

        r_sum = 0

        while q:

            for _ in range(len(q)):

                node = q.popleft()

                if low <= node.val <= high:
                    r_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
        return r_sum

                