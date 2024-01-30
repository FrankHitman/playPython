# Constraints:
# The number of nodes in both lists is in the range [0, 50.
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        merged_l = ListNode(0)
        curr = merged_l
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    curr.next = ListNode(val=list1.val)
                    list1 = list1.next
                else:
                    curr.next = ListNode(val=list2.val)
                    list2 = list2.next
                curr = curr.next
            elif list1:
                curr.next = list1
                break
            elif list2:
                curr.next = list2
                break
        return merged_l.next


# topic is from https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-interview-150
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    sol = Solution()
    sol.mergeTwoLists(list1=list1, list2=list2)
