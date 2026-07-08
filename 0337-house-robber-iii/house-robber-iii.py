class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (rob_this_node, skip_this_node)

            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            rob_current = node.val + left_skip + right_skip
            skip_current = max(left_rob, left_skip) + max(right_rob, right_skip)

            return (rob_current, skip_current)

        return max(dfs(root))