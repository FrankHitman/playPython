import random

# this solution consume more time than solution 2
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

# according to https://stackoverflow.com/questions/40143157/big-o-complexity-of-random-choicelist-in-python3
# the time complexity of random.choice is O(1) as well
    def getRandom(self) -> int:
        return random.choice(list(self.__array.keys()))

# this solution is O(1), which is inspired by other people's submission
class RandomizedSet2:

    def __init__(self):
        self.__hashmap = {}
        self.__container=[]
        self.__container_length = 0

    def insert(self, val: int) -> bool:
        if val in self.__hashmap:
            return False
        else:
            self.__container.append(val)
            self.__container_length += 1
            self.__hashmap[val] = self.__container_length -1
            return True

    def remove(self, val: int) -> bool:
        if val in self.__hashmap:
            index = self.__hashmap[val]

            self.__container[index] = self.__container[-1]
            self.__hashmap[self.__container[-1]] = index
            del self.__hashmap[val]
            self.__container.pop()
            self.__container_length -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.__container[random.randrange(0, self.__container_length, 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# topic is from https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1126405912/?envType=study-plan-v2&envId=top-interview-150
