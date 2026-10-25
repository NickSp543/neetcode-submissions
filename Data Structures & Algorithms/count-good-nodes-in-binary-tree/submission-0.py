class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, max_rn):
            nonlocal res

            if not node:
                return

            if node.val >= max_rn:
                res += 1

            max_rn = max(max_rn, node.val)

            dfs(node.left, max_rn)
            dfs(node.right, max_rn)

        dfs(root, root.val)
        return res