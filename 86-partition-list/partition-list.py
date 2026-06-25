class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0)
        after = ListNode(0)
        
        before_ptr = before
        after_ptr = after
        
        while head:
            if head.val < x:
                before_ptr.next = head
                before_ptr = before_ptr.next
            else:
                after_ptr.next = head
                after_ptr = after_ptr.next
            head = head.next
        
        after_ptr.next = None
        before_ptr.next = after.next
        
        return before.next