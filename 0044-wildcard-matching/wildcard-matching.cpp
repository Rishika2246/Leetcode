class Solution {
public:
    bool isMatch(string s, string p) {
        int i = 0, j = 0;
        int starIndex = -1;
        int matchIndex = 0;

        while (i < s.size()) {
            // Characters match, or '?' matches any one character
            if (j < p.size() && (p[j] == s[i] || p[j] == '?')) {
                i++;
                j++;
            }
            // Remember the position of '*'
            else if (j < p.size() && p[j] == '*') {
                starIndex = j;
                matchIndex = i;
                j++;
            }
            // Try expanding the previous '*'
            else if (starIndex != -1) {
                j = starIndex + 1;
                matchIndex++;
                i = matchIndex;
            }
            // No match possible
            else {
                return false;
            }
        }

        // Remaining pattern characters must all be '*'
        while (j < p.size() && p[j] == '*') {
            j++;
        }

        return j == p.size();
    }
};