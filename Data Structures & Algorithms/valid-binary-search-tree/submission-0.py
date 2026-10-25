class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid = True

        def dfs(node, min_value, max_value):
            nonlocal is_valid

            if not node:
                return

            if not min_value < node.val < max_value:
                is_valid = False
                return

            dfs(node.left, min_value, node.val)
            dfs(node.right, node.val, max_value)

        dfs(root, float('-inf'), float('inf'))
        return is_valid