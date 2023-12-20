# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
# Constraints:
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices:
            if buy > sell:
                buy = sell
            elif buy < sell:
                profit += sell - buy
                buy = sell
        print("profit is ", profit)
        return profit


if __name__ == '__main__':
    sol = Solution()
    sol.maxProfit([7, 1, 5, 3, 6, 4])
    sol.maxProfit([1, 2, 3, 4, 5])
    sol.maxProfit([7, 6, 4, 3, 1])

# topic is from https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
# idea is from https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/comments/1566137
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/comments/1880567
# output
# profit is  7
# profit is  4
# profit is  0
