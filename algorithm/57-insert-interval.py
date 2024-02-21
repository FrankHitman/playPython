# Constraints:
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
class Solution:
    # my solution with 67ms runtime
    def insert1(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        if len(intervals) == 0:
            result.append(newInterval)
            return result
        if newInterval[-1] < intervals[0][0]:
            result.append(newInterval)
            result.extend(intervals)
            return result
        if newInterval[0] > intervals[-1][-1]:
            result.extend(intervals)
            result.append(newInterval)
            return result
        # intervals=[[3, 5], [12, 15]], newInterval=[6, 6]
        i = 0
        is_merged = False
        while i < len(intervals):
            if newInterval[0] <= intervals[i][-1] and not is_merged:
                # handling no joint scenario
                if newInterval[-1] < intervals[i][0]:
                    result.append(newInterval)
                    result.append(intervals[i])
                    i += 1
                    is_merged = True
                    continue

                start, stop = None, None
                while i < len(intervals) and (start is None or stop is None):
                    if intervals[i][0] < newInterval[0]:
                        start = intervals[i][0] if start is None else start
                    else:
                        start = newInterval[0] if start is None else start

                    if newInterval[-1] <= intervals[i][-1]:
                        stop = intervals[i][-1] if stop is None else stop

                    if i == len(intervals) - 1 or (newInterval[-1] < intervals[i + 1][0]):
                        stop = newInterval[-1] if stop is None else stop

                    i += 1
                is_merged = True
                result.append([start, stop])

            if i < len(intervals):
                result.append(intervals[i])
            i += 1

        return result

    # other people's graceful solution with 64ms runtime on leetcode
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []
        merge_begin, merge_end = newInterval[0], newInterval[1]
        new_insert = False

        for interval in intervals:
            # new interval has not come
            if interval[1] < merge_begin:
                ans.append(interval)
            # new interval has gone
            elif interval[0] > merge_end:
                # make sure insert merged interval
                if not new_insert:
                    ans.append([merge_begin, merge_end])
                    new_insert = True

                ans.append(interval)
            # generate new interval range
            else:
                merge_begin = min(merge_begin, interval[0])
                merge_end = max(merge_end, interval[1])

        # handle new interval's end is greater than the intervals' end or intervals is empty
        if not new_insert:
            ans.append([merge_begin, merge_end])

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
    print(sol.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
    print(sol.insert(intervals=[], newInterval=[5, 7]))
    print(sol.insert(intervals=[[1, 5]], newInterval=[2, 3]))
    print(sol.insert(intervals=[[1, 5]], newInterval=[2, 7]))
    print(sol.insert(intervals=[[2, 4], [5, 7], [8, 10], [11, 13]], newInterval=[3, 6]))
    print(sol.insert(intervals=[[3, 5], [12, 15]], newInterval=[6, 6]))

# topic is from https://leetcode.com/problems/insert-interval/description/?envType=study-plan-v2&envId=top-interview-150
# output
# [[1, 5], [6, 9]]
# [[1, 2], [3, 10], [12, 16]]
# [[5, 7]]
# [[1, 5]]
# [[1, 7]]
# [[2, 7], [8, 10], [11, 13]]
# [[3, 5], [6, 6], [12, 15]]