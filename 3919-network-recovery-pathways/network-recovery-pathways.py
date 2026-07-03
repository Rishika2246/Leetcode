from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = []

        for u, v, cost in edges:
            graph[u].append((v, cost))
            indegree[v] += 1
            costs.append(cost)

        # Topological order of the DAG
        queue = deque(i for i in range(n) if indegree[i] == 0)
        topo = []

        while queue:
            u = queue.popleft()
            topo.append(u)

            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        # Can we reach n-1 using only edges with cost >= score
        # while total path cost stays <= k?
        def possible(score):
            INF = float("inf")
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                # Intermediate offline nodes cannot be used
                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, cost in graph[u]:
                    if cost < score:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    if dist[u] + cost < dist[v]:
                        dist[v] = dist[u] + cost

            return dist[n - 1] <= k

        if not costs or not possible(0):
            return -1

        costs = sorted(set(costs))
        left, right = 0, len(costs) - 1
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if possible(costs[mid]):
                answer = costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return answer