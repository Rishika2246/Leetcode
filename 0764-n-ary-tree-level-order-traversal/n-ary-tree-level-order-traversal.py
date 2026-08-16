class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            next_queue = []

            for node in queue:
                level.append(node.val)
                next_queue.extend(node.children)

            result.append(level)
            queue = next_queue

        return result