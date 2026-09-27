# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        resultNode = list1;

        if curr1 == None and curr2 == None:
            print("entered 1")
            return resultNode
        elif curr1 == None:
            print("entered 2")

            return curr2
        elif curr2 == None:
            print("entered 3")

            return curr1
        if curr1.val <= curr2.val:
            resultNode = curr1
            curr1 = curr1.next
        else:
            resultNode = curr2
            curr2 = curr2.next

        head = resultNode
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                resultNode.next = curr1
                curr1 = curr1.next
                resultNode = resultNode.next
            else:
                resultNode.next = curr2
                curr2 = curr2.next
                resultNode = resultNode.next
        if curr1:
            while curr1:
                resultNode.next = curr1
                curr1 = curr1.next
                resultNode = resultNode.next
        else:
            while curr2:
                resultNode.next = curr2
                curr2 = curr2.next
                resultNode = resultNode.next
        return head

        