from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        res = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            same = 1
            
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                dx = x2 - x1
                dy = y2 - y1
                
                if dx == 0 and dy == 0:
                    same += 1
                elif dx == 0:
                    slopes[(0, 1)] += 1   # vertical line
                elif dy == 0:
                    slopes[(1, 0)] += 1   # horizontal line
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g
                    
                    # normalize sign
                    if dx < 0:
                        dx, dy = -dx, -dy
                    
                    slopes[(dx, dy)] += 1
            
            max_line = max(slopes.values(), default=0)
            res = max(res, max_line + same)
        
        return res