class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        '''
        Understand:
        input: array, integer
        output: integer k (k <= max(piles))
        h >= len(piles)

        Plan:
        declare a begin and end variable 1 and max(piles)
        declare a mid variable 
        check if the mid satisfies the check
        implement a binary search

        the check:
        loop through array, calculate ceil(piles/mid)
        update a total
        if total is greater than hours, display False

        Implement
        '''
        from math import ceil
        
        begin = 1
        end = max(piles)

        while begin < end:
            mid = (begin + end) // 2
            check = sum(ceil(pile/mid) for pile in piles) <= h
            if check:
                end = mid
            else:
                begin = mid + 1

        return begin

        