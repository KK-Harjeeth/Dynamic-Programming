def subset_sum_recursive(nums, target, index):
    # Base case: If the target is 0, we've found a valid subset.
    if target == 0:
        return True
    # Base case: If we've reached the end of the array or target < 0, it's not possible.
    if index == 0 or target < 0:
        return False
    # Try including the current element or excluding it.
    include = subset_sum_recursive(nums, target - nums[index - 1], index - 1)
    exclude = subset_sum_recursive(nums, target, index - 1)
    return include or exclude

# Example usage:
nums = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum_recursive(nums, target, len(nums)))
