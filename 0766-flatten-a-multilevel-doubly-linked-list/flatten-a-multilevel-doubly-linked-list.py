class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        curr = head

        while curr:
            if curr.child:
                child = curr.child
                nxt = curr.next

                curr.next = child
                child.prev = curr
                curr.child = None

                tail = child
                while tail.next:
                    tail = tail.next

                if nxt:
                    tail.next = nxt
                    nxt.prev = tail

            curr = curr.next

        return head