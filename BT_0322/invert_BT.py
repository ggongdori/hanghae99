# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque

        if not root:
            return []

        q = deque([root])

        while q:
            for _ in range(len(q)):
                temp = q.popleft()
                if temp.right and temp.left:
                    temp.right, temp.left = temp.left, temp.right
                    q.append(temp.right)
                    q.append(temp.left)

        return root
