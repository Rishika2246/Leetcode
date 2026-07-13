import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        ans = self.head.val
        cur = self.head.next
        i = 2

        while cur:
            if random.randrange(i) == 0:
                ans = cur.val
            cur = cur.next
            i += 1

        return ans