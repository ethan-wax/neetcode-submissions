# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        acc = 0
        ans = None
        def count(root):
            if not root: return
            count(root.left)
            nonlocal acc
            nonlocal ans
            acc += 1
            if acc == k:
                ans = root.val
            count(root.right)
        count(root)
        return ans
