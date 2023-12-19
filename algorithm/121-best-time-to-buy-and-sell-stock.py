# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices:
            if sell > buy:
                profit = max(profit, sell-buy)
            else:
                buy=sell
        print("profit is",profit)
        print("buy is",buy)
        return profit

if __name__ == '__main__':
    sol = Solution()
    sol.maxProfit([7,1,5,3,6,4])
    sol.maxProfit([7,2,6,1,4])
    sol.maxProfit([7,2,6,1,5])

# topic is from https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
# idea is from https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/comments/1880567
# output
# profit is 5
# buy is 1
# profit is 4
# buy is 1
# profit is 4
# buy is 1 # this buy is not correct, it should be 2; it seems that this solution cannot record the buy and sell day