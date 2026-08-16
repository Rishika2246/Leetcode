class Node:
    def __init__(self, key="", count=0):
        self.key = key
        self.count = count
        self.prev = None
        self.next = None
        self.keys = set()


class AllOne:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodes = {}

    def _insert_after(self, node, new_node):
        new_node.next = node.next
        new_node.prev = node
        node.next.prev = new_node
        node.next = new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            if self.head.next != self.tail and self.head.next.count == 1:
                node = self.head.next
            else:
                node = Node(count=1)
                self._insert_after(self.head, node)

            node.keys.add(key)
            self.nodes[key] = node
        else:
            curr = self.nodes[key]
            new_count = curr.count + 1

            if curr.next != self.tail and curr.next.count == new_count:
                nxt = curr.next
            else:
                nxt = Node(count=new_count)
                self._insert_after(curr, nxt)

            nxt.keys.add(key)
            curr.keys.remove(key)
            self.nodes[key] = nxt

            if not curr.keys:
                self._remove(curr)

    def dec(self, key: str) -> None:
        curr = self.nodes[key]

        if curr.count == 1:
            del self.nodes[key]
        else:
            new_count = curr.count - 1

            if curr.prev != self.head and curr.prev.count == new_count:
                prev = curr.prev
            else:
                prev = Node(count=new_count)
                self._insert_after(curr.prev, prev)

            prev.keys.add(key)
            self.nodes[key] = prev

        curr.keys.remove(key)

        if not curr.keys:
            self._remove(curr)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))