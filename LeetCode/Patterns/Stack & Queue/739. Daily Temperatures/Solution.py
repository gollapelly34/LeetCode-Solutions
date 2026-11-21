class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        #monotonic decresing approach used to solve this problem on the minotoine,when you want the next greater wlwment we sue this processsto solve this
        ans = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                st ,si = stack.pop()
                d = i-si
                ans[si]= d
            stack.append([t,i])
        return ans 



        """
        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j

            stack.append(i)

        return ans
"""




        

        