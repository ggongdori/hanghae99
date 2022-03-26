# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head):
    curr = dummy = ListNode(0)
    while head:
        if curr and curr.val > head.val:
            curr = dummy
        while curr.next and curr.next.val < head.val: # classic insertion sort to find position
            curr = curr.next
        curr.next, curr.next.next, head = head, curr.next, head.next # insert
    return dummy.next