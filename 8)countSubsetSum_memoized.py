def count_subsets_with_sum(nums, target_sum):
    n = len(nums)
    
    # Initialize a memoization matrix.
    memo = [[-1] * (target_sum + 1) for _ in range(n + 1)]
    
    # Recursive function to count subsets with the target sum.
    def count_subsets_recursive(index, target):
        # Base case: If the target sum is 0, we found a valid subset.
        if target == 0:
            return 1
        # Base case: If we've reached the end of the array or the target becomes negative, return 0.
        if index == 0 or target < 0:
            return 0
        # Check if the result is already memoized.
        if memo[index][target] != -1:
            return memo[index][target]
        
        # Recursively count subsets by including or excluding the current element.
        # Store the result in the memoization matrix and return it.
        memo[index][target] = count_subsets_recursive(index - 1, target - nums[index - 1]) + ecount_subsets_recursive(index - 1, target) #add here
        return memo[index][target]
    
    # Start the recursion with the last element (index n-1) and the target sum.
    return count_subsets_recursive(n - 1, target_sum)

# Example usage:
nums = [1, 2, 3, 3]
target_sum = 6
result = count_subsets_with_sum(nums, target_sum)
print(result)  # Output: 3 (Subsets: [1, 2, 3], [1, 2, 3], [3, 3])
