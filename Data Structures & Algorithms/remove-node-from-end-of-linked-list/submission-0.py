# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        slow, fast = dummy, dummy

        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # move both until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # remove nth node from end
        slow.next = slow.next.next

        return dummy.next

