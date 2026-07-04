import heapq

class MedianFinder:

    def __init__(self):
        self.left = []   # max heap (store negatives)
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        # Ensure every value in left <= every value in right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # Keep left same size as right, or one larger
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2