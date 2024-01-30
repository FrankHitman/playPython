# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # I'm confused about the description and the parameter pos in this question.
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    def hasCycle2(self, head: [ListNode]) -> bool:
        last_pos = head[-1].next
        return True if -1 < last_pos < len(head) else False

    # solution is from https://walkccc.me/LeetCode/problems/0141/#__tabbed_1_3
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    # faster solution from other people's submission on leetcode
    def hasCycle3(self, head: ListNode) -> bool:
        temp = head
        node_set = set()
        while temp is not None:
            if temp in node_set:
                return True
            node_set.add(temp)
            temp = temp.next
        return False


if __name__ == '__main__':
    l1 = ListNode(3)
    l2 = ListNode(2)
    l3 = ListNode(0)
    l4 = ListNode(-4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l2
    sol = Solution()
    print(sol.hasCycle(head=l1))

# topic is from https://leetcode.com/problems/linked-list-cycle/submissions/1160824533/?envType=study-plan-v2&envId=top-interview-150