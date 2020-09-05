# Time: O(n), Space: O(n)
# Relevant Concepts: range objects?
# Set up a new array to hold the answer to be able to only loop through half of the original array once
# Use a range object to only loop up to n
# On each iteration add one number from the x part of the array and one number from the y
# (first half of array = x, second half of array = y)

# Thoughts -> probably a solution that takes less space would be possible

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(0, n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans
