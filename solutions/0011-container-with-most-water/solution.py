class Solution:
    def maxArea(self, height: list[int]) -> int:
        '''
        UNDERSTAND
        input: array
        output: integer
        edge cases: empty array, single element array, 

        MATCH
        two-pointers

        to calculate area: length (index diff) and the value 

        PLAN
        initiate left and right pointers at both ends of the array
        compute area, update area if it's greater than current
        
        IMPLEMENT
        '''
        maxArea = 0

        left = 0
        right = len(height) - 1

        while left < right:
            lowest = min(height[left], height[right])
            maxArea = max(((right - left) * lowest), maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea   




        