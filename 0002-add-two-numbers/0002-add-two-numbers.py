# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        r = ListNode()
        t = r
        l1_val = l1.val
        l2_val = l2.val
        carry = 0
        while True:
            val = l1_val + l2_val + carry
            carry = 0
            if val >= 10:
                carry = 1
                val -= 10
            t.val = val

            if l1.next is None:
                l1_val = 0
                if l2.next is None:
                    l2_val = 0
                    if carry == 0:
                        break
                    else:
                        s = ListNode()
                        s.val = carry
                        t.next = s
                else:
                    l2 = l2.next
                    l2_val = l2.val
            else:
                l1 = l1.next
                l1_val = l1.val
                if l2.next is None:
                    l2_val = 0
                else:
                    l2 = l2.next
                    l2_val = l2.val
            
            s = ListNode()
            t.next = s
            t = s
        return r
            
            

            


        