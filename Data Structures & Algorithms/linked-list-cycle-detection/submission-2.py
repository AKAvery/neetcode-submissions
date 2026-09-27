# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        slowNode = head
        fastNode = head
        if slowNode == None:
            return False
        elif slowNode.next == None:
            return False
        fastNode = head.next
        while slowNode or fastNode:
            if fastNode == None:
                return False
            elif slowNode.val == fastNode.val:
                return True
            fastNode = fastNode.next
            if fastNode:
                fastNode = fastNode.next
            else:
                return False
            slowNode = slowNode.next
        return False