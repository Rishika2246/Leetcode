class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        def build(start, end):
            if start > end:
                return [None]
            
            res = []
            
            for root in range(start, end + 1):
                left_trees = build(start, root - 1)
                right_trees = build(root + 1, end)
                
                for l in left_trees:
                    for r in right_trees:
                        node = TreeNode(root)
                        node.left = l
                        node.right = r
                        res.append(node)
            
            return res
        
        return build(1, n)