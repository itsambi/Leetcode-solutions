from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Determines if two binary trees are identical.
        Two trees are identical if they have the same structure and node values.

        Args:
            p: Root node of the first binary tree
            q: Root node of the second binary tree

        Returns:
            True if both trees are identical, False otherwise
        """
        # Base case: both nodes are None (reached leaf nodes simultaneously)
        if p is None and q is None:
            return True

        # If only one node is None or values don't match, trees are different
        if p is None or q is None or p.val != q.val:
            return False

        # Recursively check if left subtrees and right subtrees are identical
        # Both subtrees must be identical for the trees to be the same
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return left_same and right_same