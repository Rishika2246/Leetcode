class Solution {
public:
    bool winnerSquareGame(int n) {
        // __define-ocg__
        vector<bool> varOcg(n + 1, false);

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                if (!varOcg[i - j * j]) {
                    varOcg[i] = true;
                    break;
                }
            }
        }

        return varOcg[n];
    }
};