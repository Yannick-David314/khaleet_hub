class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        '''
        PLAN:
        window_length = 1
            len(set(slice[i:i + window_length]))

        '''
        total = 0
        count = 0
        window_length = 1
        length = len(nums)

        while window_length <= length:
            for i in range(length - window_length + 1):
                sliced = nums[i : i + window_length]
                count = len(set(sliced))
                total += count * count
            window_length += 1

        return total
