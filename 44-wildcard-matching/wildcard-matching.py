class Solution:
    def isMatch(self, s, p):
        s_len, p_len = len(s), len(p)
        i = j = 0
        star = match = -1
        
        while i < s_len:
            if j < p_len and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif j < p_len and p[j] == '*':
                star = j
                match = i
                j += 1
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            else:
                return False
        
        while j < p_len and p[j] == '*':
            j += 1
        
        return j == p_len