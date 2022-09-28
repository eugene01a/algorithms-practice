'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''

#TODO incorrect
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        elif len(prices) == 2:
            return max(0, prices[1] - prices[0])

        profit = 0
        idx=0
        while idx < len(prices)-1:
            buy=prices[idx]
            sell = max(prices[idx + 1:])
            if sell-buy > profit:
                profit = sell-buy
            idx += 1


        return profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        buy_price, profit = prices[0], 0

        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - buy_price)
            buy_price = min(buy_price, prices[i])

        return profit


prices = [7,1,5,3,6,4]
profit = Solution().maxProfit(prices)
print(profit)
