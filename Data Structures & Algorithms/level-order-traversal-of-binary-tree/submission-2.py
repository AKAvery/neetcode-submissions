# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        level = []
        queue.appendleft(root)

        while queue:
            currLevel = []
            for i in range(len(queue)):
                currNode = queue.pop()
                if currNode:
                    currLevel.append(currNode.val)
                    queue.appendleft(currNode.left)
                    queue.appendleft(currNode.right)
            if currLevel:
                level.append(currLevel)
        return level



        