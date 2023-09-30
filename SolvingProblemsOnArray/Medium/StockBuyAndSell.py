def bestTimeToBuyAndSellStock(prices):
    # Write your code here.
    # i = 0
    # n = len(prices)
    # maxi = 0
    # for i in range(n-1):
    #     j = i+1
    #     while(j<n):
    #         if maxi < prices[j]-prices[i]:
    #             maxi = prices[j]-prices[i]
    #         j += 1
    # return maxi
    min = float("inf")
    maxi = 0
    n = len(prices)
    for i in range(n):
        if min > prices[i]:
            min = prices[i]
        if (prices[i] - min) > maxi:
            maxi = prices[i] - min
    return maxi

if __name__ == "__main__":
    print(bestTimeToBuyAndSellStock([7, 1, 5, 4, 3, 6]))