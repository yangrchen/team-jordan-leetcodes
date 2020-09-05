# SOLUTION 1

# Time: O(n), Space: O(1)
# Relevant Concepts: sort of sliding window technique?
# This solution is based on permutations of subarrays
# As you iterate through count how long your current subarray length
# For a pure in bound subarray of length 4 there would be 4 + 3 + 2 + 1 subarrays
# However you also have to subtract any subarrays in the subarray that are below the lower bound

# Thoughts -> it would be good to decrease the number of counter variables, I also forgot the formula for sum to n


class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        total = 0
        subtotal = 0
        numR = 1
        subL = 0
        max_num = A[0]
        for i in range(len(A)):
            if A[i] > max_num:
                max_num = A[i]

            if max_num > R:
                total += subtotal
                subtotal = 0
                numR = 1
                subL = 0
                if i < len(A) - 1:
                    max_num = A[i + 1]
            else:
                subtotal += numR
                numR += 1
                if A[i] < L:
                    subL += 1
                    subtotal -= subL
                else:
                    subL = 0

        total += subtotal
        return total
