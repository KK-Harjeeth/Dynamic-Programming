#dp[i][w] indicates " maximum profit with first i elements considered and capacity 'w' "

def knapSack(W, wt, val, n):
    # Create a DP table to store the maximum values for different subproblems
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the DP table in a bottom-up manner
    #i is 'n' and j is capacity
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i - 1] <= j:
                # If the current item can be included, take the maximum of including and excluding it
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
            else:
                # If the current item's weight exceeds the current capacity, skip it
                dp[i][j] = dp[i - 1][j]

    # The result is stored in the bottom-right cell of the DP table
    return dp[n][W]

# Example usage:
W = 4
wt = [1, 3, 4, 2]
val = [1, 4, 5, 7]
n = len(wt)
result = knapSack(W, wt, val, n)
print(result)
