# Constraints:
# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

# idea is from Hint 1
# Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan) and
# https://leetcode.com/problems/min-stack/description/comments/2227281
class MinStack:

    def __init__(self):
        self.__stack = []
        self.__minimum = None

    def push(self, val: int) -> None:
        if not self.__stack:
            self.__stack.append((val, val))
            self.__minimum = val
        else:
            self.__minimum = self.__minimum if self.__minimum < val else val
            self.__stack.append((val, self.__minimum))

    def pop(self) -> None:
        if not self.__stack:
            return None
        self.__stack.pop()
        if self.__stack:
            self.__minimum = self.__stack[-1][1]
        else:
            self.__minimum = None

    def top(self) -> int:
        if not self.__stack:
            return None
        return self.__stack[-1][0]

    def getMin(self) -> int:
        if not self.__stack:
            return None
        return self.__stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == '__main__':
    # minStack = MinStack()
    # minStack.push(-2)
    # minStack.push(0)
    # minStack.push(-3)
    # print(minStack.getMin())  # return -3
    # minStack.pop()
    # print(minStack.top())  # return 0
    # print(minStack.getMin())  # return -2
    # ["MinStack","push","push","getMin","getMin","push","getMin","getMin","top","getMin","pop","push","push","getMin",
    # "push","pop","top","getMin","pop"]
    # [[],[-10],[14],[],[],[-20],[],[],[],[],[],[10],[-7],[],[-7],[],[],[],[]]
    minStack = MinStack()
    minStack.push(-10)
    minStack.push(14)
    minStack.getMin()
    minStack.getMin()
    minStack.push(-20)
    minStack.getMin()
    minStack.getMin()
    minStack.top()
    minStack.getMin()
    minStack.pop()
    minStack.push(10)
    minStack.push(-7)
    minStack.getMin()
    minStack.push(-7)
    minStack.pop()
    minStack.top()
    minStack.getMin()
    minStack.pop()
# Input
# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
# Output
# [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]
# Expected
# [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]

# topic is from https://leetcode.com/problems/min-stack/?envType=study-plan-v2&envId=top-interview-150
