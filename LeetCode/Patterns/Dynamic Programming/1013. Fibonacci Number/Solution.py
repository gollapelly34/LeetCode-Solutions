class Solution:
    def fib(self, n: int) -> int:
        """
        dp = [-1] * (n+1)
        if n<=1:
            return n
        dp[0] = 0
        dp[1] = 1
        for i in range (2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        """
        if n<=1:
            return n
        return self.fib(n-1) + self.fib(n-2)


        
