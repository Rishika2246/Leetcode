from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("#")

        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # Left child
            if values[i] != "#":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            # Right child
            if i < len(values) and values[i] != "#":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root