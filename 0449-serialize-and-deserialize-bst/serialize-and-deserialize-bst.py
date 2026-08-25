class Codec:

    def serialize(self, root):
        vals = []

        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(vals)

    def deserialize(self, data):
        if not data:
            return None

        vals = list(map(int, data.split(",")))
        i = 0

        def build(low, high):
            nonlocal i

            if i == len(vals) or not (low < vals[i] < high):
                return None

            val = vals[i]
            i += 1

            node = TreeNode(val)
            node.left = build(low, val)
            node.right = build(val, high)

            return node

        return build(float("-inf"), float("inf"))