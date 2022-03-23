# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q = deque([root])
        depth = 0
        while q:
            temp = q.popleft()
            if temp.left or temp.right:
                depth += 1
                q.append(temp.left)
                q.append(temp.right)

        return depth
