from collections import defaultdict, deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))

        visited = set([1])
        queue = deque([1])
        answer = float("inf")

        while queue:
            city = queue.popleft()

            for neighbor, distance in graph[city]:
                answer = min(answer, distance)

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return answer