import random


class RandomizedSet:

    def __init__(self):
        self.__array = {}

    def insert(self, val: int) -> bool:
        if val in self.__array:
            return False
        else:
            self.__array[val] = 0
            return True

    def remove(self, val: int) -> bool:
        if val in self.__array:
            del self.__array[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.__array.keys()))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# topic is from https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1126405912/?envType=study-plan-v2&envId=top-interview-150
