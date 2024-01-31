# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # solution is inspired by the hint
    def copyRandomList(self, head: Node) -> Node:
        origin_pointer = head
        while origin_pointer:
            # try to insert new node to mark the random node
            # A --> A' --> B --> B' --> C --> C' --> D --> D'
            copy_pointer = Node(origin_pointer.val)
            copy_pointer.random = origin_pointer.random
            copy_pointer.next = origin_pointer.next
            origin_pointer.next = copy_pointer
            origin_pointer = origin_pointer.next.next

        # iterate the merged linked list to get the real random node,
        # doesn't need to update the next node explicitly
        copy_list = Node(0)
        copy_pointer2 = copy_list
        origin_pointer2 = head
        while origin_pointer2:
            origin_pointer2 = origin_pointer2.next
            copy_pointer2.next = origin_pointer2  # update the next node by origin.next.next
            if origin_pointer2.random:
                copy_pointer2.next.random = origin_pointer2.random.next
            else:
                copy_pointer2.next.random = None
            copy_pointer2 = copy_pointer2.next
            origin_pointer2 = origin_pointer2.next
        return copy_list.next


if __name__ == '__main__':
    list1 = Node(1)
    list1.next = Node(2)
    list1.random = list1.next
    list1.next.next = None
    list1.next.random = list1.next
    sol = Solution()
    copy_list = sol.copyRandomList(list1)

# topic is from https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-interview-150
