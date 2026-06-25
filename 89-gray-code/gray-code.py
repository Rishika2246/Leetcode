class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        
        for i in range(n):
            for num in reversed(res):
                res.append(num | (1 << i))
        
        return res