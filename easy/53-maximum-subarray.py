# Time: O(n), Space: O(1)
# Relevant Concepts: Kadane's algorithm, Dynamic programming
# The idea here is to keep track of a global max value and a running sum in the array
# every time we add a new element to the running sum. If the new running sum is greater than
# the global max, update the max
# If the sum is less then 0 then we can start a new running sum at the current index and continue

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr = 0
        for n in nums:
            curr += n
            max_sum = max(max_sum, curr)
            if curr < 0:
                curr = 0
        return max_sum
