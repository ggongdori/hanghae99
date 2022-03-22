# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        diameter = 0
        q = deque([root])

        while q:
            diameter += 1

            for _ in range(len(q)):
                temp = q.popleft()
                if temp.right and (temp.right.right or temp.right.left):
                    diameter += 1
                    q.append(temp.right)
                    print('a')
                if temp.left and (temp.left.right or temp.left.left):
                    q.append(temp.left)
                    diameter += 1
                    print('b')
        return diameter
