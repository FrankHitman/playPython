# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # solution is from https://www.youtube.com/watch?v=RF_M9tX4Eag
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)
        pre, cur = dummy, head

        for i in range(left - 1):
            pre, cur = cur, cur.next
        lpre = pre
        lcur = cur
        for i in range(right - left + 1):
            temp = cur.next
            if i == 0:
                cur.next = None
            else:
                cur.next = pre
            pre, cur = cur, temp
        lcur.next = cur
        lpre.next = pre
        return dummy.next

# check the picture file 92-reversed-linked-list-2.jpeg for the mindset
# topic is from https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
