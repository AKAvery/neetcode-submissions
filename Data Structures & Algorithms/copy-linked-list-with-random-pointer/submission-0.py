"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCur = {None : None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCur[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = oldToCur[curr]
            copy.next = oldToCur[curr.next]
            copy.random = oldToCur[curr.random]
            curr = curr.next
        return oldToCur[head]
            
        