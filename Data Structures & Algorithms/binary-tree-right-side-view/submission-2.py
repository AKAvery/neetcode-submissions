# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.appendleft(root)
        levels = []
        while queue:
            currLevel = []
            for i in range(len(queue)):
                currNode = queue.pop()
                if currNode:
                    currLevel.append(currNode.val)
                    queue.appendleft(currNode.left)
                    queue.appendleft(currNode.right)
            if currLevel:
                levels.append(currLevel[-1])
        return levels


        