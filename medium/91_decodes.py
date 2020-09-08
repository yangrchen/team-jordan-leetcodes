# Time: not sure?? , Space: O(N) i think
# Relevant Concepts: dynamic programming and recursion
# each recursive call moves further into the string
# at each index it checks to see if the next possible character could be combined to make a letter
# each time an index is finalized with the total number of options following it ->
# it is put into the appropriate index in the dp
# then on each call before doing more recursion the function checks if the answer is already at that spot

# Thoughts ->  this was the first time I used dp so I'm unsure what the time complexity really is 
# and if this is how its supposed to lookx

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def rdecode(s, i, dp):
            if len(s) == 0:
                return 1
            if s[0] == "0":
                dp[i] = 0
                return 0
            if dp[i] >= 0:
                return dp[i]
            if len(s) == 1:
                dp[i] = 1
                return 1
            else:
                if s[0] == '1':
                    if s[1] == '0':
                        dp[i] = rdecode(s[2:], i+2, dp)
                        return dp[i]
                    dp[i] = rdecode(s[2:], i + 2, dp) + rdecode(s[1:], i +1, dp)
                    return dp[i]
                if s[0] == '2' and int(s[1]) < 7:
                    if s[1] == '0':
                        dp[i] = rdecode(s[2:], i+2, dp)
                        return dp[i]
                    dp[i] = rdecode(s[2:], i+2, dp) + rdecode(s[1:], i+1, dp)
                    return dp[i]
                dp[i] = rdecode(s[1:], i + 1, dp)
                return dp[i]
        
            
                
        dp = [-1] * len(s)
            
        return rdecode(s, 0, dp)  