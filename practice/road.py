class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for i in range(len(prices)):
        #     max = prices[i]
        #     min = prices[i]
        #     if prices[i] >= max :
        #         max = prices[i]
        #     elif(prices[i] < min):
        #         if(i != (len(prices) - 1)):
        #             min = prices[i]
        #     return max - min
        pr = 0
        for i in range(len(prices)):
            bp = prices[i]
            sp = prices[i]
            if( sp < prices[i+1] ):
                sp = prices[i+1]
            if(i != len(prices) - 1 and bp < prices[i]):
                if(prices.index(bp) < prices.index(sp)):
                    bp = prices[i]
        pr = sp - bp