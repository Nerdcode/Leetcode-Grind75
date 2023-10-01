class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
        
solution = Solution()
prices1 = [7, 1, 5, 3, 6, 4]
output1 = solution.maxProfit(prices1)
print(output1)  
prices2 = [7, 6, 4, 3, 1]
output2 = solution.maxProfit(prices2)
print(output2)  
