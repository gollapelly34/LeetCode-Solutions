class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n      
        a = 0
        b = 1       
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c      
        return b