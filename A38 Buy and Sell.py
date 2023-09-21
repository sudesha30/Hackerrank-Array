You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input Format

The first line contains a integer N denoting the size of array A. The second line contains N integers donting the elements of array A.

Constraints

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
Output Format

Print the integer which is the answer to the question

Solution:
def maxProfit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit

# Input
N = int(input())
prices = list(map(int, input().split()))

# Calculate and print the result
result = maxProfit(prices)
print(result)
