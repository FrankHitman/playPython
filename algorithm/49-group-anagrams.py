# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# the example of collections.defaultdict
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = defaultdict(list)
# for k, v in s:
#     d[k].append(v)
#
# sorted(d.items())
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
# # equal with dict.setdefault()
# d = {}
# for k, v in s:
#     d.setdefault(k, []).append(v)
#
# sorted(d.items())
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
import collections


# why not using goto statement, because of https://docs.python.org/3/faq/design.html#why-is-there-no-goto
# for groupAnagrams1 solution
class label(Exception): pass


class Solution:
    # my solution with 94ms runtime, which is inspired by other people's solution on leetcode
    # and https://docs.python.org/3/library/collections.html#collections.defaultdict
    # a = 'sdsa'
    # sorted(a) # list is not hashable, but tuple, string is hashable
    # ['a', 'd', 's', 's']
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        map4strs = {}
        for str_item in strs:
            # ''.join(sorted(str_item))
            map4strs.setdefault(tuple(sorted(str_item)), []).append(str_item)

        return list(map4strs.values())

    # my solution with 1733ms runtime
    def groupAnagrams1(self, strs: list[str]) -> list[list[str]]:
        map_list = []
        result_list = []
        for str_item in strs:
            try:
                map4i = {}
                for character in str_item:
                    map4i[character] = map4i.get(character, 0) + 1

                for index in range(len(map_list)):
                    if map_list[index] == map4i:
                        result_list[index].append(str_item)
                        raise label
                map_list.append(map4i)
                result_list.append([str_item])
            except label:
                continue
        return result_list

    # other people's solution on leetcode with 85ms runtime
    # sort the string to make the key unique
    def groupAnagrams2(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(sol.groupAnagrams(strs=[""]))
    print(sol.groupAnagrams(strs=["a"]))
    print(sol.groupAnagrams(["ddddddddddg", "dgggggggggg"]))

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# topic is from https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150
# output
#
