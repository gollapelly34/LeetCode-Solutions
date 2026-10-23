# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        val = []

        for node in lists:
            while node:
                val.append(node.val)
                node = node.next

        val.sort()

        dummy = ListNode(0)
        curr = dummy

        for x in val:
            curr.next = ListNode(x)
            curr = curr.next

        return dummy.next
        
        