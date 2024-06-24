from typing import List 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = [] # pair : [temp, index]
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = (index - stackIndex)
            stack.append([temp, index])

        return res
