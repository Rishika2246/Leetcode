from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        lookup = [-1] * n
        idxs = []  # [start_index, length] for each maximal zero-block
        cnt1 = 0
        for i, ch in enumerate(s):
            if ch == '0':
                if i - 1 >= 0 and s[i - 1] == '0':
                    idxs[-1][1] += 1
                else:
                    idxs.append([i, 1])
            else:
                cnt1 += 1
            lookup[i] = len(idxs) - 1  # last zero-block starting at or before i

        result = [cnt1] * len(queries)
        if not idxs:
            return result

        m = len(idxs)
        arr = [idxs[i][1] + idxs[i + 1][1] for i in range(m - 1)]

        st, log = None, None
        if arr:
            L = len(arr)
            log = [0] * (L + 1)
            for i in range(2, L + 1):
                log[i] = log[i // 2] + 1
            st = [arr[:]]
            j = 1
            while (1 << j) <= L:
                prev = st[-1]
                half = 1 << (j - 1)
                st.append([max(prev[i], prev[i + half]) for i in range(L - (1 << j) + 1)])
                j += 1

        def range_max(l, r):
            k = log[r - l + 1]
            return max(st[k][l], st[k][r - (1 << k) + 1])

        for qi, (l, r) in enumerate(queries):
            best = cnt1
            lb, rb = lookup[l], lookup[r]
            left = lb + 1
            right = rb - (1 if s[r] == '0' else 0)

            left_cnt = idxs[lb][1] - (l - idxs[lb][0]) if s[l] == '0' else None
            right_cnt = r - idxs[rb][0] + 1 if s[r] == '0' else None

            # two+ full zero-blocks strictly inside [l, r] -> best adjacent pair
            if st is not None and left <= right - 1:
                best = max(best, cnt1 + range_max(left, right - 1))

            # l and r each land inside zero-blocks that are directly adjacent
            if s[l] == '0' and s[r] == '0' and lb + 1 == rb:
                best = max(best, cnt1 + left_cnt + right_cnt)

            # l's partial block merges with the next full block
            if s[l] == '0' and lb + 1 <= right:
                best = max(best, cnt1 + left_cnt + idxs[lb + 1][1])

            # r's partial block merges with the full block right before it
            if s[r] == '0' and left <= rb - 1:
                best = max(best, cnt1 + right_cnt + idxs[rb - 1][1])

            result[qi] = best

        return result