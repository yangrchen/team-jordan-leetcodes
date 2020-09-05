# Time: O(n), Space: O(1)
# Relevant Concepts: Sliding Window Technique
# set up a first sum that is the sum of first k elements of cardPoints and make this the first max
# use the sliding window technique to avoid a double for loop:
# in each iteration remove the deepest element at the front
# add the deepest element from the end
# check if your new current sum is greater than max

# Thoughts -> you kinda have to imagine the list is a loop since you are sliding across a joint front and end


class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        current_sum = sum(cardPoints[:k])
        max_sum = current_sum
        for i in range(1, k + 1):
            current_sum -= cardPoints[k - i]
            current_sum += cardPoints[len(cardPoints) - i]
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
