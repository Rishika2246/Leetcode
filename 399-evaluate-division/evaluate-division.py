from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        ans = []

        for src, dst in queries:
            if src not in graph or dst not in graph:
                ans.append(-1.0)
                continue
            if src == dst:
                ans.append(1.0)
                continue

            q = deque([(src, 1.0)])
            vis = {src}
            found = -1.0

            while q:
                node, val = q.popleft()
                if node == dst:
                    found = val
                    break
                for nei, w in graph[node]:
                    if nei not in vis:
                        vis.add(nei)
                        q.append((nei, val * w))

            ans.append(found)

        return ans