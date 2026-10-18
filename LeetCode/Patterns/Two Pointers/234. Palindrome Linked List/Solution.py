# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#calculate the mid value and reverse it then compare the elemst until none

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            

        prev = None 
        while slow:
            nextnode = slow.next
            slow.next = prev 
            prev = slow
            slow = nextnode

        left = head
        right = prev
        while right:
            if  left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        

        


