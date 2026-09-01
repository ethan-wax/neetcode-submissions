from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        clone = Node(val=node.val)
        nodes = {node.val: clone}
        seen = {node.val}
        q = deque([node])
        while q:
            n = q.popleft()
            c = nodes[n.val]
            for neighbor in n.neighbors:
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(val=neighbor.val)
                c.neighbors.append(nodes[neighbor.val])
                if neighbor.val not in seen:
                    seen.add(neighbor.val)
                    q.append(neighbor)
        return clone