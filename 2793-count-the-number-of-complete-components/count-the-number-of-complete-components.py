from collections import defaultdict
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            degree_sum = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    x, y = dfs(nei)
                    nodes += x
                    degree_sum += y

            return nodes, degree_sum

        for i in range(n):
            if not visited[i]:
                nodes, degree_sum = dfs(i)

                if degree_sum // 2 == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans