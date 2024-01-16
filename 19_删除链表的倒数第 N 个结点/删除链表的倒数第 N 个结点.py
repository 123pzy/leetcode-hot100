# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        left = right = dummy = ListNode(next=head)
        for _ in range(n + 1):
            right = right.next
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next
