class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # עדכון הקוטר המקסימלי
            diameter = max(diameter, left + right)

            # החזרת העומק להורה
            return 1 + max(left, right)

        dfs(root)
        return diameter