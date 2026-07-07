from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Reverse sort so pop() gives the lexicographically smallest airport
        for src, dest in sorted(tickets, reverse=True):
            graph[src].append(dest)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())

            itinerary.append(airport)

        dfs("JFK")
        return itinerary[::-1]