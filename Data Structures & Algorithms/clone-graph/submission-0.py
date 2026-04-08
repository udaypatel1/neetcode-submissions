from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return

        clone_map = {}

        q = deque([node])

        clone_map = {}
        q = deque([node])

        clone_map[node] = Node(node.val)

        while q:

            cur_node = q.popleft()

            for nb in cur_node.neighbors:
                if nb not in clone_map:

                    clone_map[nb] = Node(nb.val)
                    q.append(nb)

                clone_map[cur_node].neighbors.append(
                    clone_map[nb]
                )

        return clone_map[node]