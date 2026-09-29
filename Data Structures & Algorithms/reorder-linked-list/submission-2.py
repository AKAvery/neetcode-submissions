# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node1 = head
        start = head
        node2 = head
        length = 0
        counter = 0;
        while node1:
            length += 1
            node1 = node1.next
        node1 = head
        limit = length // 2 
    

        while limit:
            node2 = head
            placementNode1Next = node1.next
            for i in range(1, length):
                node2 = node2.next
            print("node2:", node2.val)
            node1.next = node2
            node2.next = placementNode1Next
            print(node1.val, node1.next.val)
            node1 = placementNode1Next
            print(node1.val)
            counter += 1
            limit -= 1
            print("end cycle")
        node1.next = None
        
    def printHelper(self, length: int, head: Optional[ListNode]) -> None:
        start = head
        limit = 5
        while limit:
            print("result ", start.val)
            start = start.next
            limit -= 1
    