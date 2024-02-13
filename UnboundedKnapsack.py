# it is also called as 0/N knapsack problem 
def unboundedKnapsack(W, wt, val, n):
	# Base Case
	if n == 0 or W == 0:
		return 0

	# If weight of the nth item is more than Knapsack capacity W,
	# then this item cannot be included in the optimal solution
	if wt[n-1] > W:
		return unboundedKnapsack(W, wt, val, n-1)

	# Return the maximum of two cases:
	# (1) nth item included
	# (2) not included
	else:
		# Change here: Instead of reducing n-1, we keep n to allow multiple instances of the item
		return max(val[n-1] + unboundedKnapsack(W-wt[n-1], wt, val, n),
		           unboundedKnapsack(W, wt, val, n))  # No change in this line

# Driver Code
if __name__ == '__main__':
	profit = [60, 100, 120]
	weight = [10, 20, 30]
	W = 50
	n = len(profit)
	print(unboundedKnapsack(W, weight, profit, n))
