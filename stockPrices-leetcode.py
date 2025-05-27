class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        mn = min(prices)
        mn_idx = prices.index(mn)
        mx = max(prices)
        mx_idx = prices.index(mx)

        while mx >= mn and mn_idx > mx_idx and len(prices) >= 2:
            prices.pop(mx_idx)
            mn = min(prices)
            mn_idx = prices.index(mn)
            mx = max(prices)
            mx_idx = prices.index(mx)

        if len(prices) < 2:
            return 0
        elif mx <= mn:
            return 0
        else:
            return mx - mn

    def maxProfit2(self, prices: list[int]) -> int:

        for i in range(0,len(prices),1 ):
            profit = 0
            buy = prices[i]

            for sell in prices[i+1:]:
                if sell > buy:
                    profit = max(profit, sell - buy)
                else:
                    buy = sell
            return profit


sol = Solution()
print (sol.maxProfit2 ( [2,4,1] ) )
print (sol.maxProfit2 ( [7,1,5,3,6,4] ) )
print (sol.maxProfit ( [7,6,4,3,1] ) )
