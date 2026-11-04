class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j,sol = 0,len(heights)-1,0

        while i<j:
            distance = j - i
            hight = min(heights[i],heights[j])
            size = distance*hight
            if size > sol:
                sol = size
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return sol
            
