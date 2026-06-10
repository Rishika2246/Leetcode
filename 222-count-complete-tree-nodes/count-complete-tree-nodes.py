class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = right = root
        lh = rh = 0

        while left:
            lh += 1
            left = left.left

        while right:
            rh += 1
            right = right.right

        if lh == rh:
            return (1 << lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)