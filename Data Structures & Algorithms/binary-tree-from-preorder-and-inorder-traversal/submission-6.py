# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pair = {}
        index = 0
        for val in inorder:
            pair[val] = index
            index += 1

        self.pre_idx = 0
        def buildTreeHelper(l, r):
            if l > r:
                return None
            root = TreeNode(preorder[self.pre_idx])
            mid = pair[preorder[self.pre_idx]]
            self.pre_idx += 1
            root.left = buildTreeHelper(l, mid - 1)
            root.right = buildTreeHelper(mid + 1, r)

            return root

        return buildTreeHelper(0, len(preorder) - 1)
 