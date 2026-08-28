class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd_idx = [i for i in range(26) if cnt[i] % 2 == 1]
        if n % 2 == 0:
            if odd_idx:
                return ""
            mid_char = ''
        else:
            if len(odd_idx) != 1:
                return ""
            mid_char = chr(97 + odd_idx[0])

        half = n // 2
        half_cnt = [c // 2 for c in cnt]

        remaining_snap = [half_cnt[:]]
        cur = half_cnt[:]
        stop = half
        for i in range(half):
            ti = ord(target[i]) - 97
            if cur[ti] > 0:
                cur[ti] -= 1
                remaining_snap.append(cur[:])
            else:
                stop = i
                break

        def fill_ascending(counts):
            out = []
            for idx in range(26):
                if counts[idx]:
                    out.append(chr(97 + idx) * counts[idx])
            return ''.join(out)

        if stop == half:
            H = target[:half]
            if n % 2 == 1:
                if mid_char > target[half]:
                    return H + mid_char + H[::-1]
                elif mid_char == target[half]:
                    second_half = H[::-1]
                    if second_half > target[half + 1:]:
                        return H + mid_char + second_half
            else:
                second_half = H[::-1]
                if second_half > target[half:]:
                    return H + second_half

        start = min(stop, half - 1)
        for i in range(start, -1, -1):
            rem = remaining_snap[i]
            ti = ord(target[i]) - 97
            chosen = -1
            for c in range(ti + 1, 26):
                if rem[c] > 0:
                    chosen = c
                    break
            if chosen == -1:
                continue
            new_rem = rem[:]
            new_rem[chosen] -= 1
            H = target[:i] + chr(97 + chosen) + fill_ascending(new_rem)
            if n % 2 == 1:
                return H + mid_char + H[::-1]
            return H + H[::-1]

        return ""