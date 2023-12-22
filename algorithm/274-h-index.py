# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
#
#
# Example 1:
#
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:
#
# Input: citations = [1,3,1]
# Output: 1
#
#
# Constraints:
#
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # cita_len = len(citations)
        # if cita_len < 2:
        #     return 1 if citations[0] > 0 else 0
        # citations.sort()
        # print(citations)
        # if cita_len <= citations[0]:
        #     return cita_len
        # # elif citations[0] < cita_len < citations[-1]:
        # else:
        #     mid_index = cita_len // 2
        #     greater_num = cita_len - mid_index
        #     return min(citations[mid_index], greater_num)

        cita_len = len(citations)
        if cita_len < 2:
            return 1 if citations[0] > 0 else 0
        citations.sort()
        print(citations)
        if cita_len <= citations[0]:
            return cita_len
        else:
            for i in range(cita_len):
                if cita_len - i <= citations[i]:
                    return cita_len - i
            return 0
            # if cita_len - i >= citations[i]:
            #     continue
            # else:
            #     return min(cita_len - i + 1, citations[i - 1])

    # idea is from https://www.youtube.com/watch?v=FvnTWDKT_ck&ab_channel=TimothyHChang
    def hIndexSort(self, citations: list[int]) -> int:
        cita_len = len(citations)
        citations.sort()
        for i, v in enumerate(citations):
            if cita_len - i <= v:
                return cita_len - i
        return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.hIndex([3, 0, 6, 1, 5]))
    print(sol.hIndex([1, 3, 1]))
    print(sol.hIndex([1, 3, 3]))
    print(sol.hIndex([100]))
    print(sol.hIndex([0]))
    print(sol.hIndex([1, 2]))
    print(sol.hIndex([11, 15]))
    print(sol.hIndex([0, 1, 0]))

    print('------------')
    print(sol.hIndexSort([3, 0, 6, 1, 5]))
    print(sol.hIndexSort([1, 3, 1]))
    print(sol.hIndexSort([1, 3, 3]))
    print(sol.hIndexSort([100]))
    print(sol.hIndexSort([0]))
    print(sol.hIndexSort([1, 2]))
    print(sol.hIndexSort([11, 15]))
    print(sol.hIndexSort([0, 1, 0]))

# topic is from https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150
# output
# [0, 1, 3, 5, 6]
# 3
# [1, 1, 3]
# 1
# [1, 3, 3]
# 2
# 1
# 0
# [1, 2]
# 1
# [11, 15]
# 2
# [0, 0, 1]
# 1
# ------------
# 3
# 1
# 2
# 1
# 0
# 1
# 2
# 1
