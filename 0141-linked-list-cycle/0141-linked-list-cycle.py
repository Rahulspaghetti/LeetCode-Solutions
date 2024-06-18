# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Use two pointers, the slow and fast pointer method.

# They will meet once in the same node if they have the same value.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        empty = ListNode()
        empty.next = head
        slow = empty
        fast = empty
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow is fast:
                return True
        
        return False