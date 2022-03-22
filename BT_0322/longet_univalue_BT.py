# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        length = 0
        q = deque([root])
        while q:
            # length += 1
            for _ in range(len(q)):
                temp = q.popleft()
                if temp.right and (temp.right.val == temp.val):
                    length += 1
                    q.append(temp.right)
                elif temp.left and (temp.left.val == temp.val):
                    length += 1
                    q.append(temp.left)

        return length