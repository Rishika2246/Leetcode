class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";

        int n = num1.size();
        int m = num2.size();
        vector<int> result(n + m, 0);

        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                int digit1 = num1[i] - '0';
                int digit2 = num2[j] - '0';

                int product = digit1 * digit2;
                int position = i + j + 1;

                result[position] += product;
                result[i + j] += result[position] / 10;
                result[position] %= 10;
            }
        }

        string answer;

        for (int digit : result) {
            if (answer.empty() && digit == 0) continue;
            answer += to_string(digit);
        }

        return answer.empty() ? "0" : answer;
    }
};