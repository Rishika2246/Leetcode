class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        need = [0] * 26
        window = [0] * 26

        for ch in p:
            need[ord(ch) - ord('a')] += 1

        for i in range(len(p)):
            window[ord(s[i]) - ord('a')] += 1

        ans = []

        if window == need:
            ans.append(0)

        for i in range(len(p), len(s)):
            window[ord(s[i]) - ord('a')] += 1
            window[ord(s[i - len(p)]) - ord('a')] -= 1

            if window == need:
                ans.append(i - len(p) + 1)

        return ans