from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p or not q:
            if not p and not q:
                return True
            return False

        q1 = deque([p])
        q2 = deque([q])

        while q1 or q2:

            if len(q1) != len(q2):
                return False
            
            len_q = len(q1)

            for _ in range(len_q):

                node_1 = q1.popleft()
                node_2 = q2.popleft()

                if node_1 == None or node_2 == None:
                    if node_1 != node_2:
                        return False
                    else:
                        continue

                if node_1.val != node_2.val:
                    return False
                
                if node_1.left:
                    q1.append(node_1.left)
                else:
                    q1.append(None)

                if node_1.right:
                    q1.append(node_1.right)
                else:
                    q1.append(None)
                
                if node_2.left:
                    q2.append(node_2.left)
                else:
                    q2.append(None)

                if node_2.right:
                    q2.append(node_2.right)
                else:
                    q2.append(None)
            
        return True if len(q1) == len(q2) else False


        