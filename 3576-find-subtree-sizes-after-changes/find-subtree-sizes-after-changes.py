from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        nearest = [-1] * 26
        new_parent = parent[:]
        stack = [(0, 0, -1)]

        while stack:
            node, state, old = stack.pop()
            c = ord(s[node]) - 97

            if state == 0:
                old = nearest[c]
                if old != -1:
                    new_parent[node] = old
                nearest[c] = node

                stack.append((node, 1, old))
                for child in reversed(children[node]):
                    stack.append((child, 0, -1))
            else:
                nearest[c] = old

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[new_parent[i]].append(i)

        ans = [1] * n
        order = [0]

        for node in order:
            order.extend(children[node])

        for node in reversed(order[1:]):
            ans[new_parent[node]] += ans[node]

        return ans