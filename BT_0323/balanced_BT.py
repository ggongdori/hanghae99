# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        l_depth = r_depth = 0
        q = deque([root])
        lst = []
        while q:
            temp = q.popleft()
            if temp.left:
                l_depth += 1
                q.append(temp.left)
            if temp.right:
                r_depth += 1
                q.append(temp.right)

        if abs(l_depth - r_depth) < 2:
            return True
        else:
            return False