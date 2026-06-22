class Solution:
    def getPermutation(self, n, k):
        nums = list(range(1, n + 1))
        k -= 1
        fact = [1] * (n + 1)
        
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
        
        res = ""
        
        for i in range(n, 0, -1):
            idx = k // fact[i - 1]
            res += str(nums[idx])
            nums.pop(idx)
            k %= fact[i - 1]
        
        return res