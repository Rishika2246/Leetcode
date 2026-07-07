class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create new nodes interleaved with original ones
        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = new.next
        
        # Step 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Step 3: Separate the two lists
        curr = head
        new_head = head.next
        
        while curr:
            new = curr.next
            curr.next = new.next
            if new.next:
                new.next = new.next.next
            curr = curr.next
        
        return new_head