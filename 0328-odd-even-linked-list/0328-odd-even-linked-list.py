# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        p1,p2 = head, head.next
        start_even = head.next
        while p2 and p2.next:
            p1.next = p1.next.next
            p1 = p1.next
            p2.next = p2.next.next
            p2 = p2.next
        p1.next = start_even
        return head       
        