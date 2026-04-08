# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        '''
        traverse all nodes

        keep track of a k-sized max heap

        if heap len < k:
            blindly add node to heap
        else:
            if cur node < heap[-1]:
                heapq.heapreplace(heap, cur node)
        
        at the end, O(1) heap[0] is k smallest node value
        '''

        if not root:
            return

        heap = []
        q = deque([root])
        visited = set()

        while q:

            q_len = len(q)

            for _ in range(q_len):

                node = q.popleft()

                visited.add(node)

                if len(heap) < k:
                    heapq.heappush(heap, -node.val)
                else:
                    if node.val < abs(heap[0]):
                        heapq.heapreplace(heap, -node.val)

                if node.left and node.left not in visited:
                    q.append(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)

        return -heapq.heappop(heap)