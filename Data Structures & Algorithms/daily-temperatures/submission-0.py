class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack =[]
        res = len(temperatures) * [0]
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                cur = stack.pop()
                index = cur[1]
                res[cur[1]] = i - index
            stack.append([t,i])

        return res 