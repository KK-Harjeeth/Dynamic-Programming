def subset_sum_memoization(nums, target, index, memo):
    if target == 0:
        return True
    if index == 0 or target < 0:
        return False
    # Check if the result is already computed and stored in the memo dictionary.
    if memo[index][target] is not None:
        return memo[index][target]
    # Calculate the result and store it in the memo dictionary.
    include = subset_sum_memoization(nums, target - nums[index - 1], index - 1, memo)
    exclude = subset_sum_memoization(nums, target, index - 1, memo)
    memo[index][target] = include or exclude
    return memo[index][target]

# Example usage:
nums = [3, 34, 4, 12, 5, 2]
target = 9
memo = [[None] * (target + 1) for _ in range(len(nums) + 1)]
print(subset_sum_memoization(nums, target, len(nums), memo))
