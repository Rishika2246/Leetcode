class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # Build transition matrix
        size = 2 * m
        T = [[0] * size for _ in range(size)]

        for x in range(m):
            less = x
            greater = m - 1 - x

            # state x: last move was DOWN
            for y in range(x + 1, m):
                T[m + y][x] = 1

            # state m+x: last move was UP
            for y in range(x):
                T[y][m + x] = 1

        def matmul(A, B):
            n1, n2, n3 = len(A), len(B), len(B[0])
            C = [[0] * n3 for _ in range(n1)]

            for i in range(n1):
                for k in range(n2):
                    if A[i][k]:
                        a = A[i][k]
                        for j in range(n3):
                            C[i][j] = (C[i][j] + a * B[k][j]) % MOD
            return C

        def matpow(M, p):
            n = len(M)
            R = [[0] * n for _ in range(n)]
            for i in range(n):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = matmul(M, R)
                M = matmul(M, M)
                p >>= 1
            return R

        # Initial vector for length 2
        init = [[0] for _ in range(size)]

        for a in range(m):
            for b in range(m):
                if a < b:
                    init[m + b][0] += 1
                elif a > b:
                    init[b][0] += 1

        P = matpow(T, n - 2)
        res = matmul(P, init)

        ans = 0
        for i in range(size):
            ans = (ans + res[i][0]) % MOD

        return ans