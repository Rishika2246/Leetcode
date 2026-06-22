class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # make it circular
        tail.next = head
        
        k = k % length
        steps_to_new_head = length - k
        
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head