# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        pVal, qVal, rVal = p.val, q.val, root.val
        if pVal == rVal:
            return p
        elif qVal == rVal:
            return q
        elif pVal < rVal and qVal > rVal or pVal > rVal and qVal < rVal:
            return root
        elif pVal < rVal and qVal < rVal:
            result = self.lowestCommonAncestor(root.left, p, q)
        elif pVal > rVal and qVal > rVal:
            result =  self.lowestCommonAncestor(root.right, p, q)
        return result
