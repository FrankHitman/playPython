# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # solution is inspired by https://walkccc.me/LeetCode/problems/0002/#__tabbed_1_3
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_l = ListNode()
        curr = sum_l # new a pointer to iterate the linked list
        next_tag = 0
        continue_tag = True
        while l1 or l2 or continue_tag:
            sum_v = 0
            continue_tag = False
            if l1:
                sum_v += l1.val
                if l1.next:
                    continue_tag = True
                l1 = l1.next
            if l2:
                sum_v += l2.val
                if l2.next:
                    continue_tag = True
                l2 = l2.next
            if next_tag:
                sum_v += next_tag
            if sum_v > 9:
                next_tag = 1
                continue_tag = True
            else:
                next_tag = 0
            curr.val = sum_v % 10
            if continue_tag:
                curr.next = ListNode()
                curr = curr.next
        return sum_l

    # solution is from https://walkccc.me/LeetCode/problems/0002/#__tabbed_1_3
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next

        return dummy.next

    # failed when Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # expected Output: [8,9,9,9,0,0,0,1]
    # but get output:  [8,9,9,9,0,0,0]
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_l = ListNode()
        curr = sum_l  # new a pointer to iterate the linked list
        next_tag = 0
        while l1 or l2:
            if l1 and l2:
                curr.val = next_tag + l1.val + l2.val if next_tag + l1.val + l2.val < 10 \
                    else (next_tag + l1.val + l2.val) % 10
                next_tag = 0 if next_tag + l1.val + l2.val < 10 else 1
                if l1.next or l2.next:
                    curr.next = ListNode()
                    curr = curr.next
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                curr.val = next_tag + l1.val if next_tag + l1.val < 10 \
                    else (next_tag + l1.val) % 10
                next_tag = 0 if next_tag + l1.val < 10 else 1
                if l1.next:
                    curr.next = ListNode()
                    curr = curr.next
                l1 = l1.next
            else:
                curr.val = next_tag + l2.val if next_tag + l2.val < 10 \
                    else (next_tag + l2.val) % 10
                next_tag = 0 if next_tag + l2.val < 10 else 1
                if l2.next:
                    curr.next = ListNode()
                    curr = curr.next
                l2 = l2.next

        return sum_l


if __name__ == '__main__':
    sol = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print(sol.addTwoNumbers(l1, l2))

# topic is from https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150