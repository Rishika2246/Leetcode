class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, curr_sum, path):
            if not node:
                return
            
            path.append(node.val)
            curr_sum += node.val
            
            if not node.left and not node.right and curr_sum == targetSum:
                res.append(path[:])
            
            dfs(node.left, curr_sum, path)
            dfs(node.right, curr_sum, path)
            
            path.pop()
        
        dfs(root, 0, [])
        return res