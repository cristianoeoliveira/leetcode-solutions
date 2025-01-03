# 2270. Number of Ways to Slipt Array
# You are given a 0-indexed integer array nums of length n.
# nums contains a valid split at index i if the following are true:
# The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
# There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Calculate the total sum of the array
        total_sum = sum(nums)
        prefix_sum = 0
        valid_splits = 0

        # Iterate through the array, leaving space for at least one element on the right
        for i in range(len(nums) - 1):
            # Update the prefix sum
            prefix_sum += nums[i]
            # Calculate the suffix sum dynamically
            suffix_sum = total_sum - prefix_sum
            # Check if the split at index i is valid
            if prefix_sum >= suffix_sum:
                valid_splits += 1

        return valid_splits