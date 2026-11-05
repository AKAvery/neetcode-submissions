# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        numList1 = {}
        numList2 = {}
        node1 = l1
        node2 = l2
        index = 0
        sum = 0
        while node1:
            numList1[index] = node1.val
            node1 = node1.next
            index += 1
        index = 0
        while node2:
            numList2[index] = node2.val
            node2 = node2.next
            index += 1
        pos = max(len(numList1), len(numList2)) - 1
        while pos >= 0:
            if len(numList1) > pos:
                sum += (numList1[pos] * (10 ** pos))
            if len(numList2) > pos :
                sum += (numList2[pos] * (10 ** pos))
            pos -= 1
        result = ListNode()
        curr = result
        for i in range(len(str((sum)))):
            if i == 0:
                curr = ListNode(str(sum)[i]) 
            else:
                curr = ListNode(str(sum)[i], prev)
            prev = curr
        return curr
        
        