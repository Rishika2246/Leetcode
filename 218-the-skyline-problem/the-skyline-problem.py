from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        
        for l, r, h in buildings:
            events.append((l, -h, r))  # building start
            events.append((r, 0, 0))   # building end
        
        events.sort()
        
        res = [[0, 0]]
        heap = [(0, float('inf'))]  # (-height, end)
        
        for x, neg_h, r in events:
            while heap[0][1] <= x:
                heappop(heap)
            
            if neg_h:
                heappush(heap, (neg_h, r))
            
            curr_h = -heap[0][0]
            
            if res[-1][1] != curr_h:
                res.append([x, curr_h])
        
        return res[1:]