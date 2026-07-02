class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            papers = n - mid  # papers from mid to end

            if citations[mid] >= papers:
                right = mid - 1
            else:
                left = mid + 1

        return n - left