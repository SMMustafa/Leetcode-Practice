# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        def length(self, head: ListNode):
            count=0
            curr = head
            while curr:
                count+=1
                curr=curr.next
            return count

        new_n = (length(self, head))-n

        sentinal = ListNode(-1)
        sentinal.next = head
        curr=head
        prev=sentinal
        x=0
        while x!=new_n:
            curr=curr.next
            prev=prev.next
            x+=1

        prev.next=curr.next
        return sentinal.next
