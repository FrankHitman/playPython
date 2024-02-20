# Constraints:
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4

class Solution:
    # my solution with 130ms runtime
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort()
        # get first intervals, using sliding window algorithm
        start, stop = intervals[0][0], intervals[0][1]
        result = []
        for second in range(1, len(intervals)):
            if intervals[second][0] <= stop:
                stop = intervals[second][1] if intervals[second][1] > stop else stop
            else:
                result.append([start, stop])
                start, stop = intervals[second][0], intervals[second][1]
            if second == len(intervals) - 1:
                result.append([start, stop])
        return result

    # other people's solution with 114ms runtime on leetcode
    def merge2(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in intervals:
            if not res or i[0] > res[-1][1]:
                res.append(i)
            else:
                res[-1][1] = max(i[1], res[-1][1])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(sol.merge(intervals=[[1, 4], [4, 5]]))
    print(sol.merge([[1, 3]]))
    print(sol.merge([[1, 4], [2, 3]]))
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
