#You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
#Note that we have only one quantity of each item.


# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum value that
# can be put in a knapsack of
# capacity W


def knapSack(W, wt, val, n):

	# Base Case
	if n == 0 or W == 0:
		return 0

	# If weight of the nth item is
	# more than Knapsack of capacity W,
	# then this item cannot be included
	# in the optimal solution
	if (wt[n-1] > W):
		return knapSack(W, wt, val, n-1)

	# return the maximum of two cases:
	# (1) nth item included
	# (2) not included
	else:
		return max    (     val[n-1] + knapSack(W-wt[n-1], wt, val, n-1)     , knapSack(W, wt, val, n-1))

# end of function knapSack


# Driver Code
if __name__ == '__main__':
	profit = [60, 100, 120]
	weight = [10, 20, 30]
	W = 50
	n = len(profit)
	print knapSack(W, weight, profit, n)

# The time complexity of the recursive approach to solving the 0/1 Knapsack Problem without memoization is exponential, specifically O(2^n), where "n" is the number of items.

# This is because, for each item, there are two choices: either include it in the knapsack or exclude it. Consequently, the algorithm explores a binary tree of 
#recursive calls with a branching factor of 2^n, where "n" is the number of items. As a result, the number of recursive function calls grows exponentially with the number of items.

# Without memoization, this approach recalculates the same subproblems multiple times, leading to a significant amount of redundant computation. To improve the 
#efficiency of the recursive approach, you can use memoization (caching) to store and reuse the results of subproblems, which reduces the time complexity to O(nW), 
#as explained in the previous answer.





