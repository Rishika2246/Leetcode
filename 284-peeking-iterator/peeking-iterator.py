class PeekingIterator:
    def __init__(self, iterator: Iterator):
        self.iterator = iterator
        self.next_element = iterator.next() if iterator.hasNext() else None

    def peek(self) -> int:
        return self.next_element

    def next(self) -> int:
        current = self.next_element

        if self.iterator.hasNext():
            self.next_element = self.iterator.next()
        else:
            self.next_element = None

        return current

    def hasNext(self) -> bool:
        return self.next_element is not None