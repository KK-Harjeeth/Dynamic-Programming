def can_partition(nums):
    total_sum = sum(nums)
    
    # If the total sum is odd, it cannot be divided into two equal parts.
    if total_sum % 2 == 1:
        return False
    
    target_sum = total_sum // 2
    n = len(nums)
    
    # Initialize a DP table with dimensions (n+1) x (target_sum+1).
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    
    # Base case: If the target sum is 0, we can always achieve it by not including any elements.
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If the current number is greater than the target, we cannot include it.
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Either include the current number or exclude it.
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    
    # The final answer is found in the bottom-right corner of the DP table.
    return dp[n][target_sum]

# Example usage:
nums = [1, 5, 11, 5]
result = can_partition(nums)
print(result)  # Output: True
