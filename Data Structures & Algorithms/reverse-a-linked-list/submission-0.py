# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevHead = None
        curr = head
        while curr != None:
            normalNext = curr.next
            curr.next = prevHead
            prevHead = curr
            curr = normalNext
        return prevHead