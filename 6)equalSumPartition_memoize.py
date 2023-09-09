#https://leetcode.com/problems/partition-equal-subset-sum/
def can_partition(nums):
    # Calculate the total sum of the numbers in the input array..
    total_sum = sum(nums)
    
    # If the total sum is odd, it cannot be divided into two equal parts.
    if total_sum % 2 == 1:
        return False
    
    # Calculate the target sum for each partition.
    target_sum = total_sum // 2
    
    # Get the number of elements in the input array.
    n = len(nums)
    
    # Initialize a memoization table with -1 values.
    memo = [[-1] * (target_sum + 1) for _ in range(n + 1)]
    
    # Recursive function to check if a partition with the target sum is possible.
    def is_partition_possible(nums, target, n):
        # Base case: If the target sum is 0, a valid partition is found.
        if target == 0:
            return True
        # Base case: If the target is not 0 and there are no elements left, return False.
        if target != 0 and n == 0:
            return False
        # If the result is already memoized, return it.
        if memo[n][target] != -1:
            return memo[n][target]
        
        # Check if the current element can be included in the partition or not.
        if nums[n - 1] <= target:
            memo[n][target] = is_partition_possible(nums, target - nums[n - 1], n - 1) or \
                              is_partition_possible(nums, target, n - 1)
            return memo[n][target]
        
        # If the current element is too large to be included, exclude it.
        memo[n][target] = is_partition_possible(nums, target, n - 1)
        return memo[n][target]
    
    # Start the recursive partition check with the given parameters.
    return is_partition_possible(nums, target_sum, n)

# Example usage:
nums = [1, 5, 11, 5]
result = can_partition(nums)
print(result)  # Output: True
