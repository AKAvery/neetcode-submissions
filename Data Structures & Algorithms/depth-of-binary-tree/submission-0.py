# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        depth = 0
        q.append(root)
        while q:
            depth += 1
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
        return depth - 1
        