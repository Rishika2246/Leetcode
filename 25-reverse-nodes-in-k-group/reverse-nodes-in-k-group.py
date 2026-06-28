class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while True:
            node = prev
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next
            
            curr = prev.next
            nxt = curr.next
            
            for _ in range(k - 1):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            
            prev = curr