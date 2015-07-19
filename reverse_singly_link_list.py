#
# Reverse a singly linked list
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        
        pre = None
        while(head):
            next = head.next
            head.next = pre
            pre = head
            head = next
        
        return pre
        