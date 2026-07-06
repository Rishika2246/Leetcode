class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six",
            "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
            "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def convert(n: int) -> str:
            if n == 0:
                return ""

            if n < 20:
                return below_20[n]

            if n < 100:
                return tens[n // 10] + (" " + convert(n % 10) if n % 10 else "")

            return (
                below_20[n // 100]
                + " Hundred"
                + (" " + convert(n % 100) if n % 100 else "")
            )

        parts = []

        for value, label in [
            (1_000_000_000, "Billion"),
            (1_000_000, "Million"),
            (1_000, "Thousand"),
            (1, "")
        ]:
            if num >= value:
                group = num // value
                parts.append(convert(group) + (f" {label}" if label else ""))
                num %= value

        return " ".join(parts)