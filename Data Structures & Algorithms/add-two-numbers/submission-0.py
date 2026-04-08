# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = None
        result = []

        while l1 or l2:

            add_result = 0

            if l1:
                add_result += l1.val
            
            if l2:
                add_result += l2.val
            
            if carry:
                add_result += carry
                carry = None

            first = int(str(add_result)[0])

            if add_result >= 10:

                second = int(str(add_result)[1])
                
                result.append(second)
                carry = first
            else:
                result.append(first)

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

        if carry:
            result.append(carry)

        # build new LL

        head = ListNode(result[0])

        cur = head

        if len(result) > 1:

            for idx in range(1, len(result)):

                new_node = ListNode(result[idx])
                cur.next = new_node
                cur = cur.next

        return head

            
        